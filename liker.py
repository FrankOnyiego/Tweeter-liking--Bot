from selenium import webdriver
from selenium.common.exceptions import SessionNotCreatedException
import time
from selenium.webdriver.common.by import By

# Try to set up the webdriver for ChromeDriver 111
try:
    driver = webdriver.Chrome()
except SessionNotCreatedException as e:
    # If the error message indicates that the version is not supported, try again with ChromeDriver 110
    if "This version of ChromeDriver only supports Chrome version 111" in e.msg:
        options = webdriver.ChromeOptions()
        options.binary_location = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
        driver = webdriver.Chrome(options=options, executable_path="C:\\path\\to\\chromedriver_110.exe")
    else:
        # If the error message is not related to the version, raise the exception again
        raise e

# Navigate to the Twitter login page
driver.get('https://twitter.com/login')

# Enter your login credentials
username = driver.find_element(By.XPATH,'//input[@name="session[SKYPAHUNCHO]"]')
password = driver.find_element(By.XPATH,'//input[@name="session[@blackhat10#]"]')
username.send_keys('SKYPAHUNCHO')
password.send_keys('[@blackhat10')

# Click the login button
login_button = driver.find_element(By.XPATH,'//div[@data-testid="LoginForm_Login_Button"]')
login_button.click()

# Wait for the page to load
time.sleep(5)

# Navigate to the Twitter search page
driver.get('https://twitter.com/search')

# Enter the search keywords and filters
search_box = driver.find_element(By.XPATH,'//input[@data-testid="SearchBox_Search_Input"]')
search_box.send_keys('#newhandles')
search_box.submit()

# Wait for the page to load
time.sleep(5)

# Like each tweet containing the hashtag "newhandles"
like_buttons = driver.find_elements(By.XPATH,'//div[@data-testid="like"]')
for button in like_buttons:
    button.click()
    time.sleep(1)
