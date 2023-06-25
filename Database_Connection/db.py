import random
import sqlite3

from Models.Task_Model import Task


def getNewId():
    return random.getrandbits(28)


tasks = [
    {
        'Name': 'StudyPython',
        'Description': 'Focus on Python Slicing Techniques',
        'Progress': 'Not Started',
        'ReminderRequired': 'Yes',
        'CreatedDate': '2023-06-18',
        'ModifiedDate': '2023-06-18'
    }

]


def connect():
    conn = sqlite3.connect('Management.db')
    cur = conn.cursor()
    # cur.execute("CREATE TABLE IF NOT EXISTS Management(id BIGINT, name TEXT, description TEXT, Progress TEXT, "
    #             "ReminderRequired TEXT, CreatedDate "
    #             "NUMERIC, ModifiedDate NUMERIC) ")

    conn.execute('''CREATE TABLE IF NOT EXISTS Management
             (id INT PRIMARY KEY     NOT NULL,
             Name           VARCHAR(255)    NOT NULL,
             Description            VARCHAR(255)     NOT NULL,
             Progress        VARCHAR(255),
             ReminderRequired  VARCHAR(255),
             CreatedDate NUMERIC,
             ModifiedDate NUMERIC);''')

    conn.commit()
    conn.close()

    for i in tasks:
        tsk = Task(getNewId(), i['Name'], i['Description'], i['Progress'], i['ReminderRequired'], i['CreatedDate'],
                   i['ModifiedDate'])
        insert(tsk)


def insert(task):
    conn = sqlite3.connect('Management.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO Management(id, Name, Description, Progress, ReminderRequired, CreatedDate, ModifiedDate) "
                "VALUES(?, ?, ?, ?, ?, ?, ?)", (
                    # task.id,
                    getNewId(),
                    str(task.Name),
                    str(task.Description),
                    str(task.Progress),
                    str(task.ReminderRequired),
                    str(task.CreatedDate),
                    str(task.ModifiedDate)
                ))
    conn.commit()
    conn.close()


def view():
    # connect()

    # conn = sqlite3.connect('Task.db')

    conn = sqlite3.connect('Management.db')
    print(conn)

    print('database opened successfully')

    connect()

    cur = conn.cursor()

    cur.execute("SELECT * FROM Management")

    rows = cur.fetchall()
    taskList = []
    for i in rows:
        task = Task(i[0], i[1], i[2], i[3], i[4], i[5], i[6])
        taskList.append(task)

    conn.close()
    return taskList


def DropSpecificTable():
    conn = sqlite3.connect('Management.db')
    cur = conn.cursor()

    cur.execute("DROP TABLE Management")
