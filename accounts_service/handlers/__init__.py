from accounts_service.handlers import users

def init_app(app):
    app.register_blueprint(users.blueprint)