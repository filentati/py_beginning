''' Необходимо вывести  n месяцев, которые чаще всего встречаются в веденных датах'''

import datetime
from collections import Counter
from typing import List


def most_common_months(dates: List[str], n) -> List[int]:
    months = [datetime.datetime.strptime(date, "%Y-%m-%dT%H:%M:%S").month for date in dates]
    month_counts = Counter(months)
    most_common_ = month_counts.most_common(n)
    return [month for month, count in most_common_]


dates=["2023-01-01T23:59:59", "2023-01-01T23:59:59", "2023-02-01T23:59:59"]
print(most_common_months(dates, 2))
