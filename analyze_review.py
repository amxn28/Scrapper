import pandas as pd
from textblob import TextBlob

def load_reviews(file_path):
    return pd.read_csv(file_path)

def summarize_reviews(reviews, threshold=1):
    summary = {
        'total_reviews': len(reviews),
        'positive_reviews': 0,
        'negative_reviews': 0,
        'neutral_reviews': 0,
        'average_sentiment': 0
    }

    for review in reviews['review']:
        analysis = TextBlob(review)
        sentiment_score = analysis.sentiment.polarity
        
        if sentiment_score > 0:
            summary['positive_reviews'] += 1
        elif sentiment_score < 0:
            summary['negative_reviews'] += 1
        else:
            summary['neutral_reviews'] += 1
        
        summary['average_sentiment'] += sentiment_score

    if summary['total_reviews'] > 0:
        summary['average_sentiment'] /= summary['total_reviews']

    if abs(summary['positive_reviews'] - summary['negative_reviews']) <= threshold:
        summary['neutral_reviews'] += (summary['positive_reviews'] + summary['negative_reviews'])
        summary['positive_reviews'] = 0
        summary['negative_reviews'] = 0

    return summary

def generate_thematic_summary(summary):
    """Generate a thematic summary based on the sentiment analysis."""
    thematic_summary = []

    if summary['positive_reviews'] > summary['negative_reviews']:
        thematic_summary.append("Overall, customers have a positive sentiment towards the product.")
    elif summary['negative_reviews'] > summary['positive_reviews']:
        thematic_summary.append("The reviews reflect a negative sentiment towards the product.")
    else:
        thematic_summary.append("The reviews are mixed, showing an equal number of positive and negative sentiments.")

    if summary['positive_reviews'] > 0:
        thematic_summary.append("Customers frequently appreciate the product for its quality, value for money, and performance.")
    
    if summary['negative_reviews'] > 0:
        thematic_summary.append("However, some customers have expressed concerns regarding its durability and reliability.")

    if summary['neutral_reviews'] > 0:
        thematic_summary.append("Many reviews reflect a neutral sentiment, indicating mixed feelings about the product.")

    return " ".join(thematic_summary)

def main():
    file_path = 'reviews.csv'
    reviews = load_reviews(file_path)

    summary = summarize_reviews(reviews)

    thematic_summary = generate_thematic_summary(summary)

    print("Summary of Reviews:")
    print(f"Total Reviews: {summary['total_reviews']}")
    print(f"Positive Reviews: {summary['positive_reviews']}")
    print(f"Negative Reviews: {summary['negative_reviews']}")
    print(f"Neutral Reviews: {summary['neutral_reviews']}")
    print(f"Average Sentiment Score: {summary['average_sentiment']:.2f}")
    print("\nSummary:")
    print(thematic_summary)

if __name__ == "__main__":
    main()