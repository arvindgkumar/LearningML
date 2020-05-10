#######################DAY 0-Mean,Median & Mode ###########################
import collections

my_list = []
tInt = int(input())

# assuming list is passed  1 by 1
for _ in range(tInt):
    vl = float(input())
    my_list.append(vl)

# mean (add & divide)
Mean = sum(my_list) / tInt
print('#####')
print('%.2f' % Mean)
print('#####')

# Median
#print(tInt)
if(tInt%2!=0):
    oddMiddle = int(tInt/2)
    print('%.2f'%my_list[oddMiddle])
else:
    evenMiddle1 =  int(tInt/2)
    evenMiddle2 = int(tInt/2) - 1
    eMiddle = (my_list[evenMiddle1] + my_list[evenMiddle2])/2
    print('%.2f'%eMiddle)
print('#####')

#Mode - the number whih is popular
fq = 0
print(my_list)
#cal. the ffrequency
data = collections.Counter(my_list)
print(data)
data_list = dict(data)
print(data_list)

#most popular- find max


max_value = max(list((data.values())))
print(max_value)
mod_val = [num for num, freq in data_list.keys() if freq == max_value]
if len(mod_val) == len(my_list):
    print('No mode in the list')
else:
    print(map(str,mod_val))
##########################DAY 0
n = int(input())
X = list(map(int, input().split(" ")))
W = list(map(int, input().split(" ")))


XW = [X[i]*W[i] for i in range(len(X))]
# print(XW)
# print(sum(XW))
Wts = sum(W)
# print(Wts)


newMean = float(sum(XW)/Wts)
print('%.1f'%newMean)


#############Day 1: Standard Deviation##################
import math

n= int(input())
X = list(map(int, input().split(" ")))

mean = float(sum(X)/n)
print('%.2f'%mean)
#std deviation  = sqrt(sum of square of avg dist btwn value & mean)
#first calculate variance & then apply sqrt

varience = sum(pow(x - mean,2) for x in X)/n

stddev = math.sqrt(varience)
print('%.1f'%stddev)


##################Day 1- Quartile
n = int(input())
X = list(map(int, input().split()))
X.sort()
print(X)
ln = len(X)

# ODDnumbers in the list
if (n % 2 != 0):
    Q2 = X[int(n / 2)]
    lH = X[:int(n / 2)]
    print(lH)
    Q1 = (lH[int(len(lH) / 2) - 1] + lH[int(len(lH) / 2)])/2
    uH = X[int(n / 2) + 1:]
    print(uH)
    Q3 = (uH[int(len(uH) / 2) - 1] + uH[int(len(uH) / 2)]) / 2
else:
    Q2 = (X[int(ln / 2) - 1] + X[int(ln / 2)])/2
    lqr = X[:int(ln/2)]
    print(lqr)
    if len(lqr)%2!=0:
        Q1 = lqr[int(len(lqr)/2)]
    else:
        Q1 = (lqr[int(len(lqr)/2)] + lqr[int(len(lqr)/2)-1])/2

    uqr = X[int(ln / 2):]
    print(uqr)
    if len(uqr) % 2 != 0:
        Q3 = uqr[int(len(uqr) / 2)]
    else:
        Q3 = (uqr[int(len(uqr) / 2)] + uqr[int(len(uqr) / 2) - 1]) / 2

print(Q1)
print(Q2)
print(Q3)

############DAY 1 - Inter Quartile
import math

n = int(input())
elements = list(map(int, input().split(" ")))
frequencies = list(map(int, input().split(" ")))

data = []
for i in range(len(frequencies)):
    for j in range(int(frequencies[i])):
        data.append(int(elements[i]))

data = sorted(data)
# print data
# print len(data)
if len(data) % 2 == 0:
    data_1 = data[0: (len(data) // 2)]
    data_2 = data[(len(data) // 2):]

else:
    data_1 = data[0: int((len(data) / 2))]
    data_2 = data[int((len(data) / 2)) + 1:]


def median(my_list):
    index = len(my_list) // 2

    if len(my_list) % 2 != 0:
        return my_list[index]

    return (my_list[index] + my_list[index - 1]) / 2


# print data_1
# print data_2
mid_1 = median(data_1)
mid_2 = median(data_2)
# print mid_1, mid_2
print(float(mid_2 - mid_1))





