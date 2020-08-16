from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options


from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType

options = Options()
options.add_experimental_option("prefs", { 
    "profile.default_content_setting_values.notifications": 1 
})
options.add_argument("--start-maximized")

driver = webdriver.Chrome(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install(), options=options)

url = "https://old.reddit.com/"

driver.get(url)
driver.find_element_by_name("user").send_keys("altasshet")
driver.find_element_by_name("passwd").send_keys("Spl1t@17")
driver.find_element_by_xpath('//button[text()="login"]').click()