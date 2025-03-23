import requests
from bs4 import BeautifulSoup
from transformers import pipeline, VitsModel, AutoTokenizer
import torch
import scipy.io.wavfile as wav
import os

# News Extraction
def fetch_news(company_name):
    api_key = os.getenv("NEWSAPI_KEY", "14c0c7c5415b48e093fad78a1fd9581b")
    url = f"https://newsapi.org/v2/everything?q={company_name}&apiKey={api_key}"
    response = requests.get(url)
    
    if response.status_code == 200:
        articles = response.json().get("articles", [])
        result = []
        for article in articles:
            try:
                page = requests.get(article['url'])
                soup = BeautifulSoup(page.content, 'html.parser')
                content = ' '.join([p.text for p in soup.find_all('p')])
            except:
                content = article.get('description', 'No content available')
            
            result.append({
                "title": article['title'],
                "content": content
            })
        return result
    return []

# Sentiment Analysis
sentiment_analyzer = pipeline("sentiment-analysis")
def analyze_sentiment(text):
    result = sentiment_analyzer(text[:512])[0]
    label = result['label']
    if label == "POSITIVE":
        return "Positive"
    elif label == "NEGATIVE":
        return "Negative"
    else:
        return "Neutral"

# Text Summarization
summarizer = pipeline("summarization")
def summarize_text(text):
    try:
        summary = summarizer(text[:1024], max_length=50, min_length=25, do_sample=False)[0]['summary_text']
        return summary
    except:
        return text[:100] + "..."

# Hindi TTS using Hugging Face MMS-TTS
model = VitsModel.from_pretrained("facebook/mms-tts-hin")
tokenizer = AutoTokenizer.from_pretrained("facebook/mms-tts-hin")

def generate_hindi_tts(text):
    try:
        # Tokenize input text (limit length to avoid model issues)
        inputs = tokenizer(text[:200], return_tensors="pt")  # Limit to 200 chars for stability
        with torch.no_grad():
            outputs = model(**inputs).waveform
        
        # Normalize audio data
        audio_data = outputs.squeeze().cpu().numpy()
        if audio_data.ndim > 1:
            audio_data = audio_data[0]  # Ensure 1D array
        
        # Save as WAV file
        audio_file = "output.wav"
        wav.write(audio_file, rate=model.config.sampling_rate, data=audio_data)
        return audio_file
    except Exception as e:
        raise Exception(f"TTS generation failed: {str(e)}")