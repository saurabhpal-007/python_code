name=['anil', 'amol', 'aditya', 'avi', 'alka']
print(name)
name.insert(2,'anuj')
print(name)

name.append('zulu')
print(name)

name.remove('avi')
print(name)

# replacing

i=name.index('anil')
name[i]='anilkumar'
print(name)

# sort

name.sort()
print(name)

name.reverse()
print(name)