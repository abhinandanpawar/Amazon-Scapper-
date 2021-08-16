#import area
from contextlib import nullcontext
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from datetime import datetime
import mysql.connector 
now = datetime.now() # current date and time

# date time module 
from datetime import date
today = date.today() # current date 
#driver installer / manager
opt=Options()
opt.add_argument("--headless")
driver=webdriver.Chrome(ChromeDriverManager().install(),chrome_options=opt)

#link input taker / variable
url=input()
driver.get(url)
product_name = driver.find_element_by_id('productTitle').text
product_price=None
try:
  product_price = driver.find_element_by_id('priceblock_ourprice').text
  print(product_price)
  product_price=product_price
except:
  deal_price = driver.find_element_by_id('priceblock_dealprice').text
  product_price=deal_price
print(product_name)
driver.close()


#today = now.strftime("%m_%d_%Y")
today="02_11_2021"
col="alter table price add "+ str(today)+" varchar(150) ;"

# sql connection code
 
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="price"
)

mycursor = mydb.cursor() # object of database ;
table="CREATE TABLE price(product_name varchar(255) NOT NULL);"

try:
  a= mycursor.execute(table)
except:
  print("already exists")
  
try:
  mycursor.execute(col)
except:
  print(f"{today} already created")


try :
  ins=(
   "INSERT INTO price(product_name,"+today+")"
   "VALUES (%s, %s)")

  val=(product_name, product_price)
  mycursor.execute(ins,val)
  mydb.commit()
except Exception as a:
  print(a)

mycursor.execute("select * from price")
records = mycursor.fetchall()
print("printing data in table ")
for i in records:
  print(i)
 
