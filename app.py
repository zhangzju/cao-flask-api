from flask import Flask
from flask_restful import Api

from com.auth import Login
from res.cao import Cao, Hehe
from res.contact import Fellow

app = Flask(__name__)
api = Api(app)

api.add_resource(Login, '/login', '/login/<str:id>')
api.add_resource(Fellow, '/fellow', '/fellow/<str:id>')
api.add_resource(Cao, '/cao', '/cao/<str:id>')
api.add_resource(Hehe, '/hehe', '/hehe/<str:id>')