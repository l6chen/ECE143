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


def plot_TimeInterval_StopNumber(data):
    columns = ['0-1', '1-2', '2-3', '3-4', '4-5', '5-6', '6-7', '7-8', '8-9', '9-10', '10-11', '11-12', '12-13',
               '13-14', '14-15', '15-16', '16-17', '17-18', '18-19', '19-20', '20-21', '21-22', '22-23', '23-00']
    rows = ["Citation", "Verbal Warning", "Written Warning", "Searched", "Field Interview", "Arrested", "Other"]

    values = np.arange(0, 10000, 1000)
    value_incr = 1
    colors = plt.cm.tab20b(np.linspace(0, 1, len(rows)))
    index = np.arange(len(columns))
    bar_width = 0.8
    y_offset = np.zeros(len(columns))

    for row in range(len(data)):
        plt.bar(index, data[row], bar_width, bottom=y_offset, color=colors[row], label=rows[row])
        y_offset = y_offset + data[row]

    plt.ylabel("number of stops", fontsize=16)
    plt.xlabel("time interval", fontsize=16)
    plt.yticks(values * value_incr, ['%d' % val for val in values])
    plt.xticks(index, columns, fontsize=10)
    plt.title('Stopped number VS time', fontsize=16)
    plt.legend(prop={'size': 16})
    fig = plt.gcf()
    fig.set_size_inches(16, 9)


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

def plot_TimeInterval_ResultRatio(data_ratio):
    columns = ['0-1', '1-2', '2-3', '3-4', '4-5', '5-6', '6-7', '7-8', '8-9', '9-10', '10-11', '11-12', '12-13',
               '13-14', '14-15', '15-16', '16-17', '17-18', '18-19', '19-20', '20-21', '21-22', '22-23', '23-00']
    rows = ["Citation", "Verbal Warning", "Written Warning", "Searched", "Field Interview", "Arrested", "Other"]
    colors = plt.cm.tab20b(np.linspace(0, 1, len(rows)))
    index = np.arange(len(columns))
    for row in range(len(data_ratio)):
        plt.plot(index, data_ratio[row], lw=3, color=colors[row], label=rows[row])

    plt.ylabel("result ratio", fontsize=16)
    plt.xlabel("time interval", fontsize=16)
    plt.xticks(index, columns, fontsize=10)
    plt.title('result ratio VS time', fontsize=16)
    plt.legend(prop={'size': 16})
    fig = plt.gcf()
    fig.set_size_inches(16, 9)


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


def plot_month_StopNumber(data):
    columns = ["Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug", "Sep", "Oct", "Nov", "Dec"]
    index = np.arange(len(columns))
    plt.plot(index, data, lw=4, color=plt.cm.tab20b(2), label=columns)
    plt.ylabel("number of stops", fontsize=16)
    plt.ylim((7000, 11000))
    plt.xlabel("month", fontsize=16)
    plt.xticks(index, columns, fontsize=10)
    plt.title('Stopped number VS Month', fontsize=16)
    fig = plt.gcf()
    fig.set_size_inches(16, 6)

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


def plot_week_StopNumber(data):
    columns = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    index = np.arange(len(columns))
    plt.plot(index, data, lw=4, color=plt.cm.tab20b(2), label=columns)
    plt.ylabel("number of stops", fontsize=16)
    plt.xlabel("week", fontsize=16)
    plt.xticks(index, columns, fontsize=10)
    plt.title('Stopped number VS week', fontsize=16)
    fig = plt.gcf()
    fig.set_size_inches(16, 9)