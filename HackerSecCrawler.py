from selenium import webdriver

# Abre o arquivo com o script.
with open("script.js") as __file:
    javascript = __file.read()

# Executa o Chrome sem interface.
chrome_optioms = webdriver.ChromeOptions()
chrome_optioms.add_argument("--headless")

browser = webdriver.Chrome("chromedriver", options=chrome_optioms)

# Acessa a página.
browser.get("https://www.facebook.com/pg/hackersecbr/posts/")

# Executa um script JavaScript no navegador
# para pegar apenas as informações dos posts
# de boletim, retornando um array com cada boletim.
boletins = browser.execute_script(javascript)

# Fecha o navegador ao terminar
browser.quit()

for boletim in boletins:
    print("{}\n".format(boletim))