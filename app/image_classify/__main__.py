"""RP To-Do entry point script."""
from image_classify import cli
from image_classify import __app_name__

def main():
    cli.app(prog_name=__app_name__)

if __name__ == "__main__":
    main()