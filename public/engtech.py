from time import sleep
from selenium import webdriver
from whatsapp_api import WhatsApp
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
wp = WhatsApp()

input("pressione ENTER após executar qrcode para executar o robô\n")

wp.search_contact('nicolyvas')
wp.send_message('hello')
wp.send_message(wp.get_last_message())

sleep(10)
wp.driver.close()