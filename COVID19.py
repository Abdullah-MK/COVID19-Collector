import TwitterBot
from selenium import webdriver
from datetime import datetime
from selenium.webdriver.chrome.options import Options
import time

#some variables
username = 'YOUR_USERNAME'
password = 'YOUR_PASSWORD'
time_opj = datetime.now()

def main():
    print('Time of the system : '+str(time_opj) + '\n')

    #Create Chrome driver opject
    driver = webdriver.Chrome()
    driver.get("https://www.worldometers.info/coronavirus/")
    time.sleep(1)

    GCC(driver)
    time.sleep(1)
    World_Wide(driver)
    time.sleep(1)
    Top10(driver)

    #close the web browser opject
    driver.close()

def GCC(driver = webdriver.Chrome):
	#empty array to store countries names and numbers
    temp = []
    time.sleep(1)
    #scroll down by 2000 pixil
    driver.execute_script("window.scrollTo(0, 2000)")
    #determine the active cases button
    active_cases_button = driver.find_element_by_xpath('//*[@id="main_table_countries_today"]/thead/tr/th[8]')
    #click the button (sort the countries according to the active cases by descending order)
    webdriver.ActionChains(driver).move_to_element(active_cases_button).click(active_cases_button).perform()
    time.sleep(1)

    #for loop over all elements in the table
    for i in range(1, 200):
    	#take each country name, and compare it with the if statements below
        find_country_name = driver.find_element_by_xpath('//*[@id="main_table_countries_today"]/tbody[1]/tr[' + str(i) + ']/td[2]').text
        if (find_country_name == 'Saudi Arabia'):
            SA = driver.find_element_by_xpath(
                '//*[@id="main_table_countries_today"]/tbody[1]/tr[' + str(i) + ']/td[8]').text
            temp.append('المملكة العربية السعودية: ' + str(SA))
            continue
        if (find_country_name == 'UAE'):
            UAE = driver.find_element_by_xpath(
                '//*[@id="main_table_countries_today"]/tbody[1]/tr[' + str(i) + ']/td[8]').text
            temp.append('الامارات العربية المتحدة: ' + str(UAE))
            continue
        if (find_country_name == 'Kuwait'):
            Q8 = driver.find_element_by_xpath(
                '//*[@id="main_table_countries_today"]/tbody[1]/tr[' + str(i) + ']/td[8]').text
            temp.append('الكويت: ' + str(Q8))
            continue
        if (find_country_name == 'Bahrain'):
            Bahrain = driver.find_element_by_xpath(
                '//*[@id="main_table_countries_today"]/tbody[1]/tr[' + str(i) + ']/td[8]').text
            temp.append('البحرين: ' + str(Bahrain))
            continue
        if (find_country_name == 'Qatar'):
            Qatar = driver.find_element_by_xpath(
                '//*[@id="main_table_countries_today"]/tbody[1]/tr[' + str(i) + ']/td[8]').text
            temp.append('قطر: ' + str(Qatar))
            continue
        if (find_country_name == 'Oman'):
            Oman = driver.find_element_by_xpath(
                '//*[@id="main_table_countries_today"]/tbody[1]/tr[' + str(i) + ']/td[8]').text
            temp.append('سلطنة عُمان: ' + str(Oman))
            continue
    #variable to get the sum of all GCC countries statistics
    all_GCC = int(str(SA).replace(',','')) + int(str(UAE).replace(',','')) + int(str(Q8).replace(',','')) + int(str(Bahrain).replace(',','')) + int(str(Qatar).replace(',','')) + int(str(Oman).replace(',',''))
    #Date variable
    date = get_date()
    #payload have the final result
    payload = 'الحالات النشطة في دول الخليج ' + '\n' + \
              'آخر تحديث: ' + str(date) + '\n' + \
              'إجمالي الحالات النشطة في دول الخليج: ' + str(all_GCC) + '\n' + \
              str(temp[0]) + '\n' + \
              str(temp[1]) + '\n' + \
              str(temp[2]) + '\n' + \
              str(temp[3]) + '\n' + \
              str(temp[4]) + '\n' + \
              str(temp[5]) + '\n' + \
              '#كورونا #كوفيد19 #كوفيد_19 '
    #print the PAYLOAD to the screen
    print(payload + '\n\n')
    #create BOT opject with out USER_NAME and PASSWORD
    bot = TwitterBot.TwitterBot(username, password)
    #send the PAYLOAD to the BOT opject
    bot.login(payload)

def World_Wide(driver = webdriver.Chrome):
	#locate 3 elements (see https://www.worldometers.info/coronavirus/)
    three_elements = driver.find_elements_by_xpath('//*[@id="maincounter-wrap"]/div/span')
    COVIDcases = three_elements[0].text
    deaths = three_elements[1].text
    recovered = three_elements[2].text
    #get active,not_risk and risk statistics
    active = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/div/div[9]/div/div[2]/div/div[1]/div[1]').text
    not_risk = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/div/div[9]/div/div[2]/div/div[1]/div[3]/div[1]/span').text
    risk = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/div/div[9]/div/div[2]/div/div[1]/div[3]/div[2]/span').text
    #Date variable
    date = get_date()
    #payload have the final result
    payload = 'أهم الإحصائيات عالمياَ ' + '\n' + \
              'آخر تحديث: ' + date + '\n' + \
              'اجمالي عدد الأصابات بالفايروس: ' + COVIDcases + '\n' + \
              'حالات الوفيات: ' + deaths + '\n' + \
              'حالات الشفاء: ' + recovered + '\n' + \
              'المصابين حالياَ بالفايروس: ' + active + '\n' + \
              'عدد الحالات الغير حرجة: ' + not_risk + '\n' + \
              'عدد الحالات الحرجة: ' + risk + '\n' + \
              '#كورونا #كوفيد19 #كوفيد_19 '

    #print the PAYLOAD to the screen
    print(payload + '\n\n')
    #create BOT opject with out USER_NAME and PASSWORD
    bot = TwitterBot.TwitterBot(username, password)
    #send the PAYLOAD to the BOT opject
    bot.login(payload)

