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

x = sorted(di.items())
print(x[:5])

tmp = list()
for k,v in di.items():
    newt = (v,k)
    tmp.append(newt)
# print("Flipped", tmp)

tmp = sorted(tmp, reverse=True)
# print("Sorted", tmp[:5])

for v,k in tmp[:5] :
    print(k,v)

print(sorted([(v,k) for k,v in di.items()], reverse=True))
