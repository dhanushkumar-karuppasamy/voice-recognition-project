import google.generativeai as genai

# Configure the API with your key
API_KEY = "AIzaSyBgoPx5ye96vVkpw_W1fpRMciXOqrtUCsA"
genai.configure(api_key=API_KEY)

def get_ai_response(prompt):
    try:
        # Using a model that is confirmed to be available
        model = genai.GenerativeModel('models/gemini-1.5-pro-001')
        
        # Set generation config for shorter responses
        generation_config = {
            "max_output_tokens": 100,
            "temperature": 0.7,
            "top_p": 0.95,
        }
        
        # Generate content with the prompt and config
        response = model.generate_content(
            prompt,
            generation_config=generation_config
        )
        
        # Return the response text
        return response.text
    except Exception as e:
        return f"Error from Gemini API: {str(e)}"