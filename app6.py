from flask import Flask, request, redirect, url_for, render_template
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb+srv://chai27:1234@cluster0.10svnei.mongodb.net/?appName=Cluster0")
db = client["userdata"]
collection = db["users"]

@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'POST':
        itemName = request.form['itemName']
        itemDescription = request.form['itemDescription']

        collection.insert_one({
            "itemName": itemName,
            "itemDescription": itemDescription
        })

        return redirect(url_for("success"))

    return render_template("form2.html")


@app.route('/submittodoitem', methods=['POST'])
def submit_todo_item():

    itemName = request.form['itemName']
    itemDescription = request.form['itemDescription']

    collection.insert_one({
        "itemName": itemName,
        "itemDescription": itemDescription
    })

    return "ToDo Item Submitted Successfully"


if __name__ == '__main__':
    app.run(debug=True)