# Determining the number of pages on which to extract the information
# - find this element (number of pages) 
# - Know the value

from bs4 import BeautifulSoup   # library for pulling data out of HTML and XML files
import re                       # regular expressions operations


def extracting_content(page):

    soup = BeautifulSoup(page.content, 'html.parser')   # soup <- all site is stored in this variable

    unordered_list = soup.find('ul', class_='pagination') # into variable unordered_list

    unordered_list = unordered_list.contents # tag's children available in a list called .content. from variable to list

    return str(unordered_list[-2])


def extractMax(input):
     # get a list of all numbers separated by 
     # lower case characters 
     # \d+ is a regular expression which means
     # one or more digit
     # output will be like ['100','564','365']
    numbers = re.findall(r'\d+',input)
     # now we need to convert each number into integer
     # int(string) converts string into integer
     # we will map int() function onto all elements 
     # of numbers list
    numbers = map(int,numbers)
    return max(numbers) # returns a int number
