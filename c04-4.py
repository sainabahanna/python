class Time:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __add__(self, other):
        total = (self.hour * 3600 + self.minute * 60 + self.second +
                 other.hour * 3600 + other.minute * 60 + other.second)

        h = total // 3600
        m = (total % 3600) // 60
        s = total % 60

        return Time(h, m, s)

    def display(self):
        print(self.hour, "hours", self.minute, "minutes", self.second, "seconds")


h1 = int(input("Enter first hour: "))
m1 = int(input("Enter first minute: "))
s1 = int(input("Enter first second: "))

h2 = int(input("Enter second hour: "))
m2 = int(input("Enter second minute: "))
s2 = int(input("Enter second second: "))

t1 = Time(h1, m1, s1)
t2 = Time(h2, m2, s2)

t3 = t1 + t2

print("Sum of two times:")
t3.display()
