from fastapi import APIRouter, Depends
from dto.table import TableCreate
from sqlalchemy.orm import Session
from config.database import get_mysql_db
from repository import table_repository
from responses import error, success
from constants import error_types

router = APIRouter(
    prefix="/table",
    tags=['tables']
)

@router.post('/')
async def create_new_table(request: TableCreate, db: Session = Depends(get_mysql_db)):
    new_table = table_repository.create(request, db)

    if new_table.id:
        return success.NewSuccessResponse(new_table)
    else:
        return error.NewErrorResponse(error_types.SERVER_ERROR)

@router.get('/')
async def get_all_table(db: Session = Depends(get_mysql_db)):
    tables = table_repository.get_all(db)
    return success.NewSuccessResponse(tables)

@router.get('/{id}')
async def get_table_by_id(id: int, db: Session = Depends(get_mysql_db)):
    foundTable = table_repository.get_by_id(id, db)
    if not foundTable:
        return error.NewErrorResponse(error_types.NOT_FOUND)
    return {
        "success": True,
        "data": foundTable
    }

@router.put('/{id}')
async def update_table_by_id(id: int, request: TableCreate, db: Session = Depends(get_mysql_db)):
    result = table_repository.update(id, request, db)

    if result == error_types.NOT_FOUND:
        return error.NewErrorResponse(result)

    return success.NewSuccessResponse(result)

@router.delete('/{id}')
async def delete_table_by_id(id: int, db: Session = Depends(get_mysql_db)):
    result = table_repository.destroy(id, db)

    if result == error_types.NOT_FOUND:
        return error.NewErrorResponse(result)

    return success.NewSuccessResponse()