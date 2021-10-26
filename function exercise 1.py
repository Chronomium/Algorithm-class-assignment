def convert_to_days():
    hour = eval(input("Enter number of hours: "))
    minute = eval(input("Enter number of minutes: "))
    second = eval(input("Enter number of seconds: "))
    return hour, minute, second

h, m, s = convert_to_days()

def get_days(h, m, s):
    days = (h + (m / 60) + (s / 3600)) / 24
    return days

result = get_days(h, m, s)

print("The number of days is:",format(result, '.4f'))