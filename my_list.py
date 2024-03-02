#create empty list
my_list=[]
#using append method
my_list.append(10)
my_list.append(20) 
my_list.append(30)
my_list.append(40)
print("After append:",my_list)
#inserting 15 at index 2
my_list.insert(2, 15)
print("After insertion:",my_list)
#joining another list using extend method
my_list.extend([50,60,70])
print("After extending:",my_list)
#remove last item
my_list.pop()
print("After removing last item:",my_list)
#sorting in ascending order
my_list.sort()
print("After sorting:",my_list)
#print the index  of value 30
print("Index of value 30:",my_list.index(30))
