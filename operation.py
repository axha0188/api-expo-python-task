from tinydb import TinyDB,Query

db = TinyDB('task.json')
task = Query()

class Task:
    def ReadAllTask(self):
        try:
            return db.all()
        except Exception as e:
            return { 'error': f'{e}', 'status': False }

    def CreateTask(self,data):
        try:
            db.insert(data)
            return { 'message': 'task add!', 'status': True }
        except Exception as e:
            return { 'error': f'{e}', 'status': False }
        
    def UpdateTask(self,id,data):
        try:
            db.update(data, task.id == id)
            return { 'message': 'update add!', 'status': True }
        except Exception as e:
            return { 'error': f'{e}', 'status': False }
    def DeleteTask(self,id):
        try:
            db.remove(task.id == id)
            return { 'message': 'task add!', 'status': True }
        except Exception as e:
            return { 'error': f'{e}', 'status': False }
        
    def DeleteAllTask(self):
        try:
            db.truncate()
            return { 'message': 'task add!', 'status': True }
        except Exception as e:
            return { 'error': f'{e}', 'status': False }
