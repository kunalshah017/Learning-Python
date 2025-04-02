class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    def studentDetails(self):
        print("Name:", self.name)
        print("Marks:", self.marks)
    
    def isPassed(self):
        if(self.marks >= 40):
            print("Passed")
        else:
            print("Failed")

st1 = Student('Andy', 100)
st1.studentDetails()
st1.isPassed()