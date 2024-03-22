from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def check_website():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    service = Service(ChromeDriverManager().install())
    
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    try:
        driver.get("http://example.com")
        h1_element = driver.find_element(By.TAG_NAME, "h1")
        if h1_element:
            print("H1 element found: ", h1_element.text)
        else:
            print("H1 element not found.")
    finally:
        driver.quit()

if __name__ == "__main__":
    check_website()
