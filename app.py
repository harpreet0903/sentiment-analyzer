import streamlit as st
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Initialize the SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()

# Streamlit UI layout
st.title("Sentiment Analyzer")

# Input field for text
user_input = st.text_area("Enter text for sentiment analysis:")

# Add a submit button for mobile-friendly interaction
if st.button("Analyze Sentiment"):
    if user_input:
        # Perform sentiment analysis
        sentiment_score = analyzer.polarity_scores(user_input)
        compound_score = sentiment_score['compound']
        
        # Display the sentiment score
        st.write("Sentiment Score:", compound_score)

        if compound_score >= 0.05:
            sentiment = 'Positive'
        elif compound_score <= -0.05:
            sentiment = 'Negative'
        else:
            sentiment = 'Neutral'

        # Display the sentiment
        st.write(f"Sentiment: {sentiment}")
    else:
        st.write("Please enter some text to analyze sentiment.")
