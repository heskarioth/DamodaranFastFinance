from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.db.database import engine
#from app.db.etl.etl_main import var,main_etl
from .config import etl_settings
from .routers import essential as route_essential
from .routers import quickendpoints as route_quick
from .routers import cost_of_equity as route_coe
from .routers import cashflow_estimations as route_cfe
from .routers import growth_rate_estimations as route_gre
from .routers import capital_structure as route_cs
from .routers import dividend_policy as route_dp
from .routers import users as route_users
from .routers import auth as route_auth

from fastapi.staticfiles import StaticFiles
from fastapi.openapi.utils import get_openapi
from . import docs
from fastapi.openapi.docs import (
    get_redoc_html,
    get_swagger_ui_html,
    get_swagger_ui_oauth2_redirect_html
)


#models.Base.metadata.create_all(bind=engine)

origins = ["*"]

app = FastAPI(
    docs_url=None,
    redoc_url=None,
    title="DamodaranFastFinance",
    description=docs.description,
    version="0.0.1",
    #terms_of_service="http://example.com/terms/",
    contact= docs.contact,
    license_info=docs.license_info,
    openapi_tags=docs.tags_metadata,
    
    )

app.add_middleware(
    CORSMiddleware,
    allow_origins= origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.mount("/static",StaticFiles(directory="static"),name="static")


@app.get("/interactive",include_in_schema=False)
async def custom_swagger_ui_html():
    return get_swagger_ui_html(
        openapi_url=app.openapi_url,
        title=app.title + " - Swagger UI",
        oauth2_redirect_url=app.swagger_ui_oauth2_redirect_url,
        swagger_js_url="/static/swagger-ui-bundle.js",
        swagger_css_url="/static/swagger-ui.css",
        swagger_favicon_url="https://img.icons8.com/doodle/48/000000/money.png",
        swagger_ui_parameters={"syntaxHighlight.theme": "obsidian"},


    )

@app.get("/",include_in_schema=False)
async def redoc_html():
    return get_redoc_html(
        openapi_url=app.openapi_url,
        title=app.title + " - ReDoc",
        redoc_js_url= "/static/redoc.standalone.js",
        redoc_favicon_url= "https://img.icons8.com/doodle/48/000000/money.png",
    )

app.include_router(route_quick.router)
app.include_router(route_coe.router)
app.include_router(route_cfe.router)
app.include_router(route_gre.router)
app.include_router(route_cs.router)
app.include_router(route_dp.router)
app.include_router(route_users.router)
app.include_router(route_auth.router)
app.include_router(route_essential.router)

# uvicorn app.main:app --reload


# interesting queries
