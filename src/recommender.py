from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """A single song and its audio feature attributes."""
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """A user's stated taste preferences used to score and rank songs."""
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """OOP wrapper around the scoring and ranking logic for use in tests."""

    def __init__(self, songs: List[Song]):
        """Store the song catalog for repeated recommendation calls."""
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        """Return the top k Song objects ranked by score against the user profile."""
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        """Return a human-readable string explaining why this song was recommended."""
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """Read songs.csv and return a list of dicts with numeric fields cast to float/int."""
    import csv
    songs = []
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            songs.append({
                "id":           int(row["id"]),
                "title":        row["title"],
                "artist":       row["artist"],
                "genre":        row["genre"],
                "mood":         row["mood"],
                "energy":       float(row["energy"]),
                "tempo_bpm":    float(row["tempo_bpm"]),
                "valence":      float(row["valence"]),
                "danceability": float(row["danceability"]),
                "acousticness": float(row["acousticness"]),
            })
    print(f"Loaded songs: {len(songs)}")
    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Score one song 0-100 against user_prefs using genre, mood, energy, and acousticness rules."""
    # --- Genre similarity groups ---
    GENRE_CLUSTERS = {
        "lofi":      ["lofi", "ambient", "jazz"],
        "ambient":   ["ambient", "lofi", "jazz"],
        "jazz":      ["jazz", "lofi", "ambient"],
        "pop":       ["pop", "indie pop", "synthwave"],
        "indie pop": ["indie pop", "pop", "synthwave"],
        "synthwave": ["synthwave", "pop", "indie pop"],
        "rock":      ["rock", "metal"],
        "metal":     ["metal", "rock"],
        "hip-hop":   ["hip-hop", "r&b"],
        "r&b":       ["r&b", "hip-hop"],
        "blues":     ["blues", "jazz"],
        "folk":      ["folk", "acoustic"],
        "classical": ["classical"],
        "edm":       ["edm", "synthwave"],
        "latin":     ["latin"],
    }

    # --- Mood spectrum (calm=0 → intense/dark=high) ---
    MOOD_SCALE = {
        "melancholy": 0, "chill": 1, "relaxed": 2, "nostalgic": 3,
        "focused": 4, "romantic": 5, "happy": 6, "confident": 7,
        "festive": 8, "moody": 9, "euphoric": 10, "intense": 11, "angry": 12,
    }
    MAX_MOOD_DIST = max(MOOD_SCALE.values())  # 12

    score = 0.0
    reasons = []

    # --- Rule 1: Genre (35 pts) ---
    user_genre = user_prefs.get("favorite_genre", "")
    song_genre = song.get("genre", "")
    if song_genre == user_genre:
        score += 35
        reasons.append(f"Matches your favorite genre: {song_genre}")
    elif song_genre in GENRE_CLUSTERS.get(user_genre, []):
        score += 17.5
        reasons.append(f"Similar genre to {user_genre}: {song_genre}")

    # --- Rule 2: Mood (35 pts) ---
    user_mood = user_prefs.get("favorite_mood", "")
    song_mood = song.get("mood", "")
    user_pos = MOOD_SCALE.get(user_mood, 6)
    song_pos = MOOD_SCALE.get(song_mood, 6)
    mood_similarity = 1 - abs(user_pos - song_pos) / MAX_MOOD_DIST
    mood_pts = round(35 * mood_similarity, 1)
    score += mood_pts
    if song_mood == user_mood:
        reasons.append(f"Matches your preferred mood: {song_mood}")
    elif mood_pts >= 17.5:
        reasons.append(f"Mood '{song_mood}' is close to your preference '{user_mood}'")

    # --- Rule 3: Energy proximity (20 pts) ---
    target_energy = user_prefs.get("target_energy", 0.5)
    energy_diff = abs(song["energy"] - target_energy)
    energy_pts = round((1 - energy_diff) * 20, 1)
    score += energy_pts
    if energy_diff <= 0.10:
        reasons.append(f"Energy ({song['energy']}) closely matches your target ({target_energy})")
    elif energy_diff <= 0.25:
        reasons.append(f"Energy ({song['energy']}) is near your target ({target_energy})")

    # --- Rule 4: Acoustic alignment (10 pts) ---
    likes_acoustic = user_prefs.get("likes_acoustic", False)
    if likes_acoustic:
        acoustic_pts = round(song["acousticness"] * 10, 1)
        if song["acousticness"] >= 0.6:
            reasons.append(f"Acoustic feel ({song['acousticness']}) matches your preference")
    else:
        acoustic_pts = round((1 - song["acousticness"]) * 10, 1)
        if song["acousticness"] <= 0.4:
            reasons.append(f"Electric/produced sound ({song['acousticness']}) matches your preference")
    score += acoustic_pts

    return round(score, 1), reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Score every song, sort by score descending, and return the top k as (song, score, explanation) tuples."""
    scored = [
        (song, score, " | ".join(reasons) if reasons else "No strong matches")
        for song in songs
        for score, reasons in [score_song(user_prefs, song)]
    ]

    return sorted(scored, key=lambda x: x[1], reverse=True)[:k]
