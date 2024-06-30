import random
import string
print("welcome to our random password generator")
def main():
    length=int(input('enter the length of password you want:'))
    lowerD = string.ascii_lowercase
    upperD = string.ascii_uppercase
    digitD = string.digits
    symbolsD = string.punctuation
    combine = lowerD + upperD + digitD + symbolsD
    password = ''.join(random.choices(combine, k=length))
    print(password)
    main()
main()
