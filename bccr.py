from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from pathlib import Path
import os
import pandas as pd

REMOVE_ATTRIBUTES = ['rules', 'lang','language','onmouseover','onmouseout','script','style','font',
                        'dir','face','size','color','style','class','width','height','hspace',
                        'border','bordercolor','valign','align','background','bgcolor','text','link','vlink',
                        'alink','cellpadding','cellspacing']
user_home=str(Path.home())
options=webdriver.FirefoxOptions()
options.add_argument("--headless")
driver = webdriver.Firefox(options=options)
download_file=user_home+"/Downloads/resultado.xls"
if os.path.isfile(download_file):
   os.remove(download_file) 
try:
    driver.get("https://gee.bccr.fi.cr/IndicadoresEconomicos/Cuadros/frmConsultaTCVentanilla.aspx")
    driver.find_element(By.ID,"Button1").click()
    driver.quit()
except Exception as err:
    print("Something is wrong: "+ err)

if os.path.isfile(download_file):
    file=open(download_file, "r",encoding="ISO-8859-1")
    content=file.read()
    
webpage=BeautifulSoup(content,features="html.parser")
for attribute in REMOVE_ATTRIBUTES:
    for tag in webpage.find_all(attrs={attribute: True}):
        del tag[attribute]
dataFrame = pd.DataFrame(data = webpage)
print(dataFrame.to_string())
