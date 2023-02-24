import urllib.request as url_lib


def site_connectivity_checker(url):
    response = url_lib.urlopen(url)  # if response from server side is 200-->its ok
    if response.getcode() == 200:
        print("Connect to url ", url, 'successfully')
        print('The response code was: ', response.getcode())
    else:
        print('Your site are down')

if __name__ == '__main__':
    print("This is site connectivity checker program:")
    web_url = input("Enter your web site url to check: ")
    site_connectivity_checker(web_url)
