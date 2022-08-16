from msilib.schema import tables
from unittest import result
from fastapi import APIRouter
from app import schemas, database, models

router = APIRouter(
    prefix="/table",
    tags=['tables']
)

@router.post('/')
async def create_new_table(request: schemas.Table):
    result = database.mysql_conn.execute(models.table.insert().values(
        description=request.description,
        status=request.status
    ))

    if result.is_insert:
        new_table = database.mysql_conn.execute(models.table.select().order_by(models.table.c.id.desc())).fetchone()

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
async def get_all_table():
    tables = database.mysql_conn.execute(models.table.select()).fetchall()
    return {
        "success": True,
        "data": tables
    }

@router.get('/{id}')
async def get_table_by_id(id: int):
    table = database.mysql_conn.execute(models.table.select().where(models.table.c.id == id)).fetchone()
    if not table:
        return {
            "success": False,
            "message": "Not Found"
        }
    return {
        "success": True,
        "data": table
    }

@router.put('/{id}')
async def update_table_by_id(id: int, request: schemas.Table):
    result = database.mysql_conn.execute(models.table.update().values(
        description=request.description,
        status=request.status
    ).where(models.table.c.id == id))

    if not result:
        return {
            "success": False,
            "message": "Internal Server Error"
        }

    updated_table = database.mysql_conn.execute(models.table.select().where(models.table.c.id == id)).fetchone()

    return {
        "success": True,
        "data": updated_table
    }

@router.delete('/{id}')
async def delete_table_by_id(id: int):
    result = database.mysql_conn.execute(models.table.delete().where(models.table.c.id == id))

    if not result:
        return {
            "success": False,
            "message": "Internal Server Error"
        }

    return {
        "success": True
    }