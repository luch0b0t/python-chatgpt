import dotenv
import os
import openai


dotenv.load_dotenv()

def main():

    openai.organization = "org-MNpGtwNUecIdgArFyfvz6qVs"
    openai.api_key = os.environ.get('OPENAI_KEY')

    openai.ChatCompletion.create(model="gpt-3.5-turbo")




if __name__ == '__main__':
    main()
