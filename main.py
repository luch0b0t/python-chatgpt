import dotenv
import os
import openai


dotenv.load_dotenv()

def main():

    openai.organization = "org-MNpGtwNUecIdgArFyfvz6qVs"
    openai.api_key = os.environ.get('OPENAI_KEY')

    response = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                 messages=[{
                                     "role": "user", "content": "Cual esla vision de OpenAI?"
                                 }])

    print(response.choices[0].message.content)



if __name__ == '__main__':
    main()
