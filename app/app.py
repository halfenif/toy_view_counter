# Load .env
from env import Settings
config = Settings()

# FastAPI
from fastapi import Depends, FastAPI, Header
from fastapi import HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse

# DBMS
import dbModels, dbApi
from dbEngin import engine

from counterApi import get_counter_file_by_uuid, get_counter_data_by_uuid

# --------------------------------------------------------------
# Init DB
dbModels.Base.metadata.create_all(bind=engine)

# Init Server
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=config.ORIGINS,
)

@app.get("/readcount_svg/{uuid}", response_model_by_alias=FileResponse)
def get_count_svg_by_uuid(uuid: str, Referer: str = Header(...)):
    # Referer Check

    if not len(uuid) == 36:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, 
                            detail='Invalid Request ID')    

    filename = get_counter_file_by_uuid(uuid, Referer)
    return FileResponse(filename, media_type="image/svg+xml")

@app.get("/readcount_json/{uuid}")
def get_count_json_by_uuid(uuid: str, Referer: str = Header(...)):
    # Referer Check

    if not len(uuid) == 36:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, 
                            detail='Invalid Request ID')    

    return get_counter_data_by_uuid(uuid, Referer)


# Set Swagger
if not config.IS_DEBUG:
    app.openapi_url = None
    app.docs_url = None
    app.redoc_url = None
