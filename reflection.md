# Reflection

## Profile Comparisons

### Calm Lofi vs. Happy Pop
The Calm Lofi profile produced low-energy, acoustic results like `Library Rain` and `Midnight Coding`, while the Happy Pop profile pushed brighter, more energetic songs like `Sunrise City` and `Gym Hero` to the top. This makes sense because the scoring logic strongly rewards matching genre and mood, so switching from `lofi/chill` to `pop/happy` changes both the sound and the energy level of the top results.

### Calm Lofi vs. High-Energy EDM
The Calm Lofi output stayed centered on soft, mellow songs, but the High-Energy EDM profile immediately moved to `Drop Zone` and other louder tracks. That shift makes sense because the EDM profile asked for very high energy and a euphoric mood, so the model favored songs with stronger intensity even when the genre match became less exact after the top result.

### Calm Lofi vs. Acoustic Sad
Both profiles preferred lower-energy and more acoustic songs, so there was some overlap in the kinds of tracks that appeared. The main difference is that Calm Lofi favored `lofi`, `ambient`, and `jazz`, while Acoustic Sad pulled in `folk`, `classical`, and `blues` because the mood target moved from `chill` to `melancholy` and the genre preference changed.

### Calm Lofi vs. Metal Anger
The Calm Lofi profile recommended soft and reflective songs, while the Metal Anger profile jumped to `Ironclad` and `Storm Runner`, which are the most aggressive tracks in the set. This makes sense because the model treats mood and genre as major signals, so changing from `chill/lofi` to `angry/metal` flips the ranking toward intense, high-energy songs almost completely.

### Happy Pop vs. High-Energy EDM
Both profiles liked energetic music, so they shared some high-energy songs near the top, but the Happy Pop list stayed closer to `pop` while the High-Energy EDM list centered on `Drop Zone` and similar intense tracks. That difference makes sense because both users want energy, but one profile rewards pop melody and happy mood while the other rewards EDM and a more euphoric club-like feeling.

### Happy Pop vs. Acoustic Sad
The Happy Pop profile produced bright, polished songs, while the Acoustic Sad profile moved toward gentler and more emotional tracks like `Porch Light` and `Autumn Strings`. This makes sense because the profiles differ on almost every major input: genre, mood, target energy, and acoustic preference.

### Happy Pop vs. Metal Anger
Both profiles surfaced strong, energetic songs, but Happy Pop started with `Sunrise City` and `Gym Hero`, while Metal Anger put `Ironclad` and `Storm Runner` first. That makes sense because the model sees both users as liking intensity, but it separates them by whether that intensity should sound upbeat and mainstream or harsh and aggressive.

### High-Energy EDM vs. Acoustic Sad
These two profiles produced almost opposite outputs: High-Energy EDM preferred loud, synthetic dance tracks, while Acoustic Sad preferred soft, acoustic, low-energy songs. The contrast makes sense because the scoring logic gives very different scores when the requested energy level and acoustic preference move in opposite directions.

### High-Energy EDM vs. Metal Anger
Both profiles ranked very high-energy songs well, which is why their outputs overlapped more than some other pairs. The difference is that High-Energy EDM favored euphoric electronic music first, while Metal Anger favored darker rock and metal tracks, which makes sense because genre and mood split the two users even though both want intensity.

### Acoustic Sad vs. Metal Anger
The Acoustic Sad profile produced the softest and most reflective list, while Metal Anger produced the hardest and most aggressive list. This makes sense because the two users disagree on genre, mood, energy, and acoustic taste, so the model had almost no reason to rank the same songs highly for both of them.
