# we split the email address of user into username, domain and then we split
# domain into domain and extentiion
import re
def Email_Slicer():
    user_email_address = input("Input your email address: ")
    # First I need to check email address whether it is valid or not
    # To check Email address i will used Python Regular expression

    if Email_address_checker(user_email_address):
        (username, domain) = user_email_address.split('@')
        (domain_name , extensiom) = domain.split('.')
        print("Username: ", username)
        print("Domain_Name: ", domain_name)
        print("Extenion: ", extensiom)
    else:
        print("Please enter valid email address")


def Email_address_checker(user_email):
    # regular expression for validation email
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    if(re.fullmatch(regex, user_email)):
        return True
    else:
        return False



#Driver code
if __name__ == '__main__':
    Email_Slicer()
