from flask import Flask, request, jsonify, render_template
from models import db, Produto

app = Flask(__name__)

# Criar um produto
@app.route('/produtos', methods=['POST'])
def criar_produto():
    dados = request.json
    if len(dados['nome']) < 3 or dados['preco'] <= 0 or dados['estoque'] < 0:
        return jsonify({'erro': 'Dados inválidos'}), 400
    novo_produto = Produto(nome=dados['nome'], preco=dados['preco'], estoque=dados['estoque'])
    db.session.add(novo_produto)
    db.session.commit()
    return jsonify({'mensagem': 'Produto criado'}), 201

# Listar todos os produtos
@app.route('/produtos', methods=['GET'])
def listar_produtos():
    produtos = Produto.query.all()
    return jsonify([{'id': p.id, 'nome': p.nome, 'preco': p.preco, 'estoque': p.estoque} for p in produtos])

# Obter um produto específico
@app.route('/produtos/<int:id>', methods=['GET'])
def obter_produto(id):
    produto = Produto.query.get_or_404(id)
    return jsonify({'id': produto.id, 'nome': produto.nome, 'preco': produto.preco, 'estoque': produto.estoque})

# Atualizar um produto
@app.route('/produtos/<int:id>', methods=['PUT'])
def atualizar_produto(id):
    produto = Produto.query.get_or_404(id)
    dados = request.json
    if len(dados['nome']) < 3 or dados['preco'] <= 0 or dados['estoque'] < 0:
        return jsonify({'erro': 'Dados inválidos'}), 400
    produto.nome = dados['nome']
    produto.preco = dados['preco']
    produto.estoque = dados['estoque']
    db.session.commit()
    return jsonify({'mensagem': 'Produto atualizado'})

# Excluir um produto
@app.route('/produtos/<int:id>', methods=['DELETE'])
def deletar_produto(id):
    produto = Produto.query.get_or_404(id)
    db.session.delete(produto)
    db.session.commit()
    return jsonify({'mensagem': 'Produto excluído'})
