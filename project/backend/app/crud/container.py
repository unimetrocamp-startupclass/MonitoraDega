from sqlalchemy.orm import Session
from app.models.container import Container

def create_container(db: Session, name: str):
    container = Container(name=name)
    db.add(container)
    db.commit()
    db.refresh(container)
    return container

def get_container(db: Session, container_id: int):
    return db.query(Container).filter(Container.id == container_id).first()

def get_containers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Container).offset(skip).limit(limit).all()

def delete_container(db: Session, container_id: int):
    container = db.query(Container).filter(Container.id == container_id).first()
    if container:
        db.delete(container)
        db.commit()
    return container
