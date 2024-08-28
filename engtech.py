from time import sleep
from whatsapp_api import WhatsApp
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
wp = WhatsApp()

input("pressione enter após executar qrcode")

sleep(10)
wp.driver.close()