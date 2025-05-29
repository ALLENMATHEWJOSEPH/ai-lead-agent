# app.py
import streamlit as st
from scraper import scrape_leads
from exporter import export_to_excel, export_to_word

st.set_page_config(page_title="AI Lead Generation Agent", layout="centered")
st.title("🤖 AI Lead Generation Agent")

with st.form("lead_form"):
    industry = st.text_input("Industry", value="Technology")
    location = st.text_input("Location", value="Canada")
    funding = st.selectbox("Funding Program", ["SR&ED", "Innovation Grants", "R&D Incentives"])
    min_leads = st.slider("Number of Leads", min_value=10, max_value=100, value=20)
    submitted = st.form_submit_button("Generate Leads")

if submitted:
    with st.spinner("Scraping real data from the web..."):
        try:
            leads = scrape_leads(industry, location, funding, min_leads)
        except Exception as e:
            st.error(f"Error occurred during scraping: {e}")
            leads = []

    if leads:
        st.success(f"Generated {len(leads)} leads!")
        excel_path = export_to_excel(leads)
        word_path = export_to_word(leads)

        st.markdown("### Download Your Lead Files")
        with open(excel_path, "rb") as f:
            st.download_button("📊 Download Excel (Structured Data)", f, file_name="leads.xlsx")
        with open(word_path, "rb") as f:
            st.download_button("📄 Download Word (Summary Report)", f, file_name="summary.docx")
    else:
        st.error("No leads found. Try different filters.")
