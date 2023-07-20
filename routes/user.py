from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models.user import User, Base
from database import get_db, engine

Base.metadata.create_all(bind=engine)

router = APIRouter()


@router.get("/users/{user_id}")
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).get(user_id)
    if user is None:
        return {"message": "User not found"}
    return user


@router.get("/users")
def get_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return users


@router.post("/users")
def create_user(username: str, email: str, db: Session = Depends(get_db)):
    user = User(username=username, email=email)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


@router.put("/users/{user_id}")
def update_user(user_id: int, username: str, email: str, db: Session = Depends(get_db)):
    user = db.query(User).get(user_id)
    if user is None:
        return {"message": "User not found"}
    user.username = username
    user.email = email
    db.commit()
    db.refresh(user)
    return user


@router.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).get(user_id)
    if user is None:
        return {"message": "User not found"}
    db.delete(user)
    db.commit()
    return {"message": "User deleted successfully"}
