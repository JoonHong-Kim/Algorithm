import sys

def pelindrome(num:str)->bool:
    if num==num[::-1]:
        return True
    else:
        return False

if __name__=="__main__":
    input=sys.stdin.readline
    while True:
        num=input().strip()
        if num=="0":
            break
        if pelindrome(num):
            print("yes")
        else:
            print("no")
