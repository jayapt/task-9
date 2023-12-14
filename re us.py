import re
def validate_phone (phonenumber):

    pattern = re.compile(r"(\+\d{1,3})?\s?\(?\d{1,4}\)?[\s.-]?\d{3}[\s.-]?\d{4}")

    return pattern .match(phonenumber)

num=input("Enter the number:")
if validate_phone(num):

        print('True')
else:
        print('False')



