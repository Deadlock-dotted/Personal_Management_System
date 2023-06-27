from flask import Flask, render_template, request, jsonify
import os, re, datetime
from Database_Connection import db
from Database_Connection.db import DropSpecificTable, DeleteFromSpecificTable, connect
from Models import Task_Model
from Models.Task_Model import Task

app = Flask(__name__)

if not os.path.isfile('Task.db'):
    db.connect()


@app.route('/GetTasks', methods=['GET'])
def GetTasks():
    content_type = request.headers.get('Content-Type')
    tasks = [task.serialize() for task in db.view()]

    if content_type == 'application/json':
        json = request.json
        for task in tasks:
            if task['id'] == int(json['id']):
                return jsonify({
                    'res': task,
                    'status': '200',
                    'msg': 'Successfully Got all the tasks !👍😀'
                })
        return jsonify({
            'error': f"Error ⛔❌! Task with id '{json['id']}' not found!",
            'res': '',
            'status': '404'
        })
    else:
        return jsonify({
            # 'error': '',
            'res': tasks,
            'status': '200',
            'msg': 'Successfully Got all the tasks !👍😀',
            'no_of_books': len(tasks)
        })


@app.route('/AddTask', methods=['POST'])
def AddTask():
    req_data = request.get_json()
    # Email Validation Skipped
    Name = req_data['Name']
    bks = [b.serialize() for b in db.view()]

    for b in bks:
        if b['Name'] == Name:
            return jsonify({
                'res': f'Error ⛔❌! Task with title {Name} is already present!',
                'status': '404'
            })

    bk = Task(db.getNewId(), Name, req_data['Description'], req_data['Progress'],
              req_data['ReminderRequired'], req_data['CreatedDate'], req_data['ModifiedDate'])
    print('new Book:', bk.serialize())
    db.insert(bk)

    # new_bks = [b.serialize() for b in db.view()]
    # print('books in lib :', new_bks)

    return jsonify({
        # 'res': bk.serialize(),
        'status': '200',
        'msg': 'Success creating a new Task!👍😀'
    })


@app.route('/DropTable', methods=['GET'])
def DropTable():
    DropSpecificTable()

    return jsonify({
        'status': '200',
        'msg': 'Successfully deleted the table!👍😀'
    })


@app.route('/DeleteAllRecordsFromTable', methods=['POST'])
def DeleteFromTable():
    req_data = request.get_json()
    table = req_data['Table']
    result = DeleteFromSpecificTable(table)

    return jsonify({
        'res': [],
        'status': '200',
        'msg': 'Successfully deleted all records from the table!'
    })


@app.route('/CreateNewTable', methods=['POST'])
def CreateNewTable():
    req_data = request.get_json()
    table = req_data['Table']
    connect()

    return jsonify(
        {
            'res': [],
            'status': '200',
            'msg': 'Successfully created new table!'
        }
    )

if __name__ == '__main__':
    app.run(debug=True)
