doubleClick(Pattern("1370537456805-1.png").targetOffset(26,0))

type(Pattern("1370537456805-2.png").targetOffset(20,0), 's')

sleep(5) #let the search find it

type(Key.DOWN)

type(Key.ENTER)

doubleClick("1370982387429.png")

click(Pattern("1370380451375.png").similar(0.52))

click("open.png")

find(Pattern("day_week.png").similar(0.63).targetOffset(1,0))

d = find(Pattern("1371012352800.png").similar(0.91).targetOffset(-12,1))
#print d.getX()
st = find(Pattern("1371012595962.png").similar(0.74).targetOffset(-1,0))

r = Region(d.getX() -20, st.getY() - 10,200,280)

l = r.find("1371014028315.png")

rightClick(Location(l.getX()-50, l.getY()+15))

for i in range(4):
    type(Key.DOWN)

type(Key.ENTER)



             

