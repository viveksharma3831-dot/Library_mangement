from datetime import date

books = {
    "Python": 3,
    "Java": 2,
    "C Language": 2
}

issued_books = {}


def calculate_fine(late_days):
    fine = 0
    for day in range(1, late_days + 1):
        week = ((day - 1) // 7) + 1
        rate = 10
        for number in range(2, week + 1):
            rate = rate * number
        fine = fine + rate
    return fine
