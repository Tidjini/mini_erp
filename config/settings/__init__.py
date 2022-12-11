from decouple import config

env = config("ENV")
print('env', env)

if env.lower() == "development":
    from .development import *
else:
    from .production import *
    


