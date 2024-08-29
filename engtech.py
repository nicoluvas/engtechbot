from time import sleep
from selenium import webdriver
from whatsapp_api import WhatsApp
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
wp = WhatsApp()

input("pressione enter após executar qrcode")
wp.search_contact('nicolyvas')
wp.send_message('hello')

sleep(10)
wp.driver.close()