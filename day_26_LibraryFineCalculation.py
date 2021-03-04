
return_date = input()
due_date = input()

def date_to_array(date):
    return list(map(int, date.split(' ')))

def fine(return_date, due_date):
    year_diff = date_to_array(return_date)[2] - date_to_array(due_date)[2]
    if year_diff > 0 :
        return 10000
    else:
        month_diff = date_to_array(return_date)[1] - date_to_array(due_date)[1]
        if month_diff > 0 and year_diff == 0:
            return 500*month_diff
        else:
            day_diff = date_to_array(return_date)[0] - date_to_array(due_date)[0]
            if day_diff > 0 and month_diff == 0:
                return 15*day_diff
            else:
                return 0
    
print(fine(return_date, due_date))
