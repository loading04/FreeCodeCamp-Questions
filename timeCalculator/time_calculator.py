import math


def return_min(start):
    minutes = start.split(":")
    min = minutes[1][0:2]

    return int(min)


def return_hours(start):
    hours = start.split(":")

    return int(hours[0])


def return_period(start):
    return start[-2:]


def return_duration_hours(duration):
    dur = duration.split(":")

    return int(dur[0])


def return_duration_minutes(duration):
    dur = duration.split(":")

    return int(dur[1])


def add_time(start, duration, *args):
    days_list = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    # start time
    time_hour = return_hours(start)
    time_min = return_min(start)
    time_period = return_period(start)

    # duration time
    duration_hour = return_duration_hours(duration)
    duration_min = return_duration_minutes(duration)

    hours_calculated = 0
    min_calculated = 0
    counter = 0
    period = None
    days = 0

    # minutes calculation
    if duration_min + time_min >= 60:
        duration_hour += 1
        origne_duration = duration_hour
        min_calculated = (duration_min + time_min) - 60
    else:
        min_calculated = (duration_min + time_min)
        origne_duration = duration_hour
    # end minutes calculation

    # day calculation

    if time_period == 'PM' and time_hour + duration_hour >= 12:
        time_left = 11 - time_hour
        hours_left = duration_hour - time_left
        days = math.ceil(hours_left / 24)
        # print("days", days)

    if time_period == 'AM' and time_hour + duration_hour >= 23:
        days = math.ceil(duration_hour / 24)
        # print("days", days)

    # end day calculation

    # get the name of the day
    if len(args) != 0:
        days_counter = days
        the_day = str(args[0]).lower()

        index = days_list.index(the_day)
        if days_counter == 0:
            get_the_day = f", {the_day}"
        while days_counter != 0:
            index += 1
            if index >= len(days_list):
                index = 0
            get_the_day = f", {days_list[index]}"
            days_counter -= 1


    ##

    # hours_calcualtion
    # case 1
    somme = duration_hour + time_hour
    if duration_hour < 12 and somme <= 12:
        hours_calculated = somme

    # case 2
    elif duration_hour < 12 < somme:
        time_left = 12 - time_hour
        hours_calculated = duration_hour - time_left

    # case3

    elif duration_hour > 12:
        while duration_hour >= 12:
            counter += 1
            duration_hour -= 12
        if duration_hour + time_hour <= 12:
            hours_calculated = duration_hour + time_hour
        elif duration_hour + time_hour > 12:
            time_left = 12 - time_hour
            hours_calculated = duration_hour - time_left
        # period calculation
    if time_hour != 12:
        if counter % 2 == 0 and (duration_hour + time_hour) >= 12 and time_period == 'AM':
            period = 'PM'
        elif counter % 2 == 0 and (duration_hour + time_hour) >= 12 and time_period == 'PM':
            period = 'AM'
        elif counter % 2 != 0 and (duration_hour + time_hour) < 12 and time_period == 'AM':
            period = 'PM'
        elif counter % 2 != 0 and (duration_hour + time_hour) < 12 and time_period == 'PM':
            period = 'AM'
        else:
            period = time_period
        # end period calculation
        # print("counter", counter)
    else:
        if counter % 2 == 0 and time_period == 'PM':
            period = time_period
        elif counter % 2 == 0 and time_period == 'AM':
            period = time_period
        elif counter % 2 != 0 and time_period == 'AM':
            period = 'PM'
        elif counter % 2 != 0 and time_period == 'PM':
            period = 'AM'
    # end hours calculation

    if len(str(min_calculated)) == 1:
        min_calculated = f'0{min_calculated}'
    if days == 0 and len(args) != 0:
        return f'{hours_calculated}:{min_calculated} {period}{get_the_day.title()}'
    elif days == 0 and len(args) == 0:
        return f'{hours_calculated}:{min_calculated} {period}'
    elif days == 1 and len(args) != 0:
        message = "(next day)"
        return f'{hours_calculated}:{min_calculated} {period}{get_the_day.title()} {message}'
    elif days == 1 and len(args) == 0:
        message = "(next day)"
        return f'{hours_calculated}:{min_calculated} {period} {message}'
    elif days > 1 and len(args) != 0:
        message = f"({days} days later)"
        return f'{hours_calculated}:{min_calculated} {period}{get_the_day.title()} {message}'
    elif days > 1 and len(args) == 0:
        message = f"({days} days later)"
        return f'{hours_calculated}:{min_calculated} {period} {message}'

x = add_time("11:30 AM", "20:32")
print(x)
