from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {
        'id': 1,
        'titulo': 'Harry Potter e a pedra filosofal',
        'autor': 'J.K. Rowling',
    },
    {
        'id': 2,
        'titulo': 'Harry Potter e o enigma do príncipe',
        'autor': 'J.K. Rowling',
    },
    {
        'id': 3,
        'titulo': 'O Senhor dos Anéis - A Sociedade do Anel',
        'autor': 'J.R.R. Tolkien',
    },
    {
        'id': 4,
        'titulo': 'O Senhor dos Anéis - As Duas Torres',
        'autor': 'J.R.R. Tolkien'
    },
    {
        'id': 5,
        'titulo': 'O Senhor dos Anéis - O Retorno do Rei',
        'autor': 'J.R.R. Tolkien'
    },
    {
        'id': 6,
        'titulo': 'A Origem',
        'autor': 'Dan Brown',
    },
]


@app.route('/livros', methods=['GET'])  # Consultar(todos)
def obter_livros():
    return jsonify(livros)


@app.route('/livros/<int:id>', methods=['GET'])  # Consultar por id
def obter_livro_por_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)


@app.route('/livros/<int:id>', methods=['PUT'])  # Editar
def editar_livro_por_id(id):
    livro_alterado = request.get_json()
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])


@app.route('/livros', methods=['POST'])  # Incluir novo livro
def incluir_novo_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)

    return jsonify(livros)


# Deletar um livro a partir do seu id
@app.route('/livros/<int:id>', methods=['DELETE'])
def excluir_livro(id):
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]

    return jsonify(livros)


app.run(port=5000, host='localhost', debug=True)
