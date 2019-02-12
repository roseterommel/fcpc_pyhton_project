
mlist = {}

f = open('file.txt','w')
f.write("hi")
f.write("im rommel")
f.write("thanks")
f.write("bye")
f.close()

f = open ('file.txt','r')
print(f.read())


