from os import getenv

SECRET_KEY = getenv('SECRET_KEY')
ENV = getenv('ENV')
DEBUG = bool(int(getenv('DEBUG')))


MONGO_URI = f'mongodb+srv://{getenv("DB_USER")}:{getenv("DB_PASSWORD")}@cluster0.oeact.mongodb.net/' \
            f'{getenv("DB_NAME")}?retryWrites=true&w=majority'


