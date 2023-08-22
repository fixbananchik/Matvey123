class User():
    def __init__(self , name, s, id) -> None:
        self.name = name
        self.secname = s
        self.id = id
        self.online = False

    def __str__(self):
        return self.name + ' ' + self.secname 
    
    def toJSON(self):
        buffer = {
            'name': self.name,
            'sname': self.secname,
            'id': self.id,
            'online': self.online
        }
        return buffer