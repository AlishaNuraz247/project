from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
class DogForm(FlaskForm):
    name = StringField("Name")
    breed = SelectField("Dog Breed", choices=[
        ("pomeranian", "Pomeranian"), 
        ("retriever", "Retriever"), 
        ("teacup", "Teacup")
    ])
    owner= StringField("Owner")
    notes= StringField("Notes")
    submit = SubmitField("Submit")