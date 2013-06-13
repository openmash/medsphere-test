App.open('${CLIN_SCHED_EXE}')


wait("1370484104956.png", 30)

type(Pattern("1370484141761.png").targetOffset(-20,8),'${ACCESS_CODE}')

type(Pattern("1370484160610.png").targetOffset(-17,10), '${VERIFY_CODE}')

click("1370379805985.png")

waitVanish("1370484104956.png")

wait("1369935523661.png", 30)

if exists("1370969915297.png"):
    raise Exception( 'Login failed')
    


click("1370484388287.png")




