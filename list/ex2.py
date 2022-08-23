#this is a program to append two lists
listone = ['shimoni','gandi','che']
listtwo = ['ane','setu','dahyo','che']
listone.extend(listtwo)
print(listone)
listone.append('bawli')
print(listone)
listone.insert(2,'chotu')
print(listone)
listone.remove('chotu')
print(listone)
listone.pop(2)
print(listone)
print(listone + listtwo)
listone.sort()
print(listone)
listone.reverse() #string reverses
print(listone)
listone.sort(reverse = True)
