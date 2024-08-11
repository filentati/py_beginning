'''Написать функцию shift_time, которая принимает 2 параметра: количество дней и количество секунд и сдвигает дату и время 01.01.2023 12:30:00
на указанное количество дней и секунд. В качестве выходного значения нужно вывести кортеж: день и секунда от сдвинутого времени.'''
import datetime

days, seconds = int(input()), int(input())

def shift_time(days: int, seconds: int):
    initial_time = datetime.datetime(2023, 1, 1, 12, 30, 0)
    shifted_time = initial_time + datetime.timedelta(days=days, seconds=seconds)
    day = shifted_time.day
    second = shifted_time.second
    return (day, second)


print(shift_time(days, seconds))

