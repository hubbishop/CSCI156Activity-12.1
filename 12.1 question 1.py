__author__ = 'Dark-Knight'


email=input('please enter your email adress:')
username,mail = email.split('@')
domainname,genericdomain = mail.split('.')
print(username)
print(domainname)
print(genericdomain)