import dotenv
import os
import openai
import typer
from rich import print
from rich.table import Table


dotenv.load_dotenv()


class Context():
    def __init__(self):
        self.__messages = []

    def add_context(self, role: str, content: str):
        __context = {"role": role, "content": content}
        self.add(__context)

    def add(self, context):
        self.__messages.append(context)

    def get_messages(self):
        return self.__messages


def __prompt() -> str:
    prompt = typer.prompt("Que deseas preguntar?: ")
    if prompt == "exit":
        raise typer.Exit()

    return prompt


def main():

    openai.organization = os.environ.get('OPENAPI_ORGANIZATION')
    openai.api_key = os.environ.get('OPENAI_KEY')
    context = Context()

    print("[bold blue] Welcome to this ChatGPT API implementation [/bold blue]")

    context.add_context("system", "Eres un asistente muy útil.")

    table = Table("Comando", "Descripción")
    table.add_row("exit", "Salir de la aplicación")
    table.add_row("new", "Crear una nueva conversación")

    print(table)

    while True:
        content = __prompt()

        if content == "new":
            conetxt = Context()
            context.add_context("system", "Eres un asistente muy útil.")
            break

        context.add_context("user", content)

        response = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                     messages=context.get_messages())

        response_context = response.choices[0].message.content
        print(f"[bold green]> [/bold green]  {response_context} \n"
              f"----------------------------------------------------------")

        context.add_context("assistant", response_context)


if __name__ == '__main__':
    typer.run(main)
