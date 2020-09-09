from selenium import webdriver
import csv
import sys

def company_list(n, uname , pas):

   driver = webdriver.Chrome('/Users/sadhanakesavan/Downloads/chromedriver') 
   driver.get('https://www.linkedin.com')  
   username = driver.find_element_by_name("session_key")
   username.send_keys(uname)  
   password = driver.find_element_by_name("session_password")
   print(uname)
   password.send_keys(pas) 
   submit = driver.find_element_by_class_name("sign-in-form__submit-button")  
   submit.click() 

   driver.get('https://www.linkedin.com/search/results/companies/?origin=SWITCH_SEARCH_VERTICAL')

   username = driver.find_element_by_class_name("reusable-search__entity-results-list") 
   options = username.find_elements_by_tag_name("li") 
   print(len(options))
   csvfile = open('samplecomps2.csv', 'w', newline='')
   pg = 0
   while pg < n :
    for option in options:
     if len(option.text.split('\n')) > 2 : 
      print(option.text)
      ar = option.text.split('\n')
      print(len(ar))
      print(option.text)
      print(len(ar))  
      print("Company Name:")
      y = driver.find_element_by_partial_link_text(ar[0])
      x = y.get_attribute("href")
      ar[2] = x
      spamwriter = csv.writer(csvfile,quotechar='|', quoting=csv.QUOTE_MINIMAL)
      new_arr=[]
      new_arr.append(ar[0])
      new_arr.append(ar[1])
      new_arr.append(ar[2])
      spamwriter.writerow(new_arr) 
      print(x)
    pg = pg + 1
    driver.get('https://www.linkedin.com/search/results/companies/?origin=SWITCH_SEARCH_VERTICAL&page={}'.format(pg))
    username = driver.find_element_by_class_name("reusable-search__entity-results-list")
    options = username.find_elements_by_tag_name("li")

list_of_args = sys.argv
company_list(int(list_of_args[1]),list_of_args[2],list_of_args[3])
