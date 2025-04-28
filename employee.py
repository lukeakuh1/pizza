class Employee:
    def __init__(self, name, employee_number):
        self.name = name
        self.emp_num = employee_number

    def __str__(self):
        return f"Employee Name: {self.name} \nEmployee Number: {self.emp_num}"

class ProductionWorker(Employee):
    def __init__(self, name, employee_number, hourly_pay_rate, shift_number):
        super().__init__(name, employee_number)
        self.hourly_pay = hourly_pay_rate
        self.shift_number =shift_number

    def shift_name(self):
        return "Day Shift" if self.shift_number == 1 else "Night Shift" if self.shift_number == 2 else "Invalid"

    def __str__(self):
        return f"{super().__str__()} \nHourly pay rate: {self.hourly_pay} \nShift: {self.shift_name()}({self.shift_number})"


def main():
    name = input("Enter employee name: ")
    empl_number = input("Enter employee ID: ")
    pay = float(input("Enter hourly pay: "))
    shift = int(input("Enter shift number: "))

    worker = ProductionWorker(name, empl_number, pay, shift)
    print("\nProduction Worker Information:")
    print(worker)

if __name__=="__main__":
    main()

