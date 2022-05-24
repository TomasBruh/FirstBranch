from fastapi import FastAPI
from database import engine
import models
from routers import user_routers
from routers import post_routers

app = FastAPI()
app.include_router(user_routers.router)
app.include_router(post_routers.router)

models.Base.metadata.create_all(engine)
