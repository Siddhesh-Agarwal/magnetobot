import requests
import typer
import wikipedia

from rich import print

app = typer.Typer()


@app.command(name="ddg")
def search_ddg(topic: str):
    """Get search results from duckduckgo.com"""
    url = f"https://api.duckduckgo.com/?q={topic}&format=json"
    response = requests.get(url, timeout=10)
    if response.status_code == 200:
        data = response.json()
        if isinstance(data, dict):
            data.pop("meta")
        print(data)
    else:
        print(f"[red bold]Error:[/] {response.status_code}")


@app.command(name="wiki")
def search_wiki(topic: str):
    """Get search results from Wikipedia"""
    summary = wikipedia.summary(topic, sentences=3)
    print(summary)


if __name__ == "__main__":
    app()
