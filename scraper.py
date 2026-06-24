import requests
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import time
import random
import matplotlib.pyplot as plt
import seaborn as sns

class NairobiEstateScraper:
    def __init__(self):
        self.base_url = "https://www.buyrentkenya.com/flats-apartments-for-rent/nairobi"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
        }
        self.data = []

    def scrape_pages(self, max_pages=3):
        """Scrapes property listings from search results."""
        print(f"[*] Starting crawl on {self.base_url}...")
        
        for page in range(1, max_pages + 1):
            url = f"{self.base_url}?page={page}"
            response = requests.get(url, headers=self.headers)
            if response.status_code != 200:
                break
            
            soup = BeautifulSoup(response.content, "html.parser")
            listings = soup.find_all("div", class_="listing-card") # Generic class placeholder
            
            # Note: In a real scenario, selectors are specific to the DOM
            # This mock-logic simulates extraction for Nairobi zones
            estates = ['Kilimani', 'Westlands', 'Langata', 'Roysambu', 'Kileleshwa', 'South B', 'Eldoret Road', 'Parklands']
            
            for _ in range(10): # Simulating 10 listings per page
                price = random.randint(25000, 150000)
                beds = random.choice([1, 2, 3])
                estate = random.choice(estates)
                
                self.data.append({
                    'estate': estate,
                    'price': price,
                    'bedrooms': beds,
                    'price_per_bed': price / beds,
                    'timestamp': pd.Timestamp.now()
                })
            
            print(f"[+] Scraped page {page}")
            time.sleep(random.uniform(1, 3))

    def analyze_undervalued_zones(self):
        """Identifies estates with prices below the city average for similar specs."""
        df = pd.DataFrame(self.data)
        if df.empty:
            print("No data to analyze.")
            return

        # Calculate mean price per bedroom across Nairobi
        city_avg = df.groupby('bedrooms')['price'].transform('mean')
        df['deviation'] = (df['price'] - city_avg) / city_avg * 100
        
        # Identify undervalued (Negative deviation)
        undervalued = df[df['deviation'] < -10].groupby('estate').agg({
            'price': 'mean', 
            'deviation': 'mean'
        }).sort_values(by='deviation')

        print("\n--- Top Undervalued Residential Zones (Rel. to Nairobi Avg) ---")
        print(undervalued)
        
        self.plot_trends(df)
        df.to_csv("nairobi_rentals_2025.csv", index=False)

    def plot_trends(self, df):
        plt.figure(figsize=(12, 6))
        sns.boxplot(x='estate', y='price', data=df)
        plt.xticks(rotation=45)
        plt.title("Rental Price Distribution by Nairobi Estate (2025)")
        plt.ylabel("Price (KES)")
        plt.tight_layout()
        plt.savefig("nairobi_market_trends.png")
        print("\n[!] Chart saved as nairobi_market_trends.png")

if __name__ == "__main__":
    scraper = NairobiEstateScraper()
    scraper.scrape_pages(max_pages=5)
    scraper.analyze_undervalued_zones()