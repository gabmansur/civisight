import requests
from bs4 import BeautifulSoup
import json
import re
from pathlib import Path

# Map of known politician URLs on parlement.com
politicians = {
    "Pieter Omtzigt": "https://www.parlement.com/id/vg09llj2z1z3/p_h_c_m_pieter_omtzigt",
    "Sigrid Kaag": "https://www.parlement.com/id/vj1c2y69ph5t/s_a_m_sigrid_kaag",
    "Mark Rutte": "https://www.parlement.com/id/vge7dm5pmszl/m_mark_rutte"
}

def extract_bio(soup):
    """Get the 'biografie' section as plain text"""
    bio_section = soup.find("div", class_="biografie")
    if bio_section:
        return bio_section.get_text(separator=" ", strip=True)
    return "Biography not available."

def extract_party(soup):
    """Try to find the party by looking at list items"""
    for li in soup.find_all("li"):
        if "partij" in li.get_text().lower():
            return li.get_text().split(":")[-1].strip()
    return "Unknown"

def extract_birth(soup):
    """Find birth year and city from profile header"""
    header = soup.find("div", class_="profiel_head")
    if not header:
        return "Unknown", "Unknown"

    text = header.get_text()
    year_match = re.search(r"\b(\d{4})\b", text)
    city_match = re.search(r"\s+in\s+([A-Za-zéëä -]+)", text)

    return (
        year_match.group(1) if year_match else "Unknown",
        city_match.group(1).strip() if city_match else "Unknown"
    )

def scrape_profile(name, url):
    print(f"[•] Scraping {name}")
    res = requests.get(url)
    if res.status_code != 200:
        print(f"[!] Failed to fetch {name}")
        return None

    soup = BeautifulSoup(res.text, "html.parser")

    bio = extract_bio(soup)
    party = extract_party(soup)
    birth_year, city = extract_birth(soup)

    return {
        "name": name,
        "party": party,
        "birth_year": birth_year,
        "city": city,
        "topics": [],  # Not easy to scrape here
        "bio": bio,
        "sentiment": "Coming soon",
        "leaning": "Coming soon"
    }

def main():
    data = []
    for name, url in politicians.items():
        profile = scrape_profile(name, url)
        if profile:
            data.append(profile)

    Path("data/processed").mkdir(parents=True, exist_ok=True)
    with open("data/processed/parlement_politicians.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"[✓] Scraped {len(data)} profiles into parlement_politicians.json")

if __name__ == "__main__":
    main()