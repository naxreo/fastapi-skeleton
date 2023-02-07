from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from common.metadata import get_metadata
from routes import rt_items, rt_home, rt_admin

## declare app
meta = get_metadata()
app = FastAPI(
    title=meta['title'],
    description=meta['description'],
    version=meta['version'],
    terms_of_service=meta['terms_of_service'],
    # contact=meta['contact'],
    # license_info=meta['license_info'],
    redoc_url=None,
)
app.mount("/statics", StaticFiles(directory="statics"), name="statics")

## https://fastapi.tiangolo.com/ko/tutorial/cors/
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


## routing
# home templates
app.include_router(rt_home.router)
# admin for security
app.include_router(rt_admin.router)
# items
app.include_router(rt_items.router)

