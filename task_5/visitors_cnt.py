import ast


def solver(dates):
    changes = []

    for date_in, date_out in dates:
        date_out += '_out'
        changes.append((date_in, 1))
        changes.append((date_out, -1))
    
    changes.sort()

    guests_cnt = 0
    max_guests = 0
    max_date = None

    for day, change in changes:
        guests_cnt += change
        if guests_cnt > max_guests:
            max_guests = guests_cnt
            max_date = day
    
    return max_date, max_guests

def max_guests():
    dates = ast.literal_eval(input())
    return solver(dates)


        