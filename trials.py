performance = {"March":100, "April":200, "May":300, "June":400, "July":500}
date="2016-12-1"
date_original = "March"

speech=''
if date_original in performance:
    speech = "The performance for the " + str(date_original) + " is " + str(performance[str(date_original)])
else:
    speech = "The performance for " + str(date) + " is "+str(performance['April'])

print speech