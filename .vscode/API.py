# python api - framework - fast api - rest api 
# api oops pip install fastapi uvicorn 
# server install uvicorn -browser - 8000 
# base model = structure and validate 
from fastapi import FastAPI
from pydantic import BaseModel

# fastapi oops -class 
# class initialization data store 
app = FastAPI()  # initialization of fast api class 

student = []  # blank list 

class mydata(BaseModel):
    id: int
    name: str
    email: str

# get post delete - function decorator/annotation
# set of instruction 
# server properly work 
# routes /
@app.get("/")
def testing():
    return {"msg": "server is running"}

# all datafetch - get
@app.get("/alldata") 
def alldatafetch():
    return student

# data insert - post 
# insert into tb name, email, id 
@app.post("/datainsert")
def datainsert(s: mydata):
    student.append(s.model_dump())
    return {"msg": "data inserted"}

# delete - put patch = data set 
# delete * from tb where id=5
# id pass = list student  
@app.delete("/mydelete/{id}")
def datadelete(id: int):
    for s in student:
        if s["id"] == id:
            student.remove(s)
            return {"msg": "data deleted"}
    return {"msg": "id not found"}

# python run uvicorn 
# uvicorn API:app --reload    
# common end point http://127.0.0.1:8000/