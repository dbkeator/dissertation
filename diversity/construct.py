

d2 = set()
d3 = set()
d4 = set()
d5 = set()
d6 = set()
d7 = set()
d8 = set()


ss = set()
for line in open('d2.ss').readlines():
  d2.add(line.strip())
  ss.add(line.strip())
  
for line in open('d3.ss').readlines():
  d3.add(line.strip())
  ss.add(line.strip())
  
for line in open('d4.ss').readlines():
  d4.add(line.strip())
  ss.add(line.strip())
  
for line in open('d5.ss').readlines():
  d5.add(line.strip())
  ss.add(line.strip())
  
for line in open('d6.ss').readlines():
  d6.add(line.strip())
  ss.add(line.strip())
  
for line in open('d7.ss').readlines():
  d7.add(line.strip())
  ss.add(line.strip())
  
for line in open('d8.ss').readlines():
  d8.add(line.strip())
  ss.add(line.strip())
  
print len(d2), len(d3), len(d4), len(d5), len(d6), len(d7), len(d8)
print len(ss)

lss = list(ss)

vennFile = open('list', 'w')


def newZ():
  az = []
  for i in xrange(700): az.append("0")
  return az

az = newZ()
vennFile.write("D2 <- c(")
for p in d2: 
  az[lss.index(p)] = "1"
vennFile.write (", ".join(az))
vennFile.write (")\n")
  
vennFile.write("\nD3 <- c(")
az = newZ()
for p in d3: az[lss.index(p)] = "1"
vennFile.write (", ".join(az))
vennFile.write (")\n")

vennFile.write("\nD4 <- c(")
az = newZ()
for p in d4: az[lss.index(p)] = "1"
vennFile.write (", ".join(az))
vennFile.write (")\n")

vennFile.write("\nD5 <- c(")
az = newZ()
for p in d5: az[lss.index(p)] = "1"
vennFile.write (", ".join(az))
vennFile.write (")\n")

vennFile.write("\nD6 <- c(")
az = newZ()
for p in d6: az[lss.index(p)] = "1"
vennFile.write (", ".join(az))
vennFile.write (")\n")

vennFile.write("\nD7 <- c(")
az = newZ()
for p in d7: az[lss.index(p)] = "1"
vennFile.write (", ".join(az))
vennFile.write (")\n")

vennFile.write("\nD8 <- c(")
az = newZ()
for p in d8: az[lss.index(p)] = "1"
vennFile.write (", ".join(az))
vennFile.write (")\n")


vennFile.write("\n")

vennFile.close()

