from fastapi import FastAPI
import mysql.connector
import os

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Backend Running"}

@app.get("/db")
def db_check():

    connection = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )

    return {"status": "Database Connected"}
