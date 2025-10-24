n = int(input())
temp=n,res=0
while(temp!=0):
    int l=temp%10
    res=res*10+l
    temp/=10
if(res==n):
    print("Palindrome")
else:
    print("Not Palindrome")
