from flask import Flask, jsonify, request

app = Flask(__name__) #Flask is a class, App is a class object (CREATED A CLASS USING FLASK CONSTRUCTOR)

tasks = [{
    'id': 1,
    'title': "Code the Projects",
    'description': "Python",
    'Done': False
    }]

@app.route("/add-data", methods = ["POST"])

def add_task():
    if not request.json:

        return jsonify({
            'status': "ERROR",
            'message': "Please provide the data!"
        },400)

    contact = {
        'id': tasks[-1]['id'] + 1,
        'Name': request.json['Name'],
        'Contact': request.json.get('Contact', ""),
        'done': False
    }

    tasks.append(contact)

    return jsonify({
        'status': 'success',
        'message': 'task added successfully'
    })

app.run()