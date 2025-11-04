import pandas as pd
from google_play_scraper import app, reviews, Sort
import time
import json

print("Memulai proses scraping...")

# ID aplikasi Shopee di Google Play Store
APP_ID = 'com.shopee.id'
TARGET_COUNT = 11000  # Target 11.000 data

# Proses scraping menggunakan 'reviews'
# Menggunakan Sort.NEWEST agar mendapat review terbaru
# Scrape dalam bahasa Indonesia ('id')
result, continuation_token = reviews(
    APP_ID,
    lang='id',
    country='id',
    sort=Sort.NEWEST,
    count=TARGET_COUNT,
    filter_score_with=None  # Ambil semua skor
)

print(f"Berhasil mengumpulkan {len(result)} data review.")

# Mengubah hasil scraping menjadi DataFrame pandas
df_reviews = pd.DataFrame(result)

# Pilih kolom yang relevan saja
# 'content' adalah teks review, 'score' adalah rating bintang
df_final = df_reviews[['content', 'score', 'at']]
df_final = df_final.rename(columns={'content': 'text', 'at': 'timestamp'})

# Simpan ke file CSV
OUTPUT_FILE = 'dataset_mentah.csv'
df_final.to_csv(OUTPUT_FILE, index=False)

print(f"Data mentah berhasil disimpan ke {OUTPUT_FILE}")

# Tampilkan 5 data pertama
print("\nContoh 5 data pertama:")
print(df_final.head())