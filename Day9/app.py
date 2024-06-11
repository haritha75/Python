
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
 
# Initialize Chrome WebDriver
browser = webdriver.Chrome()
 
# Open GitHub homepage
browser.get("https://github.com")
 
# Wait for the "Sign in" link to be clickable
signin_link = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Sign in")))
 
# Click on the "Sign in" link
signin_link.click()
 
# Wait for the login form to be visible
login_form = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.ID, "login_field")))
 
# Find username input field and enter username
username_input = browser.find_element(By.ID, "login_field")
username_input.send_keys("haritha75")  # Replace "your_username" with your GitHub username
 
# Find password input field and enter password
password_input = browser.find_element(By.ID, "password")
password_input.send_keys("Y.Haritha@123")  # Replace "your_password" with your GitHub password
 
# Click the "Sign in" button
signin_button = browser.find_element(By.NAME, "commit")
signin_button.submit()
# to verify something like haritha75 in this browser html page
assert "haritha75" in browser.page_source
# with the class name of text bold i am selecting profile link in that if text is haritha75 it return noting if wrong it shows error
profile_link =  browser.find_element(By.CLASS_NAME,"text-bold")
link_label = profile_link.get_attribute("innerHTML")
assert "haritha75" in link_label
time.sleep(10)

 
# Close the browser (comment out if you want to keep the browser open)
# browser.quit()
 