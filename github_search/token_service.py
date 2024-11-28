def get_token():
    with open('Token.txt', 'r') as file:
        text = file.read()
        return text
