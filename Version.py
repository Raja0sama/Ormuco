

def Version(a,b):
    try:
        if(float(a) > float(b)):
            return "Value "+a+" is Greater Then "+b
        else:
            return "Value "+b+" is Greater Then "+a
    except:
        print("The Value you Provide is wrong and it should be on this format 1.1 or 2.2")

print (Version("1.1","1.2"))