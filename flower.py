#nis odd print weird
# n=1
# if n % 2!=0:
#      print("weird")
# else:
#     print("not weird")

#nis even in range 2 to 5 print not weird
# n=11
# if n%2==0 and n>=2 and n>=5:
#     print("not weird")
# else:
#     print("weird")

#n is even in range 6 to 20 print  weird
# n =11
# if n%2==0 and n>=6 and n<=20:
#     print("weird")
# else:
#     print("not weird")

# nis even and gretaer then 20 print not weird

#n=24
#if n%2==0 and n>=20:
    #print(" not weird")
#else:
    #print("weird")
# addition, substraction, multipication
# a=3
# b=5
# print(a+b , a-b, a*b)   

#division
#a=3
#b=5
#print(a/b,a//b)



#nis even in range 2 to 5 print not weird
# n=11
# if n%2==0:
#elif n>=2 and n>=5:
#     print("not weird")
# else:
#     print("weird")

# divisible by 7 or not

# n=20
# if n%5==0:
#   print("hello")
# else:
#   print("bye")

# a= int(input("enter your score"))
# b= int(input("total number of subjects"))
# c=a/b
# print(c)

# year=int(input("enter year of service"))
# salary=int(input("enter salary"))
# if year>5:
#     print("add ", 0.05 * salary)
# else:
#     print("no bonus")

# length= input()
# breadth=input()
# if length == breadth:
#     print("square")
# else:
#     print("its rectangle")


# value1 = int(input())
# value2 = int(input())
# if value1>value2:
#     print("value1greater")
# elif value1<value2:
#     print("value2greater1")
# else:
#     print("equal")


# qnty= int(input("enter the quantity"))
# if qnty>1000:
#     print("cost is" ,0.1*qnty*100)
# else:
#     print("cost is",qnty *100)






# mks = int(input())
# if mks>80:
#     print("gradeA")
# if mks>=60 and mks<80:
#     print("grade B")
# if mks>=50 and mks<60:
#     print("grade C")
# if mks>=45 and mks<50:
#     print("grade D")
# if mks>=25 and mks<45:
#     print("grade E")
# else:
#     print("grade F")


# mks = int(input())
# if mks<25:
#     print ("f")
# elif mks>=25 and mks<45:
#     print("e")
# elif mks>=45 and mks<50:
#     print("d")
# elif mks>=50 and mks<=60:
#     print("c")
# elif mks>=60 and mks<=80:
#     print("b")
# else:
#     print("a")

# ppl1= int(input())
# ppl2= int(input())
# ppl3= int(input())
# if ppl1>=ppl2 and ppl1>=ppl3:
#     print("old is ppl1")
#     if ppl2<ppl3:
#        print("young is ppl2")
#     else:
#         print("young is ppl3")
# elif ppl2>=ppl1 and ppl2>=ppl3:
#     print("old is ppl2")
# elif ppl3>=ppl1 and ppl3>=ppl2:
#     print("old is ppl3")
# else:
#     print ("equal")


# clshld=int(input())
# clsattnd=int(input())
# pcattnd=(clshld/(clsattnd))*100
# print("attendence is",pcattnd)
# if pcattnd>=75:
#     print("allowed to exam")
# else:
#     print("not allowed to exam")

# medicause =input()
# if medicause == "y":
#   print("your allowed")
# else:
#   print("not allowed") 



#range (start-'num,end_num,sep_num)
# for n in range(0,10,3):
#     print(n)
# #length
# list1="Hello"
# for n in range (0,len(list1),2):
#     print(list1[n])
   
# list2="pqalvmajn"
# for i in range (0,len(list2),2):
#  print(i, list2[i])

# list3 ="skumdaham"
# for i in range (0, len(list3),2):
#     print(i,list3[i])

# list4="sarmajvnna"
# for i in range (0, len(list4),2):
#     print(i,list4[i])
# list5="hwrertmwea"
# list2=[]
# for i in range(len(list5)-1,0,-1):
#     list2.append(list5[i])
# print(list2)

x=75
def myfunc():
    x=x+1
    print(x)
myfunc()
print(x)