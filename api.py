from fastapi import FastAPI
from utils import fetch_news, analyze_sentiment, summarize_text

app = FastAPI()

@app.get("/news/{company_name}")
def get_news(company_name: str):
    articles = fetch_news(company_name)
    return {"company": company_name, "articles": articles}

@app.get("/analyze/{company_name}")
def analyze_company(company_name: str):
    articles = fetch_news(company_name)
    report = {"Company": company_name, "Articles": []}
    
    for article in articles[:10]:
        summary = summarize_text(article['content'])
        sentiment = analyze_sentiment(article['content'])
        report["Articles"].append({
            "Title": article['title'],
            "Summary": summary,
            "Sentiment": sentiment,
            "Topics": ["Business"]
        })
    return report