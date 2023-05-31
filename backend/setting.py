from pydantic import BaseSettings

class Setting(BaseSettings):
    ACCESS_TOKEN_EXPIRE_MINUTES = 30  # 30 minutes
    REFRESH_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7  # 7 days
    ALGORITHM = "HS256"
    JWT_SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
    # os.environ['JWT_SECRET_KEY']   # should be kept secret
    JWT_REFRESH_SECRET_KEY = "37aa6a6ca255694f9d25956afccf63bb937099f70f4cae06f0818166b88e8d3e"
    # os.environ['JWT_REFRESH_SECRET_KEY']    # should be kept secret

setting = Setting()