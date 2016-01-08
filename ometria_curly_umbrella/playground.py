from selenium import webdriver

browser = webdriver.Firefox()
browser.get('https://www.roseandgrey.co.uk/')

#find if ometria tracking pixel exists
# elem = browser.execute_script("return ometria", [])
# print elem

#find if ometria tracking pixel exists
elem = browser.
print elem.__dict__

# elem.send_keys('seleniumhq' + Keys.RETURN)

browser.quit()