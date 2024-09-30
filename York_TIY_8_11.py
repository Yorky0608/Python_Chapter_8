short_messages = ['Love your life.', 'Do not be harming.', 'Make sure you breath air.']
s_messages = []

def show_messages():
    for message in short_messages:
        print(message)
        s_messages.append(message)

show_messages()
print(s_messages)
print(short_messages)