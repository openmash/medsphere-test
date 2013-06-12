doubleClick(Pattern("1370537456805-1.png").targetOffset(26,0))

type(Pattern("1370537456805-2.png").targetOffset(20,0), 's')

sleep(5) #let the search find it

type(Key.DOWN)

type(Key.ENTER)

doubleClick("1370982387429.png")

click(Pattern("1370380451375.png").similar(0.52))

click("open.png")

#find(Pattern("day_week.png").similar(0.63).targetOffset(46,0))

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
st = find(Pattern("1371012595962.png").similar(0.88))

l = Location(d.getX(), st.getY() + 5)
rightClick(l)

type(Key.DOWN)
type(Key.DOWN)
type(Key.ENTER)

click("1371045409184.png")
click("1371045481968.png")
type(Key.ENTER)




             

