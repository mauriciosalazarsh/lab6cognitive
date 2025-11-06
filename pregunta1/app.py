from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    pokemon_data = None
    error = None

    if request.method == 'POST':
        pokemon_name = request.form.get('pokemon_name', '').strip().lower()

        if pokemon_name:
            try:
                response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}')

                if response.status_code == 200:
                    data = response.json()

                    pokemon_data = {
                        'name': data['name'].capitalize(),
                        'id': data['id'],
                        'types': [t['type']['name'] for t in data['types']],
                        'moves': [m['move']['name'] for m in data['moves'][:10]],
                        'sprites': {
                            'front_default': data['sprites']['front_default'],
                            'front_shiny': data['sprites']['front_shiny'],
                            'back_default': data['sprites']['back_default'],
                            'back_shiny': data['sprites']['back_shiny']
                        }
                    }
                else:
                    error = f"Pokémon '{pokemon_name}' no encontrado. Intenta con otro nombre."
            except Exception as e:
                error = f"Error al buscar el Pokémon: {str(e)}"
        else:
            error = "Por favor ingresa el nombre de un Pokémon."

    return render_template('index.html', pokemon_data=pokemon_data, error=error)

if __name__ == '__main__':
    app.run(debug=True)
