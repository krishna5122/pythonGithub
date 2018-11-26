class Employee:
    comp_name="sathya"
    @staticmethod
    def showinfo():
        print("iam static method")
        print(Employee.comp_name)
Employee.showinfo()
print(Employee.comp_name)