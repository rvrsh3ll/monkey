import os

DEFAULT_MONGO_DB_NAME = "monkey_island"
DEFAULT_MONGO_DB_HOST = "localhost"
DEFAULT_MONGO_DB_PORT = 27017
MONGO_URL = os.environ.get(
    "MONKEY_MONGO_URL",
    f"mongodb://{0}:{1}/{2}".format(
        DEFAULT_MONGO_DB_HOST, DEFAULT_MONGO_DB_PORT, DEFAULT_MONGO_DB_NAME
    ),
)
