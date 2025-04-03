from flask import Blueprint
from controllers.produto_controller import (
    criar_produto, listar_produtos, buscar_produto, atualizar_produto, excluir_produto
)

produto_bp = Blueprint("produto_bp", __name__)

produto_bp.route("/produtos", methods=["POST"])(criar_produto)
produto_bp.route("/produtos", methods=["GET"])(listar_produtos)
produto_bp.route("/produtos/<int:id>", methods=["GET"])(buscar_produto)
produto_bp.route("/produtos/<int:id>", methods=["PUT"])(atualizar_produto)
produto_bp.route("/produtos/<int:id>", methods=["DELETE"])(excluir_produto)
