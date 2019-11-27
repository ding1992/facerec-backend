from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow



app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/test.db'
db = SQLAlchemy(app)
ma = Marshmallow(app)



if __name__ == 'app':
    from api import video_api
    app.register_blueprint(video_api)
    app.run()
