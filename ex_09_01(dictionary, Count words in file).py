fname = input("Enter File: ")
if len(fname) < 1 : fname = "clown.txt"

with open (fname, "r", encoding='UTF8') as fh :
    di = {}
    for line in fh :
        line = line.rstrip()
        wds = line.split()
        for w in wds :
            # idiom : retrieve/create/update counter
            di[w] = di.get(w,0) + 1

    # print(di)

# now we wnat to find the most common word
    largest = -1
    theword = None
    for k,v in di.items() :
        if v > largest :
            largest = v
            theword = k # cature / remember the word that was largest
    print(theword, largest)
