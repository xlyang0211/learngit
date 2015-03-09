def main(x):
    hello_world()
    print "x is:", x

def hello_world():
    print "Hello world!"

if __name__ == "__main__":
    x = 1
    main(x)
    import sys
    print sys.getdefaultencoding()
