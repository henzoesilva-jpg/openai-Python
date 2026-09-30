#Author: Raphael Campos Squilaro
#Project: Using API's

from openai import OpenAI

api_openai = OpenAI(
    api_key = 'chave_api'
)

response = client.responses.create(
    model = 'gpt-5.4-mini',
    input = 'manga'
)

print(response.output_text)