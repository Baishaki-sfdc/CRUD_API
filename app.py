# app.py
from flask import Flask, jsonify
from config import SQLALCHEMY_DATABASE_URI, SQLALCHEMY_TRACK_MODIFICATIONS
from database.db import db
from routes.user_routes import user_bp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = SQLALCHEMY_TRACK_MODIFICATIONS

db.init_app(app)

# Create database tables if they don't exist
with app.app_context():
    db.create_all()

# Register the blueprint with a prefix (e.g., /api)
app.register_blueprint(user_bp, url_prefix='/api')

# Root route
@app.route('/')
def index():
    return jsonify({
        "message": "Welcome to the User CRUD API!",
        "routes": {
            "Create User": "POST /api/users",
            "Retrieve All Users": "GET /api/users",
            "Retrieve Single User": "GET /api/users/<id>",
            "Update User": "PUT /api/users/<id>",
            "Delete User": "DELETE /api/users/<id>"
        }
    }), 200

# Error handlers
@app.errorhandler(400)
def bad_request(e):
    return jsonify({"error": str(e.description)}), 400

@app.errorhandler(404)
def not_found(e):
    return jsonify({"error": str(e.description)}), 404

if __name__ == '__main__':
    app.run(debug=True)
