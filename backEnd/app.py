"""further details about the process:
https://flask-marshmallow.readthedocs.io/en/latest/#flask_marshmallow.sqla.SQLAlchemyAutoSchema

For installation:
pip install -U flask-sqlalchemy marshmallow-sqlalchemy
"""

from flask import Flask

# Get DBs and Marschmallow
from extensions import db, ma

# Get Blueprints
from blueprints.operationalEndpoints.geopy import blueprint as geopy_endpoints

import os

geopyDBPath = os.path.join(os.getcwd(), "blueprints","operationalEndpoints","geopy", "geopydb.sqlite")

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{geopyDBPath}"

# Order matters: Initialize SQLAlchemy before Marshmallow


#Blueprint registration
app.register_blueprint(geopy_endpoints)    

db.init_app(app)
ma.init_app(app)

if __name__ == '__main__':
    app.run()