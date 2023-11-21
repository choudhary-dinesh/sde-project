#Author : Dinesh Kumar(M22AIE227)
#Flsak api for news summerization.
from flask import Flask, render_template, request, jsonify
# Replace below with import of news summarization function
import os
import openai
import json
import time



def get_completion(prompt, model="gpt-3.5-turbo-1106"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response.choices[0].message["content"]

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_text', methods=['POST'])
def process_text():
    text = request.form.get('input_text')
    # Insert news summarization function call on input text 
    prompt = f"""
You will be provided with text delimited by triple backticks. \
And Assume you are a News analyst working for a News company who analysis news content. \
Your task is to Summarise the given content\
that align with text provided only and don't make any assumptions. \
Focus on the content that are provided.\

```{text}```
""" 
    response_ = get_completion(prompt)

    return jsonify({'processed_text': response_})

if __name__ == '__main__':
    os.environ["OPENAI_API_KEY"] = "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"
    openai.api_key = os.getenv("OPENAI_API_KEY")
    app.run(host = "0.0.0.0", port = "80", debug=True)
