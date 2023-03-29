
# Pacotes
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service

print('Pacotes OK')

# Configurando o Driver
service = Service(r'C:\Program Files\Mozilla Firefox\geckodriver.exe')
options = Options()
options.add_argument('--headless')
driver = webdriver.Firefox(service=service, options=options)
print('Driver OK')

# Listando FIIs
url = "https://fiis.com.br/lista-de-fundos-imobiliarios/"
driver.get(url)
print('URL configurada')
allTicker = []
getTicker = driver.find_elements(By.CLASS_NAME, "tickerBox__title")
for ticker in getTicker:
    allTicker.append(ticker.text)
print('Lista de FIIs OK')

# Filtro
funds = []
maximo = len(allTicker)
for i in range(0, maximo):
    url = "https://fiis.com.br/" + allTicker[i] + "/"
    driver.get(url)
    statement = [allTicker[i]]
    valor_patrimonial = driver.find_element(by=By.XPATH, value="//*[@id=\"carbon_fields_fiis_quotations_chart-2\"]/div[2]/div[3]/p[1]/b").get_attribute('innerText').replace('.', '').replace(',', '.')
    statement.append(float(valor_patrimonial))
    cotacao = driver.find_element(by=By.XPATH, value="//*[@id=\"carbon_fields_fiis_quotations_chart-2\"]/div[1]/div[2]/div[1]/div[1]/span[2]").get_attribute("textContent").replace('.', '').replace(',', '.')
    statement.append(float(cotacao))
    patrimonio_liquido = driver.find_element(by=By.XPATH, value="//*[@id=\"carbon_fields_fiis_header-2\"]/div/div/div[1]/div[2]/div/div[3]/p[1]/b").get_attribute("textContent").split(' ')
    statement.append(patrimonio_liquido[0])
    rendimento = driver.find_element(by=By.XPATH, value="//*[@id=\"carbon_fields_fiis_header-2\"]/div/div/div[1]/div[2]/div/div[2]/p[1]/b").get_attribute("textContent").replace('.', '').replace(',', '.')
    statement.append(float(rendimento))
    dividend_yield = driver.find_element(By.XPATH, "//*[@id=\"carbon_fields_fiis_header-2\"]/div/div/div[1]/div[2]/div/div[1]/p[1]/b").get_attribute("textContent").replace('.', '').replace(',', '.')
    statement.append(float(dividend_yield))
    print('Dados Capturados - Valor Patrimonial, Cotação, Patrimônio Líquido, Dividend Yield')

    # Seleção de FIIs
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

# Apresentação
print(len(funds))
print(funds)
print('Tarefa executada com sucesso!')
