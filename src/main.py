"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from src.recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv") 

    # Taste profile — defines what this user enjoys
    # Used by score_song() to score every song out of 100 pts
    user_prefs = {
        "favorite_genre":  "lofi",    # Primary genre preference
        "favorite_mood":   "chill",   # Preferred emotional tone
        "target_energy":    0.40,     # 0.0 (very quiet) to 1.0 (very intense)
        "likes_acoustic":   True,     # True = prefers organic/acoustic sound
    }

    recommendations = recommend_songs(user_prefs, songs, k=5)

    print("\n" + "=" * 52)
    print(f"  Top {len(recommendations)} Recommendations for You")
    print(f"     Genre: {user_prefs['favorite_genre']}  |  "
          f"Mood: {user_prefs['favorite_mood']}  |  "
          f"Energy: {user_prefs['target_energy']}")
    print("=" * 52)

    for rank, (song, score, explanation) in enumerate(recommendations, start=1):
        # Score bar: each # = 5 pts, max 20 chars
        filled = int(score / 5)
        bar = "#" * filled + "-" * (20 - filled)

        print(f"\n  #{rank}  {song['title']}  -  {song['artist']}")
        print(f"       {song['genre']} | {song['mood']} | energy {song['energy']}")
        print(f"       [{bar}] {score}/100")
        print(f"       Why: ", end="")
        for i, reason in enumerate(explanation.split(" | ")):
            prefix = "       " + " " * 5 if i > 0 else ""
            print(f"{prefix}{reason}")

    print("\n" + "=" * 52 + "\n")


if __name__ == "__main__":
    main()
