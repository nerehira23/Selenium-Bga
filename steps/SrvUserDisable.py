import random
import time
from behave import given, when, then
from selenium import webdriver
from pom.SrvUserDisablePage import pomUserDisable
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains

@given('El usuario ingresa a la página web de Gananet')
def step_impl(context):
    context.driver = webdriver.Chrome() 
    context.driver.maximize_window()
    context.driver.get(pomUserDisable.url)

@when('El usuario selecciono el tipo de usuario Alias')
def step_impl(context):
    wait = WebDriverWait(context.driver, 10)
    iframe = wait.until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, pomUserDisable.iframe)))
    select_element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, pomUserDisable.selectTypeUser)))
    select = Select(select_element)
    select.select_by_visible_text(pomUserDisable.typeUserAlias)
    context.driver.switch_to.default_content()
    
    
@then('E ingreso el usuario ALIAS y hago clic en verificar')
def step_impl(context):
    wait = WebDriverWait(context.driver, 10)
    iframe = wait.until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, pomUserDisable.iframe)))

    input_element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, pomUserDisable.inputAlias)))
    input_element.clear()
    input_element.send_keys(pomUserDisable.txtAlias)
    
    button_element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, pomUserDisable.btnVerify)))
    context.driver.execute_script("arguments[0].click();", button_element)
    context.driver.switch_to.default_content()

@then('Obtiene un mensaje restrictivo')
def step_impl(context):
    wait = WebDriverWait(context.driver, 10)
    iframe = wait.until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, pomUserDisable.iframe)))
    msg_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, pomUserDisable.msgUserDisable))).text
    txt = 'Su usuario no se encuentra habilitado para el Servicio. Por favor contáctese con su Ejecutivo.'
    assert msg_element == txt, f"Actual text: '{msg_element}', Expected text: '{txt}'"
    context.driver.switch_to.default_content()
       
