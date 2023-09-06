import os
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Ensure the 'static/img' directory exists
avatar_dir = os.path.join(app.root_path, 'static', 'img')
os.makedirs(avatar_dir, exist_ok=True)

# Temporary storage for user data
user_data = {
    "name": "John Doe",
    "age": 30,
    "place": "City, Country",
    "bio": "This is my bio.",
    "username": "JohnDoe",
    "email": "johndoe@example.com",
    "avatar": "/static/img/default_avatar.jpg"
}


@app.route('/')
def user_profile():
    return render_template('user_profile.html', user_data=user_data)


@app.route('/edit', methods=['GET', 'POST'])
def edit_profile():
    if request.method == 'POST':
        # Update user data from the form
        user_data['name'] = request.form['name']
        user_data['age'] = request.form['age']
        user_data['place'] = request.form['place']
        user_data['bio'] = request.form['bio']
        user_data['username'] = request.form['username']
        user_data['email'] = request.form['email']

        # Handle image upload
        if 'avatar' in request.files:
            avatar = request.files['avatar']
            if avatar.filename != '':
                avatar_path = os.path.join(avatar_dir, 'custom_avatar.jpg')
                avatar.save(avatar_path)
                user_data['avatar'] = "/static/img/custom_avatar.jpg"

        # Redirect to the user profile page after saving
        return redirect(url_for('user_profile'))

    return render_template('edit_profile.html', user_data=user_data)


if __name__ == '__main__':
    app.run(port=5040)
    app.run(debug=False)

