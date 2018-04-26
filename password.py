# Ibnul Jahan
# SoftDev2 pd7
# K#15: Do You Even List?
# 2018-4-25

import math


#print [(x,x*x,x*x*x) for x in range(8)]

p = 'myNoobPass1234'
#print [x for x in p]


UC_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LC_LETTERS = "abcdefghijklmnopqrstuvwxyz"
numbers = "1234567890"

#print [x for x in p if x in UC_LETTERS]
#print [1 for x in p if x in UC_LETTERS]
#print [1 if x in UC_LETTERS else 0 for x in p]

def test_pword ( p ):
    if (len([1 for x in p if x in UC_LETTERS]) > 0):
        if (len([1 for x in p if x in LC_LETTERS]) > 0):
            if (len([1 for x in p if x in numbers]) > 0):
                return True
    return False

print "Test cases for verifying a password\n"
print "trumkbhasw567 ->  " + str(test_pword("trumkbhasw567"))
print "23sdfFd ->  " + str(test_pword("23sdfFd"))
print "aetudfuwefh ->  " + str(test_pword("aetudfuwefh"))
print "IUDFHUIHHUHUIOHAoh ->  " + str(test_pword("IUDFHUIHHUHUIOHAoh"))
print "\n\n"


#ALGO EXPLANATION
'''
A 'good' password is characterized by having letters, numbers, and special characters. But to make it even more efficient, we should try to get an even mix of these numbers. Also, a general trend will be that a longer password will tend to be stronger than a shorter one.
'''
def rate_pword ( p ):
    size = len(p)
    if not test_pword(p):
        return "Not a valid password / 0 rating"
    strength = size
    #These 4 things will  add up to the size
    num_uc = len([1 for x in p if x in UC_LETTERS])
    num_lc = len([1 for x in p if x in LC_LETTERS])
    num_num = len([1 for x in p if x in numbers])
    num_special = size - (num_uc + num_lc + num_num)

    avg = math.ceil(size / 4)
    strength -= abs(0 if avg - num_uc < 0 else avg-num_uc)
    strength -= abs(0 if avg - num_lc < 0 else avg-num_lc)
    strength -= abs(0 if avg - num_num < 0 else avg-num_num)
    strength -= abs(0 if avg - num_special < 0 else avg-num_special)

    return str(strength)
    
    
print 'Test cases for strength of a password\n'
print "abc123 ->  " + rate_pword("abc123")
print "password ->  " + rate_pword("password")
print "Hhdh8838&h ->  " + rate_pword("Hhdh8838&h")
print "aaaaaaaaaaaaaaaaaaaaaaaaaaaa ->  " + rate_pword("aaaaaaaaaaaaaaaaaaaaaaaaaaaa")
print "Lo0k@tThIsPa55W0Rd ->  " + rate_pword("Lo0k@tThIsPa55W0Rd")
print "23sdfFd ->  " + rate_pword("23sdfFd")
print "Aa1&&&&&&&&&&&&&&&&&& ->  " + rate_pword("Aa1&&&&&&&&&&&&&&&&&&")





