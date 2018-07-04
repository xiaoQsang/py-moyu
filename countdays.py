# coding=utf-8
def is_R_or_N(user_in_date=2017):  # 判断是否闰年
    value_r_n = (user_in_date % 4 == 0 and user_in_date % 100 != 0) \
                or user_in_date % 400 == 0
    return value_r_n


def getBeforeMonthsTotalDays(mEnd=12, is_R_N=True):
    totaldays = 0
    if is_R_N:
        if mEnd == 12:
            totaldays = 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30 + 31 + 29 + 31
        elif mEnd == 11:
            totaldays = 31 + 30 + 31 + 31 + 30 + 31 + 30 + 31 + 29 + 31
        elif mEnd == 10:
            totaldays = 30 + 31 + 31 + 30 + 31 + 30 + 31 + 29 + 31
        elif mEnd == 9:
            totaldays = 31 + 31 + 30 + 31 + 30 + 31 + 29 + 31
        elif mEnd == 8:
            totaldays = 31 + 30 + 31 + 30 + 31 + 29 + 31
        elif mEnd == 7:
            totaldays = 30 + 31 + 30 + 31 + 29 + 31
        elif mEnd == 6:
            totaldays = 31 + 30 + 31 + 29 + 31
        elif mEnd == 5:
            totaldays = 30 + 31 + 29 + 31
        elif mEnd == 4:
            totaldays = 31 + 29 + 31
        elif mEnd == 3:
            totaldays = 29 + 31
        elif mEnd == 2:
            totaldays = 31
        elif mEnd == 1:
            totaldays = 0
    else:
        if mEnd == 12:
            totaldays = 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30 + 31 + 28 + 31
        elif mEnd == 11:
            totaldays = 31 + 30 + 31 + 31 + 30 + 31 + 30 + 31 + 28 + 31
        elif mEnd == 10:
            totaldays = 30 + 31 + 31 + 30 + 31 + 30 + 31 + 28 + 31
        elif mEnd == 9:
            totaldays = 31 + 31 + 30 + 31 + 30 + 31 + 28 + 31
        elif mEnd == 8:
            totaldays = 31 + 30 + 31 + 30 + 31 + 28 + 31
        elif mEnd == 7:
            totaldays = 30 + 31 + 30 + 31 + 28 + 31
        elif mEnd == 6:
            totaldays = 31 + 30 + 31 + 28 + 31
        elif mEnd == 5:
            totaldays = 30 + 31 + 28 + 31
        elif mEnd == 4:
            totaldays = 31 + 28 + 31
        elif mEnd == 3:
            totaldays = 28 + 31
        elif mEnd == 2:
            totaldays = 31
        elif mEnd == 1:
            totaldays = 0
    return totaldays


def getTotalDaysOneWholeYear(year=2017):
    if is_R_or_N(year):
        total = 366
    else:
        total = 365
    return total


def getBeforeYearsTotalDays(yEnd=2017):
    totalDays = 0
    years = range(1, yEnd)
    for year_every in years:
        if is_R_or_N(year_every):
            totalDays += 366
        else:
            totalDays += 365
    return totalDays


def countDaysDiffer(dayStart='20150101', dayEnd='20170102'):
    yStart, mStart, dStart = int(dayStart[:4]), int(dayStart[4:6]), int(dayStart[6:8])
    yEnd, mEnd, dEnd = int(dayEnd[:4]), int(dayEnd[4:6]), int(dayEnd[6:8])
    print('dayStart:', yStart, mStart, dStart)
    print('dayEnd:', yEnd, mEnd, dEnd)
    EndDays = getBeforeYearsTotalDays(yEnd) + getBeforeMonthsTotalDays(mEnd, is_R_or_N(yEnd)) + dEnd
    StartDays = getBeforeYearsTotalDays(yStart) + getBeforeMonthsTotalDays(mStart, is_R_or_N(yStart)) + dStart
    return EndDays - StartDays

if __name__ == '__main__':

    days = countDaysDiffer('20040731', '20180701')
    print('days：', days)