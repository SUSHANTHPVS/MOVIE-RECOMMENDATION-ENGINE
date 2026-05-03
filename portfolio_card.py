import subprocess

def generate_portfolio_snippet():
    print("⏳ Fetching GitHub repository info...")

    try:
        # Fetch remote URL
        repo_url_raw = subprocess.getoutput("git remote get-url origin")

        # Handle case where git is not initialized
        if "fatal" in repo_url_raw.lower() or repo_url_raw.strip() == "":
            print("❌ Git remote not found.")
            print("🔧 Make sure you ran: git remote add origin <your-repo-url>")
            return

        # Clean URL
        repo_url = repo_url_raw.replace(".git", "").strip()

    except Exception as e:
        print(f"❌ Error fetching repo URL: {e}")
        return

    # Project details
    project_title = "Movie Recommendation Engine"
    tech_used = "Python, Pandas, Scikit-Learn, Cosine Similarity"
    key_achievement = "Built a content-based filtering engine for 5,000+ movies."

    # Print portfolio card
    print("\n" + "=" * 50)
    print("🚀 YOUR PROFESSIONAL PORTFOLIO SNIPPET 🚀")
    print("=" * 50)
    print(f"Project: {project_title}")
    print(f"URL:     {repo_url}")
    print(f"Stack:   {tech_used}")
    print(f"Impact:  {key_achievement}")
    print("=" * 50)
    print("\n💡 ACTION: Copy the URL above and add it to your LinkedIn 'Featured' section!")

# Run the snippet generator
if __name__ == "__main__":
    generate_portfolio_snippet()