from datetime import datetime, date
from operator import attrgetter

from Models.Task_Model import Task


def FindTaskCompletionTime(task):

    datetime_object1 = datetime.strptime(task[7], '%Y-%m-%d')
    datetime_object2 = datetime.strptime(task[5], '%Y-%m-%d')

    # TypeError: 'Task' object is not subscriptable when trying to use like, task['ExpectedCompletionTime']
    # so, used task.ExpectedCompletionTime
    return (datetime_object1 - datetime_object2).days


def DisplayTasksbasedontimeCompletion(tasks):
    task_list = []
    for i in tasks:
        # convert the cursor sql lite object to list
        convertedlist = list(i)
        # so that, it can be assigned the difference in days value
        # since the tuple cannot be assigned the value
        value = FindTaskCompletionTime(convertedlist)
        convertedlist[8] = value
        # append the task list
        # called the model class for the sorting process
        # did not work without the identifier
        task_list.append(
            Task(convertedlist[0],
                 convertedlist[1],
                 convertedlist[2],
                 convertedlist[3],
                 convertedlist[4],
                 convertedlist[5],
                 convertedlist[6],
                 convertedlist[7],
                 convertedlist[8]
                 ))

    task_list.sort(key=lambda x: x.DaysDifference)
    return task_list


def print_data_in_string(tasks):
    for i in tasks:
        print(type(i['CreatedDate']))
        print(type(i['Name']))
        date_time_obj = datetime.strftime(i['CreatedDate'], '%Y-%m-%d')
        print(date_time_obj)


def print_data_in_date_type(tasks):
    for i in tasks:
        print(type(i['CreatedDate']))
        print(type(i['Name']))
        date_time_obj = datetime.strptime(i['CreatedDate'], '%Y-%m-%d')
        print(date_time_obj)

# Problems Faced

## task.fieldname did not work -- changed to task['fieldName']
## unsupported operand type of str and str for finding out difference
