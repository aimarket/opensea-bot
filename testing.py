from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
import time
URL = "https://marketplace.treasure.lol/collection/smol-bodies?tab=activity"

options = Options()
options.page_load_strategy = 'normal'
options.add_argument("--disable-extensions")
options.add_argument("--disable-gpu")
options.add_argument("--headless")
driver = webdriver.Firefox(options=options, executable_path="C:\\Location\\of\\screenshot.png")
driver.set_window_size(460, 2400)
driver.get(URL)
time.sleep(.5)


S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
driver.set_window_size(S('Width'),S('Height')) # May need manual adjustment

driver.find_element_by_tag_name('body').screenshot('test.png')

driver.quit()