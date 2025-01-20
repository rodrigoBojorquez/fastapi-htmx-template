from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from container import Container
from presentation.routers import contact_router

def create_app() -> FastAPI:
    app = FastAPI()
    container = Container()

    app.container = container
    container.db().create_database()

    app.include_router(contact_router)

    return app


app = create_app()

app.mount("/static", StaticFiles(directory="presentation/common/assets"), name="static")

@app.get("/")
async def home():
    return RedirectResponse(url="/contact")