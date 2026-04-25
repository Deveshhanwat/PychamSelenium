from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time
# Setting up Chrome options
options = Options()
options.add_experimental_option("detach", True)

# Initializing the Chrome driver with options
driver = webdriver.Chrome(options=options)
driver.maximize_window()

# Opening Flipkart
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
frame_element =driver.find_element(By.XPATH, "//iframe[@id='courses-iframe']")
driver.switch_to.frame(frame_element)
time.sleep(2)
driver.find_element(By.XPATH,"//a[@href='consulting']").click()
driver.switch_to.default_content()
driver.find_element(By.XPATH,"//input[@id='name']").send_keys("Devesh hanwat")