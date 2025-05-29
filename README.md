# 🤖 AI Lead Generation Agent

This is a Streamlit app that scrapes real-time company data for businesses likely eligible for funding programs like SR&ED. It outputs the results in Excel and Word formats.

## 🚀 Features
- Autonomous web scraping using Bing search
- Collects company name, website, summary, and placeholder executive details
- Generates downloadable Excel and Word reports
- Customizable by industry, location, and funding program

## 📦 Requirements
Install dependencies:
```bash
pip install -r requirements.txt
```

## ▶️ Run Locally
```bash
streamlit run app.py
```

## 📤 Deploy to GitHub
1. Create a new repository on GitHub (e.g., `ai-lead-agent`)
2. Push your project files:
```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/ai-lead-agent.git
git push -u origin main
```

## ☁️ Deploy on Vercel or Streamlit Cloud
### Option 1: [Streamlit Community Cloud](https://streamlit.io/cloud)
- Connect your GitHub repo
- Add `app.py` as the main entry point
- App auto-deploys

### Option 2: Vercel Workaround (Experimental)
Streamlit doesn't natively support Vercel. Use this method only if needed:
- Create a `vercel.json` file with a Python server config
- Use Docker + serverless function adapter (not recommended for Streamlit)

## ✅ To-Do (Advanced)
- Real contact info enrichment (via LinkedIn, Apollo.io, etc.)
- Scheduler for periodic scraping
- Duplicate filtering

## 📄 Output Example
Excel: Leads in rows with structured fields
Word: Company summary in readable format

---
Built with ❤️ using Streamlit + BeautifulSoup + Python
