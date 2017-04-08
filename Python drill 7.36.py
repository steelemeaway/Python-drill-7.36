#1 Assign an integer
x = 11111
#2 Assign a string
y = "I am a string being assigned to a variable"
#3 Assign a float
z = 3.14
#4 Print assigned variables with .format() notation
print "Here we have an assigned integer {}, \nan assigned string '{}', \nand a assigned float {}.".format(x,y,z)
#5 Use operators + - * / += = %
a = 1
b = 2
c = 5
print(a+b-a*b/a) 
a +=1
print a
print (c%b)

#6 using and, or, & not
#7 using if, elif, else
if a == 1 and b == 2 or c == 5:
    print "YAY"
elif not a==1 and b==2 or c == 5:
    print "NEIGH"
else:
    print "MAYBE HAY?"
j = 12
if not j == 12:
    print "WOOOOO!"
else:
    print "NOOOOO!"

#8 while loop
Methuselah_age = 0 
while Methuselah_age <= 969:
    print "Stiiiiiilllllll alive...."
    Methuselah_age += 96.9

#9 for loop
for Methuselah_age in range(965,971):
    if Methuselah_age <=969:
        print "Still kickin'"
    elif Methuselah_age >=970:
        print "Not kickin'"

#10 creating a list & iterating through it
bucket_list = ["tame dragon", "travel world", "make millions", "not die alone"]
for activity in bucket_list:
    print activity

#11 creating tuple & iterate through it
bucket_list2 = ("tame another dragon", "travel world twice", "make double millions", "not die alone")
for activity2 in bucket_list2:
    print activity2

#12 define function & return string variable
name = ""
def say_hey(name):
    stop = True
    while stop:
        if name =="":
            name = raw_input("\nWhat is your name? ".capitalize())
            if name !="":
                print ("\nhey hey heeeeeeey, {}!!!".format(name))
                stop = False
    return name

#13 call & print function defined above

print say_hey(name)





