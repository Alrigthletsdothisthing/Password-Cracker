# chr is 96-122
print('Please enter a 5 letter password that is all lowercase.')
import random as ran

i = input('Enter password here: ')
li = ['']
p = (li[0]) = i
first = (li[0][0])
sec = (li[0][1])
third = (li[0][2])
fourth = (li[0][3])
fifth = (li[0][4])
print(first)
r = ran.randint(96, 122)
conv = chr(r)
conv2 = chr(r)
conv3 = chr(r)
conv4 = chr(r)
conv5 = chr(r)
while first != conv:
    r = ran.randint(96, 122)
    conv = chr(r)
    print(conv)
else:
    while sec != conv2:
        r = ran.randint(96, 122)
        conv2 = chr(r)
        print(conv2)
    else:
        while third != conv3:
            r = ran.randint(96, 122)
            conv3 = chr(r)
            print(conv3)
        else:
            while fourth != conv4:
                r = ran.randint(96, 122)
                conv4 = chr(r)
                print(conv4)
            else:
                while fifth != conv5:
                    r = ran.randint(96, 122)
                    conv5 = chr(r)
                    print(conv5)
                else:
                    print('The password is:', conv, conv2, conv3, conv4, conv5)
# For testing the different letter and number conversions
# conv=chr(r)
# print(conv)
# print(r)
# print(li)
# print(li[0][0])
