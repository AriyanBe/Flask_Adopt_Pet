from flask import Flask
from helper import pets

app = Flask(__name__)
pet_dict = pets

@app.route('/')
def index():
    return '''
    <h1>Adopt A Pet!</h1>
    <p>Browse through the links below to find your new furry friend:</p>
    <ul>
        <li><a href='/animals/dogs'>Dogs</a></li>
        <li><a href='/animals/cats'>Cats</a></li>
        <li><a href='/animals/rabbits'>Rabbits</a></li>
    </ul>
    '''

@app.route('/animals/<pet_type>')
def animals(pet_type):
    html = f"<h1>List of {pet_type}</h1>"
    html += "<ul>"
    for i, pet in enumerate(pet_dict[pet_type]):
        html += f"<li><a href='/animals/{pet_type}/{i}'>{pet['name']}</a></li>"
    html += "</ul>"
    return html

@app.route('/animals/<pet_type>/<int:pet_id>')
def pet(pet_type, pet_id):
    pet_list = pet_dict[pet_type]
    if pet_id >= 0 and pet_id < len(pet_list):
        pet = pet_list[pet_id]
        name = pet['name']
        breed = pet['breed']
        age = pet['age']
        description = pet['description']
        photo_url = pet['photo_url']
        html = f"<h1>{name}</h1>"
        html += f"<img src='{photo_url}' alt='{name}'>"
        html += f"<p>{description}</p>"
        html += "<ul>"
        html += f"<li>Breed: {breed}</li>"
        html += f"<li>Age: {age}</li>"
        html += "</ul>"
        return html
    else:
        return "<h1>Invalid Pet ID</h1>"