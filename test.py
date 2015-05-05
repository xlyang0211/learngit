<<<<<<< HEAD
import sys

print >> sys.stdout, "%s %s" % ("hello", "world")
=======
class OnlyOne:
    class __OnlyOne:
        def __init__(self, arg):
            self.val = arg
        def __str__(self):
            return repr(self) + self.val
    instance = None # assign None to those variable whose type is not sure is a wise choice
    def __init__(self, arg):
        if not OnlyOne.instance: # If there is no instance, create one
            OnlyOne.instance = OnlyOne.__OnlyOne(arg)
        else: # else change/assign value to the instance
            OnlyOne.instance.val = arg
    def __getattr__(self, name):
        return getattr(self.instance, name)
 
x = OnlyOne('sausage')
print(x)
y = OnlyOne('eggs')
print(y)
z = OnlyOne('spam')
print(z)
print(x)
print(y)
print(`x`)
print(`y`)
print(`z`)
>>>>>>> bd62a4b7caaa9f2b53f05b58e0437e92b408050a
