'''Написать функцию parse_time, которая принимает строку в качестве параметра, которая является временем формата “ГГГГ ММ ДД ЧЧ ММ СС”
и парсит эту строку в объект datetime.datetime и сдвигает ее на один день вперед. И выводит этот день''' 

import datetime

string_datetime = input()

def parse_time(s):
    dt = datetime.datetime.strptime(s, "%Y %m %d %H %M %S")
    dt_shifted = dt + datetime.timedelta(days=1)
    
    return dt_shifted.day

print(parse_time(string_datetime))
