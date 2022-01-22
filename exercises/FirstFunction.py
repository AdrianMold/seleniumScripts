def orice(x,y,z):
    print("Hello From My Function! " + x)
    print("2nd line " + y)
    print("3rd line " + z)

def orice2(*args):

    x = "ceva"
    y = "ceva2"
    z = "ceva3"

    print(x,y,z)



def testArgs(*args):
    for x in args:
        print(x)

#orice("xx", "yy", "zz")
#orice("x1", "y1", "z1")
#orice("x2", "y2", "z2")
#orice2()
#testArgs(1,2,3,4,5,6,7,8,9,10,11,12,"re","in")

def suma(x,y):
    print(x+y)
    return x+y

ss = suma(1,2)
print(ss)


