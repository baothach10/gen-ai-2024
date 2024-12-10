import google.generativeai as genai
import os
from dotenv import load_dotenv


load_dotenv()
API_KEY = os.getenv('GOOGLE_API_KEY')


class Gemini:
    def __init__(self):
        genai.configure(api_key=API_KEY)

        self.model = genai.GenerativeModel('gemini-1.5-flash')

    def generate_content(self, prompt):
        response = self.model.generate_content(prompt)
        return response.text

    def get_categories(self, prompt):
        template = (
            "Extract the keyword that represents the category of news from the following user query. Only return categories in the supported categories list. match closes meaning to the categories list. For example: sport -> sport\n\n"

            "Supported categories are:\n\n"
            "general - Uncategorized News\n"
            "business - Business News\n"
            "entertainment - Entertainment News\n"
            "health - Health News\n"
            "science - Science News\n"
            "sports - Sports News\n"
            "technology - Technology News\n"

            "Return only the categories as the result, and nothing else, it can have multiple categories. For example:\n\n"
            "Input: \"Find today's news about sport.\"\n"
            "Output: \"sport\"\n\n"
            "Input: \"Show me news about technology this week.\"\n"
            "Output: \"technology\"\n\n"
            "Input: \"News about crypto and sports\"\n"
            "Output: \"sports\"\n Because crypto is not in the supported list \n"
            "Now, process the following input:\n\n"
            "Input: \"" + prompt + "\""
        )
        response = self.model.generate_content(template)
        return response.text

    def get_key_words(self, prompt):
        template = (
            """Extract the keyword that represents the main topic of the news from the following user query. The keyword should be a list of single word. For example, if the user query is \"Show me news about the stock market\", the keyword should be \"stock\".\n\n"
            Another example: If the user query is \"What is the latest news about the US economy?\", the keyword should be \"latest,economy,US\".\n\n"
            Another example: If the user query is \"What is the latest news about the US economy?\", the keyword should be \"latest,economy,US\".\n\n"
            "Now, process the following input:\n\n"
            "Input: \"""" + prompt
        )

        # template = (
        #     """Extract the most important and meaningful keywords from the following news query. 

        #     Guidelines for keyword extraction:
        #     - Focus on substantive nouns, key concepts, and specific entities
        #     - Avoid common stop words like 'the', 'a', 'an', 'in', 'of'
        #     - Prioritize terms that capture the core meaning of the query
        #     - Include only single words
        #     - Aim for 5-8 keywords total
        #     - Provide only the keywords as a list, without additional explanation

        #     Query: "{query}"

        #     Keywords:"""
        # )

        response = self.model.generate_content(template)
        return response.text

    def get_summarize(self, titles, descriptions):
        template = (
            """"
            Given a list of titles and descriptions of news articles, summarize the news articles in one paragraph around 100 words to quickly update readers. 
            The summary should be concise and informative, and should not exceed 100 words.
            
            List of titles and descriptions:
            """
            + "Titles:" + ",".join(titles) +
            "\nDescriptions:" + ",".join(descriptions)
        )

        response = self.model.generate_content(template)
        return response.text
