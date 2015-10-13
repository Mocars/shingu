i = 1
while i < 10:
 print i
 i += 1

for i in range(0,5):
    print i

i = 0
while i < 5:
    print i
    i = i + 1

for i in range(10):
    if i==5: break
    print i
print "EOP"

for i in range(10):
    if i==5: continue
    print i
print "EOP"

for i in range(10):
    print i,
else:
    print "EOP"

i = 0
while i < 10:
    print i,
    i +=1
else:
    print "EOP"
