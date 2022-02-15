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
            span_Agregar_Foto = self.driver.find_element_by_xpath("//span[contains(.,'Agregar Foto')]")
            span_Agregar_Foto.click()
            time.sleep(4)
            campos = self.driver.find_element_by_xpath("//input[contains(@name,'user')]")
            time.sleep(1)
            campos.send_keys('foviedo')
            campos =  self.driver.find_element_by_xpath("//input[contains(@name,'imagen')]")
            time.sleep(1)
            campos.send_keys('C:/Users/foviedo/Desktop/ProyectoFinal/blogPortafolios/media/img_avatar/Avatar_Goku2_.jpg')
            modificar = self.driver.find_element_by_xpath("//button[contains(.,'Enviar foto')]")
            modificar.click()
            time.sleep(3)
        except Exception as E:
            print(f"Error {E} al automatizar Prueba Revise Sus Xpath, oh los scripts")

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
        
        

    