from fastapi import APIRouter, Depends
from app import schemas
from sqlalchemy.orm import Session
from app.database import get_mysql_db
from app.repository import table

router = APIRouter(
    prefix="/table",
    tags=['tables']
)

@router.post('/')
async def create_new_table(request: schemas.Table, db: Session = Depends(get_mysql_db)):
    new_table = table.create(request, db)

    if new_table.id:
        return{
            "success": True,
            "data": new_table
        }
    else:
        return {
            "success": False,
            "message": "Internal server error"
        }

@router.get('/')
async def get_all_table(db: Session = Depends(get_mysql_db)):
    tables = table.get_all(db)
    return {
        "success": True,
        "data": tables
    }

@router.get('/{id}')
async def get_table_by_id(id: int, db: Session = Depends(get_mysql_db)):
    foundTable = table.get_by_id(id, db)
    if not foundTable:
        return {
            "success": False,
            "message": "Not Found"
        }
    return {
        "success": True,
        "data": foundTable
    }

@router.put('/{id}')
async def update_table_by_id(id: int, request: schemas.Table, db: Session = Depends(get_mysql_db)):
    updatedTable = table.update(id, request, db)

    if updatedTable == "Not Found":
        return {
            "success": False,
            "message": "Not Found"
        }

    return {
        "success": True,
        "data": updatedTable
    }

@router.delete('/{id}')
async def delete_table_by_id(id: int, db: Session = Depends(get_mysql_db)):
    result = table.destroy(id, db)

    if result == "Not Found":
        return {
            "success": False,
            "message": "Not Found"
        }

    return {
        "success": True
    }