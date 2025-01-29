from mymodels_MySQL import Base  # User, Comment
from connect_MySQL import engine

import platform
print(platform.uname())


print("Creating tables >>> ")
Base.metadata.create_all(bind=engine)
