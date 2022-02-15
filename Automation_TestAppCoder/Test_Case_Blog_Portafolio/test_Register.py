import unittest
from selenium import webdriver
import time

class TesteLoginApp_Codeer(unittest.TestCase):
    def setUp(self):
        path = "blogPortafolios\Automation_TestAppCoder\chromedriver\chromedriver.exe"
        self.driver = webdriver.Chrome(executable_path = path)

    def test_login_logout(self):
        try:
            self.driver.get("http://127.0.0.1:8000/Blog/login_requests/")
            register = self.driver.find_element_by_xpath("//a[contains(.,'¿Aun No estas Registrado?')]")
            register.click()
            time.sleep(1)
            datos = ["GOKU","pepe@gmail.com","Goku123456","Goku123456"]
            nombres = ["username","email","password1","password2"]
            for n,d in zip(nombres,datos):
                campo =  self.driver.find_element_by_xpath(f"//input[contains(@name,'{n}')]")
                time.sleep(1)
                campo.send_keys(d)
            botton =  self.driver.find_element_by_xpath("//button[@type='submit'][contains(.,'Registrar')]")
            time.sleep(1)
            botton.click()
            time.sleep(3)
        except Exception as E:
            print(f"Error {E} al automatizar Prueba Revise Sus Xpath, oh los comandos")

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
        
        

    