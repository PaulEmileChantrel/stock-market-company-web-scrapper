import pandas as pd
import requests
import shutil

df = pd.read_csv('topMarketCap.csv')
img_links = list(df['image_link'])
tickers =list(df['ticker'])

# function to download an image given an img_link and save it to a file_name
def download_img(img_link,file_name):
   
   res = requests.get(img_link,stream=True)

   if res.status_code == 200:
      with open(file_name,'wb') as f:
         shutil.copyfileobj(res.raw, f)
      print('Image sucessfully Downloaded: ',file_name)
   else:
      print('Image Couldn\'t be retrieved')


# Download every image in the csv file
for i in range(10):
   ticker = tickers[i].lower()
   file_name = f'company_logo/{ticker}.webp'
   print(img_links[i])
   download_img(img_links[i],file_name)