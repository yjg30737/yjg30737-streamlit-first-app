from openai import OpenAI
from settings import OPENAI_API_KEY

openai_client = OpenAI(api_key=OPENAI_API_KEY)

openai_arg = {
    "model": 'gpt-3.5-turbo',
    "messages": [{'role': 'system', 'content': 'You are a helpful assistant.'}],
    "n": 1,
    "stream": True,
}

def get_response(content):
    new_message = {'role': 'user', 'content': content}
    openai_arg['messages'].append(new_message)
    response = openai_client.chat.completions.create(**openai_arg)
    return response

