# ⚽ FBRef Scraper 🐍

[![License](https://img.shields.io/github/license/patel-mark/fbref-scraper)](LICENSE)  
[![Python](https://img.shields.io/badge/Python-3.x-blue)]  
[![Status](https://img.shields.io/badge/Status-Production--ready-brightgreen)]  

> A lightweight Python scraper to pull player and match statistics from **FBref.com**, exporting clean `.csv` files for analysis.

---

## 🚀 Features

- Scrapes detailed player stats and match data directly from **FBref.com**.
- Supports multiple top European leagues (Premier League, La Liga, Serie A, Ligue 1, Bundesliga) from recent seasons :contentReference[oaicite:1]{index=1}.
- Extracts CSVs with:
  - Fixture-level data: match date, teams, score, xG, etc.
  - Player-level stats: goals, assists, xG/xA, defensive stats, passing metrics, keeper stats, and more :contentReference[oaicite:2]{index=2}.
- Automatically handles HTML comments and hidden table parsing (FBref wraps tables in comments) :contentReference[oaicite:3]{index=3}.

---

## 🛠 Tech Stack

- **Language**: Python 3.x
- **Libraries**:
  - `requests`, `pandas`, `BeautifulSoup4`
- **Outputs**: `.csv` files—ready for data analysis pipelines

---

## 🔧 Installation

```bash
git clone https://github.com/patel-mark/fbref-scraper.git
cd fbref-scraper
pip install -r requirements.txt
````

---

## 📦 Usage

Run the scraper script:

```bash
python fbref_scraper.py
```

You'll be prompted to choose:

* ⚽ League (e.g., Premier League)
* 📅 Season (e.g., 2022-23)

The script then:

* Scrapes fixture and player stats.
* Saves two CSV files:

  * `fixtures_<league>_<season>.csv`
  * `players_<league>_<season>.csv`

> ⚠️ **Tip**: Scrape one league-season at a time to avoid IP blocking, as FBref enforces rate limits ([GitHub][1], [EduFootball Analytics][2]).

---

## 🧹 Data Details

### Fixture CSV includes:

* Game week, date, teams, final score, xG home/away, season, game ID ([GitHub][1])

### Player CSV covers:

* Demographics: name, shirt number, nationality, position, age
* Play metrics: minutes, goals, assists, shots, cards
* xG/xA values, passing stats, tackles, interceptions, carries, attacking actions, etc.
* Goalkeeper-specific: saves, save %, PSxG conceded, goal kicks, crosses faced/stopped ([GitHub][1])

---

## ⚠️ Rate Limiting

FBref restricts scraping to \~1 request per 6 seconds. Ensure your script respects this to avoid being blocked.
You may add delays (`time.sleep(6)`) between page requests.

---

## 🛡️ License

Licensed under the **MIT License**.
Data belongs to **fbref.com** and StatsBomb; this tool doesn’t claim ownership ([FBR API][3], [GitHub][1]).

---

## 📄 Acknowledgements

Inspired by community FBref scrapers and tutorials:

* Adam Corren’s \[fbref\_football\_player\_data\_scraper] ([GitHub][1])
* Techniques to extract hidden tables from FBref ([Stack Overflow][4])

---

## 🤝 Contribution

1. Fork it
2. Create your feature branch (`git checkout -b feature/foo`)
3. Commit your changes (`git commit -am 'Add feature'`)
4. Push (`git push origin feature/foo`)
5. Open a pull request

---

## 🔗 Resources

* FBref.com – source of football stats
* BeautifulSoup4 – HTML parsing in Python
* pandas – data handling & CSV export

---

Made by [@patel-mark](https://github.com/patel-mark)

