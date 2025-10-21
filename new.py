class employee:
    def __init__(self):
        print("started executing data")
        self.id=123
        self.salary=50000
        self.designation="SDE"
        print("data initiated")

    def travel(self, destination):
            print("called travel func manually")
            print(f"Employee is now travelling to {destination}")
sam=employee()

sam.travel("kerala")
sam.travel("bhusawal")
print(type(sam))