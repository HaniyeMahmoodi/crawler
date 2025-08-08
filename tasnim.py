import requests
from bs4 import BeautifulSoup
import csv
import time

# =============================
# ⚙️ تنظیمات
START_PAGE = 36001    # صفحه شروع
END_PAGE = 50000  # صفحه پایان
PAGES_PER_FILE = 500
BASE_URL = "https://rojnews.news/?p={}"
HEADERS = {
    "User-Agent": "Mozilla/5.0"
}
# =============================

def scrape_page(page_id):
    url = BASE_URL.format(page_id)
    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
        if response.status_code != 200:
            return {"URL": url, "Title": "", "Body": "", "Time and Date": ""}

        soup = BeautifulSoup(response.text, "html.parser")

        title = soup.select_one("span[itemprop='headline']")
        body = soup.select_one("article")
        datetime = soup.select_one(".post-published b")

        return {
            "URL": url,
            "Title": title.get_text(strip=True) if title else "",
            "Body": body.get_text(strip=True) if body else "",
            "Time and Date": datetime.get_text(strip=True) if datetime else ""
        }
    except Exception as e:
        print(f"❌ Error on page {page_id}: {e}")
        return {"URL": url, "Title": "", "Body": "", "Time and Date": ""}

def main():
    all_data = []
    file_index = 73
    for i, page_id in enumerate(range(START_PAGE, END_PAGE + 1), start=1):
        print(f"📄 Scraping page: {page_id}")
        data = scrape_page(page_id)
        all_data.append(data)

        # ذخیره هر ۵۰۰ صفحه یا پایان کار
        if i % PAGES_PER_FILE == 0 or page_id == END_PAGE:
            filename = f"rojnews_{file_index}.csv"
            with open(filename, "w", encoding="utf-8-sig", newline="") as f:
                writer = csv.DictWriter(f, fieldnames=["URL", "Title", "Body", "Time and Date"])
                writer.writeheader()
                writer.writerows(all_data)
            print(f"✅ Saved {len(all_data)} records to {filename}")
            all_data = []
            file_index += 1

        time.sleep(1)  # برای کاهش فشار روی سرور

if __name__ == "__main__":
    main()
