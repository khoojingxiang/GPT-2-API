from flask import Flask, request, jsonify
import requests
app = Flask(__name__)

API_URL = "https://api-inference.huggingface.co/models/openai-community/gpt2"
headers = {"Authorization": "Bearer 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"}

@app.route("/generate-text",methods=['POST'])
#method
def generate_text():
    data = request.get_json() #request POST data
    #input validation handling
    if not data or not data.get('inputs'):
        return jsonify({'Error': 'Missing "inputs" fields in request data'}), 400
    #return response from gpt-2
    response = requests.post(API_URL, headers=headers, json=data)
    return response.json()

@app.route('/')
def index():
    # code to handle the root path (instruction message)
    instructions = (
        "Welcome to Jing Xiang API!\n\n"

        "For this API to work, you'll need the Postman application and append the back of the url with /generate-text.\n\n"

        "To use the GPT-2 API:\n\n"

        "1. In the Postman web application (or download it), set the request URL to:\n"
        
        "https://api-back-with-gpt-2-ai.azurewebsites.net/generate-text\n"
        "```\n\n"

        "2. Set the request method to \"POST\".\n\n"

        "3. Go to the request body and choose \"json\" as the type.\n\n"

        "4. Use the following JSON format:\n\n"
        
        "{\"inputs\": \"*Type your sentence here*\"}"
        "```\n"
        "Replace \"*Type your sentence here*\" with the sentence you want the model to continue.\n\n"

        "5. In the response body, you should see your sentence elaborated upon.\n"
    )

    return instructions
    
# Run the API using flask
if __name__ == "__main__":
    app.run(debug=True)
    
