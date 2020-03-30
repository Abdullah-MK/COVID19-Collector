import TwitterBot
from selenium import webdriver
from datetime import datetime
from datetime import datetime
import time

username = 'YOUR USERNAME'
password = 'YOUR PASSWORD'
time_opj = datetime.now()


def main():
    print('Time of the system : '+str(time_opj))
    driver = webdriver.Chrome()
    driver.get("https://www.worldometers.info/coronavirus/")
    #driver.maximize_window()
    #driver.execute_script("window.scrollTo(0, 400)")
    time.sleep(1)

    GCC(driver)
    #time.sleep(2)
    #World_Wide(driver)
    #time.sleep(2)
    #Top12(driver)

def GCC(driver = webdriver.Chrome):
    print('-Graping GCC Countries informations...')

    for i in range(1, 200):
        find_country_name = driver.find_element_by_xpath(
            '//*[@id="main_table_countries_today"]/tbody[1]/tr[' + str(i) + ']/td[1]').text
        if (find_country_name == 'Saudi Arabia'):
            SA = driver.find_element_by_xpath(
                '//*[@id="main_table_countries_today"]/tbody[1]/tr[' + str(i) + ']/td[2]').text
            continue
        if (find_country_name == 'UAE'):
            UAE = driver.find_element_by_xpath(
                '//*[@id="main_table_countries_today"]/tbody[1]/tr[' + str(i) + ']/td[2]').text
            continue
        if (find_country_name == 'Kuwait'):
            Q8 = driver.find_element_by_xpath(
                '//*[@id="main_table_countries_today"]/tbody[1]/tr[' + str(i) + ']/td[2]').text
            continue
        if (find_country_name == 'Bahrain'):
            Bahrain = driver.find_element_by_xpath(
                '//*[@id="main_table_countries_today"]/tbody[1]/tr[' + str(i) + ']/td[2]').text
            continue
        if (find_country_name == 'Qatar'):
            Qatar = driver.find_element_by_xpath(
                '//*[@id="main_table_countries_today"]/tbody[1]/tr[' + str(i) + ']/td[2]').text
            continue
        if (find_country_name == 'Oman'):
            Oman = driver.find_element_by_xpath(
                '//*[@id="main_table_countries_today"]/tbody[1]/tr[' + str(i) + ']/td[2]').text
            continue

    all_GCC = int(str(SA).replace(',','')) + int(UAE) + int(Q8) + int(Bahrain) + int(Qatar) + int(Oman)
    date = get_date()

    payload = 'إحصائيات دول الخليج ' + '\n' + \
              'آخر تحديث: ' + str(date) + '\n' + \
              'عدد الحالات المؤكدة في دول الخليج العربي: ' + str(all_GCC) + '\n' + \
              'المملكة العربية السعودية: ' + str(SA) + '\n' + \
              'الامارات العربية المتحدة: ' + str(UAE) + '\n' + \
              'الكويت: ' + str(Q8) + '\n' + \
              'البحرين: ' + str(Bahrain) + '\n' + \
              'قطر: ' + str(Qatar) + '\n' + \
              'سلطنة عُمان: ' + str(Oman) + '\n' + \
              '#كورونا #كوفيد19 #كوفيد_19 '

    print('-Pass GCC payload to TwitterBot script...')
    print(payload)
    bot = TwitterBot.TwitterBot(username, password)
    bot.login(payload)

def World_Wide(driver = webdriver.Chrome):
    print('-Graping World_Wide Countries informations...')

    driver2 = webdriver.Chrome

    three_elements = driver.find_elements_by_xpath('//*[@id="maincounter-wrap"]/div/span')
    COVIDcases = three_elements[0].text
    deaths = three_elements[1].text
    recovered = three_elements[2].text
    active = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/div/div[9]/div/div[2]/div/div[1]/div[1]').text
    not_risk = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/div/div[9]/div/div[2]/div/div[1]/div[3]/div[1]/span').text
    risk = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/div/div[9]/div/div[2]/div/div[1]/div[3]/div[2]/span').text

    date = get_date()

    payload = 'أهم الإحصائيات عالمياَ ' + '\n' + \
              'آخر تحديث: ' + date + '\n' + \
              'اجمالي عدد الأصابات بالفايروس: ' + COVIDcases + '\n' + \
              'حالات الوفيات: ' + deaths + '\n' + \
              'حالات الشفاء: ' + recovered + '\n' + \
              'المصابين حالياَ بالفايروس: ' + active + '\n' + \
              'عدد الحالات الغير حرجة: ' + not_risk + '\n' + \
              'عدد الحالات الحرجة: ' + risk + '\n' + \
              '#كورونا #كوفيد19 #كوفيد_19 '

    print('-Pass World_Wide payload to TwitterBot script...')
    print(payload)
    bot = TwitterBot.TwitterBot(username, password)
    bot.login(payload)

