import streamlit as st
from utils import fetch_news, analyze_sentiment, summarize_text, generate_hindi_tts

st.title("News Summarization and Sentiment Analysis")

# Input company name
company_name = st.text_input("Enter Company Name")

if st.button("Analyze"):
    # Fetch news
    articles = fetch_news(company_name)
    
    if articles:
        st.write(f"Found {len(articles)} articles for {company_name}")
        report = {"Company": company_name, "Articles": [], "Comparative Sentiment Score": {"Sentiment Distribution": {"Positive": 0, "Negative": 0, "Neutral": 0}}}

        # Process each article
        for article in articles[:10]:  # Limit to 10 articles
            summary = summarize_text(article['content'])
            sentiment = analyze_sentiment(article['content'])
            topics = ["Business"]  # Placeholder
            
            report["Articles"].append({
                "Title": article['title'],
                "Summary": summary,
                "Sentiment": sentiment,
                "Topics": topics
            })
            report["Comparative Sentiment Score"]["Sentiment Distribution"][sentiment] += 1

        # Comparative Analysis in English
        sentiment_dist = report["Comparative Sentiment Score"]["Sentiment Distribution"]
        comparative = f"Positive articles focus on {company_name}'s growth, while negative ones highlight challenges."
        report["Comparative Analysis"] = comparative

        # Display report
        st.json(report)

        # Generate detailed Hindi TTS summary
        hindi_summary = (
            f"{company_name} की खबरों का सारांश: "
            f"कुल {len(report['Articles'])} लेख मिले। "
            f"सकारात्मक: {sentiment_dist['Positive']}, "
            f"नकारात्मक: {sentiment_dist['Negative']}, "
            f"तटस्थ: {sentiment_dist['Neutral']}। "
            f"सकारात्मक लेखों में {company_name} की वृद्धि पर ध्यान है, जबकि नकारात्मक लेख चुनौतियों को उजागर करते हैं।"
        )
        
        try:
            audio_file = generate_hindi_tts(hindi_summary)
            st.audio(audio_file, format="audio/wav")
            st.success("Hindi TTS audio generated and playable above!")
        except Exception as e:
            st.error(f"Error generating audio: {str(e)}")

    else:
        st.error("No articles found!")
