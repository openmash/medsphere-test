
days = {"monday":"Monday.png", 
        "tuesday": Pattern("Tuesday.png").similar(0.82), 
        "wednesday": "Wednesday.png", 
        "thursday":Pattern("thursday.png").similar(0.48), 
        "friday":"Friday.png", 
        "saturday":"Saturday.png", 
        "sunday":Pattern("Sunday.png").similar(0.74) }

if "${MAKE_APPOINTMENT_DAY}" in days:
    day = days["${MAKE_APPOINTMENT_DAY}"]
else:
    day = days["monday"]

d = find(day)
#print d.getX()
st = find(Pattern("9am.png").similar(0.75))

l = Location(d.getX(), st.getY() + 5)
rightClick(l)

type(Key.DOWN)
type(Key.ENTER)

find("1370983419933.png")

click("ok.png")

