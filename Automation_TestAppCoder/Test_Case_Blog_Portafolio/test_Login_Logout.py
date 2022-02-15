import unittest
from selenium import webdriver
import time

class TesteLoginApp_Codeer(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = "chromedriver/chromedriver.exe")

    def test_login_logout(self):
        try:
            self.driver.get("http://127.0.0.1:8000/Blog/login_requests/")
            time.sleep(1)
            user =  self.driver.find_element_by_xpath("//input[contains(@type,'text')]")
            time.sleep(1)
            user.send_keys("foviedo")
            password =  self.driver.find_element_by_xpath("//input[contains(@type,'password')]")
            time.sleep(1)
            password.send_keys("Mamamia1423")
            botton =  self.driver.find_element_by_xpath("//input[contains(@type,'submit')]")
            time.sleep(1)
            botton.click()
            time.sleep(3)
            logout =  self.driver.find_element_by_xpath("//span[contains(.,'Logout')]")
            time.sleep(1)
            logout.click()
            returnLogin = self.driver.find_element_by_xpath("//button[contains(.,'Volver a Iniciar sesion')]")
            time.sleep(2)
            returnLogin.click()
            time.sleep(5)
        except Exception as E:
            print(f"Error {E} al automatizar Prueba Revise Sus Xpath, oh los comandos")

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
        
        

    