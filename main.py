import dotenv
import os
import openai


def main():

    openai.organization = "org-MNpGtwNUecIdgArFyfvz6qVs"
    openai.api_key = os.environ.get('OPENAI_KEY')


if __name__ == '__main__':
    main()
