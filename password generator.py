import random
import string

def make_pass(pwd_len):
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(pwd_len))
    return password

def main():
    print("Epic Password Generator")
    try:
        length = int(input("Yo, how long do you want your password to be? "))
        if length <= 0:
            print("C'mon, enter a positive number!")
            return
        
        new_password = make_pass(length)
        print(f"Your super cool password: {new_password}")
    except ValueError:
        print("Not cool! Enter a number, dude.")

if __name__ == "__main__":
    main()

