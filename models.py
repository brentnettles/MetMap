from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///artworks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Artwork(db.Model, SerializerMixin):
    __tablename__ = 'artwork'  # Ensuring table name is explicitly defined

    id = db.Column(db.Integer, primary_key=True)
    objectID = db.Column(db.Integer, unique=True, nullable=False)
    galleryNumber = db.Column(db.String(120), index=True, nullable=True)
    primaryImage = db.Column(db.String(255))
    primaryImageSmall = db.Column(db.String(255))
    objectName = db.Column(db.String(255))
    title = db.Column(db.String(255))
    artistDisplayName = db.Column(db.String(255))

    def to_dict(self):
        return {
            "id": self.id,
            "objectID": self.objectID,
            "galleryNumber": self.galleryNumber,
            "primaryImage": self.primaryImage,
            "primaryImageSmall": self.primaryImageSmall,
            "objectName": self.objectName,
            "title": self.title,
            "artistDisplayName": self.artistDisplayName
        }