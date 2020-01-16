#1
# v1=[2 ,4, 5]
# v2=[2, 3, 6]
# v3=[]
# for i in range(len(v1)):
#     i=v1[i]*v2[i]
#     v3.append(i)
# print(v3)

# #2
# a=[[1,3],[2,4]]
# b=[[5,2],[1,0]]
# c=[]
# for i in range(len(a)):
#     c_new=[]
#     for j in range(len(a[i])):
#         q = a[i][j] +b[i][j]
#         c_new.append(q)
#     c.append(c_new)
# print(c)

#3
a=[[1,3,5],[2,4,5],[3,4,6]]
b=[[5,22,2],[1,0,3],[1,2,4]]
c=[]
for i in range(len(a)):
    c_new=[]
    for j in range(len(a[i])):
        q = a[i][j] +b[i][j]
        c_new.append(q)
    c.append(c_new)
print(c)

# #4
# list =[1,2,7,8,5,9,6,3,7,5,]
# list_sorted =list.sort()
# print (list_sorted)
# new_list =[]
# for index in range(len(list_sorted)):
#     new_list.append(list_sorted[index])
#     if list_sorted[index]==list_sorted[index+1]:
#         del list_sorted[index+1]
#     print(new_list)

# #5
# string = "I am a leet programmer"
# print(string.upper())
# for index in range(len(string)):
#     if string[index]=='A':
#         string[index]="4"
#     if string[index]=='E':
#         string[index]='3'
#     if string[index]=='G':
#         string[index]='6'
#     if string[index]=='I':
#         string[index]='1'
#     if string[index]=='O':
#         string[index]='0'
#     if string[index]=='S':
#         string[index]='5'
#     if string[index]=='T':
#         string[index]='7'
#     print(string[index])




