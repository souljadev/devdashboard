# dev dashboard
# A developer productivity dashboard using GitHub API, Pandas, and Streamlit

import requests
import pandas as pd
import streamlit as st
from datetime import datetime, timedelta
from dotenv import load_dotenv
import os

load_dotenv()
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
HEADERS = {"Authorization": f"token {GITHUB_TOKEN}"} if GITHUB_TOKEN else {}
GITHUB_API = "https://api.github.com"

# --- FUNCTIONS ---
def get_commits(owner, repo):
    url = f"{GITHUB_API}/repos/{owner}/{repo}/commits"
    response = requests.get(url, headers=HEADERS)
    if response.status_code == 200:
        return response.json()
    return []

def get_issues(owner, repo, state="all"):
    url = f"{GITHUB_API}/repos/{owner}/{repo}/issues?state={state}"
    response = requests.get(url, headers=HEADERS)
    if response.status_code == 200:
        return [i for i in response.json() if 'pull_request' not in i]
    return []

def get_pull_requests(owner, repo, state="all"):
    url = f"{GITHUB_API}/repos/{owner}/{repo}/pulls?state={state}"
    response = requests.get(url, headers=HEADERS)
    if response.status_code == 200:
        return response.json()
    return []

# --- STREAMLIT APP ---
st.title("🚀 DevInsights: Developer Productivity Dashboard")

owner = st.text_input("GitHub Owner (username or org)", value="grubhub")
repo = st.text_input("Repository Name", value="public-repo-name")

if st.button("Fetch Data"):
    with st.spinner("Fetching data from GitHub..."):
        commits = get_commits(owner, repo)
        issues = get_issues(owner, repo)
        prs = get_pull_requests(owner, repo)

    st.subheader("📈 Summary")
    st.write(f"**Commits:** {len(commits)}")
    st.write(f"**Issues:** {len(issues)}")
    st.write(f"**Pull Requests:** {len(prs)}")

    if issues:
        df_issues = pd.DataFrame([{
            "Title": i["title"],
            "State": i["state"],
            "Created At": i["created_at"],
            "Closed At": i.get("closed_at")
        } for i in issues])
        df_issues["Created At"] = pd.to_datetime(df_issues["Created At"])
        df_issues["Closed At"] = pd.to_datetime(df_issues["Closed At"])
        df_issues["Resolution Time"] = df_issues["Closed At"] - df_issues["Created At"]

        st.subheader("📊 Issue Resolution Time")
        st.bar_chart(df_issues["Resolution Time"].dt.days.dropna())
