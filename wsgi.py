from os import getenv, sep, getcwd

from dotenv import load_dotenv
from app import Main


def start():
    path_env = sep.join([getcwd(), 'app', 'config', '.env'])
    load_dotenv(path_env)
    params = {
        'port': int(getenv('PORT', 5000)),
    }
    Main().run(**params)


if __name__ == "__main__":
    """Entrypoint"""
    start()
