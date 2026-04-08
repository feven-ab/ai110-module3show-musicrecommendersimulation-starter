# 🎧 Model Card: Music Recommender Simulation
# Model Card - Music Recommender Simulation

## 1. Model Name

VibeFinder 1.0

---

## 2. Intended Use

This system recommends songs from a small music catalog.
It is for classroom learning and practice.
It assumes the user can describe their taste with a genre, mood, energy level, and acoustic preference.
It is not meant for real users.

---

## 3. How the Model Works

The model gives each song a score out of 100.
It looks at genre, mood, energy, and acousticness.
Songs get more points when they are closer to the user's preferences.
Genre and mood matter the most in the current score.
After scoring all songs, the model returns the top matches.

---

## 4. Data

The dataset has 18 songs.
It includes genres like pop, lofi, rock, ambient, jazz, folk, EDM, hip-hop, metal, and classical.
It also includes moods like happy, chill, focused, romantic, melancholy, and intense.
I did not remove any songs from the current dataset.
The catalog is still small, so many music tastes are missing.

---

## 5. Strengths

The system works well when a user has clear preferences.
It gives strong results for profiles like calm lofi or high-energy EDM.
The scoring rules are simple, so the recommendations are easy to explain.
The top songs often make sense when the catalog includes a close match.

---

## 6. Limitations and Bias

One weakness is that the system can reward the right label more than the right feel.
For example, "Gym Hero" can show up for someone who wants "Happy Pop" because it matches `pop` and still gets enough points in other categories.
That means the system may treat a song as "close enough" even when it feels more intense than the user wanted.
This can make the results feel repetitive or a little off.

---

## 7. Evaluation

I tested the system with several different user profiles.
I tried profiles like Calm Lofi, Happy Pop, High-Energy EDM, Acoustic Sad, and Metal Anger.
I checked whether the top songs felt like good matches for each profile.
The system usually worked best when the genre and mood were very clear.
It was less reliable when a user wanted a softer or more specific version of a broad style like pop.

---

## 8. Future Work

I would add more songs first.
I would also use more features like tempo, valence, and danceability.
Another good step would be adding more diversity to the top results.
I would also improve the explanation text so it sounds more natural.

---

## 9. Personal Reflection

My biggest learning moment was seeing how a simple scoring rule could produce results that felt believable, even when the logic was very small and mechanical. Building the project helped me understand that recommendation systems do not need to be very complex to shape what a user sees again and again.

AI tools helped me move faster when I was brainstorming test profiles, writing explanations, and checking whether my model card sections were clear. I still had to double-check the outputs against the actual scoring logic and song data, because a helpful explanation is not always the same thing as a correct one.

What surprised me most was how quickly a basic point system started to feel like a real recommender. Even with only a few features, the results looked personal because the system consistently matched patterns in genre, mood, and energy. If I extended this project, I would try adding more songs, using features like danceability and valence, and adding some diversity rules so the top recommendations do not feel too narrow.
