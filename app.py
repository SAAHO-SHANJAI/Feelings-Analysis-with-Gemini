import streamlit as st
import pandas as pd
import plotly.express as px
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import google.generativeai as genai

# Configure Gemini API with the API key directly
genai.configure(api_key="AIzaSyCp62avOSJCp4QIE21Vb2j2UljmhrBvnvU")

# Initialize Gemini model
model = genai.GenerativeModel('gemini-1.5-flash')

def classify_sentiment(comment):
    prompt = f"""Classify the sentiment of the following comment as either 'positive', 'negative', or 'neutral'. 
    Respond with ONLY ONE of these three words, nothing else.
    
    Comment: '{comment}'
    
    Classification:"""
    
    response = model.generate_content(prompt)
    sentiment = response.text.strip().lower()
    
    # Ensure only valid responses are returned
    if sentiment not in ['positive', 'negative', 'neutral']:
        sentiment = 'neutral'  # Default to neutral if response is unexpected
    
    return sentiment

def process_file(file, comments_column):
    try:
        df = pd.read_csv(file)
        if comments_column not in df.columns:
            st.error(f"The uploaded file does not contain a column named '{comments_column}'.")
            return None
        df['Sentiment'] = df[comments_column].apply(classify_sentiment)
        return df
    except Exception as e:
        st.error(f"Error processing file: {e}")
        return None

def create_wordcloud(text):
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis('off')
    return fig

def main():
    st.title("Sentiment Analysis with Gemini 1.5 Flash")

    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

    if uploaded_file is not None:
        # Load the file to check the column names
        try:
            df = pd.read_csv(uploaded_file)
            st.write("Columns in the uploaded file:", df.columns.tolist())

            # Allow user to select the column for comments
            comments_column = st.selectbox("Select the column containing comments", df.columns)
            df = process_file(uploaded_file, comments_column)

            if df is not None:
                st.write("Processed Data:")
                st.write(df)

                # Provide a download link for the processed data
                st.download_button(
                    label="Download results as CSV",
                    data=df.to_csv(index=False),
                    file_name="sentiment_analysis_results.csv",
                    mime="text/csv"
                )

                # Create and display sentiment distribution chart
                sentiment_counts = df['Sentiment'].value_counts()
                fig = px.bar(x=sentiment_counts.index, y=sentiment_counts.values,
                             labels={'x': 'Sentiment', 'y': 'Count'},
                             title='Sentiment Distribution')
                st.plotly_chart(fig)

                # Create and display word cloud
                st.subheader("Word Cloud of Comments")
                all_comments = " ".join(df[comments_column].astype(str))
                wordcloud_fig = create_wordcloud(all_comments)
                st.pyplot(wordcloud_fig)
        except Exception as e:
            st.error(f"Error reading file: {e}")

if __name__ == "__main__":
    main()
