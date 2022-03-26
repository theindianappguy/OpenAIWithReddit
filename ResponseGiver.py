import openai
from creds import SECRET_KEY

openai.api_key = SECRET_KEY


def response(question):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=question,
        temperature=0,
        max_tokens=100,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.0,
    )
    return response['choices'][0]['text'].strip('\n')
