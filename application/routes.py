from application import app, db
from application.models import Dog 

@app.route('/add')
def add():
    dog_breed = Dog(name="breed")
    db.session.add(dog_breed)
    db.session.commit()
    return "Added new dog breed to database"

@app.route('/read')
def read():
    all_dogs_breed = dogs.query.all()
    dog_string = ""
    for dog in all_dogs:
        dog_sring += "<br>"+ dog.breed
    return dog_string

@app.route('/update/<name>')
def update(name):
    name = __name__.query.first()
    first_dog_name.name = name
    db.session.commit()
    return first_dog_name.name