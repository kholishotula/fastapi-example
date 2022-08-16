from fastapi import APIRouter, Depends
from app import schemas, database, models
from sqlalchemy.orm import Session
from app.database import get_mysql_db
from fastapi.encoders import jsonable_encoder

router = APIRouter(
    prefix="/table",
    tags=['tables']
)

@router.post('/')
async def create_new_table(request: schemas.Table, db: Session = Depends(get_mysql_db)):
    new_table = models.Table(description=request.description, status=request.status)
    db.add(new_table)
    db.commit()
    db.refresh(new_table)

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
    tables = db.query(models.Table).all()
    return {
        "success": True,
        "data": tables
    }

@router.get('/{id}')
async def get_table_by_id(id: int, db: Session = Depends(get_mysql_db)):
    table = db.query(models.Table).filter(models.Table.id == id).first()
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
async def update_table_by_id(id: int, request: schemas.Table, db: Session = Depends(get_mysql_db)):
    table = db.query(models.Table).filter(models.Table.id == id)

    if not table.first():
        return {
            "success": False,
            "message": "Not Found"
        }

    table.update(request.dict())
    db.commit()
    return {
        "success": True,
        "data": table.first()
    }

@router.delete('/{id}')
async def delete_table_by_id(id: int, db: Session = Depends(get_mysql_db)):
    table = db.query(models.Table).filter(models.Table.id == id)

    if not table.first():
        return {
            "success": False,
            "message": "Not Found"
        }

    table.delete(synchronize_session=False)
    db.commit()
    return {
        "success": True
    }