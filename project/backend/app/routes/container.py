from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.crud import container as crud_containers
from app.models.container import Container
from app.database import get_db
from app.schemas.container import Container as ContainerSchema, ContainerCreate

router = APIRouter(
    tags=["containers"]
)

@router.post("/", response_model=ContainerSchema)
def create_container(container: ContainerCreate, db: Session = Depends(get_db)):
    db_container = crud_containers.create_container(db, container.name)
    return db_container

@router.get("/", response_model=list[ContainerSchema])
def list_containers(db: Session = Depends(get_db)):
    containers = crud_containers.get_containers(db)
    return containers

@router.get("/{container_id}", response_model=ContainerSchema)
def get_container(container_id: int, db: Session = Depends(get_db)):
    container = crud_containers.get_container(db, container_id)
    if not container:
        raise HTTPException(status_code=404, detail="Container not found")
    return container

@router.delete("/{container_id}", response_model=dict)
def delete_container(container_id: int, db: Session = Depends(get_db)):
    container = crud_containers.delete_container(db, container_id)
    if not container:
        raise HTTPException(status_code=404, detail="Container not found")
    return {"detail": "Container deleted"}
