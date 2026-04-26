from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

# Setting up Chrome options
options = Options()
options.add_experimental_option("detach", True)

# Initializing the Chrome driver with options
driver = webdriver.Chrome(options=options)
driver.maximize_window()

# Opening Flipkart
driver.get("https://www.flipkart.com/")

driver.find_element(By.XPATH,"//span[text()='Mobiles & Tablets']").click()