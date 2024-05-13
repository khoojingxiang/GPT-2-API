# GPT-2-API
API with GPT-2 by KJX(KHoo Jing Xiang)
For this API to work, you'll need the Postman application and append the back of the url with /generate-text.

# API Functions
It leverages the GPT-2 pre-trained model on English language using a causal language modeling (CLM) objective. This model can be found in the open ai comunity under GPT-2

Link to pre-trained model: https://huggingface.co/openai-community/gpt2

# Insutrctions on how to use the API
To use the GPT-2 API:

  1. In the Postman web application (or download it), set the request URL to the one below   appending generate-text at the back:
        
      https://api-back-with-gpt-2-ai.azurewebsites.net/generate-text
        

  2. In postman Set the request method to "POST".

  3. Go to the request body and choose "json" as the type.

  4. Use the following JSON format:
        
     {"inputs": "*Type your sentence here*"}"

        Replace "*Type your sentence here*" with the sentence you want the model to continue.

  5. In the response body, you should see your sentence elaborated upon.
