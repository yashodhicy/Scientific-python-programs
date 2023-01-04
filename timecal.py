def add_time(start, duration,day=False):
    
    new_time=''
    t1= start.split()
    t2= t1[0].split(':')
    t3= duration.split(':')
    if t1[1]=='PM':
        t2[0]=str(int(t2[0])+12)
    hours= int(t2[0])+int(t3[0])+int((int(t2[1])+int(t3[1]))/60)
    minutes = ((int(t2[1])+int(t3[1]))%60)
    n=0
    if hours>=24:
        n=int(hours/24)
        hours=hours-n*24
    if hours<12:
        val="AM"
    elif hours==12:
        val="PM"
    else:
        val='PM'
        hours=hours-12
    days = {0: 'Monday' , 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday',5: 'Saturday',6: 'Sunday'}
    if hours==0:
        hours=12
    
    

    if day:
        for d in days:
            if day.lower()==days[d].lower():
                day=days[d]
                index=(d+n)%7
                break;
        if n==0:
            new_time=f"{hours}:{minutes:02} {val}, {day}"
        elif n==1:
            new_time=f"{hours}:{minutes:02} {val}, {days[index]} (next day)"
        else:
            new_time=f"{hours}:{minutes:02} {val}, {days[index]} ({n} days later)"
    else:
        if n==0:
            new_time=f"{hours}:{minutes:02} {val}"
        if n==1:
            new_time=f"{hours}:{minutes:02} {val} (next day)"
        if n>1 :
           new_time=f"{hours}:{minutes:02} {val} ({n} days later)"
            

    
    return new_time