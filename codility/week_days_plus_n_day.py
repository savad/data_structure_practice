

def solution(S, K):
    week_days = {"Mon": 1, "Tue": 2, "Wed": 3, "Thu": 4, "Fri": 5, "Sat": 6, "Sun": 7}
    week_days_rev = {y: x for x, y in week_days.items()}
    K = K%7
    value = week_days[S] + K
    if value > 7:
        value = value % 7
    return week_days_rev[value]


print(solution("Wed", -5))
