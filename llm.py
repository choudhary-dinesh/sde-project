import os
import openai
import json
import time

os.environ["OPENAI_API_KEY"] = "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"
openai.api_key = os.getenv("OPENAI_API_KEY")

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

if __name__ == '__main__':

    content="""
    Three senior OpenAI researchers Jakub Pachocki, Aleksander Madry and Szymon Sidor resigned. Three senior OpenAI researchers Jakub Pachocki, Aleksander Madry and Szymon Sidor told associates they have resigned, news agency Reuters reported. 
    The board of the company behind ChatGPT on Friday fired OpenAI CEO Sam Altman - to many, the human face of generative AI - sending shock waves across the tech industry.
    OpenAI's chief technology officer Mira Murati will serve as interim CEO, the company said, adding that it will conduct a formal search for a permanent CEO.
    The announcement also said another OpenAI co-founder and top executive, Greg Brockman, the board’s chairman, would step down from that role but remain at the company, where he serves as president.
    But later on X, formerly Twitter, Brockman posted a message he sent to OpenAI employees in which he wrote, “based on today’s news, i quit.
    """

    prompt = f"""
    You will be provided with text delimited by triple backticks. \
    And Assume you are a News analyst working for a News company who analysis news content. \
    Your task is to Summarise the given content\
    that align with text provided only and don't make any assumptions. \
    Focus on the content that are provided.\

    ```{content}```
    """ 

    response = get_completion(prompt)
    print(response)
        
