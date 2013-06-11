doubleClick(Pattern("1370537456805.png").targetOffset(38,0))

type(Pattern("1370537456805.png").targetOffset(38,0), 's')

sleep(5) #let the search find it

type(Key.DOWN)

type(Key.ENTER)

find(Pattern("1370981821621.png").similar(0.79))