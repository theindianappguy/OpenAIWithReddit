import openai
from creds import SECRET_KEY

openai.api_key = SECRET_KEY
for engine in openai.Engine.list():
    print(engine)
