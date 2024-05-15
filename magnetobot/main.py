import typer
import wikipedia
from duckduckgo_search import DDGS
from magentic import prompt

from rich.console import Console

# app = typer.Typer()
console = Console()


def search_ddg(topic: str):
    """Get search results from duckduckgo.com"""
    ddg = DDGS()
    results = ddg.news(topic, max_results=3)
    return results


def search_wiki(topic: str):
    """Get search results from Wikipedia"""
    summary = wikipedia.summary(topic, sentences=3)
    return summary


@prompt(
    "You are a Wizard. Use the appropriate functions to answer: {question}",
    functions=[search_ddg, search_wiki],
)
def ask_wizard(question: str) -> str: ...


def main() -> None:
    question = typer.prompt("What do you want to know?")
    answer = ask_wizard(question)
    console.print(answer)


if __name__ == "__main__":
    typer.run(main)
