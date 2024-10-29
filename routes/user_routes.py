from flask import Blueprint, request, render_template, redirect, url_for
from bson import ObjectId  
from utils.db import mongo
from models.user import User

user_routes = Blueprint('user_routes', __name__)

@user_routes.route('/users')
def get_users():
    users = list(mongo.db.users.find())
    return render_template('user_list.html', users=users)

@user_routes.route('/users/new', methods=['GET', 'POST'])
def create_user():
    if request.method == 'POST':
        user_data = request.form
        user = User(
            id=str(ObjectId()),  
            name=user_data['name'],
            email=user_data['email'],
            password=user_data['password']
        )
        mongo.db.users.insert_one(user.dict())
        return redirect(url_for('user_routes.get_users'))
    return render_template('user_form.html', title='Add User', action=url_for('user_routes.create_user'))

@user_routes.route('/users/<user_id>', methods=['GET', 'POST'])
def update_user(user_id):
    if request.method == 'POST':
        user_data = request.form
        mongo.db.users.update_one({"_id": ObjectId(user_id)}, {"$set": user_data})
        return redirect(url_for('user_routes.get_users'))
    
    user = mongo.db.users.find_one({"_id": ObjectId(user_id)})
    return render_template('user_form.html', title='Edit User', user=user, action=url_for('user_routes.update_user', user_id=user_id))

@user_routes.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    mongo.db.users.delete_one({"_id": ObjectId(user_id)})
    return redirect(url_for('user_routes.get_users'))
