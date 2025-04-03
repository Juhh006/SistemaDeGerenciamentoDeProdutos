from flask_marshmallow import Marshmallow
from models.produto import Produto

ma = Marshmallow()

class ProdutoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Produto

produto_schema = ProdutoSchema()
produtos_schema = ProdutoSchema(many=True)
