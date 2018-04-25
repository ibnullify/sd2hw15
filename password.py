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
                return "finessed"

    return "ALERT! ALERT! ALERT!"


print test_pword("trumkbhasw567")
print test_pword("23sdfFd")
print test_pword("aetudfuwefh")
print test_pword("IUDFHUIHHUHUIOHAoh")


def rate_pword ( p ):
    if len(p) = 0:
        return "Please input an actual password :("
    le


    
