"""
EP - 19

You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

"""
import calendar as ca

def sundays(year):
    total = 0
    for mon in range(1, 13): # (Jan .. Dec)
        cal = ca.monthcalendar(year,mon)
        if cal[0][0] == 1:
            total += 1 # we have got our sunday on 1st!
    return total

if __name__ == "__main__":
    ca.setfirstweekday(6) # 0 - Monday,.. 6 - Sunday
    count = 0
    for yr in range(1901, 2001):
        count += sundays(yr)
    print("Number of sundays on 1st of month during 20th century: {}".format(count))
