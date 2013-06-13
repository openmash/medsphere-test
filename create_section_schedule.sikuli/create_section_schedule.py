click(Pattern("1370484723896.png").similar(0.64))

click("1370908084289.png")

wait("1370484802822.png", 10)

type('${CLINIC_SEARCH}')

click(Pattern("1370384788086.png").similar(0.60))

wait("1370485257041.png")


days = ["Monday.png", Pattern("Tuesday.png").similar(0.82), "Wednesday.png", Pattern("thursday.png").similar(0.48), "Friday.png", "Saturday.png", Pattern("Sunday.png").similar(0.74) ]

for day in days:
    
    d = find(day)
    t = find(Pattern("9am.png").similar(0.75))
    
    click(Location(d.getX(), t.getY()))
    
    t = find(Pattern("1pm.png").similar(0.77))
    l = Location(d.getX(), t.getY())
    
    click(l, KEY_SHIFT)
    
    rightClick(l)
    
    click(Pattern("add_new_access_block.png").similar(0.50))
    
    wait("1370485571939.png", 5)
    
    for x in range(4):
        click(Pattern("1370389005138.png").targetOffset(1,-7))
    
    click(Pattern("1370389069947.png").similar(0.49))

fa = findAll("slots260minutes.png")
fal = list(fa)
#if len(fal) < 7:
#    raise Exception('Failed to find 7 sections')





             

