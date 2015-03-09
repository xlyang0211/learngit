import pprint
class Button(object):
    """
    This is the button factory
    """
    html = "a"
    def get_html(self):
        self.html = "b"
        return self.html # Here why html beocmes instance variable instead of class variable?

    def set_html(self, value):
        self.html = value
class New(object):
    pass
my_name = ""
if __name__ == "__main__":
    your_name = "dapenti"
    button = Button()
    print button.html
    print Button.html
    print button.get_html()
    print Button.html
    button.set_html("c")
    print button.html
    print Button.html

    pprint globals()