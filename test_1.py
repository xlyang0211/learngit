class Collection():
    value = ["yes"]
    def __init__(self):
        self.value = []
        self.value.append("hello")
        print "e", self.value
        print type(self)

    @classmethod
    def haha(cls):
        print "Is this class method?"
        print type(cls)

    def attr_1(self):
        print "attr_1 is to print 1."

    def attr_2(self):
        print "attr_2 is to print 2."

if __name__ == "__main__":
    collection = Collection()
    collection.haha()
    Collection.haha()
