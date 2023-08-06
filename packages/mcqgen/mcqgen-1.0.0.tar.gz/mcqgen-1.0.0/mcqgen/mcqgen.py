import os
import openai
import json

class MCQGenerator():
    def __init__(self):
        # Get the API key from the system environment variable
        try:
            openai.api_key = os.environ.get("OPENAI_API_KEY")
        except Exception as err:
            print("ERROR: " + str(err))

    def generate_mcqs(self, topic, model="gpt-3.5-turbo", no=5):
        try:
            prompt = "Generate a set of " + str(no) + " Multiple Choice Questions on topic: " + topic + ". Each question should have 4 options, only one of which is correct. Questions should be very difficult. Generate the questions, answers, and correct answer in JSON format"
            response = openai.ChatCompletion.create(
                model=model,  # Use the chat-based model
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": prompt},
                ],
            )
            generated_text = response['choices'][0]['message']['content']
            json_data = json.loads(generated_text)
            return json_data
        except Exception as err:
            print("ERROR: " + str(err))
            return None
