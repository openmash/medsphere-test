
d = find(Pattern("Thursday-1.png").similar(0.91))
#print d.getX()
st = find(Pattern("9am.png").similar(0.75))

et = find(Pattern("1pm.png").similar(0.77))

r = Region(d.getX() -20, st.getY() - 10, 200, 280)

r.find(Pattern("appointment_corner.png").similar(0.79))


