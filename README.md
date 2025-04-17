# DevInsights Dashboard

**DevInsights** is a Python-based productivity dashboard that gives insights into GitHub repositories by analyzing commits, issues, and pull requests. It’s built with Streamlit and powered by the GitHub API — perfect for showcasing product thinking, data analysis, and full-stack Python skills as a Technical Product Manager.

---

## Features

- 📊 Summary of commits, issues, and PRs
- ⏱ Issue resolution time analysis
- 🧩 Uses GitHub API with authentication
- 📉 Interactive charts using Streamlit

---

## Tech Stack

- Python
- Streamlit
- GitHub API
- Pandas
- Requests
- dotenv (`python-dotenv`)

---

## Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/devinsights-dashboard.git
cd devinsights-dashboard
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Create a `.env` File
Create a `.env` file in the root directory with the following line:
```env
GITHUB_TOKEN=your_personal_access_token
```
> 💡 [How to generate a GitHub token](https://github.com/settings/tokens)

### 4. Run the App
```bash
streamlit run dev-dashboard.py
```

---

## Example Use Cases

- Engineering managers tracking team velocity
- Product managers measuring dev throughput
- Showcasing API, data handling, and product metrics in technical interviews

---

## 🛡 Security Note

This project uses environment variables to protect your API token. Be sure to include `.env` in your `.gitignore` and never commit secrets.

---

## 📄 License

MIT License – use freely with attribution!

---

## 🙌 Contributing

Feel free to open issues or submit PRs to enhance the dashboard or add new insights.

---

## 📬 Contact

Made by Souljadev – souljadevgit@gmail.com