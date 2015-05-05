class Button(object):
    html = ""
    def get_html(self):
        return self.html # Here why html beocmes instance variable instead of class variable?
 
class Image(Button):
    html = "<img alt="" />"
 
class Input(Button):
    html = "<input type='text' />"
 
class Flash(Button):
    html = "dada"

class Factory(object):
    def generate_button(self, button_type):
        button_type = button_type.capitalize()
        return globals()[button_type]()

if __name__ == "__main__":
    for type in ["image", "input", "flash"]:
        button = Factory()
        print button.generate_button(type).get_html()
