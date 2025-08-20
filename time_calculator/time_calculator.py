** I knew later I can use str.zfill(2) to add a 0 on the left for minutes if they are under 10 **
** I learned also I could use hours, minutes = divmod(total_minutes, 60) to simplify code rather than using // and % in separate lines **


def add_time(start, duration, starting_day='None'):
    start_hour = int(start.split(':')[0])
    print(start_hour)
    start_minute = int(start.split(':')[1].split(' ')[0])
    print(start_minute)
    start_ampm = start.split(':')[1].split(' ')[1]
    print(start_ampm)
    duration_hour = int(duration.split(':')[0])
    duration_minute = int(duration.split(':')[1])
    new_time_minute = (start_minute + duration_minute)%60
    new_time_minute_str = str(new_time_minute)
    if new_time_minute < 10:
        new_time_minute_str = '0'+str(new_time_minute)
    new_time_hour = (start_hour + duration_hour + (start_minute + duration_minute)//60)%12
    new_time_hour_str = str(new_time_hour)
    if new_time_hour == 0:
        new_time_hour_str = '12'
    added_ampm = (start_hour + duration_hour + (start_minute + duration_minute)//60)//12
    print(f'added_ampm: {added_ampm}')
    new_ampm = start_ampm
    days_past = 0
    if added_ampm%2!=0:
        if start_ampm == 'AM':
            new_ampm = 'PM'
            days_past = added_ampm//2
        else:
            new_ampm = 'AM'
            days_past = added_ampm//2+1
    else:
        days_past = added_ampm//2
    print(days_past)
    week = {0:'Monday',1:'Tuesday',2:'Wednesday',3:'Thursday',4:'Friday',5:'Saturday',6:'Sunday'}
    new_day=''
    if starting_day!='None':
        for key,value in week.items():
            if value.upper() == starting_day.upper():
                new_day = week[(key+days_past)%7]
                print(new_day)    
    new_time=''
    if days_past == 0:
        if starting_day == 'None':
            new_time = new_time_hour_str+':'+new_time_minute_str+' '+new_ampm
        else:
            new_time = new_time_hour_str+':'+new_time_minute_str+' '+new_ampm+', '+new_day
    elif days_past == 1:
        if starting_day == 'None':
            new_time = new_time_hour_str+':'+new_time_minute_str+' '+new_ampm+' (next day)'
        else:
            new_time = new_time_hour_str+':'+new_time_minute_str+' '+new_ampm+', '+new_day+' (next day)'    
    else:
        if starting_day == 'None':
            new_time = new_time_hour_str+':'+new_time_minute_str+' '+new_ampm+f' ({days_past} days later)'
        else:
            new_time = new_time_hour_str+':'+new_time_minute_str+' '+new_ampm+', '+new_day+f' ({days_past} days later)'

    return new_time

print(add_time('8:16 PM', '466:02', 'tuesday'))
