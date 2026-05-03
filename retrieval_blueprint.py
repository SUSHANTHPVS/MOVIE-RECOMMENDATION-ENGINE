# Import pandas to help us look up the index of a movie
import pandas as pd

# Import pickle to load our 'Warehouse Ledger'
import pickle
import sys

# --- STEP 1: LOAD THE ASSETS ---
try:
    # Load our movie list (The warehouse map)
    with open('models/movies_list.pkl', 'rb') as f:
        movies = pickle.load(f)

    # Load our similarity matrix (The scores ledger)
    with open('models/similarity.pkl', 'rb') as f:
        similarity = pickle.load(f)

except FileNotFoundError as e:
    print(f"❌ File not found: {e}")
    sys.exit()

print("✅ Assets loaded successfully!")

# --- STEP 2: THE INDEX LOOKUP (SAFE VERSION) ---
user_choice = "Avatar"

# Normalize and search safely
matches = movies[
    movies['title'].str.lower().str.strip() ==
    user_choice.lower().strip()
]

# If movie not found
if matches.empty:
    print(f"\n❌ Movie '{user_choice}' not found in database.")
    print("\n🔍 Sample available movies:")
    print(movies['title'].head(10).tolist())
    sys.exit()

# Get index safely
movie_index = matches.index[0]

print(f"\n✅ User selected: {user_choice}")
print(f"📍 Location in Warehouse (Index): {movie_index}")

# --- STEP 3: ACCESS THE SCORES ---
distances = similarity[movie_index]

print(f"📊 Number of scores retrieved: {len(distances)}")
print(f"🔢 First 5 similarity scores in this row: {distances[0:5]}")

# --- STEP 4: THE CONCEPT OF SORTING (PREVIEW) ---
print("\nNext Step: We will sort these numbers to find the highest matches!")