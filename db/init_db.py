from db.session import engine
from db.base import Base

import models

Base.metadata.create_all(bind=engine)

