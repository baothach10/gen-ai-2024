import Gemini
import MediaStack
from test import news_queries
from datetime import datetime
from nltk.corpus import words


gemini = Gemini.Gemini()
mediastack = MediaStack.MediaStack()


# for i in range(len(news_queries)):
#     inp = news_queries[i]
#     print(gemini.get_key_words(inp))




input = """Government chief calls for greater efforts to streamline State apparatus"""
keywords = gemini.get_key_words(input)
categories = gemini.get_categories(input)

today_date = datetime.today().strftime('%Y-%m-%d')

news = mediastack.get_news(keywords, today_date, "en")
print(news)


titles = mediastack.get_titles(news)
descriptions = mediastack.get_descriptions(news)
citations = mediastack.get_citations(news)

summarized = gemini.get_summarize(titles, descriptions)
print("Keywords: " + keywords)

print("Summarized: " + summarized)

