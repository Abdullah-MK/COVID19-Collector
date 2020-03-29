import TwitterBot
from selenium import webdriver
from datetime import datetime
import time

username = 'YOUR USERNAME'
password = 'YOUR PASSWORD'
time_opj = datetime.now()


def main():
    print('Time of the system : '+str(time_opj))
    driver = webdriver.Chrome()
    driver.get("https://covid19.cdc.gov.sa/ar/daily-updates-ar/")
    driver.maximize_window()
    driver.execute_script("window.scrollTo(0, 400)")
    time.sleep(3)

    GCC(driver)
    time.sleep(10)
    World_Wide(driver)
    time.sleep(10)
    Top12(driver)

def GCC(driver = webdriver.Chrome):
    print('-Graping GCC Countries informations...')
    SA = driver.find_element_by_xpath('/html/body/div/div[2]/div/div'
                                      '/div/section/div/section[2]'
                                      '/div/div/div/div[1]/div/div'
                                      '/section[1]/div/div/div/div[2]/div/div/span').text
    UAE = driver.find_element_by_xpath('/html/body/div/div[2]/div/div'
                                       '/div/section/div/section[2]'
                                       '/div/div/div/div[2]/div/div'
                                       '/div/div/table/tbody/tr[63]/td[2]').text
    Q8 = driver.find_element_by_xpath('/html/body/div/div[2]/div/div'
                                      '/div/section/div/section[2]/div/'
                                      'div/div/div[2]/div/div/div/div/table'
                                      '/tbody/tr[70]/td[2]').text
    Bahrain = driver.find_element_by_xpath('/html/body/div/div[2]/div'
                                           '/div/div/section/div/section[2]'
                                           '/div/div/div/div[2]/div/div/div'
                                           '/div/table/tbody/tr[51]/td[2]').text
    Qatar = driver.find_element_by_xpath('/html/body/div/div[2]/div'
                                         '/div/div/section/div/section[2]'
                                         '/div/div/div/div[2]/div/div/div'
                                         '/div/table/tbody/tr[44]/td[2]').text
    Oman = driver.find_element_by_xpath('/html/body/div/div[2]/div/div'
                                        '/div/section/div/section[2]'
                                        '/div/div/div/div[2]/div/div'
                                        '/div/div/table/tbody/tr[89]/td[2]').text
    last_update = driver.find_element_by_xpath('/html/body/div/div[2]/div/div/div'
                                               '/section/div/section[1]/div/div/div/div/div/div/p').text
    all_GCC = driver.find_element_by_xpath('/html/body/div/div[2]/div/div/div/section/div'
                                           '/section[2]/div/div/div/div[1]/div/div/section[2]'
                                           '/div/div/div/div[3]/div/div/span').text

    payload = 'إحصائيات دول الخليج '+'\n'+\
              last_update +'\n'+\
              'عدد الحالات المؤكدة في دول الخليج العربي: '+ all_GCC +'\n'+\
              'المملكة العربية السعودية: '+ SA +'\n'+\
              'الامارات العربية المتحدة: '+ UAE +'\n'+\
              'الكويت: '+ Q8 + '\n'+\
              'البحرين: '+ Bahrain + '\n'+\
              'قطر: '+ Qatar + '\n'+\
              'سلطنة عُمان: ' + Oman +'\n'+ \
              '#كورونا #كوفيد19 '

    print('-Pass GCC payload to TwitterBot script...')
    bot = TwitterBot.TwitterBot(username, password)
    bot.login(payload)

def World_Wide(driver = webdriver.Chrome):
    print('-Graping World_Wide Countries informations...')
    elem1 = driver.find_element_by_xpath('/html/body/div/div[2]/div/div/div/section'
                                         '/div/section[2]/div/div/div/div[1]/div/div'
                                         '/section[1]/div/div/div/div[1]/div/div/span').text
    elem3 = driver.find_element_by_xpath('/html/body/div/div[2]/div/div/div/section'
                                         '/div/section[2]/div/div/div/div[1]/div/div'
                                         '/section[2]/div/div/div/div[1]/div/div/span').text
    elem4 = driver.find_element_by_xpath('/html/body/div/div[2]/div/div/div/section'
                                         '/div/section[2]/div/div/div/div[1]/div/div'
                                         '/section[2]/div/div/div/div[2]/div/div/span').text
    elem6 = driver.find_element_by_xpath('/html/body/div/div[2]/div/div/div/section/div'
                                         '/section[2]/div/div/div/div[1]/div/div/section[3]'
                                         '/div/div/div/div[1]/div/div/span').text
    elem7 = driver.find_element_by_xpath('/html/body/div/div[2]/div/div/div/section/div'
                                         '/section[2]/div/div/div/div[1]/div/div/section[3]'
                                         '/div/div/div/div[2]/div/div/span').text
    elem8 = driver.find_element_by_xpath('/html/body/div/div[2]/div/div/div/section/div'
                                         '/section[2]/div/div/div/div[1]/div/div/section[3]'
                                         '/div/div/div/div[3]/div/div/span').text
    elem9 = driver.find_element_by_xpath('/html/body/div/div[2]/div/div/div/section/div'
                                         '/section[2]/div/div/div/div[1]/div/div/section[4]'
                                         '/div/div/div/div[1]/div/div/span').text
    elem10 = driver.find_element_by_xpath('/html/body/div/div[2]/div/div/div/section/div'
                                          '/section[2]/div/div/div/div[1]/div/div/section[4]'
                                          '/div/div/div/div[2]/div/div/span').text
    last_update = driver.find_element_by_xpath('/html/body/div/div[2]/div/div/div'
                                               '/section/div/section[1]/div/div/div/div/div/div/p').text

    payload = 'أهم الأحصائيات عاليماَ ' +'\n'+\
              last_update +'\n'+\
              'الحالات المؤكدةً: ' + elem1 +'\n'+\
              'خارج الصين: ' + elem3 +'\n'+\
              'داخل الصين: ' + elem4 +'\n'+\
              'الحالات الحرجة: ' + elem6 +'\n'+\
              'الحالات الغير حرجة: ' + elem7 + '\n'+\
              'المصابين حالياً: ' + elem8 + '\n'+\
              'إجمالي حالات الشفاء: ' + elem9 + '\n'+\
              'إجمالي الوفيات: ' + elem10+ '\n'+\
              '#كورونا #كوفيد19 '

    print('-Pass World_Wide payload to TwitterBot script...')
    bot = TwitterBot.TwitterBot(username, password)
    bot.login(payload)

