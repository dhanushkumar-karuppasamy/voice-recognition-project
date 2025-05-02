import google.generativeai as genai

API_KEY = "AIzaSyBgoPx5ye96vVkpw_W1fpRMciXOqrtUCsA"
genai.configure(api_key=API_KEY)

# Variable to store context
conversation_history = []

def get_ai_response(prompt):
    global conversation_history

    try:
        # Add the new prompt to the conversation history
        conversation_history.append(f"User: {prompt}")

        # If the conversation history exceeds 2 exchanges, limit it to the last 2
        if len(conversation_history) > 4:
            conversation_history = conversation_history[-4:]  # Keep 2 prompts + 2 responses

        # Combine context into one string
        context = "\n".join(conversation_history)

        # Generate prompt with instruction to keep answer short and direct
        final_prompt = f"{context}\n\nPlease provide a short and direct answer."

        model = genai.GenerativeModel('models/gemini-1.5-pro-001')

        # Set generation config with a limit on output tokens and temperature for diversity
        generation_config = {
            "max_output_tokens": 60,  # Shorter response
            "temperature": 0.7,
            "top_p": 0.9,
        }

        # Generate content based on the final prompt
        response = model.generate_content(final_prompt, generation_config=generation_config)

        # Get the generated response text
        ai_response = response.text.strip()

        # Add AI's response to the conversation history
        conversation_history.append(f"AI: {ai_response}")

        # Return the response text
        return ai_response

    except Exception as e:
        return f"Error from Gemini API: {str(e)}"
