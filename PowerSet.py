ourset = ["a","b","c", "d","e"]
setSize = len(ourset)
PowerSetSize = 2**setSize

for a in range(0, PowerSetSize):
    for b in range(0, setSize):
        if((a & (1<<b))>0):
            print(ourset[b], end="")
    print("")
