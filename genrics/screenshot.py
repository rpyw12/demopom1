
import time

def takeScreenshot(driver):
    name = str(round(time.time()))+'.png'
    path = "D:/demopom1/screenshots/"
    file = path+name
    driver.save_screenshot(file)