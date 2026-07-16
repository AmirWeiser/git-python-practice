from datetime import datetime

def greet(name):
    now = datetime.now()
    return f"Hello, {name}, the time is: {now}! Have a good day!"


if __name__ == "__main__":
    user = "World"
    print(greet(user))

