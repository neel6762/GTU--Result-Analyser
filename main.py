from selenium import webdriver
from selenium.webdriver.support.select import Select


def enterDetails(rollno, browser):
    startNo = int(input('Enter the first Roll No:'))
    endNo = int(input('Enter the last Roll No:'))

    for i in range(startNo, endNo):
        rollno.clear()
        rollno.send_keys(i)
        browser.get_screenshot_as_file('main-page.png')


def main():
    # Setting up Chrome in headless mode

    path = r'C:\Users\ONEST\AppData\Local\Programs\Python\Python36-32\selenium\webdriver\chromedriver_win32\chromedriver.exe'
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    # options.add_argument('window-size=1200x600')
    browser = webdriver.Chrome(path, chrome_options=options)

    # Runnig the browser and opening the site

    try:
        browser.get('http://www.gturesults.in/')
    except:
        print('Sorry encountered an error ! Try again later..')

    # browser.get_screenshot_as_file('main-page.png')

    # Selecting the options menu

    select_element = Select(browser.find_element_by_css_selector('#ddlbatch'))
    print('Declared Results:')

    index = []
    for i, res in enumerate(select_element.options):
        print(i + 1, res.text)
        index.append(i)
        print()

    termSelection = int(input('Select the result for analysis\t ex: enter 1 for BE SEM 8 result analysis:')) - 1

    while True:
        if termSelection in index:
            select_element.select_by_index(termSelection)
            # browser.get_screenshot_as_file('main-page.png')

            # now get the range of the roll number to input
            rollno = browser.find_element_by_css_selector('#txtenroll')
            # enterDetails(rollno, browser)
            break
        else:
            print('Sorry no such index .. Enter a valid Index')
            termSelection = int(input('Select the result for analysis\t ex: enter 1 for BE SEM 8 result analysis:'))


if __name__ == 'main':
    main()
