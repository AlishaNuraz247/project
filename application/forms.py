class DogForm(FlaskForm):
    name = StringField("Name")
    dob = IntegerField("dob")
    breed = SelectField("Dog Breed", choices=[
        ("pomeranian", "Pomeranian"), 
        ("retriever", "Retriever"), 
        ("teacup", "Teacup")
    ])
    submit = SubmitField("Submit")