d = find(Pattern("Thursday-1.png").similar(0.91))
#print d.getX()
st = find(Pattern("9am.png").similar(0.75))

et = find(Pattern("1pm.png").similar(0.77))

r = Region(d.getX() -20, st.getY() - 10, 200, 280)

l = r.find(Pattern("appointment_corner.png").similar(0.79))

rightClick(Location(l.getX()-50, l.getY()+15))

for i in range(3):
    type(Key.DOWN)

type(Key.ENTER)

click("ok.png")

r.find(Pattern("cancelled_corner.png").similar(0.80))