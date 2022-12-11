from decouple import config

env = config("ENV")

if env.lower() == "development":
    from .development import *
else:
    from .production import *
    


