from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# Parameters
WP_LINK = 'https://web.whatsapp.com'

class WhatsApp:
    def __init__(self):
        self.driver = self._setup_driver()
        self.driver.get(WP_LINK)
        print("scan qr code")

    @staticmethod
    def _setup_driver():
        print('Loading...')
        chrome_options = Options()
        chrome_options.add_argument("disable-infobars")
        driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)
        return driver

    def _get_element(self, xpath, attempts=5, _count=0):
        '''Safe get_element method with multiple attempts'''
        try:
            element = self.driver.find_element(By.XPATH, xpath)
            #print('Found element!')
            return element
        except Exception as e:
            if _count<attempts:
                sleep(1)
                #print(f'Attempt {_count}')
                self._get_element(xpath, attempts=attempts, _count=_count+1)
            else:
                print("Element not found")

    def _click(self, xpath):
        el = self._get_element(xpath)
        el.click()

    def _send_keys(self, xpath, message):
        el = self._get_element(xpath)
        el.send_keys(message)

    def write_message(self, message):
        '''Write message in the text box but not send it'''
        self._click(MESSAGE_BOX)
        self._send_keys(MESSAGE_BOX, message)

    def _paste(self):
        el = self._get_element(MESSAGE_BOX)
        el.send_keys(Keys.SHIFT, Keys.INSERT)

    def send_message(self, message):
        '''Write and send message'''
        self.write_message(message)
        self._click(SEND)

    def get_group_numbers(self):
        '''Get phone numbers from a whatsapp group'''
        try:
            el = self.driver.find_element(By.XPATH, CONTACTS)
            return el.text.split(',')
        except Exception as e:
            print("Group header not found")

    def search_contact(self, keyword):
        '''Write and send message'''
        self._click(NEW_CHAT)
        self._send_keys(NEW_CHAT, keyword)
        sleep(1)
        try:
            self._click(FIRST_CONTACT)
        except Exception as e:
            print("Contact not found")
            
    def get_all_messages(self):
        '''Get all messages from the chat'''
        all_messages_element = self.driver.find_elements(By.CLASS_NAME, '_akbu')
        all_messages_text = [e.text for e in all_messages_element]
        return all_messages_text
        
    def get_last_message(self):
        '''Get last message from the chat'''
        all_messages = self.get_all_messages()
        print("return debug all: " + str(all_messages))
        print("return debug last one: " + str(all_messages[-1]))
        return str(all_messages[-1])

    def get_actual_username(self):
        from selenium.webdriver.common.by import By
        current_user_element = self.driver.find_element(By.XPATH, '//*[@id="main"]/header/div[2]/div[1]/div/div/span[1]')
        current_user_text = current_user_element.text

    