def Top12(driver = webdriver.Chrome):
    print('-Graping Top12 Countries informations...')
    date = get_date()
    name1 = translator(driver.find_element_by_xpath('//*[@id="main_table_countries_today"]/tbody[1]/tr[2]/td[1]/a').text)
    name2 = translator(driver.find_element_by_xpath('//*[@id="main_table_countries_today"]/tbody[1]/tr[3]/td[1]/a').text)
    name3 = translator(driver.find_element_by_xpath('//*[@id="main_table_countries_today"]/tbody[1]/tr[4]/td[1]/a').text)
    name4 = translator(driver.find_element_by_xpath('//*[@id="main_table_countries_today"]/tbody[1]/tr[5]/td[1]/a').text)
    name5 = translator(driver.find_element_by_xpath('//*[@id="main_table_countries_today"]/tbody[1]/tr[6]/td[1]/a').text)
    name6 = translator(driver.find_element_by_xpath('//*[@id="main_table_countries_today"]/tbody[1]/tr[7]/td[1]/a').text)
    name7 = translator(driver.find_element_by_xpath('//*[@id="main_table_countries_today"]/tbody[1]/tr[8]/td[1]/a').text)
    name8 = translator(driver.find_element_by_xpath('//*[@id="main_table_countries_today"]/tbody[1]/tr[9]/td[1]/a').text)
    name9 = translator(driver.find_element_by_xpath('//*[@id="main_table_countries_today"]/tbody[1]/tr[10]/td[1]/a').text)
    name10 = translator(driver.find_element_by_xpath('//*[@id="main_table_countries_today"]/tbody[1]/tr[11]/td[1]/a').text)

    num1 = driver.find_element_by_xpath('//*[@id="main_table_countries_today"]/tbody[1]/tr[2]/td[2]').text
    num2 = driver.find_element_by_xpath('//*[@id="main_table_countries_today"]/tbody[1]/tr[3]/td[2]').text
    num3 = driver.find_element_by_xpath('//*[@id="main_table_countries_today"]/tbody[1]/tr[4]/td[2]').text
    num4 = driver.find_element_by_xpath('//*[@id="main_table_countries_today"]/tbody[1]/tr[5]/td[2]').text
    num5 = driver.find_element_by_xpath('//*[@id="main_table_countries_today"]/tbody[1]/tr[6]/td[2]').text
    num6 = driver.find_element_by_xpath('//*[@id="main_table_countries_today"]/tbody[1]/tr[7]/td[2]').text
    num7 = driver.find_element_by_xpath('//*[@id="main_table_countries_today"]/tbody[1]/tr[8]/td[2]').text
    num8 = driver.find_element_by_xpath('//*[@id="main_table_countries_today"]/tbody[1]/tr[9]/td[2]').text
    num9 = driver.find_element_by_xpath('//*[@id="main_table_countries_today"]/tbody[1]/tr[10]/td[2]').text
    num10 = driver.find_element_by_xpath('//*[@id="main_table_countries_today"]/tbody[1]/tr[11]/td[2]').text

    date = get_date()


    payload = 'أول 10 دول في عدد الإصابات'+'\n'+\
              'آخر تحديث: ' + date + '\n' + \
              str(name1) + ': ' + str(num1) + '\n' + \
              str(name2) + ': ' + str(num2) + '\n' + \
              str(name3) + ': ' + str(num3) + '\n' + \
              str(name4) + ': ' + str(num4) + '\n' + \
              str(name5) + ': ' + str(num5) + '\n' + \
              str(name6) + ': ' + str(num6) + '\n' + \
              str(name7) + ': ' + str(num7) + '\n' + \
              str(name8) + ': ' + str(num8) + '\n' + \
              str(name9) + ': ' + str(num9) + '\n' + \
              str(name10) + ': ' + str(num10) + '\n' + \
              '#كورونا #كوفيد19 #كوفيد_19 '

    print('-Pass Top12 payload to TwitterBot script...')
    print(payload)
    bot = TwitterBot.TwitterBot(username, password)
    bot.login(payload)

def translator(name):
    driver = webdriver.Chrome()
    driver.get("https://translate.google.com.sa/?hl=ar")

    search_box = driver.find_element_by_xpath('//*[@id="source"]')
    search_box.click()
    search_box.send_keys(name)
    time.sleep(2)
    response = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[3]/div[1]/div[2]').text

    return response

def get_date():
    now = datetime.now()

    date = now.strftime("%d-%m-%Y")
    time = now.strftime("%I:%M")
    PMorAM = now.strftime("%p")

    if (PMorAM == 'PM'):
        inarabic = 'م'
    else:
        inarabic = 'ص'

    return date+' '+time+' '+inarabic

if __name__ == '__main__':
    main()
