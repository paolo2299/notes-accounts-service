from accounts_service.database import db
from datetime import datetime

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128), nullable=False, unique=True)
    password = db.Column(db.String(128), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    @classmethod
    def create(cls, username, password_hash):
        # TODO validation
        new_user = cls(
            username=username,
            password=password_hash
        )
        db.session.add(new_user)
        db.session.commit()
        # TODO error handling
        return new_user

