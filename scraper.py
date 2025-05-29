# scraper.py
import requests
from bs4 import BeautifulSoup
import time

def scrape_leads(industry, location, funding, min_leads):
    query = f"{industry} companies in {location} eligible for {funding}"
    headers = {"User-Agent": "Mozilla/5.0"}
    leads = []
    seen_urls = set()

    for i in range(0, 100, 10):
        if len(leads) >= min_leads:
            break

        url = f"https://www.bing.com/search?q={query}&first={i}"
        res = requests.get(url, headers=headers)
        soup = BeautifulSoup(res.text, "html.parser")
        results = soup.select("li.b_algo h2 a")

        for link in results:
            href = link.get("href")
            if href and href not in seen_urls:
                seen_urls.add(href)
                company_name = link.text.strip()
                summary = get_summary(href)

                lead = {
                    "Company Name": company_name,
                    "Website": href,
                    "CEO Name": "N/A",
                    "CEO Email": "N/A",
                    "CEO Phone": "N/A",
                    "CFO Name": "N/A",
                    "CFO Email": "N/A",
                    "CFO Phone": "N/A",
                    "Contact Person Name": "N/A",
                    "Contact Email": "N/A",
                    "Company Summary": summary
                }
                leads.append(lead)

        time.sleep(2)

    return leads

def get_summary(url):
    try:
        res = requests.get(url, timeout=5)
        soup = BeautifulSoup(res.text, "html.parser")
        ps = soup.find_all("p")
        for p in ps:
            txt = p.get_text().strip()
            if len(txt) > 100:
                return txt[:300] + "..."
        return "No description available."
    except:
        return "No description available."

