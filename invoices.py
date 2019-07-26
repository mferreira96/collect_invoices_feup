import re
import getpass
import os
import time

from robobrowser import RoboBrowser


def gatherData(user, password):
    baseURL = 'https://sigarra.up.pt/feup/pt/'
    browser = RoboBrowser(history=True, parser='html.parser')
    browser.open(baseURL + 'web_page.Inicial')

    form = browser.get_form(action=re.compile(r'validacao'))

    form['p_user'].value = user
    form['p_pass'].value = password

    browser.submit_form(form)
    user_numbers = re.sub("[^0-9]", "", user)
    accountURL = baseURL + 'gpag_ccorrente_geral.conta_corrente_view?pct_cod=' + user_numbers
    browser.open(accountURL)

    files = []    
    titles = []
    links = browser.find_all('a', {"title": re.compile(r'Documento I03S')})
    
    if links != None and len(links) > 0:
        files = []
        for link in links:
            files.append(baseURL + link["href"])
            titles.append(link["title"])

    i = 0
    printProgressBar(i, len(titles), prefix = 'Progress:', suffix = 'Complete', length = 50)
    
    for index, file_href in enumerate(files[:]):
        browser.open(file_href)
        file_name = titles[index].replace(" ", "_")
    
        with open(folder_name + "/" + file_name + ".pdf", "wb") as _file:
            _file.write(browser.response.content)

        i = i + 1
        printProgressBar(i, len(titles), prefix = 'Progress:', suffix = 'Complete', length = 50)    

def save_files():
    print('Username:', end=' ')
    user = input()
    password = getpass.getpass()
    
    global folder_name
    folder_name = "invoices"
    
    try:
        if not os.path.exists(folder_name):
            os.mkdir(folder_name)
    except OSError:
        print("Unable to create folder 'invoices'")
        return
        
    gatherData(user, password)


def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█'):
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end = '\r')
    # Print New Line on Complete
    if iteration == total: 
        print()

save_files()