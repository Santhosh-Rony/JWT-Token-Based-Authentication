from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from . import auth, schemas, users, dependencies
from datetime import timedelta
from .config import ACCESS_TOKEN_EXPIRE_MINUTES

app = FastAPI()

@app.post("/login", response_model=schemas.Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = users.get_user(form_data.username)
    if not user or not auth.verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    access_token = auth.create_access_token(
        data={"sub": user.username, "role": user.role},
        expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    )
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/dashboard")
async def dashboard(user=Depends(dependencies.get_current_user)):
    return {"message": f"Hello {user['username']}! You're a {user['role']}"}

@app.get("/admin")
async def admin_dashboard(user=Depends(dependencies.admin_required)):
    return {"message": f"Welcome Admin {user['username']}!"}
