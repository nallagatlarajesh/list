#reqirements
#function def
#increment function 
#parameter list2
#list1

def increment(list2):
    for i in range(0,len(list2)):
        list2[i]+=5 #5 is added to indivaidual elements in the list
    print("reference of the list inside  function  id",id(list2))
    #function ends here
#list1
list1=[10,20,30,40,50]
print("reference of list in main",id(list1))
print("the list before the function caLL")
print(list1)
increment(list1)
print("the list  after the function call")
print(list1)
