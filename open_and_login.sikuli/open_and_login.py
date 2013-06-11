App.open('C:\ClinicalSchedulerCA\ClinSchd.exe')


wait("1370484104956.png", 30)

type(Pattern("1370484141761.png").targetOffset(-20,8),'boating1')

type(Pattern("1370484160610.png").targetOffset(-17,10), 'boating1.')

click("1370379805985.png")

waitVanish("1370484104956.png")

wait("1369935523661.png", 30)

if exists("1370969915297.png"):
    print 'Login failed'
    exit(1)


click("1370484388287.png")




