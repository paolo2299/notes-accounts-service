from werkzeug.security import check_password_hash, generate_password_hash

from accounts_service.models.storage import user as storage

class User:
    def __init__(self, stored):
        self.id =   stored.id
        self.username = stored.username
        self.created_at = stored.created_at
        self.updated_at = stored.updated_at
        self._password_hash = stored.password

    @classmethod
    def from_id(cls, user_id):
        stored =  storage.User.query.filter_by(id=user_id).first()
        if stored:
            return cls(stored)
        return None

    @classmethod
    def from_username(cls, username):
        stored =  storage.User.query.filter_by(username=username).first()
        if stored:
            return cls(stored)
        return None

    @classmethod
    def create(cls, data):
        # TODO validation
        username = data.get('username')
        password_hash = generate_password_hash(data.get('password'))

        new_user = storage.User.create(username, password_hash)
        # TODO error handling
        return {'status': 'success', 'user_id': new_user.id}

    @classmethod
    def login(cls, username, password):
        user = cls.from_username(username)

        errors = None
        if user is None:
            errors = ['Incorrect username.']
        elif not user.check_password(password):
            errors = ['Incorrect password.']

        if errors is not None:
            return {'status': 'error', 'errors': errors}
        else:
            return {'status': 'success', 'user_id': user.id}
    
    def check_password(self, password):
        return check_password_hash(self._password_hash, password)

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }