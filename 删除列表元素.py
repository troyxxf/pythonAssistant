example1=input()
print("---------------------看看你直接用input得到的是什么：")
print(example1)
print(type(example1))
print()
print("list[0]位置的值：")
list0=example1[0]
print(list0)
print(type(list0))
print()
print("list[1]位置的值：")
list1=example1[1]
print(list1)
print(type(list1))
print()
print("---------------------看看你用eval()之后得到的是什么：")
example1=eval(example1)
print(example1)
print(type(example1))
print()
print("list[0]位置的值：")
list0=example1[0]
print(list0)
print(type(list0))
print()
print("list[1]位置的值：")
list1=example1[1]
print(list1)
print(type(list1))
print()
print("将list[0]位置的值从float类型变成了int类型")
list0Toint=int(list0)
print(list0Toint)
print(type(list0Toint))