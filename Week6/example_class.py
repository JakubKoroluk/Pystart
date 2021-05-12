class Student:
    def __init__(self, first_name: str, last_name: str, semester: int = 1):
        self.first_name = first_name
        self.last_name = last_name
        self.semester = semester

    def Promote(self):
        self.semester += 1


george = Student('George', 'Jetson', 1)
print(george)
print(george.first_name, george.last_name)
print(george.semester)
george.Promote()
print(george.semester)

judy = george
george.first_name = "Judy"
print(george.first_name, george.last_name)