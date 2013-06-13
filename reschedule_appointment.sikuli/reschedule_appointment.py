
days = {"monday":"Monday.png", 
        "tuesday": Pattern("Tuesday.png").similar(0.82), 
        "wednesday": "Wednesday.png", 
        "thursday":Pattern("thursday.png").similar(0.57), 
        "friday":"Friday.png", 
        "saturday":"Saturday.png", 
        "sunday":Pattern("Sunday.png").similar(0.74) }

#build script will change this
if "${RESCHED_APPOINTMENT_DAY}" in days:
    day = days["${RESCHED_APPOINTMENT_DAY}"]
else:
    day = days["monday"]
    
if "${RESCHED_NEW_APPOINTMENT_DAY}" in days:
    rday = days["${RESCHED_NEW_APPOINTMENT_DAY}"]
else:
    rday = days["tuesday"]

d = find(day)
#print d.getX()
st = find(Pattern("9am.png").similar(0.75))

et = find(Pattern("1pm.png").similar(0.77))

r = Region(d.getX() -20, st.getY() - 10, 200, 30)

l = r.find(Pattern("appointment_corner.png").similar(0.79))

rightClick(Location(l.getX()-50, l.getY()+15))

for i in range(3):
    type(Key.DOWN)

type(Key.ENTER)

wait("AutoRebook.png", 10)

click(Pattern("AutoRebookChk.png").targetOffset(-35,1))

for i in range(6):
    click(Pattern("Start.png").targetOffset(-24,2))

click("ok.png")

sleep(5)

wait("Anewannninfm.png", 10)

click("OK-1.png")

d = find(rday)

st = find(Pattern("9am.png").similar(0.75))

et = find(Pattern("1pm.png").similar(0.77))

r = Region(d.getX() -20, st.getY() - 10, 200, 30)

l = r.find(Pattern("appointment_corner.png").similar(0.78))
