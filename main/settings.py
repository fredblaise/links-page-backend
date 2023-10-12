import environ
import os

# Initialise environment variables
env = environ.Env()
environ.Env.read_env()

if env("DJANGO_ENV") == "PRODUCTION":
    from .production_settings import *
else:
    from .local_settings import *
