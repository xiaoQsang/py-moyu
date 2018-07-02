def is_R_or_N(user_in_date=2017):
    value_r_n = (user_in_date % 4 == 0 and user_in_date % 100 != 0) \
            or user_in_date % 400 ==0
    return value_r_n

def get_mend_days(mEnd=12, is_R_N=True):
    totaldays = 0
    if is_R_N:
        if mEnd == 12:
            totaldays= 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30 + 31 + 29 + 31
        elif mEnd == 11:
            totaldays= 31 + 30 + 31 + 31 + 30 + 31 + 30 + 31 + 29 + 31
        elif mEnd == 10:
            totaldays= 30 + 31 + 31 + 30 + 31 + 30 + 31 + 29 + 31
        elif mEnd == 9:
            totaldays= 31 + 31 + 30 + 31 + 30 + 31 + 29 + 31
        elif mEnd == 8:
            totaldays= 31 + 30 + 31 +  30 + 31 + 29 + 31
        elif mEnd == 7:
            totaldays= 30 + 31 + 30 + 31 + 29 + 31
        elif mEnd == 6:
            totaldays= 31 + 30 + 31 + 29 + 31
        elif mEnd == 5:
            totaldays= 30 + 31 + 29 + 31
        elif mEnd == 4:
            totaldays= 31 + 29 + 31
        elif mEnd == 3:
            totaldays= 29 + 31
        elif mEnd == 2:
            totaldays= 31
        elif mEnd == 1:
            totaldays= 0
    else:
        if mEnd == 12:
            totaldays= 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30 + 31 + 28 + 31
        elif mEnd == 11:
            totaldays= 31 + 30 + 31 + 31 + 30 + 31 + 30 + 31 + 28 + 31
        elif mEnd == 10:
            totaldays= 30 + 31 + 31 + 30 + 31 + 30 + 31 + 28 + 31
        elif mEnd == 9:
            totaldays= 31 + 31 + 30 + 31 + 30 + 31 + 28 + 31
        elif mEnd == 8:
            totaldays= 31 + 30 + 31 +  30 + 31 + 28 + 31
        elif mEnd == 7:
            totaldays= 30 + 31 + 30 + 31 + 28 + 31
        elif mEnd == 6:
            totaldays= 31 + 30 + 31 + 28 + 31
        elif mEnd == 5:
            totaldays= 30 + 31 + 28 + 31
        elif mEnd == 4:
            totaldays= 31 + 28 + 31
        elif mEnd == 3:
            totaldays= 28 + 31
        elif mEnd == 2:
            totaldays= 31
        elif mEnd == 1:
            totaldays= 0
    return totaldays
def get_total_days_of_one_year(year=2017, is_R_N=True):
    if is_R_N :
        one_year = 366
    else:
        one_year = 365
    return one_year

def get_before_years_total_days(yEnd=2017, yStart=2000):
    totaldays = 0
    years = range(yStart, yEnd)
    for year_every in years:
        if is_R_or_N(year_every):
            totaldays += 366
            totaldays = totaldays + 366
        else:
            totaldays = totaldays + 365
    return totaldays
def count_days_between_two_years(Sday="20000701",Eday="20180701"):
    yStart, mStart, dStart = int(Sday[:4]), int(Sday[4:6]), int(Sday[6:8])
    yEnd, mEnd, dEnd, = int(Eday[:4]), int(Eday[4:6]), int(Eday[6:8])
    print('dayStart:', yStart, mStart, dStart)
    print('dayEnd:', yEnd, mEnd, dEnd)
    EndDays = get_before_years_total_days(yEnd) + get_mend_days(mEnd,is_R_or_N(yEnd)) + dEnd
    StartDays = get_before_years_total_days(yStart) + get_mend_days(mStart, is_R_or_N(yStart)) + dStart
    return EndDays - StartDays

days = count_days_between_two_years('20010820','20180702')
print('days:', days)
