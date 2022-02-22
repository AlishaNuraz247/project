from application import app, db
from application.models import Dog 
from application.forms import DogForm
from flask import render_template, url_for
@app.route('/')
def home():
    return render_template('layout.html', title='home')

@app.route('/add')
def add():
    form = DogForm()
    if form.validate_on_submit():
        dog = Dog(
            name=form.name.data,
            breed = form.breed.data,
            owner= form.owner.data,
            notes= form.notes.data)
        db.session.add(dog)
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