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
            user.send_keys("Bob1423")# Galicia
            password =  self.driver.find_element_by_xpath("//input[contains(@type,'password')]")
            time.sleep(1)
            password.send_keys("kukumber") #S
            botton =  self.driver.find_element_by_xpath("//input[contains(@type,'submit')]")
            time.sleep(1)
            botton.click()
            time.sleep(3)
            modificarPerfil = self.driver.find_element_by_xpath("//span[contains(.,'Editar Perfil')]")
            modificarPerfil.click()
            time.sleep(4)
            nombresCampos = ['username','email','password1','password2','last_name','first_name']
            datos = ['Fossjblu','bobkakawate@gmail.com','Mamamia1423','Mamamia1423','Oviedo','Facundo']
            for nombre,dato in  zip(nombresCampos,datos):
                campos =  self.driver.find_element_by_xpath(f"//input[contains(@name,'{nombre}')]")
                time.sleep(1)
                campos.clear()
                campos.send_keys(dato)
            modificar = self.driver.find_element_by_xpath("//button[contains(.,'Enviar modificacion')]")
            modificar.click()
            time.sleep(3)
        except Exception as E:
            print(f"Error {E} al automatizar Prueba Revise Sus Xpath, oh los scripts")

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
        
        

    