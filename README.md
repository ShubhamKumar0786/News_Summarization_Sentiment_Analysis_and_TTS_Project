# News Summarization and Sentiment Analysis

This project is a web-based application that fetches news articles for a given company, summarizes the content, performs sentiment analysis, and generates a Hindi text-to-speech (TTS) summary. It uses a combination of a Streamlit frontend for user interaction and a FastAPI backend for API-based access to the core functionality. The app is also deployed on Hugging Face Spaces for easy access.

## Features
- **News Fetching**: Retrieves news articles for a specified company using the NewsAPI.
- **Text Summarization**: Summarizes article content using a pre-trained transformer model.
- **Sentiment Analysis**: Analyzes the sentiment (Positive, Negative, Neutral) of each article.
- **Hindi TTS**: Generates an audio summary in Hindi using a pre-trained TTS model.
- **Web Interface**: Provides an interactive UI via Streamlit to input company names and view results.
- **API Access**: Exposes endpoints via FastAPI for programmatic access to news and analysis.

## Dependencies
The project relies on the following Python libraries:
- `streamlit`: For building the interactive web interface.
- `requests`: For making HTTP requests to fetch news data.
- `beautifulsoup4`: For scraping article content from web pages.
- `transformers`: For text summarization, sentiment analysis, and TTS generation.
- `torch`: For running transformer models.
- `scipy`: For handling audio file generation.
- `fastapi`: For creating a RESTful API.
- `uvicorn`: For serving the FastAPI application.

## Project Structure
- **`main.py`** (assumed name for the Streamlit app):
  - Defines the Streamlit frontend.
  - Handles user input, displays results, and plays Hindi TTS audio.
- **`utils.py`**:
  - Contains core functions for fetching news, sentiment analysis, summarization, and TTS generation.
- **`api.py`** (assumed name for the FastAPI app):
  - Defines API endpoints for news fetching and analysis.
- **`requirements.txt`**:
  - Lists all Python dependencies required for the project.

## Core Functionality

### 1. News Fetching (`fetch_news`)
- Uses the NewsAPI to fetch articles based on a company name.
- Scrapes full article content using BeautifulSoup if available; otherwise, uses the article description.
- Returns a list of dictionaries with `title` and `content`.

### 2. Sentiment Analysis (`analyze_sentiment`)
- Uses a pre-trained sentiment analysis model from Hugging Face's `transformers`.
- Classifies text as "Positive", "Negative", or "Neutral".
- Limits input to 512 characters to avoid model constraints.

### 3. Text Summarization (`summarize_text`)
- Uses a pre-trained summarization model from `transformers`.
- Summarizes text to 25-50 words, truncating input to 1024 characters.
- Falls back to a truncated version of the original text if summarization fails.

### 4. Comparative Analysis
- Aggregates sentiment scores across articles to provide a distribution (e.g., Positive: 6, Negative: 2, Neutral: 2).
- Generates a textual summary in English, such as "Positive articles focus on [company]'s growth, while negative ones highlight challenges."
- Included in the JSON report and used as a basis for the Hindi TTS summary.

### 5. Hindi TTS (`generate_hindi_tts`)
- Uses the `facebook/mms-tts-hin` model from Hugging Face for Hindi TTS.
- Converts a text summary (limited to 200 characters) into a WAV audio file.
- Incorporates the comparative analysis into the audio output (e.g., "सकारात्मक लेखों में वृद्धि पर ध्यान है").
- Handles exceptions and ensures audio data is correctly formatted.

### 6. Streamlit Frontend
- Provides a simple UI to:
  - Input a company name (e.g., Tesla, Amazon, Apple).
  - Fetch and analyze up to 10 articles.
  - Display a JSON report with titles, summaries, sentiments, and a comparative analysis.
  - Play a Hindi TTS summary as audio.

### 7. FastAPI Backend
- Exposes two endpoints:
  - `/news/{company_name}`: Returns raw news articles.
  - `/analyze/{company_name}`: Returns a report with summaries and sentiments for up to 10 articles.


## Deployment on Hugging Face Spaces
This project has been deployed on Hugging Face Spaces, making it accessible online without local setup. Here’s how it was deployed and how you can use or replicate it:

### Deployment Steps
1. **Create a Space**:
   - Go to [Hugging Face Spaces](https://huggingface.co/spaces) and create a new Space.
   - Choose "Streamlit" as the framework since the frontend uses Streamlit.

2. **Upload Files**:
   - Upload `api.py`,`apy.py`, `utils.py`, and `requirements.txt`.
   - Ensure the NewsAPI key is added as a Secret in the Space settings (Settings > Secrets > Add `NEWSAPI_KEY`).

3. **Configure `requirements.txt`**:
   ```
   streamlit
   requests
   beautifulsoup4
   transformers
   torch
   scipy
   fastapi
   uvicorn
   ```
   Hugging Face Spaces will automatically install these dependencies.

4. **Set Up the App**:
   - The Space runs `streamlit run main.py` by default, providing the interactive UI.
  

5. **Deploy**:
   - Commit the files and let Hugging Face build the Space.
   - Once built, the app is live at a https://huggingface.co/Shubham0786 

### Accessing the Deployed App
- Visit the Hugging Face Space https://huggingface.co/spaces/Shubham0786/News_Summarization_and_Sentiment_Analysis
- Enter a company name in the text input and click "Analyze" to see the results and hear the Hindi TTS summary.


## Usage 

### Streamlit UI (Hugging Face)
1. Open the app .
2. Enter a company name (e.g., "Tesla","Amazon","Apple").
3. Click "Analyze".
4. View the JSON report andnPlayable audio file summarizing the sentiment report.


## Preview



https://github.com/user-attachments/assets/8bf695a6-50ec-478c-872a-02bfdd620ea5






## Output
### Streamlit JSON Report
```json
{
  "Company": "Tesla",
  "Articles": [
    {
      "Title": "Tesla's New Factory Opens",
      "Summary": "Tesla opened a new factory in Shanghai, boosting production.",
      "Sentiment": "Positive",
      "Topics": ["Business"]
    },
    ...
  ],
  "Comparative Sentiment Score": {
    "Sentiment Distribution": {"Positive": 6, "Negative": 2, "Neutral": 2}
  },
  "Comparative Analysis": "Positive articles focus on Tesla's growth, while negative ones highlight challenges."
}
```

### Hindi TTS Audio
- Generated audio file (`output.wav`) with a summary like:
  "टेस्ला की खबरों का सारांश: कुल 10 लेख मिले। सकारात्मक: 6, नकारात्मक: 2, तटस्थ: 2।"

## Feedback and Contributions

We welcome contributions! If you have improvements, or suggestions, please open an issue or submit a pull request.
- 🌐 [GitHub Profile](https://github.com/ShubhamKumar0786https://github.com/ShubhamKumar0786)  
- 📧 Email:shubhamkashyap9501@gmail.com
- LinkedIn: [Linkedin_link](https://www.linkedin.com/in/shubham0786/)


## License
This project is open-source and available under the MIT License.

---
