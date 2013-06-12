
days = {"monday":"Monday.png", 
        "tuesday": Pattern("Tuesday.png").similar(0.83), 
        "wednesday":"Wednesday.png", 
        "thursday":Pattern("thursday.png").similar(0.48), 
        "friday":"Friday.png", 
        "saturday":"Saturday.png", 
        "sunday":Pattern("Sunday.png").similar(0.74) }

day = days["wednesday"]

d = find(day)

#print d.getX()
st = find(Pattern("10AM.png").similar(0.83))

l = Location(d.getX() + 5, st.getY() + 5)
rightClick(l)
sleep(1)
type(Key.DOWN)
type(Key.DOWN)
type(Key.ENTER)

if exists("question.png"):
    print 'promted for overbook'
    click("OK.png")

sleep(1)

click("OK-1.png")

if exists("1371072628925.png"):
    type(Key.ENTER) 
    click("Cancel.png")
    raise Exception('Cannot create walk-in appointment')

