import requests
from bs4 import BeautifulSoup

def main():
    url = "https://github.com/CSSEGISandData/COVID-19/blob/master/csse_covid_19_data/csse_covid_19_daily_reports/03-20-2020.csv"

    req = requests.get(url)
    soup = BeautifulSoup(req.text, 'html.parser')
    html = soup.findAll('tr', 'js-file-line')
    text_file = open("all_site_values.txt", "w")

    # Convert all tupels into a text file
    for i, j in enumerate(html):
        for a in j.findAll('td'):
            temp = j.text.strip("\n \t")
            text_file.write("\n")
            for char in temp:
                text_file.write(char)
            text_file.write("\n")
            break

    # Read from the file
    text_file = open("all_site_values.txt", "r")
    content = []

    for line in text_file:
        content.append(line.strip())

    for i in range(0,len(content)):
        if content[i] == "Saudi Arabia":
            Saudi_Arabia(content, i)
        if content[i] == "United Arab Emirates":
            UAE(content, i)
        if content[i] == "Kuwait":
            Kuwait(content, i)
        if content[i] == "Bahrain":
            Bahrain(content, i)
        if content[i] == "Oman":
            Oman(content, i)
        if content[i] == "Qatar":
            Qatar(content, i)

def Saudi_Arabia(content, i):
    print('-----------------------')
    print('Country : Saudi Arabia')
    print('Last Update : ' + content[i + 1])
    print('Confirmed :' + content[i + 2])
    print('Deaths : ' + content[i + 3])
    print('recovered : ' + content[i + 4])

def UAE(content, i):
    print('-----------------------')
    print('Country : United Arab Emirates')
    print('Last Update : ' + content[i + 1])
    print('Confirmed :' + content[i + 2])
    print('Deaths : ' + content[i + 3])
    print('recovered : ' + content[i + 4])

def Kuwait(content, i):
    print('-----------------------')
    print('Country : Kuwait')
    print('Last Update : ' + content[i + 1])
    print('Confirmed :' + content[i + 2])
    print('Deaths : ' + content[i + 3])
    print('recovered : ' + content[i + 4])

def Bahrain(content, i):
    print('-----------------------')
    print('Country : Bahrain')
    print('Last Update : ' + content[i + 1])
    print('Confirmed :' + content[i + 2])
    print('Deaths : ' + content[i + 3])
    print('recovered : ' + content[i + 4])

def Oman(content, i):
    print('-----------------------')
    print('Country : Oman')
    print('Last Update : ' + content[i + 1])
    print('Confirmed :' + content[i + 2])
    print('Deaths : ' + content[i + 3])
    print('recovered : ' + content[i + 4])

def Qatar(content, i):
    print('-----------------------')
    print('Country : Qatar')
    print('Last Update : ' + content[i + 1])
    print('Confirmed :' + content[i + 2])
    print('Deaths : ' + content[i + 3])
    print('recovered : ' + content[i + 4])

if __name__ == '__main__':
    main()




