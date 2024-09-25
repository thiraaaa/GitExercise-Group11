import os

SQLALCHEMY_DATABASE_URI = 'sqlite:///mmu_map.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False

UPLOAD_FOLDER = os.path.join(os.getcwd(), 'static', 'uploads')