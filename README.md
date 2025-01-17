# Feelings Analysis with Gemini 1.5 Flash

This project is an end-to-end NLP application that performs sentiment analysis on user-provided comments using Google's Gemini 1.5 Flash model. It features a Streamlit web interface for easy interaction and visualization of results.

## Features

- Upload CSV files containing comments
- Sentiment classification (positive, negative, neutral) using Gemini 1.5 Flash
- Results saved to a new CSV file
- Interactive visualizations:
  - Bar chart of sentiment distribution
  - Word cloud of all comments

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.7+
- A Google Cloud account with access to the Gemini API
- Gemini API key

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/SAAHO-SHANJAI/Feelings-Analysis-with-Gemini.git
   cd Feelings Analysis with Gemini
   ```

2. Install the required packages:
   ```
   pip install streamlit pandas plotly python-dotenv google-generativeai wordcloud matplotlib
   ```

3. Create a `.env` file in the project root and add your Gemini API key:
   ```
   GEMINI_API_KEY=your_api_key_here
   ```

## Usage

1. Run the Streamlit app:
   ```
   streamlit run app.py
   ```

2. Open your web browser and go to the URL provided by Streamlit (usually `http://localhost:8501`).

3. Use the file uploader to select a CSV file containing a 'Comments' column.

4. The app will process the file, perform sentiment analysis, and display the results along with visualizations.

5. The processed data will be saved to a new CSV file named `sentiment_analysis_results.csv` in the project directory.

## File Structure

- `app.py`: The main application file containing the Streamlit interface and sentiment analysis logic
- `.env`: Contains the Gemini API key (not tracked by git)
- `requirements.txt`: List of Python dependencies
- `sentiment_analysis_results.csv`: Output file generated after processing (not tracked by git)

## LIVE APPLICATION

LINK-https://feelings-analysis-with-gemini-whmtubmtrzjljq3ygpbhax.streamlit.app

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Google for providing the Gemini 1.5 Flash model
- Streamlit for the web application framework
- The creators of WordCloud for the word cloud visualization