def Top12(driver = webdriver.Chrome):
    print('-Graping Top12 Countries informations...')
    top1 = driver.find_element_by_xpath('/html/body/div/div[2]/div/div/div/section/div/section[2]/div/div/div/div[2]/div/div/div/div/table/tbody/tr[1]').text
    top2 = driver.find_element_by_xpath('/html/body/div/div[2]/div/div/div/section/div/section[2]/div/div/div/div[2]/div/div/div/div/table/tbody/tr[2]').text
    top3 = driver.find_element_by_xpath('/html/body/div/div[2]/div/div/div/section/div/section[2]/div/div/div/div[2]/div/div/div/div/table/tbody/tr[3]').text
    top4 = driver.find_element_by_xpath('/html/body/div/div[2]/div/div/div/section/div/section[2]/div/div/div/div[2]/div/div/div/div/table/tbody/tr[4]').text
    top5 = driver.find_element_by_xpath('/html/body/div/div[2]/div/div/div/section/div/section[2]/div/div/div/div[2]/div/div/div/div/table/tbody/tr[5]').text
    top6 = driver.find_element_by_xpath('/html/body/div/div[2]/div/div/div/section/div/section[2]/div/div/div/div[2]/div/div/div/div/table/tbody/tr[6]').text
    top7 = driver.find_element_by_xpath('/html/body/div/div[2]/div/div/div/section/div/section[2]/div/div/div/div[2]/div/div/div/div/table/tbody/tr[7]').text
    top8 = driver.find_element_by_xpath('/html/body/div/div[2]/div/div/div/section/div/section[2]/div/div/div/div[2]/div/div/div/div/table/tbody/tr[8]').text
    top9 = driver.find_element_by_xpath('/html/body/div/div[2]/div/div/div/section/div/section[2]/div/div/div/div[2]/div/div/div/div/table/tbody/tr[9]').text
    top10 = driver.find_element_by_xpath('/html/body/div/div[2]/div/div/div/section/div/section[2]/div/div/div/div[2]/div/div/div/div/table/tbody/tr[10]').text
    top11 = driver.find_element_by_xpath('/html/body/div/div[2]/div/div/div/section/div/section[2]/div/div/div/div[2]/div/div/div/div/table/tbody/tr[11]').text
    top12 = driver.find_element_by_xpath('/html/body/div/div[2]/div/div/div/section/div/section[2]/div/div/div/div[2]/div/div/div/div/table/tbody/tr[12]').text
    last_update = driver.find_element_by_xpath('/html/body/div/div[2]/div/div/div'
                                               '/section/div/section[1]/div/div/div/div/div/div/p').text

    #top1 = str(top1).replace(' ', ' : ')
    #top2 = str(top2).replace(' ', ' : ')
    #top3 = str(top3).replace(' ', ' : ')
    #top4 = str(top4).replace(' ', ' : ')
    #top5 = str(top5).replace(' ', ' : ')
    #top6 = str(top6).replace(' ', ' : ')
    #top7 = str(top7).replace(' ', ' : ')
    #top8 = str(top8).replace(' ', ' : ')
    #top9 = str(top9).replace(' ', ' : ')
    #top10 = str(top10).replace(' ', ' : ')
    #top11 = str(top11).replace(' ', ' : ')
    #top12 = str(top12).replace(' ', ' : ')
    #top13 = str(top13).replace(' ', ' : ')
    #top14 = str(top14).replace(' ', ' : ')
    #top15 = str(top15).replace(' ', ' : ')

    payload = 'أول 12 دولة في عدد الإصابات'+'\n'+ last_update +'\n'+top1+'\n'+top2+'\n'+top3+'\n'+top4+'\n'+top5+'\n'+top6+'\n'+top7+'\n'+top8+'\n'+top9+'\n'+top10 \
    +'\n' +top11+'\n'+top12+'\n'+'#كورونا #كوفيد19 '

    print('-Pass Top12 payload to TwitterBot script...')
    bot = TwitterBot.TwitterBot(username, password)
    bot.login(payload)




if __name__ == '__main__':
    main()




