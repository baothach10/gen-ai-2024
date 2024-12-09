import Gemini
import MediaStack
# from test import news_queries
from datetime import datetime
from nltk.corpus import words


gemini = Gemini.Gemini()
mediastack = MediaStack.MediaStack()

def summarize(prompt: str) -> str:
    
    input = prompt
    keywords = gemini.get_key_words(input)
    categories = gemini.get_categories(input)

    today_date = datetime.today().strftime('%Y-%m-%d')

    news = mediastack.get_news(keywords, today_date, "en")
    # print(news)


    titles = mediastack.get_titles(news)
    descriptions = mediastack.get_descriptions(news)
    citations = mediastack.get_citations(news)

    summarized = gemini.get_summarize(titles, descriptions)
    # print("Keywords: " + keywords)

    # print("Summarized: " + summarized)

    return summarized, citations

