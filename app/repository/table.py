from msilib import schema
from app import schemas, models
from sqlalchemy.orm import Session

def create(request: schemas.Table, db: Session):
    new_table = models.Table(description=request.description, status=request.status)
    db.add(new_table)
    db.commit()
    db.refresh(new_table)
    return new_table

def get_all(db: Session):
    return db.query(models.Table).all()

def get_by_id(id: int, db: Session):
    table = db.query(models.Table).filter(models.Table.id == id).first()
    return table

def update(id: int, request: schemas.Table, db: Session):
    table = db.query(models.Table).filter(models.Table.id == id)

    if not table.first():
        return "Not Found"

    table.update(request.dict())
    db.commit()
    return table.first()

def destroy(id: int, db: Session):
    table = db.query(models.Table).filter(models.Table.id == id)

    if not table.first():
        return "Not Found"

    table.delete(synchronize_session=False)
    db.commit()
    return "success"