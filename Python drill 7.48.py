#The Tech Academy Python drill 7.48 - sorting
#by Matt Steele!

# Sort [67, 45, 2, 13, 1, 998] in ascending order,
#not using .sort or .sorted

def mattSort(mattList):
   for mattIndex in range(1,len(mattList)):

     currentvalue = mattList[mattIndex]
     position = mattIndex

     while position>0 and mattList[position-1]>currentvalue:
         mattList[position]=mattList[position-1]
         position = position-1

     mattList[position]=currentvalue

mattList = [67, 45, 2, 13, 1, 998]
mattSort(mattList)
print(mattList)



# Sort [89, 23, 33, 45, 10, 12, 45, 45, 45] in ascending order,
# not using .sort or .sorted
def mattSortsAgain(mattList2):
   for pendingSlot in range(len(mattList2)-1,0,-1):
       pendingMax=0
       for location in range(1,pendingSlot+1):
           if mattList2[location]>mattList2[pendingMax]:
               pendingMax = location

       temp = mattList2[pendingSlot]
       mattList2[pendingSlot] = mattList2[pendingMax]
       mattList2[pendingMax] = temp

mattList2 = [89, 23, 33, 45, 10, 12, 45, 45, 45]
mattSortsAgain(mattList2)
print(mattList2)
