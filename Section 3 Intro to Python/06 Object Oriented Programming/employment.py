# This program is a demonstration of Parent/Child classes
class Employees:
    def __init__(self, name, last) -> None:
        self.name = name
        self.last = last

class Supervisors(Employees):
    def __init__(self, name, last, password) -> None:
        super().__init__(name, last)
        self.password = password

class Chefs(Employees):
    def leave_request(self, days):
        return "May I take a leave for " + str(days) + " days"
    
adrian = Employees("Adrian", "A")

emily = Chefs("Emily", "E")
adrian = Chefs("Juno", "J")

print(emily.leave_request(3))
print(adrian.password)
print(emily.name)