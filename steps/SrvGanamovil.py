import random
import time
from behave import given, when, then
from selenium import webdriver
from pom.SrvGanaMovilPage import pomGanamovil
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given('El usuario ingresa al portal web www.bg.com.bo')
def step_impl(context):
    context.driver = webdriver.Chrome() 
    context.driver.maximize_window()
    context.driver.get(pomGanamovil.url)

@when('Ingresa al menú SERVICIOS, GanaMóvil, Funcionalidades')
def step_impl(context):
    #Ganamovil
    search_button = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, pomGanamovil.targetGanamovil))
    )
    search_button.click()
    #Funcionalidades
    search_button = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, pomGanamovil.menuFuncionalidades))
    )
    search_button.click()
    
@then('Obtiene listado donde se encuentra las funcionalidades')
def step_impl(context):

    random_number = random.randint(0, len(pomGanamovil.listOptions) - 1)
    xpath = '//a[@target="_blank"][contains(text(),"' + pomGanamovil.listOptions[random_number] + '")]'
    search_button = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, xpath))
    )
    search_button.click()
    

    

    
