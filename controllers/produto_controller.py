from flask import request, jsonify
from models.produto import db, Produto
from models.schemas import produto_schema, produtos_schema

def criar_produto():
    data = request.json

    
    if len(data["nome"]) < 3:
        return jsonify({"erro": "O nome deve ter pelo menos 3 caracteres"}), 400
    if data["preco"] <= 0:
        return jsonify({"erro": "O preço deve ser positivo"}), 400
    if data["estoque"] < 0:
        return jsonify({"erro": "O estoque deve ser maior ou igual a zero"}), 400

    novo_produto = Produto(nome=data["nome"], preco=data["preco"], estoque=data["estoque"])
    db.session.add(novo_produto)
    db.session.commit()
    return produto_schema.jsonify(novo_produto), 201

def listar_produtos():
    produtos = Produto.query.all()
    return produtos_schema.jsonify(produtos)

def buscar_produto(id):
    produto = Produto.query.get(id)
    if not produto:
        return jsonify({"erro": "Produto não encontrado"}), 404
    return produto_schema.jsonify(produto)

def atualizar_produto(id):
    produto = Produto.query.get(id)
    if not produto:
        return jsonify({"erro": "Produto não encontrado"}), 404

    data = request.json
    produto.nome = data.get("nome", produto.nome)
    produto.preco = data.get("preco", produto.preco)
    produto.estoque = data.get("estoque", produto.estoque)

    db.session.commit()
    return produto_schema.jsonify(produto)

def excluir_produto(id):
    produto = Produto.query.get(id)
    if not produto:
        return jsonify({"erro": "Produto não encontrado"}), 404

    db.session.delete(produto)
    db.session.commit()
    return jsonify({"mensagem": "Produto excluído"}), 200
