import dotenv
import os
import openai


dotenv.load_dotenv()

def new_content(role: str, content: str):
    return {"role": role, "content": content}

def main():


    openai.organization = os.environ.get('OPENAPI_ORGANIZATION')
    openai.api_key = os.environ.get('OPENAI_KEY')
    messages = []

    system_context = new_content("system", "Eres un asistente muy útil.")

    messages.append(system_context)

    while True:
        content = input("Que deseas preguntar?: ")
        if content == "exit":
            return None

        user_content = new_content("user", content)
        messages.append(user_content)

        response = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                     messages=messages)

        print(response.choices[0].message.content)


if __name__ == '__main__':
    main()