def Top10(driver = webdriver.Chrome):
	#initialize empty array to store Top 10 countries names
    names = []
    names.append(driver.find_element_by_xpath('//*[@id="main_table_countries_today"]/tbody[1]/tr[1]/td[2]/a').text)
    names.append(driver.find_element_by_xpath('//*[@id="main_table_countries_today"]/tbody[1]/tr[2]/td[2]/a').text)
    names.append(driver.find_element_by_xpath('//*[@id="main_table_countries_today"]/tbody[1]/tr[3]/td[2]/a').text)
    names.append(driver.find_element_by_xpath('//*[@id="main_table_countries_today"]/tbody[1]/tr[4]/td[2]/a').text)
    names.append(driver.find_element_by_xpath('//*[@id="main_table_countries_today"]/tbody[1]/tr[5]/td[2]/a').text)
    names.append(driver.find_element_by_xpath('//*[@id="main_table_countries_today"]/tbody[1]/tr[6]/td[2]/a').text)
    names.append(driver.find_element_by_xpath('//*[@id="main_table_countries_today"]/tbody[1]/tr[7]/td[2]/a').text)
    names.append(driver.find_element_by_xpath('//*[@id="main_table_countries_today"]/tbody[1]/tr[8]/td[2]/a').text)
    names.append(driver.find_element_by_xpath('//*[@id="main_table_countries_today"]/tbody[1]/tr[9]/td[2]/a').text)
    names.append(driver.find_element_by_xpath('//*[@id="main_table_countries_today"]/tbody[1]/tr[10]/td[2]/a').text)
    #pass the array to translate all countries names to arabic
    names = translator(names)

    #initialize empty array to store Top 10 countries statistics
    numbers = []
    numbers.append(driver.find_element_by_xpath('//*[@id="main_table_countries_today"]/tbody[1]/tr[1]/td[8]').text)
    numbers.append(driver.find_element_by_xpath('//*[@id="main_table_countries_today"]/tbody[1]/tr[2]/td[8]').text)
    numbers.append(driver.find_element_by_xpath('//*[@id="main_table_countries_today"]/tbody[1]/tr[3]/td[8]').text)
    numbers.append(driver.find_element_by_xpath('//*[@id="main_table_countries_today"]/tbody[1]/tr[4]/td[8]').text)
    numbers.append(driver.find_element_by_xpath('//*[@id="main_table_countries_today"]/tbody[1]/tr[5]/td[8]').text)
    numbers.append(driver.find_element_by_xpath('//*[@id="main_table_countries_today"]/tbody[1]/tr[6]/td[8]').text)
    numbers.append(driver.find_element_by_xpath('//*[@id="main_table_countries_today"]/tbody[1]/tr[7]/td[8]').text)
    numbers.append(driver.find_element_by_xpath('//*[@id="main_table_countries_today"]/tbody[1]/tr[8]/td[8]').text)
    numbers.append(driver.find_element_by_xpath('//*[@id="main_table_countries_today"]/tbody[1]/tr[9]/td[8]').text)
    numbers.append(driver.find_element_by_xpath('//*[@id="main_table_countries_today"]/tbody[1]/tr[10]/td[8]').text)
    #Date variable
    date = get_date()
    #payload have the final result
    payload = 'أعلى 10 دول في عدد الحالات النشطة'+'\n'+\
              'آخر تحديث: ' + date + '\n' + \
              str(names[0]) + ': ' + str(numbers[0]) + '\n' + \
              str(names[1]) + ': ' + str(numbers[1]) + '\n' + \
              str(names[2]) + ': ' + str(numbers[2]) + '\n' + \
              str(names[3]) + ': ' + str(numbers[3]) + '\n' + \
              str(names[4]) + ': ' + str(numbers[4]) + '\n' + \
              str(names[5]) + ': ' + str(numbers[5]) + '\n' + \
              str(names[6]) + ': ' + str(numbers[6]) + '\n' + \
              str(names[7]) + ': ' + str(numbers[7]) + '\n' + \
              str(names[8]) + ': ' + str(numbers[8]) + '\n' + \
              str(names[9]) + ': ' + str(numbers[9]) + '\n' + \
              '#كورونا #كوفيد19 #كوفيد_19 '

    #print the PAYLOAD to the screen
    print(payload + '\n\n')
    #create BOT opject with out USER_NAME and PASSWORD
    bot = TwitterBot.TwitterBot(username, password)
    #send the PAYLOAD to the BOT opject
    bot.login(payload)

def translator(names):
	#create web browser opject (chrome)
    driver = webdriver.Chrome()
    #request the website
    driver.get("https://translate.google.com.sa/?hl=ar")
    #locate the search box element
    search_box = driver.find_element_by_xpath('//*[@id="source"]')
    #for loop to translate each element in the array
    for i in range(0, len(names)):
        search_box.clear()
        search_box.click()
        search_box.send_keys(names[i])
        time.sleep(1.5)
        response = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[3]/div[1]/div[2]').text
        if (response == 'ديك رومي'):
            response = 'تركيا'
        if (response == 'الولايات المتحدة الأمريكية'):
            response = 'أمريكا'
        names[i] = response
    #close the web browser opject, and return the array
    driver.close()
    return names

def get_date():
	#method to get the current time of the system
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
