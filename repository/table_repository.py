from dto.table import TableCreate
from models.tables import Table
from sqlalchemy.orm import Session
from constants import error_types

def create(request: TableCreate, db: Session):
    new_table = Table(description=request.description, status=request.status)
    db.add(new_table)
    db.commit()
    db.refresh(new_table)
    return new_table

def get_all(db: Session):
    return db.query(Table).all()

def get_by_id(id: int, db: Session):
    table = db.query(Table).filter(Table.id == id).first()
    return table

def update(id: int, request: TableCreate, db: Session):
    table = db.query(Table).filter(Table.id == id)

    if not table.first():
        return error_types.NOT_FOUND

    table.update(request.dict())
    db.commit()
    return table.first()

def destroy(id: int, db: Session):
    table = db.query(Table).filter(Table.id == id)

    if not table.first():
        return error_types.NOT_FOUND

    table.delete(synchronize_session=False)
    db.commit()
    return "success"