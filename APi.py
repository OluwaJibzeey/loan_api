from fastapi import FastAPI
import joblib
import pandas as pd
from pydantic import BaseModel

app = FastAPI(title = "loan_ability api")

model = joblib.load("loan model.pkl")
class loandata(BaseModel):
    Married:int
    Dependents:int
    Education:int
    Self_Employed:int
    Applicant_Income:int
    Coapplicant_Income:int
    Loan_Amount:int
    Term:int
    Credit_History:int
    Area:int
    Status:int

@app.get("/")
def home():
    return {"message":"welcome to loan_api"}


