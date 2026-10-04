class student:
    name = "Dhanvin"
    grade = 9

    def introduce(self):
        print("Hi i am a student")
    def details(self):
        print("My name is", self.name, "and i am a student of grade", self.grade)
ob = student()
ob.introduce()
ob.details()