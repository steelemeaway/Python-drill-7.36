#The Tech Academy Python Drill 7.46
#by Matt Steele!

#1.Python range() function with one parameter displaying 0-3
print ("Question 1")
for matts_counter in range (4):
    print (matts_counter)

#2.Python range() function with three parameters displaying 3 2 1 0
print ("Question 2")
matts_list = [0,1,2,3,4,5,6,7,8,9,10]
matts_list_len = len(matts_list)
for i in range(3,-1,-1):
    print(matts_list[i])

#3 Python range() function with three parameters displaying 8 6 4 2
print ("Question 3")
matts_list = [0,1,2,3,4,5,6,7,8,9,10]
matts_list_len = len(matts_list)
for i in range(8,0,-2):
    print(matts_list[i])


