__author__ = 'Dark-Knight'

def usermail():
    email= input('please enter your email address:')
    gtld= ['com', 'mil', 'gov', 'edu', 'gov' , 'net']


    try:
        username, temp = email.split('@')
        #print(username)
    except ValueError:
        return 'you must enter an @ symbol'
    try:
        domainname, genericdomain = temp.split('.')
    except ValueError:
        return 'you must have a period in your emailadress'
    if genericdomain in gtld:

        return username, domainname, genericdomain
    else:
          return'you must enter a proper gtld'

print(usermail())