import tkinter as tk
import requests

def search_pokemon():
    pokemon_name = entry.get()
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}")
    if response.status_code == 200:
        data = response.json()
        result_label.config(text=f"Nome: {data['name'].capitalize()}\n"
                                 f"Altura: {data['height']}\n"
                                 f"Peso: {data['weight']}")
    else:
        result_label.config(text="Pokémon não encontrado.")

# Criação da janela
window = tk.Tk()
window.title("Informações de Pokémon")

# Caixa de entrada
entry = tk.Entry(window, width=35)
entry.pack(pady=10)

# Botão de pesquisa
search_button = tk.Button(window, text="Buscar", command=search_pokemon, font= 'arial', fg='blue', width=15 )
search_button.pack()

# Rótulo para exibir os resultados
result_label = tk.Label(window, text="", width=150, font='arial', fg='green', height=35 )
result_label.pack()

# Inicia a janela
window.mainloop()



# if response.status_code == 200:: Este é um condicional que verifica se o código de status da resposta 
# da API é igual a 200. O código de status 200 é geralmente usado para indicar que a solicitação foi bem-sucedida.

