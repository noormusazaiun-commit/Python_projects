n =input("enter \n")
t=[]
for i in n:
    t.append(i)
m =t.copy()
t.reverse()
if t == m:
    print("the text is palindrome")
else :
    print("the text is not palindrome")