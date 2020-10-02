# jashan 
import math
import json
import string
import random
import re

'''
    This code basically is like sign up and login type functionality.
    It contains various functions like : 
    New user, Existing user, pasword check, create password, take place, take birthday etc...
'''


def about():
    '''
        Shows user the purpose and the info about the program.
    '''
    display = """\
Hello User!, this program basically the same thing we see on the
starting and what we say the login or signup page of the website.
It uses some of the technique of string matching and also check
whether this string satisfies the conditions or not. It also uses
the concept we call as file handling it stores the data in file
in the backend. Also hashing or we say some kind of encoding technique
also used in this program. Random generation of strings also happen
in this program.
"""
    print('\n'+"This is what 'I AM'".center(70)+'\n'+"="*70+"\n"+display+'='*70)



def bye():
    message = """\
Good Bye User !!!
Have a nice day !!!
Keep coming Again !!!
"""
    print('\n'+"="*22+"\n"+message+"="*22)



def get_mail_id():
    '''
        Take the user mail id as input.
        and return string value back to new_user function.
    '''
    mail_id = input("Enter your mail address : ")
    pattern = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.+[a-zA-Z0-9-.]+')
    matches = pattern.findall(mail_id)
    if len(matches) != 1:
        print("Enter a valid mail address !!!")
        mail_id = get_mail_id()
    else:
        pass
    return mail_id



def get_name():
    '''
        Take the name of the user as input and also check 
        whether it is a valid name or not.
        And the return string value back to the new_user functuion.
    '''
    name = input("Enter your name : ")
    if name[0] not in (string.ascii_lowercase+string.ascii_uppercase):
        message = """
            First letter cannot be a number or special character.
            Please Enter a valid name
        """
        print(message)
        name = get_name()
    else:
        pass
    return name



def check_day(birthday_list):
    '''
        Check whether the entered birthday date is valid or not.
        For a simple year !!!
        and then return bool value back to the get_birthday function.
    '''
    value = True

    if int(birthday_list[1]) == 2:
        if 0 < int(birthday_list[0]) < 29:
            pass
        else:
            print("You Enter a wrong Birthday !!!")
            print("Please enter a valid birthday.")
            value = False
    elif int(birthday_list[1]) in [4, 6, 9, 11] and 0 < int(birthday_list[0]) < 31:
        pass
    elif 0 < int(birthday_list[0]) < 32:
        pass
    else:
        print("You Enter wrong Birthday !!!")
        print("Please enter a valid birthday.")
        value = False

    return value



def check_leap_day(birthday_list):
    '''
        Check whether the entered birthday date is valid or not.
        For a leap year !!!
        and then return bool value back to the get_birthday function.
    '''
    value = True

    if int(birthday_list[1]) == 2:
        if 0 < int(birthday_list[0]) <= 29:
            pass
        else:
            print("You Enter a wrong day !!!")
            print("Please enter a valid birthday.")
            value = False
    elif int(birthday_list[1]) in [4, 6, 9, 11] and 0 < int(birthday_list[0]) < 31:
        pass
    elif 0 < int(birthday_list[0]) < 32:
        pass
    else:
        print("You Enter wrong month !!!")
        print("Please enter a valid birthday.")
        value = False

    return value



def get_birthday():
    '''
        Take the birthday as input from the user.
        and then return this birthday back to the function
        new_user.
    '''
    message = """
            Enter the birthday in the given format or
            Enter a valid birthday !!!
        """
    birthday = input("Enter your birthday (DD/MM/YYYY) : ")
    pattern=re.compile(r'(\d{2}/\d{2}/\d{4})$')
    matches = pattern.findall(birthday)
    if len(matches) != 1:
        print(message)
        birthday=get_birthday()

    birthday_list = birthday.split('/')
    
    if not 0 < int(birthday_list[1]) < 13:
        print("You enter a wrong month !!!")
        print("Please enter a valid birthday.")
        birthday = get_birthday()

    elif (int(birthday_list[2]) % 4 == 0 and int(birthday_list[2]) % 100 != 0) or int(birthday_list[2]) % 400 == 0:
        value = check_leap_day(birthday_list)
        if value == False:
            birthday = get_birthday()
        else:
            pass

    else:
        value = check_day(birthday_list)
        if value == False:
            birthday = get_birthday()
        else:
            pass
    return birthday



def get_place():
    '''
        Take the residence of user as input and return
        this back to the new_user function.
    '''
    place = input("Enter the city where you live : ")
    if len(place)==0:
        print('Please enter the city !!!')
        place = get_place()
    if place[0] in (string.ascii_lowercase+string.ascii_uppercase):
        pass
    else:
        message = """
            First letter cannot be a number or special character.
            Please Enter a valid place.
        """
        print(message)
        place = get_place()
    return place



def check_password(password):
    '''
        Checks whether the password enter by the user is a
        valid password or not !
        and return bool value back to get_password function.
    '''
    value = True
    sp_sym = 0
    low_chr = 0
    up_chr = 0
    digit = 0
    if len(password) >= 8:
        for i in password:
            if i in (string.ascii_lowercase):
                low_chr += 1
            elif i in (string.ascii_uppercase):
                up_chr += 1
            elif i in (string.digits):
                digit += 1
            elif i in ('_@$'):
                sp_sym += 1
            else:
                print('Entered password consists of unwanted symbols !!!')
                break
        else:
            return value
    else:
        print('Password Length is less then 8 !!')
        value = False
    return value



