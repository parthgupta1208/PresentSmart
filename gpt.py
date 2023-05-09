import openai
import os

# Set OpenAI API key
openai.api_key = os.getenv("OPENAI_KEY")

def gpt_summarise(system,text):
    completion = openai.ChatCompletion.create(
                model="gpt-3.5-turbo", 
                messages = [{"role": "system", "content" : system},
                {"role": "user", "content" : text}]
                )
    return(completion['choices'][0]['message']['content'])