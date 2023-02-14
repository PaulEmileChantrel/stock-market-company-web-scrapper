from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

import pandas as pd



target_link = 'https://companiesmarketcap.com/'



path = "/Users/paul-emile/Downloads/chromedriver"

# Options
options = Options()
# don't open the browser
options.headless=True




# create a dataframe
df = pd.DataFrame()


#Initializing Chrome driver
service = Service(executable_path=path)
driver = webdriver.Chrome(service = service)

#Open the web page
driver.get(target_link)

def accept_cookies(driver):
   try:
      button = driver.find_element(by="xpath",value="//div[@class='popup-buttons popup-buttons-2']/div[2]/button")
      button.click()
   except:
      print('no cookies')
   
def scrap_page(driver,df):
   #get html container with their xpath
   containers = driver.find_elements(by="xpath",value="//td[@class='name-td']")
   
   # We iterate through the containers to get the info
   for container in containers:
      try:
         name = container.find_element(by="xpath",value='./div[2]/a/div[1]').text
      except:
         name = ''
      try:
         rank = container.find_element(by="xpath",value='./div[2]/a/div[2]/span').text
      except:
         rank = ''
      try:
         
         ticker = container.find_element(by="xpath",value='./div[2]/a/div[2]').text
         ticker = ticker[len(rank):]
      except:
         ticker = ''
      try:
         image_link = container.find_element(by="xpath",value='./div/img').get_attribute("src")

      except:
         image_link = ''

      new_row = pd.DataFrame({'name':[name],'ticker':[ticker],'image_link':[image_link]})
      df = pd.concat([df,new_row],ignore_index=True)
      
   return df

accept_cookies(driver)
df = scrap_page(driver,df)



df.to_csv('topMarketCap2.csv',index=False)

driver.quit()







