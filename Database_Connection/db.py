import random
import sqlite3

from Models.Task_Model import Task


def getNewId():
    return random.getrandbits(28)


#
# tasks = [
#     {
#         'Name': 'StudyPython',
#         'Description': 'Focus on Python Slicing Techniques',
#         'Progress': 'Not Started',
#         'ReminderRequired': 'Yes',
#         'CreatedDate': '2023-06-18',
#         'ModifiedDate': '2023-06-18'
#     }
#
# ]


def connect():
    conn = sqlite3.connect('Management.db')
    cur = conn.cursor()
    cur.execute("CREATE TABLE Tasks (id INTEGER PRIMARY KEY, Name TEXT, Description TEXT, Progress "
                "TEXT, ReminderRequired TEXT, CreatedDate NUMERIC, ModifiedDate NUMERIC) ")

    conn.commit()
    conn.close()


def insert(task):
    conn = sqlite3.connect('Management.db')
    cur = conn.cursor()

    sqlite_insert_query = """INSERT INTO Tasks(id, Name, Description, Progress, ReminderRequired, CreatedDate, 
    ModifiedDate, ExpectedCompletionTime) VALUES (?, ?, ?, ?, ?, ?, ?, ?); """

    data_tuple = (getNewId(), str(task.Name), str(task.Description), str(task.Progress), str(task.ReminderRequired),
                  str(task.CreatedDate), str(task.ModifiedDate), str(task.ExpectedCompletionTime))

    cur.execute(sqlite_insert_query, data_tuple)

    conn.commit()
    conn.close()


def view():

    conn = sqlite3.connect('Management.db')

    print('database opened successfully')

    cur = conn.cursor()

    cur.execute("SELECT id, Name, Description, Progress, ReminderRequired, CreatedDate, ModifiedDate, ExpectedCompletionTime, DaysDifference  FROM Tasks")

    rows = cur.fetchall()
    taskList = []
    for i in rows:
        task = Task(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8])
        taskList.append(task)

    conn.close()
    return taskList


def DropSpecificTable():
    conn = sqlite3.connect('Management.db')
    cur = conn.cursor()

    cur.execute("DROP TABLE Tasks")

    conn.close()


def DeleteFromSpecificTable(table):
    conn = sqlite3.connect('Management.db')
    cur = conn.cursor()

    try:

        cur.execute("DELETE FROM " + str(table))

        conn.commit()

    except:

        conn.rollback()

    print('Contents updated')

    conn.close()

    return cur.execute("SELECT id, Name, Description, Progress, CreatedDate, ModifiedDate, ExpectedCompletionTime FROM Tasks")


def ShowReminder():
    conn = sqlite3.connect('Management.db')
    cur = conn.cursor()

    try:

        rows = cur.execute('SELECT * FROM Tasks WHERE ReminderRequired = 1')

    except:

        print('Some error has occured')

## commenting for checking --
    # taskList = []
    # for i in rows:
    #     task = Task(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8])
    #     taskList.append(task)

    return rows


def ArrangeTasksInAscendingOrderBasedOnCompletionTime():
    conn = sqlite3.connect('Management.db')
    cur = conn.cursor()

    try:

        rows = cur.execute('SELECT id, Name, Description, Progress, CreatedDate, ModifiedDate, ExpectedCompletionTime FROM Tasks ORDER BY DaysDifference ASC')

    except:

        print('Some error has occured')

    taskList = []
    for i in rows:
        task = Task(i[0], i[1], i[2], i[3], i[4], i[5], i[6])
        taskList.append(task)

    return taskList




