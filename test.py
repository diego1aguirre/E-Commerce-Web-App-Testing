from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = Firefox()
driver.get('https://www.saucedemo.com/')



def send_credentials(user,password_):

    driver.find_element(By.ID,"user-name").send_keys(user)
    driver.find_element(By.ID,"password").send_keys(password_)
    driver.find_element(By.ID,"password").send_keys(Keys.ENTER)
    sleep(2)

def add_to_chart():

    driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]').click()
    sleep(1.5)
    driver.find_element(By.CLASS_NAME, 'shopping_cart_link').click()
    sleep(1.5)
    driver.find_element(By.ID, 'checkout').click()
    sleep(1.5)
    driver.find_element(By.ID, 'first-name').send_keys('Dele')
    driver.find_element(By.ID, 'last-name').send_keys('Ali')
    driver.find_element(By.ID, 'postal-code').send_keys('120036')
    sleep(1.5)
    driver.find_element(By.ID, 'continue').click()
    sleep(1.5)
    driver.find_element(By.ID, 'finish').click()
    sleep(2)

def check_path(user,pas):
    try:
        send_credentials(user, pas)
        add_to_chart()
        print('For the credentials:', user,' and', pas,' the test pass')
    except:
        print('For the credentials:', user,' and', pas,' the test failed')
        driver.close()


check_path('standard_user','secret_sauce')
#check_path('locked_out_user','secret_sauce')
#check_path('problem_user','secret_sauce')