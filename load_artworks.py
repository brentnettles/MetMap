import json
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///artworks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Artwork(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    objectID = db.Column(db.Integer, unique=True, nullable=False)
    galleryNumber = db.Column(db.String(120), index=True, nullable=True)
    primaryImage = db.Column(db.String(255))
    primaryImageSmall = db.Column(db.String(255))
    objectName = db.Column(db.String(255))
    title = db.Column(db.String(255))
    artistDisplayName = db.Column(db.String(255))

def load_artworks(json_path='artworks.json', gallery_numbers=None):
    with open(json_path, 'r') as file:
        artworks_data = json.load(file)
        for artwork_data in artworks_data:
            if gallery_numbers and artwork_data.get('GalleryNumber') not in gallery_numbers:
                continue  # Skip artworks not in the specified gallery numbers
            artwork = Artwork(
                objectID=artwork_data['objectID'],
                galleryNumber=artwork_data.get('GalleryNumber', ''),
                primaryImage=artwork_data.get('primaryImage', ''),
                primaryImageSmall=artwork_data.get('primaryImageSmall', ''),
                objectName=artwork_data.get('objectName', ''),
                title=artwork_data.get('title', ''),
                artistDisplayName=artwork_data.get('artistDisplayName', '')
            )
            db.session.add(artwork)
        db.session.commit()

if __name__ == '__main__':
    with app.app_context():
        db.drop_all()  # Drop all tables
        db.create_all()  # Create all tables based on the models defined
        load_artworks(gallery_numbers=['512', '516'])