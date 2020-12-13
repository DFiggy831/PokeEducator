from flask import Flask, render_template, url_for, flash, redirect
from flask_bootstrap import Bootstrap

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

from pokemon_info import pokemon_info
from PIL import Image

app = Flask(__name__)
app.config['SECRET_KEY'] = 'csumb-otter' # added a secret key
boostrap = Bootstrap(app)

# form for asking what pokemon they want to choose
class Pokemon(FlaskForm):

    # changed the wording a bit
    pokemon_1 = StringField(
        'Choose your 1ˢᵗ Pokemon from Generation 6: ', 
        validators=[DataRequired()]
    )

    pokemon_2 = StringField(
        'Choose your 2ⁿᵈ Pokemon from Generation 6: ', 
        validators=[DataRequired()]
    )

both_pokemon = []
# storing chosen pokemon in a list
def store_pokemon(poke_1, poke_2):

    if len(both_pokemon) != 0:
        both_pokemon.clear()
    
    both_pokemon.append(poke_1)
    both_pokemon.append(poke_2)


@app.route('/', methods=('GET', 'POST'))
def home():

    form = Pokemon()
    
    if form.validate_on_submit():
        store_pokemon(form.pokemon_1.data, form.pokemon_2.data)
        return redirect('/battle_arena')
    
    # home page
    return render_template('index.html', pokemon_info = pokemon_info, form = form)

@app.route('/battle_arena', methods=('GET', 'POST'))
def battle_arena():
    
    # if validate_on_submit():
    #     return redirect('/winner')

    # page displaying pokemon on battle arena
    return render_template('battle_arena.html', pokemon_info = pokemon_info, both_pokemon = both_pokemon)

@app.route('/winner', methods=('GET', 'POST'))
def winner():
    pokemon_winner = "chespin"
    p1_c = 0
    p2_c = 0
    for pokemon in pokemon_info:
        if both_pokemon[0] == pokemon['name']:
            p1_type1 = pokemon['type1']

    for pokemon in pokemon_info:
        if both_pokemon[1] == pokemon['name']:
            p2_type1 = pokemon['type1']

    for pokemon in pokemon_info:
        if both_pokemon[0] == pokemon['name']:
            p1_type2 = pokemon['type2']

    for pokemon in pokemon_info:
        if both_pokemon[1] == pokemon['name']:
            p2_type2 = pokemon['type2']

    for pokemon in pokemon_info:
        if both_pokemon[0] == pokemon['name']:
            p1_strengths = pokemon['strengths']
        
    for pokemon in pokemon_info:
        if both_pokemon[1] == pokemon['name']:
            p2_strengths = pokemon['strengths']
    
    if p2_type1 in p1_strengths:
        p1_c +=1

    if p2_type2 in p1_strengths:
        p1_c +=1
    
    if p1_type1 in p2_strengths:
        p2_c +=1

    if p1_type2 in p2_strengths:
        p2_c +=1
    
    print(p1_strengths[0])

    if p1_c > p2_c:
        pokemon_winner = both_pokemon[0]
    elif p2_c > p1_c:
        pokemon_winner = both_pokemon[1]
    else:
        pokemon_winner = "none"
    
    # page displaying the winner pokemon
    return render_template('winner.html', pokemon_info = pokemon_info, pokemon_winner = pokemon_winner, both_pokemon = both_pokemon)
