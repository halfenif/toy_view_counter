# Load .env
from env import Settings
config = Settings()

# FastAPI
from fastapi import Depends

import inspect
import datetime

from sqlalchemy.orm import Session
from dbEngin import SessionLocal, engine
import dbModels

from uuid_extensions import uuid7

def sql_get_count_by_uuid(itemUuid: str, Referer: str):
    db = SessionLocal()

    dbCounterMain = db.query(dbModels.CounterMain).filter(dbModels.CounterMain.counter_id == itemUuid).first()

    # Main
    if dbCounterMain:
        dbCounterMain.read_count += 1
        dbCounterMain.update_req_id = Referer
        dbCounterMain.update_date = datetime.datetime.now()

    else:
        dbCounterMain = dbModels.CounterMain()
        dbCounterMain.counter_id = itemUuid
        dbCounterMain.read_count = 1
        dbCounterMain.create_req_id = Referer
        dbCounterMain.update_req_id = Referer

        db.add(dbCounterMain)        
    
    # Detail
    dbCounterDetail = dbModels.CounterDetail()
    dbCounterDetail.counter_id = itemUuid
    dbCounterDetail.detail_id = uuid7(as_type='str')
    dbCounterDetail.read_count = dbCounterMain.read_count
    dbCounterDetail.create_req_id = Referer
    dbCounterDetail.update_req_id = Referer
    db.add(dbCounterDetail)    


    db.commit()
    # db.refresh(dbItem)

    return dbCounterMain.read_count

    
