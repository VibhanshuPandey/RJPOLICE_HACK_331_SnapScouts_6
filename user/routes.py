from user.models import *

def routes(app):
    @app.route('/')
    def hello_world():
        # db.new_doc.insert_one({"a": 1})
        return 'Hello, World!'

    @app.route('/user/signup', methods=['GET'])
    def signup():
        return User().signup()
    
    @app.route('/user/signup/camera', methods=['GET'])
    def camera():
        return Camera().cam_reg()