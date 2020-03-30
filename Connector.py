import COVID19
from selenium import webdriver
import time

last_date = ''
while (1<2):
    driver = webdriver.Chrome()
    driver.get("https://www.worldometers.info/coronavirus/")

    date = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/div/div[2]')
    date = date.text
    print('the date is')
    print(date)

    print('-+-+-+-+-+-+-+-+-+-+-')
    if (date == last_date):
        print('>The time does not change, sleep for 10mins...')
        time.sleep(600)
    else:
        print('>There is a new informations...')
        print('>Invoking COVID19 Python File')
        COVID19.main()
        print('>COVID File has been compiled successfully')
        print('>time sleep for 10mins...')
        last_date = date
        time.sleep(600)
    print('-+-+-+-+-+-+-+-+-+-+-')

