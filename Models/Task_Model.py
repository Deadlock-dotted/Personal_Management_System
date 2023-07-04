class Task:
    def __init__(self, id, Name, Description, Progress, ReminderRequired, CreatedDate, ModifiedDate, ExpectedCompletionTime, DaysDifference):
        self.id = id,
        self.Name = Name,
        self.Description = Description,
        self.Progress = Progress,
        self.ReminderRequired = ReminderRequired,
        self.CreatedDate = CreatedDate,
        self.ModifiedDate = ModifiedDate,
        self.ExpectedCompletionTime = ExpectedCompletionTime
        self.DaysDifference = DaysDifference

    def serialize(self):
        return {
            'id': self.id,
            'Name': self.Name,
            'Description': self.Description,
            'Progress': self.Progress,
            'ReminderRequired': self.ReminderRequired,
            'CreatedDate': self.CreatedDate,
            'ModifiedDate': self.ModifiedDate,
            'ExpectedCompletionTime': self.ExpectedCompletionTime,
            'DiffernceDays' : self.DaysDifference
        }