def create_password(length):
    while True:
        password = ""
        i=0
        len1 = math.floor(length/4)
        len2 = length-3*len1
        password += ''.join(random.choice(string.ascii_lowercase)
                            for _ in range(int(len2)))
        password += ''.join(random.choice(string.ascii_uppercase)
                            for _ in range(int(len1)))
        password += ''.join(random.choice(string.digits)
                            for _ in range(int(len1)))
        password += ''.join(random.choice('_@$')
                            for _ in range(int(len1)))
        password = ''.join(random.sample(password, len(password)))
        print(f"Your {i+1}st generated password is : ", end="")
        print(password)
        i+=1
        ch = input("Do you want to set this as your password ? (Yes or NO)")
        if ch in ['y', 'yes', 'Yes', 'YES']:
            return password
        else:
            pass



def get_password():
    '''
        Take the password from the new user.
        return string password back to new_user function.
    '''
    while True:
        print("\nSelect only one (minimum length = 8)".center(50))
        message = '''\
        1. Want to Enter your own password.
        2. We generate password for you.
        '''
        try:
            ch = int(input(message))
            break
        except ValueError as e:
            print('Print a valid Literal !!!')
            continue
    while ch == 1:
        print(" Password should contain minimum\n 1 lower case\n 1 upper case\n 1 special symbol\n 1 numeric digit")
        print(' With the minimum length of 8')
        password = input(" Enter your password : ")
        value = check_password(password)
        if value == False:
            print(" Re-enter your password")
        else:
            break
    while ch == 2:
        print(" We create a random password for you.")
        length = int(input(" Enter the length of password you want ( Minimum 8 ): "))
        if length<8:
            print('Entered length is less then standard password length !!!')
            continue
        else:
            password = create_password(length)
            break

    return password



def new_user():
    '''
        Take the mail id, user name, birthday, place, and also password from
        the user and check whether these satisfies the basic condition for
        being password. Also check the syntax of birthdate and the pre-existing
        of the mail id in the backend file.
    '''
    mail_id = get_mail_id()
    name = get_name()
    birthday = get_birthday()
    place = get_place()
    password = get_password()
    print('*'*50)
    print('User Info'.center(50))
    print('*'*50)
   # print(
    #    f'Mail ID : {mail_id}\nName : {name}\nBirthday : {birthday}\nPlace : {place}\nPassword : {password}')
    user_dict = dict()
    user_dict[mail_id] = {'Name': name, 'Birthday': birthday,
                          'Place': place, 'Password': password}
    print('Mail ID : '+mail_id+'\n'+'Name : '+name+'\n'+'Birthday : '+birthday)
    print('Place : '+place+'\n'+'Password : '+password)
    with open('mydata.txt','a+') as fh:
        fh.write(str(user_dict)+'\n')



def verify_user(mail_id,password):
    '''\
    To verify that user enter a valid credentials for the input.
    Only verified user can access their info. Take mail_id from user.
    '''
    with open('mydata.txt','r') as fh:
        for line in fh:
            line=eval(line)
            if mail_id not in line:
                continue
            else:
                if line[mail_id]['Password']==password:
                    message="\n  Hello My Friend !!!\n  Your Other info is shown below\n"
                    info=('  Mail ID : '+mail_id+'\n'+'  Name : '+line[mail_id]['Name']+'\n')
                    info+=('  Birthday : '+line[mail_id]['Birthday']+'\n')
                    info+=('  Place : '+line[mail_id]['Place']+'\n')
                    info+=('  Password : '+line[mail_id]['Password'])
                    return (message+info)
                else:
                    return'  You Entered Wrong Credentials !!!!'
        else:
            return'  You Entered Wrong Credentials !!!!'



def existing_user():
    '''
        Used to get the mail id and password from the user and check whether 
        it exists in the backend in file data. If the given mail id and 
        password matches then only the program continues.
    '''
    mail_id = input('Enter your Mail ID : ')
    password = input('Enter your Password : ')
    check=verify_user (mail_id, password)
    print(check)


def menu():
    '''
        Display user the starting menu of the program from where user should
        select any option which he wants to select and move further to the
        program. This function continues until the user input satisfies the
        while condition.
    '''
    ch = 'y'
    while ch in['y', 'yes', 'Yes', 'YES', 'YUP', 'yup', 'Yup']:
        print("*"*50+'\n'+"What you want to do?".center(50)+'\n'+'*'*50)
        print("1. New User\n2. Existing User\n3. About\n4. Exit")
        try:
            selected = int(input("Select any one option : "))
        except ValueError as e:
            print('Enter a valid number')
            ch=input('You want to see the menu again ? (Yes or No)')
            if ch in ['y','yes','Yes','YES']:
                continue
            else:
                print('Bye Visiter !!!')
                break
        if selected == 1:
            new_user()
        elif selected == 2:
            existing_user()
        elif selected == 3:
            about()
        else:
            bye()
            break
        ch = input("\nWant to see the Menu again ? ( Enter 'y' or 'n' )")



if __name__ == '__main__':
    menu()
