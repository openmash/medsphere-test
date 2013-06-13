days = {"monday":"Monday.png", 
        "tuesday": Pattern("Tuesday.png").similar(0.82), 
        "wednesday": "Wednesday.png", 
        "thursday":Pattern("thursday.png").similar(0.48), 
        "friday":"Friday.png", 
        "saturday":"Saturday.png", 
        "sunday":Pattern("Sunday.png").similar(0.74) }

if "${CHECKIN_APPOINTMENT_DAY}" in days:
    day = days["${CHECKIN_APPOINTMENT_DAY}"]
else:
    day = days["monday"]

d = find(day)    
#print d.getX()
st = find(Pattern("9am.png").similar(0.75))

et = find(Pattern("1pm.png").similar(0.77))

r = Region(d.getX() -20, st.getY() - 10, 200, 30)

l = r.find(Pattern("appointment_corner.png").similar(0.79))

rightClick(Location(l.getX()-50, l.getY()+15))

for i in range(4):
    type(Key.DOWN)

type(Key.ENTER)

wait("PatientName.png")

click("OK.png")

sleep(1)

find(Pattern("1.png").similar(0.74))
