# 📊 Adobe Stock Search Volume Tool

Get **live Adobe Stock Video search counts** for any event or keyword.  
Paste your events → fetch counts via [Jina AI Reader](https://jina.ai/api-dashboard) → download as XLSX.

Built with [Streamlit](https://streamlit.io).

---

## ✨ Features

- 🔑 **Bring your own API key** – users provide their own free Jina AI key (never stored)
- 📝 **Paste events** – one per line, optional date prefix (e.g. `January 1 - New Year's Day`)
- 🚀 **Live counts** – fetches real-time Adobe Stock Video search results via Jina AI
- 📥 **Download XLSX** – structured spreadsheet with dates, event names, and counts
- 🌐 **Public web app** – deployable on Streamlit Community Cloud (free)

---

## 🚀 Live Demo (Streamlit Cloud)

https://adobe-search-volume-tool.streamlit.app

> *Deploy your own copy by forking this repo and following the steps below.*

---

## 🧪 Run Locally

### Prerequisites

- Python 3.10+
- A free [Jina AI API key](https://jina.ai/api-dashboard) (1 minute to get)

### Setup

```bash
# Clone the repo
git clone https://github.com/nmohamma/adobe-search-volume-tool.git
cd adobe-search-volume-tool

# Create and activate a virtual environment (recommended)
python -m venv .venv
# Windows (Git Bash / MSYS):
source .venv/Scripts/activate
# Windows (CMD):
# .venv\Scripts\activate.bat
# Windows (PowerShell):
# .venv\Scripts\Activate.ps1
# macOS / Linux:
# source .venv/bin/activate

# Install dependencies
pip install -r streamlit_app/requirements.txt

# Run the app
streamlit run streamlit_app/app.py
```

Open `http://localhost:8501` in your browser.

---

## 🖥️ Usage

1. **Enter your Jina AI API key** (password field – never stored on any server)
2. **Paste events** – one per line. Optionally prefix with a date:
   ```
   New Year's Day
   Valentine's Day
   January 1 - New Year's Day
   March 17 - St. Patrick's Day
   Diwali
   ```
3. Click **"Get Search Counts"** – progress bar shows each event being fetched
4. **Download the XLSX** – structured spreadsheet with all results

---

## ☁️ Deploy on Streamlit Community Cloud (Free)

1. Push this repo to GitHub (public repo required for free tier)
2. Go to [streamlit.io/cloud](https://streamlit.io/cloud)
3. Sign in with GitHub → **New app**
4. **Repository:** `nmohamma/adobe-search-volume-tool`
5. **Branch:** `master` (or `main`)
6. **Main file path:** `streamlit_app/app.py`
7. Click **Deploy**

Your app will be live at `https://your-app-name.streamlit.app`.

---

## 📁 Project Structure

```
streamlit_app/
├── app.py              # Streamlit UI (main entry point)
├── fetch_utils.py      # Jina AI fetch, text parser, XLSX builder
└── requirements.txt    # Python dependencies
```

---

## 🔐 Security

- **Your Jina API key** is used only for the current browser session – never stored on any server
- **Users bring their own API key** – the app doesn't use a shared key
- The `.env` file with your personal key is excluded from Git via `.gitignore`

---

## 🛠️ Tech Stack

- **[Streamlit](https://streamlit.io)** – Python web framework
- **[Jina AI Reader](https://r.jina.ai)** – web scraping API bypassing bot protection
- **[OpenPyXL](https://openpyxl.readthedocs.io)** – XLSX generation
- **[Requests](https://requests.readthedocs.io)** – HTTP client
- **[Pandas](https://pandas.pydata.org)** – data display

---

## 📄 License

MIT – feel free to use, modify, and share.
