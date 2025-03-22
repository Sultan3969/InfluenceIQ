# utils/data_fetch.py
import wikipedia
from pytrends.request import TrendReq
from textblob import TextBlob

def get_credibility_score(name):
    try:
        page = wikipedia.page(name)
        content = page.content
        # Simple credibility: number of sections or links
        return min(10, len(page.links) // 5)
    except:
        return 2  # fallback

def get_longevity_score(name):
    try:
        pytrends = TrendReq()
        pytrends.build_payload([name], timeframe='today 5-y')
        data = pytrends.interest_over_time()
        if not data.empty:
            avg_interest = int(data[name].mean())
            return min(10, avg_interest // 10)
        return 2
    except:
        return 2

def get_engagement_score(name):
    # Placeholder: sentiment based on sample sentence
    text = f"{name} is a respected and influential figure in their industry."
    sentiment = TextBlob(text).sentiment.polarity
    return int(sentiment * 10) + 5  # Range 0–10
