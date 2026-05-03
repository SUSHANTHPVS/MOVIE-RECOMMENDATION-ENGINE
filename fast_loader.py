import pickle
import pandas as pd
import os

def load_engine():
    print("⏳ Loading the Recommendation Engine...")

    # 🔥 Get project root dynamically
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    movies_path = os.path.join(BASE_DIR, "models", "movies_list.pkl")
    similarity_path = os.path.join(BASE_DIR, "models", "similarity.pkl")

    print(f"📂 Loading from: {BASE_DIR}")

    with open(movies_path, 'rb') as f:
        movies = pickle.load(f)

    with open(similarity_path, 'rb') as f:
        similarity = pickle.load(f)

    return movies, similarity


# --- START THE SCRIPT ---
if __name__ == "__main__":
    movies_list, similarity_matrix = load_engine()

    print(f"✅ Engine Ready! Loaded {len(movies_list)} movies.")
    print("\n--- Preview of Movie Library ---")
    print(movies_list['title'].head())