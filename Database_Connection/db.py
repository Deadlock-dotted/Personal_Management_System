import sqlite3, random, datetime

from Models import Task


def getNewId():
    return random.getrandbits(28)


tasks = [
    {
        'Name': 'Study Python',
        'Description': 'Focus on Python Slicing Techniques',
        'Progress': 'Not Started',
        'ReminderRequired': 'Yes',
        'CreatedDate': '2023-06-18',
        'ModifiedDate': '2023-06-18'
    }

]


def connect():
    conn = sqlite3.connect('Task.db')
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS Task (id INTEGER PRIMARY KEY, name TEXT, description TEXT, Progress TEXT, "
                "ReminderRequired BOOLEAN, CreatedDate "
                "TEXT, ModifiedDate TEXT) ")

    conn.commit()
    conn.close()

    for i in tasks:
        tsk = Task()
        insert(bk)


def insert(task):

    conn = sqlite3.connect('Task.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO Task VALUES(?, ?, ?, ?)", (
        task.id,
        task.Name,
        task.Description,
        task.Progress,
        task.ReminderRequired,
        task.CreatedDate,
        task.ModifiedDate
    ))
    conn.commit()
    conn.close()


def view():
    #connect()
    conn = sqlite3.connect('Task.db')
    cur = conn.cursor()

    cur.execute("SELECT * FROM Task")

    rows = cur.fetchall()
    taskList = []
    for i in rows:
        task = Task(i[0], i[2], i[3], i[4], True if i[5] == 1 else False, i[6], i[7])
        taskList.append(task)

    conn.close()
    return taskList
