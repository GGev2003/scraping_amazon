🚀 Amazon Product Scraper 🛒

A powerful Python-based web scraper that extracts gaming headset data from Amazon using Selenium and BeautifulSoup (bs4). This script automates pagination, collects product details, and stores them in HTML & JSON for easy analysis.

🔥 Features

✔ Automated Pagination – Scrapes multiple pages seamlessly (up to 20 pages).
✔ Extracts Key Product Data – Name, Price, Reviews, Delivery Info.
✔ Structured Output – Saves data in HTML (raw) and JSON (processed).
✔ Error Handling – Gracefully handles missing data and file operations.
✔ Headless-Ready – Can be modified for silent browser execution.

📦 Tech Stack

Python 🐍

Selenium 🌐 (for dynamic page interaction & pagination)

BeautifulSoup (bs4) 🍜 (for parsing HTML content)

JSON 📄 (for structured data storage)



📊 Data Extracted

Product Name 📛

Price 💰 (in USD)

Customer Reviews ⭐

Delivery Info 🚚

Raw HTML (for backup & extended parsing)


🛠️ How It Works

Opens Amazon and searches for "gaming headsets".

Automatically clicks through pages (1-20) using Selenium.

Saves each page’s HTML for backup.

Parses product details (name, price, reviews, delivery) using BeautifulSoup.

Exports clean JSON data for each page.