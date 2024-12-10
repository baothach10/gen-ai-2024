#post api 
# body consists of prompt
# prompt nạp vào media stack 

# xong trả về front end

from flask import Flask, request, jsonify
from flask_cors import CORS
import Gemini
import summarize
import imageGen
import gen_meme
import vidGen


app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def hello():
    return "hello world"

@app.route('/mediastack', methods=['POST'])
def get_summary_media():

    gemini = Gemini.Gemini()

    # Check if the request has JSON data
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400
    
    # Get the query from the request
    data = request.get_json()
    query = data.get('query')
    
    # Validate query
    if not query:
        return jsonify({"error": "No query provided"}), 400
    
    # Extract keywords
    try:
        keywords = gemini.get_key_words(query)
        summary, citation = summarize.summarize(query)
        print(summary)
        res =  jsonify({
            "query": query,
            "keywords": keywords.split(','),
            "summary": summary,
            "imageUrl": imageGen.generate_image(summary),
            "citation": citation,
            "meme": gen_meme.gen_meme(summary),
            "videoUrl": vidGen.gen_vid(summary, keywords)
        })

        return res

    except Exception as e:
        return jsonify({"error": str(e)}), 500

app.run(host='0.0.0.0')