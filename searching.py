#requirements
#linearsearch function 
#parameters num,list1
#for loop
#num = searching element

def linearsearch(num,list1):
    for i in range(0,len(list1)):
        if list1[i]==num:         #num is prasent 
            return i             #return the position
    return None                  #num is not prasent in the position 
#ens of the function
list1=[]
print("how many numbers do you want to enetr in the list:")
maximum=int(input())
print("enter a list of elements :")
for i in range(0,maximum):
    n=int(input())
    list1.append(n)
num=int(input("enter the number to be searched:"))
#functioin calling
result=linearsearch(num,list1)
if result is None:
    print("number",num,"is not prasent inthere list")
else:
    print("number",num,"is prasent at position ",result+1)
