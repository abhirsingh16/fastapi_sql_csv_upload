from fastapi import FastAPI, UploadFile, File, Depends
import pandas as pd
import io
from sqlalchemy.orm import Session
from app.database.connection import SessionLocal
from app.schema.model import Product



app = FastAPI()

# Dependency to get the DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/upload-csv/")
async def upload_csv(file: UploadFile = File(...), db: Session = Depends(get_db)):
    # Read the uploaded CSV file using pandas
    contents = await file.read()
    df = pd.read_csv(io.StringIO(contents.decode("utf-8")))

    
    # Iterate through the dataframe and add entries to the database
    for _, row in df.iterrows():
        product = Product(
            id=row['id'],
            name=row['name'],  # Assuming columns in CSV are named 'name', 'description', and 'price'
            phone=row['phone'],
            city=row['city']
        )
        db.add(product)

    db.commit()  # Commit the transaction to the database
    return {"message": "CSV uploaded successfully"}
