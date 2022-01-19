from urllib.request import urlopen
import time

def get_load_time(url):
    """This function takes a user input for a url and
        returns the time taken to load the site in seconds 
    """
    if ('https' or 'http') in url:
        open_this_url = urlopen(url)
    else:
        open_this_url = urlopen("https://" + url)
    start_time = time.time() #Time stamp before the reading of url starts
    open_this_url.read() #Reading the user input url
    end_time = time.time() #Time stamp before the reading of url starts
    open_this_url.close() #Closing the instance of the urlopen object
    time_to_load = end_time - start_time

    return time_to_load

if __name__ == '__main__':
    url = input("Enter the url whose loading time you want to check: ")
    print(f"\nThe time taken to load {url} is {get_load_time(url):.2} seconds.")