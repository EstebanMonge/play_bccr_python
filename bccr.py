from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from pathlib import Path
import os
import pandas as pd

REMOVE_ATTRIBUTES = ['rules', 'lang','language','onmouseover','onmouseout','script','style','font',
                        'dir','face','size','color','style','class','width','height','hspace',
                        'border','bordercolor','valign','align','background','bgcolor','text','link','vlink',
                        'alink','cellpadding','cellspacing','title', 'id']
user_home=str(Path.home())
options=webdriver.FirefoxOptions()
options.add_argument("--headless")
#driver=webdriver.Firefox(options=options)
download_file=user_home+"/Downloads/resultado.xls"
#if os.path.isfile(download_file):
#   os.remove(download_file) 
#try:
#    driver.get("https://gee.bccr.fi.cr/IndicadoresEconomicos/Cuadros/frmConsultaTCVentanilla.aspx")
#    driver.find_element(By.ID,"Button1").click()
#    driver.quit()
#except Exception as err:
#    print("Something is wrong: "+ err)

if os.path.isfile(download_file):
    file=open(download_file, "r",encoding="ISO-8859-1")
    content=file.read()
    content=content.replace('\n','')
webpage=BeautifulSoup(content,"html.parser")
for attribute in REMOVE_ATTRIBUTES:
    for tag in webpage.find_all(attrs={attribute: True}):
        del tag[attribute]
for td in webpage.find_all('td'):
    td.string=td.get_text().strip()
for table in webpage.find_all('table'):
    webtable=table
webtable=str(webtable)
dataFrames=pd.read_html(webtable)
dataFrame=dataFrames[0]
dataFrame.columns = dataFrame.iloc[0]
dataFrame.drop([0],inplace=True)
dataFrame.drop([len(dataFrame)],inplace=True)
tipo_entidad=''
for ind in dataFrame.index:
    if pd.isna(dataFrame['Tipo de Entidad'][ind]):
        dataFrame['Tipo de Entidad'][ind]=tipo_entidad
    else:
        tipo_entidad=dataFrame['Tipo de Entidad'][ind]
print(dataFrame)
dataFrame.to_csv('caca.csv')
