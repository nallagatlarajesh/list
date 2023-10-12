#requerements
#computeavereage
#list1
#n
#total=0
def computeaverage(list1,n):
    total=0
    for marks in list1:
        #add marks to total
        total=total+marks
    average=total/n
    return average
#create an empty list
list1=[]
print("how many students marks you want to enter:")
n=int(input())
for i in range(0,n):
    print("enetr marks of student ",(i+1),":",end=" ")
    marks=int(input())
    #append marks in the list
    list1.append(marks)
    print(marks)
average=computeaverage(list1,n)
print("average marks of ",n,"students is :",average)
