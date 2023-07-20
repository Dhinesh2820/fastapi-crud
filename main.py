from fastapi import FastAPI
from routes.user import router as user_router

app = FastAPI()

# Include the user routes from the user_router
app.include_router(user_router)
