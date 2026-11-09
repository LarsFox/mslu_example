import requests
from bs4 import BeautifulSoup

# Example URL: An article from the site
url = "https://motovskikh.ru/"

# 1. Fetch the page
try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()  # Check for HTTP errors
except requests.exceptions.RequestException as e:
    print(f"Error fetching the page: {e}")
    exit()

# 2. Parse the HTML
soup = BeautifulSoup(response.text, "html.parser")

# 3. Extract the Title
# Based on the site structure, the title is usually in an <h1> tag
title_tag = soup.find("h1")
if title_tag:
    print(f"Title: {title_tag.get_text(strip=True)}")
else:
    print("Title not found.")

print("-" * 30)

# 4. Extract the Main Content
# The text is typically contained within paragraph tags <p> inside the main body.
# We can find all paragraphs and print their text.
paragraphs = soup.find_all("p")

if paragraphs:
    print("Content Preview:")
    for p in paragraphs:
        text = p.get_text(strip=True)
        if text:  # Skip empty paragraphs
            print(text)
            # Optional: Stop after a few paragraphs for a preview
            # break 
else:
    print("No paragraph content found.")


time.sleep(4)
