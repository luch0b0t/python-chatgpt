import dotenv
import os
import openai
import typer
from rich import print
from rich.table import Table


dotenv.load_dotenv()

def new_content(role: str, content: str):
    return {"role": role, "content": content}


def add_context(role: str, content: str, messages: list):
    content = new_content(role, content)
    return messages.append(content)


def __prompt() -> str:
    prompt = typer.prompt("Que deseas preguntar?: ")
    if prompt == "exit":
        raise typer.Exit()

    return prompt

def main():


    openai.organization = os.environ.get('OPENAPI_ORGANIZATION')
    openai.api_key = os.environ.get('OPENAI_KEY')
    messages = []

    print("[bold blue] Welcome to this ChatGPT API implementation [/bold blue]")

    add_context("system", "Eres un asistente muy útil.", messages)

    table = Table("Comando", "Descripción")
    table.add_row("exit", "Salir de la aplicación")
    table.add_row("new", "Crear una nueva conversación")

    print(table)

    while True:
        content = __prompt()

        if content == "new":
            messages = []
            add_context("system", "Eres un asistente muy útil.", messages)
            break

        add_context("user", content, messages)

        response = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                     messages=messages)

        response_context = response.choices[0].message.content
        print(f"[green]>[/green]  {response.choices[0].message.content} \n"
              f"----------------------------------------------------------")

        add_context("assistant", response_context, messages)


if __name__ == '__main__':
    typer.run(main)
