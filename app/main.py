#arquifo principal da aplicação 
#fastAPI

#importando as rotas
from fastapi import FastAPI
from app.core.config import settings
from app.routes import health

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION
)

#incluindo as rotas de saúde
app.include_router(health.router)