def readable_timedelta(num):
    week=int(num/7)
    days=int(num % 7 )
    print("{} week(s) and {} day(s)".format(week,days) )

readable_timedelta(10)
