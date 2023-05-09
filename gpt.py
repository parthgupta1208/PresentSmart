import openai
import os

# Set OpenAI API key
openai.api_key = os.getenv("OPENAI_KEY")

def gpt_summarise(text):
    completion = openai.ChatCompletion.create(
                model="gpt-3.5-turbo", 
                messages = [{"role": "system", "content" : "I am giving you a paragraph. return a topic and summary in five points. strictly follow the syntax'Topic : topic goes here , Summary : summary sentence 1, summary sentence 2,summary sentence 3,summary sentence 4,summary sentence 5'. make the points ppt friendly and concise."},
                {"role": "user", "content" : text}]
                )
    return(completion['choices'][0]['message']['content'])