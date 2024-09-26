def make_shirt(size, text):
    message = f"The size of the shirt is {size}, and the text on the shirt is {text}."
    return message

size = "Medium"
text = "Weeeeeeeeee"

print(make_shirt(size, text))

print(make_shirt(size = "small", text = "nooooooo"))