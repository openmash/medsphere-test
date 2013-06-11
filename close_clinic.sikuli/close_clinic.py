click(Pattern("1370983812503.png").similar(0.82).targetOffset(7,11))

sleep(2)

if exists("day_week.png"):
    raise Exception('Failed to close clinic schedule')