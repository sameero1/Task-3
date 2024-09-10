class Config:
    SECRET_KEY = 'your_secret_key_here'  # Ensure you have a secret key
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
