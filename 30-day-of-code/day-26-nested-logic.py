from datetime import date

def calculateFine(dueDate, returnDate):
    diff = returnDate - dueDate

    if(diff.days <= 0): return 0

    if(returnDate.year > dueDate.year):
        return 10e3
    
    if(returnDate.month > dueDate.month):
        monthDiff = returnDate.month - dueDate.month
        if (monthDiff < 0): monthDiff += 12
        return 500 * monthDiff

    return 15 * diff.days

if __name__ == "__main__":
    day, month, year = map(int, input().strip().split(' '))
    returnDate = date(year, month, day)
    
    day, month, year = map(int, input().strip().split(' '))
    dueDate = date(year, month, day)

    print(int(calculateFine(dueDate, returnDate)))

