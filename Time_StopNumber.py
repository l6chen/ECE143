import csv
import numpy as np
import matplotlib.pyplot as plt
import calendar

def TimeInterval_StopNumber():
    '''
    get the data of TimeInterval of a day and StopNumber from TimeInterval_results_3.csv'
    :return: a list called "data", which contains lists representing the outcome of the stop. Those list consist of StopNumber in a certain TimeInterval of a day
    '''
    filename = './datasets/TimeInterval_results_3.csv'
    time_interval_stop = {"00": 0, "01": 0, "02": 0, "03": 0, "04": 0, "05": 0, "06": 0, "07": 0, "08": 0, "09": 0,
                          "10": 0, "11": 0, "12": 0, "13": 0, "14": 0, "15": 0, "16": 0, "17": 0, "18": 0, "19": 0,
                          "20": 0, "21": 0, "22": 0, "23": 0}
    data = []
    with open(filename) as f:
        reader = list(csv.reader(f))
        line_counter = 0
        path = [0] * 24
        for row in reader:
            if line_counter == 0:
                line_counter += 1
            else:
                if row[2] == 'Citation' and (row[1] in time_interval_stop):
                    path[int(row[1])] += 1
        data.append(path)
    f.close()

    with open(filename) as f:
        reader = list(csv.reader(f))
        line_counter = 0
        path = [0] * 24
        for row in reader:
            if line_counter == 0:
                line_counter += 1
            else:
                if row[2] == 'Verbal Warning' and (row[1] in time_interval_stop):
                    path[int(row[1])] += 1
        data.append(path)
    f.close()

    with open(filename) as f:
        reader = list(csv.reader(f))
        line_counter = 0
        path = [0] * 24
        for row in reader:
            if line_counter == 0:
                line_counter += 1
            else:
                if row[2] == 'Written Warning' and (row[1] in time_interval_stop):
                    path[int(row[1])] += 1
        data.append(path)
    f.close()

    with open(filename) as f:
        reader = list(csv.reader(f))
        line_counter = 0
        path = [0] * 24
        for row in reader:
            if line_counter == 0:
                line_counter += 1
            else:
                if row[2] == 'Searched' and (row[1] in time_interval_stop):
                    path[int(row[1])] += 1
        data.append(path)
    f.close()

    with open(filename) as f:
        reader = list(csv.reader(f))
        line_counter = 0
        path = [0] * 24
        for row in reader:
            if line_counter == 0:
                line_counter += 1
            else:
                if row[2] == 'FI' and (row[1] in time_interval_stop):
                    path[int(row[1])] += 1
        data.append(path)
    f.close()

    with open(filename) as f:
        reader = list(csv.reader(f))
        line_counter = 0
        path = [0] * 24
        for row in reader:
            if line_counter == 0:
                line_counter += 1
            else:
                if row[2] == 'Arrested' and (row[1] in time_interval_stop):
                    path[int(row[1])] += 1
        data.append(path)
    f.close()

    with open(filename) as f:
        reader = list(csv.reader(f))
        line_counter = 0
        path = [0] * 24
        for row in reader:
            if line_counter == 0:
                line_counter += 1
            else:
                if (row[2] == 'NULL' or row[2] == 'Other') and (row[1] in time_interval_stop):
                    path[int(row[1])] += 1
        data.append(path)
    f.close()
    return data

def TimeInterval_ResultRatio():
    '''
    get the outcome ratio of the total stop number in certain time interval
    :return: a list called "data_ratio", it contains lists representing outcome. Those lists are the ratio of each outcome in a certain time interval
    '''
    data = TimeInterval_StopNumber()
    data_ratio = data
    number = [0] * 24
    for i in range(24):
        number[i] = sum(data[j][i] for j in range(7))

    for i in range(len(data_ratio)):
        for j in range(len(data_ratio[0])):
            data_ratio[i][j] = data[i][j] / number[j]

    return data_ratio


def month_StopNumber():
    '''
    get the stop number VS month
    :return: a list called "data", it contains the stop number of each month
    '''
    filename = './datasets/vehicle_stops_2016_datasd_original.csv'
    month_number = {"Jan": 0, "Feb": 0, "Mar": 0, "Apr": 0, "May": 0, "June": 0, "July": 0, "Aug": 0, "Sep": 0,
                    "Oct": 0, "Nov": 0, "Dec": 0}
    with open(filename) as f:
        reader = list(csv.reader(f))
        for item in reader:
            if len(item[6]) > 0 and len(item[6].split()[0]) == 10 and len(
                    item[6].split()[0].split('-')[0]) == 4 and int(item[6].split()[0].split('-')[0]) == 2016:
                temp = get_month(int(item[6].split()[0].split('-')[1]))
                if temp in month_number:
                    month_number[temp] += 1

    data = [i for i in month_number.values()]
    return data


def get_month(month):
    '''
    return the string name of the day of the month on a given month,day, and year.
    month: int
    '''
    month_number = ["Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug", "Sep","Oct", "Nov", "Dec"]
    return month_number[month-1]

def week_StopNumber():
    '''
    get the stop number VS week
    :return: a list called "data", it contains the stop number of week
    '''
    filename = './datasets/vehicle_stops_2016_datasd_original.csv'
    week_number = {"Mon": 0, "Tue": 0, "Wed": 0, "Thu": 0, "Fri": 0, "Sat": 0, "Sun": 0}
    with open(filename) as f:
        reader = list(csv.reader(f))
        for item in reader:
            if len(item[6]) > 0 and len(item[6].split()[0]) == 10 and len(
                    item[6].split()[0].split('-')[0]) == 4 and int(item[6].split()[0].split('-')[0]) == 2016:
                temp = get_day_of_week(int(item[6].split()[0].split('-')[0]), int(item[6].split()[0].split('-')[1]), int(item[6].split()[0].split('-')[2]))
                if temp in week_number:
                    week_number[temp] += 1
    data = [i for i in week_number.values()]
    return data

def get_day_of_week(year,month,day):
    '''
    return the string name (e.g., Monday, Tuesday) of the day of the week on a given month,day, and year.
    year: int
    month: int
    day: int
    '''
    week = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri','Sat', 'Sun']
    return week[calendar.weekday(year, month, day)]