#https://www.hackerrank.com/challenges/py-if-else/problem?isFullScreen=true
'''if __name__ == '__main__':
    n = int(input().strip())
    if n%2!=0:
        print('Weird')
    elif n%2==0:
        if 2<=n<=5:
            print('Not Weird')
        elif 6<=n<=20:
            print('Weird')
        else:
            print('Not Weird')'''


#https://www.hackerrank.com/challenges/write-a-function/problem?isFullScreen=true
'''def is_leap(year):
    
    if year%400==0:
        return True
    elif year%100==0:
        return False
    elif year%4==0:
        return True
    else:
        return False
year = int(input())'''

#match statement 
n=int(input("Enter a number : "))
match n:
    case  1:
        print('Sunday')
    case 2:
        print('Monday')
    case 3:
        print('Tuesday')
    case 4 :
        print('Wednesday')
    case  5:
        print('Thursday')
    case  6:
        print('Friday')
    case  7:
        print('Saturday')
    case _:
        print("Invalid number")