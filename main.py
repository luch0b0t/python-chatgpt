import dotenv
import os
import openai


dotenv.load_dotenv()

def main():


    openai.organization = os.environ.get('OPENAPI_ORGANIZATION')
    openai.api_key = os.environ.get('OPENAI_KEY')

    user_content = input("Que deseas preguntar?: ")

    response = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                 messages=[{
                                     "role": "user", "content": user_contentcual
                                 }])

    print(response.choices[0].message.content)



if __name__ == '__main__':
    main()
