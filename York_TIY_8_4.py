def make_shirt(text, size = "large"):
    message = f"The size of the shirt is {size}, and the text on the shirt is {text}."
    return message

size = "Medium"
texts = "I love Python"

print(make_shirt(texts))

print(make_shirt(texts, size = "medium"))

print(make_shirt(text = "Java is better", size = "small"))