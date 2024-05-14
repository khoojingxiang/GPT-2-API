# GPT-2-API
API with GPT-2 by KJX(KHoo Jing Xiang)
For testing of the API, i have used the Postman API application and you would need to append the back of the url with /generate-text in Postman if you are using it.

# About Postman
Postman is a platform for API development. allowing developers to design, test, and document APIs quickly and easily. With Postman, you can create and send HTTP requests, inspect responses, automate workflows, and share your APIs.

# API Functions and description
It leverages the GPT-2 pre-trained model on English language using a causal language modeling (CLM) objective. This model can be found in the open ai comunity under GPT-2

The GPT-2 model is part of the Transformers architecture, trained extensively on a vast amount of English text without human labeling. It's designed to predict the next word in a sentence. Essentially, the model takes raw text as input, without any explicit instructions or annotations, and learns to generate coherent responses based on the patterns it discerns in the training data. In simpler terms, you provide the model with a piece of text, and it generates a continuation or completion of that text, often in the form of coherent sentences or paragraphs. 

The API route to /generate-text only accepts POST method and input json data else it will throwback and error message. e.g of json data

{
  "inputs": "i love writing"
}

Link to pre-trained model: https://huggingface.co/openai-community/gpt2

# Insutrctions on how to use the API
To use the GPT-2 API:

  1. In the Postman web application (or download it), set the request URL to the one below   appending generate-text at the back:
        
      https://api-back-with-gpt-2-ai.azurewebsites.net/generate-text
        

  2. In postman Set the request method to "POST".

  3. Go to the request body and choose "json" as the type.

  4. Use the following JSON format:
        
     {"inputs": "*Type your sentence here*"}

        Replace "*Type your sentence here*" with the sentence you want the model to continue.
        E.g {"inputs": "i love reading"}

  5. In the response body, you should see your original sentence you typed being elaborated upon.
