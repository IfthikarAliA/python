#User input no. of Element
a=int(input("Enter the number of Element: "))

#Empty List
l=[]

#Function to get list of input
for i in range(a):
    l.append(int(input(f"Enter the {i+1} item: ")))

#Iterator over a list
for i in l:
    if(i%2==0):
        print(i)