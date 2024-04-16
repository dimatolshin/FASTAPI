from fastapi import FastAPI, Body, status, Depends
from fastapi.responses import JSONResponse, FileResponse
from SQLAlchemi.database import *


Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()


@app.get('/')
def main():
    return FileResponse('publick/index.html')


@app.get('/api/users')
def all_data(db: Session = Depends(get_db)):
    return db.query(Person).all()


@app.get('/api/users/{id}')
def get_person(id, db: Session = Depends(get_db)):
    user = db.query(Person).filter(Person.id == id).first()
    if user == None:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={'message': 'user does not exits'})
    return user


@app.post('/api/users')
def create_person(user=Body(), db: Session = Depends(get_db)):
    person = Person(name=user['name'], age=user['age'])
    if person.name == '' or person.age == None:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={'message': 'user does not exits'})
    else:
        db.add(person)
        db.commit()
        db.refresh(person)
        return person


@app.put("/api/users")
def edit_person(data=Body()):
    person = db.query(Person).filter(Person.id == data['id']).first()
    if not person:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={'message': 'user does not exits'})
    else:
        person.name = data['name']
        person.age = data['age']
        db.commit()
        db.refresh(person)
        return person


@app.delete('/api/users/{id}')
def delete_data(id):
    person = db.query(Person).filter(Person.id == id).first()
    if person:
        db.delete(person)
        db.commit()
        return person
    else:
        JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={'message': "user does not exit"})


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8002)
