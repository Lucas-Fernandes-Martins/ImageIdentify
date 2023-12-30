from typing import Optional
import typer
from image_classify import __app_name__, __version__
from classifier.nn import ImageClassifier
from image_classify.server import RequestHandler
from http.server import HTTPServer


app = typer.Typer()

def _version_callback(value: bool) -> None:
    if value:
        typer.echo(f"{__app_name__} v{__version__}")
        raise typer.Exit()

@app.command()
def classify(path: str) -> None:
    classifier = ImageClassifier()
    classifier.classify(path)

@app.command()
def run() -> None:
    port = 8000
    server_class=HTTPServer
    handler_class=RequestHandler
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Server running on port {port}")
    httpd.serve_forever()

@app.callback()
def main(
    version: Optional[bool] = typer.Option(
        None,
        "--version",
        "-v",
        help="Show the application's version and exit.",
        callback=_version_callback,
        is_eager=True,
    )
) -> None:
    return