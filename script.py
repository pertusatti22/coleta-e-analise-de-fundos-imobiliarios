# Etapa 1
!apt update
!apt install chromium - chromedriver
!pip install selenium
print('Dependências Instaladas')

# Etapa 2
from selenium import webdriver
from selenium.webdriver.common.by import By

print('Bibliotecas carregadas')

# Etapa 3
# Configurando web scraping
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')  # Run in headless mode, i.e., without a UI or display server dependencies.
chrome_options.add_argument('--no-sandbox')  # Disables the sandbox for all process types that are normally sandboxed. Meant to be used as a browser-level switch for testing purposes only. https://www.google.com/googlebooks/chrome/med_26.html
chrome_options.add_argument('--disable-dev-shm-usage')  # The /dev/shm partition is too small in certain VM environments, causing Chrome to fail or crash (see http://crbug.com/715363). Use this flag to work-around this issue (a temporary directory will always be used to create anonymous shared memory files).
wd_chrome = webdriver.Chrome(chrome_options=chrome_options)
print('Driver configurado')

# Etapa 4
url = "https://fiis.com.br/lista-de-fundos-imobiliarios/"
wd_chrome.get(url)
print('URL configurada')
allTicker = []
getTicker = wd_chrome.find_elements(By.CLASS_NAME, "ticker")
for ticker in getTicker:
    allTicker.append(ticker.text)
print('Lista de FIIs carregada')

# Etapa 5
funds = []
max = len(allTicker)  # Esse parâmetro determina pro python quantos fiis ele vai analisar da lista
for i in range(0, max):
    url = "https://fiis.com.br/" + allTicker[i] + "/"
    wd_chrome.get(url)
    statement = []
    statement.append(allTicker[i])
    vp = wd_chrome.find_element(By.XPATH, "/html/body/div[4]/section[2]/div/table/tbody/tr/td[4]/h3[1]").get_attribute("textContent").replace('.', '').replace(',', '.').split('R$')
    statement.append(float(vp[1]))
    cot = wd_chrome.find_element(By.XPATH, "/html/body/div[4]/section[3]/div/div/div[3]/div/div[1]/span[2]").get_attribute("textContent").replace('.', '').replace(',', '.')
    statement.append(float(cot))
    pl = wd_chrome.find_element(By.XPATH, "/html/body/div[4]/section[2]/div[1]/table/tbody/tr/td[3]/h3[1]").get_attribute("textContent").split(' ')
    statement.append(pl[1])
    rend = wd_chrome.find_element(By.XPATH, "/html/body/div[4]/section[2]/div[1]/table/tbody/tr/td[2]/h3[1]").get_attribute("textContent").replace('.', '').replace(',', '.').split('R$')
    statement.append(float(rend[1]))
    dy = wd_chrome.find_element(By.XPATH, "/html/body/div[4]/section[2]/div[1]/table/tbody/tr/td[1]/h3[1]").get_attribute("textContent").split('%')
    statement.append(float(dy[0].replace(',', '.')))
    print('Dados Capturados - VP, Cot, PL, Dy')

    # Etapa 6
    print('Aplicando filtro em {}'.format(allTicker[i]))
    # VP > Cot
    condicao1 = statement[1] > statement[2]
    # PL > 1 Bi
    condicao2 = 'B' in statement[3]
    # Rend > 0,70 centavos
    condicao3 = statement[4] > 0.7
    # DY >= 0.6%
    condicao4 = statement[5] > 0.6
    filtro = condicao1 and condicao2 and condicao3 and condicao4
    print('Teste condicional aplicado')
    if filtro:
        funds.append(statement)
        print("FII selecionado: O FII que atende os requisitos é: {}".format(statement[0]))
    else:
        print('FII não atende requisitos!')

# Etapa 7
print(len(funds))
print(funds)
print('Tarefa executada com sucesso!')
