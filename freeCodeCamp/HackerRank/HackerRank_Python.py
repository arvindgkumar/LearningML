import string
#str1= input('Enter the input: ')

def split(word):
    return [char for char in word]
#BuiltIn

str1='I86E24gV3dfNQ2NVI2P2T5UdVyqPw8jN0EACrH31X3174LIdr5jd21ML5w2t3229QdQq85PAhUX5LU33h6347qe21458Nd7j7L5802wJe126w0rEL89VIw94M7G56fy39HJ11XMF3A515fI745E5fEjy9D91SI1LA83M4M578S40j35K7rJhM1fHUDTQW36WKwS2fMq5G4GA8q3SF4RgE213Wf9BK1C49yRwB87jMQOWV3615HUMq6Y7D9yHtT1It422J574IhDw6yT1GSGTTH53fN1OHY5GeD94941JOC4FV1NEj7Dq496Z463h1F5FVJ3RQ5P45N4452rGK8U3J18M1LGMMj4LLYVw17BIfZUhZMgV482Ij462O19Vt813N57N4wNS8hTqF3WHO4Dq79yLJLP9WjwTwC75e66DX34697W1tM19K8VP3qqgVJ4MRdHX4BMfO666dP9B3BS14LwDhZ65LhHwQeTY98MMjqJ5etq7X2YWrhYeVMyj15HI754W7XKZhJ93W2qXJ1C83M2Fe6445HeR1873r262fHM88XQ3L558Q8yH574Rw88rAw4U0rJJ8j2Q932M59ROqVwG3D3jXfIMX639EfINGJ6BgS3r6tWH7ZUV841127dK6JAeES61T72LeeW7r31Aw76eAy73wU6R43Z65jf0hW8rR81hPJFe5T27VLrM6DgTyBJU4yrS6qRht6P7y99Xw93R12Lq7e4UPM1A9ZEWSI8rAfH3Z5S5A3SeYDyJ1140h4dJUOO9F1IQ8M705e6YH5WJ31H5OHyY442rB9392FL7DR35FO14f2K42A18J0d14FEWj83TA0568w16dd52843NO867gT64VH5VU429r648CB9B9rSF9QCPf276dXGO5rOB3499d6841OB0852Af8455y3HH52rj3R57183822d8tO321e124V47N1J3OHNV3SQ3j1DyLt5HhC7F67CZd3DWyEgN7'
lower = [c for c in str1 if c.islower()]
upper=  [c for c in str1 if c.isupper()]
odds = [c for c in str1 if c.isdigit() and int(c)%2!=0 ]
even = [c for c in str1 if c.isdigit() and int(c)%2==0 ]
a = sorted(lower)+sorted(upper) +sorted(odds)+sorted(even)
print(a)

def convert(a):
    str1=''
    return(str1.join(a))
print(convert(a))


#19/3
#ListComprehension

x = 1
y = 1
z = 1
n = 3

ans = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if i + j + k != n]
print(ans)

#Built Data Types

n = 5
arr = [-7, -7, -7, -7, -6]
maxVal =max(arr)
indices = [i for i in range(len(arr)) if arr[i]== maxVal]
print("Indices : "+str(indices))
for ele in sorted(indices, reverse=True):
    del arr[ele]
print("new Arr:"+str(arr))
lMax= max(arr)
print(lMax)

#NestedLists
print('$$$$$$$$$$$$$$$')
pStu = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
marksheets=[]
scoresheet=[]
if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        marksheets+=[[name, score]]
        scoresheet+=[score]

x = sorted(set(scoresheet))[1]

for n, s in sorted(marksheets):
    if s ==x:
        print(n)

##Percentage

n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores


query_name = input()
avgScore = sum(student_marks[query_name])/len(scores)
print("{:.2f}".format(avgScore))


## Mutation
def mutate_string(string, position, character):
    modStr = string[:position]+character+string[position+1:]
    return modStr

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)

##########Tuples

n = int(input())
t = tuple(map(int, input().split(" ")))
print(hash(t))

##########swap-cases

S = str(input())
C = S.swapcase()
print(C)


#String Split and Join

S = list(input().split(" "))
print(S)
J = "-".join(S)
print(J)



#What's Your Name?

def print_full_name(a, b):
    print("Hello {0} {1}! You just delved into python.".format(a,b))

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)


#String Validators

S = input()


#In the first line, print True if  has any alphanumeric characters. Otherwise, print False.
#In the second line, print True if  has any alphabetical characters. Otherwise, print False.
#In the third line, print True if  has any digits. Otherwise, print False.
#In the fourth line, print True if  has any lowercase characters. Otherwise, print False.
#In the fifth line, print True if  has any uppercase characters. Otherwise, print False.

print(any(c.isalnum() for c in S))
print(any(c.isalpha() for c in S))
print(any(c.isdigit() for c in S))
print(any(c.islower() for c in S))
print(any(c.isupper() for c in S))

#Text Alignment

#TextAlinment

thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))

