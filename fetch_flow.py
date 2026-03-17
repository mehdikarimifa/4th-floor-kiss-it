import requests
import os

# The specific Google Flow URL you want to mirror
TARGET_URL = "https://labs.google/flow" 
OUTPUT_DIR = "docs"

def fetch_and_save():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
        
    # We spoof a real browser header to avoid being blocked by Google
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    
    response = requests.get(TARGET_URL, headers=headers)
    
    # Save the main HTML
    with open(f"{OUTPUT_DIR}/index.html", "w", encoding="utf-8") as f:
        # We perform a tiny 'hack' here: 
        # Replacing relative links so they don't break on GitHub Pages
        content = response.text.replace('href="/', 'href="https://labs.google/')
        content = content.replace('src="/', 'src="https://labs.google/')
        f.write(content)

if __name__ == "__main__":
    fetch_and_save()
