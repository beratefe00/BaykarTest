from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from webbrowser import Chrome
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.action_chains import ActionChains

import time
import pytest
import requests

PATH_TO_CHROMEDRIVER = r"C:\Users\kral1\Downloads\chromedriver-win64\chromedriver.exe"
driver = webdriver.Chrome(PATH_TO_CHROMEDRIVER)

#Baykar Kariyer websitesi
website_url = "https://kariyer.baykartech.com/" 
languages = ["EN", "TR"]

# Test Senaryoları için oluşturulan Class yapısı
class TestBaykarClass:
        
        # SetUp -> Her bir test senaryosu için baykar_webpage fonksiyonu otomatik olarak başlayacaktır.
        @pytest.fixture(autouse =True)
        def baykar_webpage(self):
            self.driver = driver
            self.driver.get(website_url)
            time.sleep(2)
            self.driver.maximize_window()
            time.sleep(2)
            
        
        @pytest.mark.navbar # Test senaryosunun ismi:navbar
        def test_navbar_elems_click_and_verify(self):
            self.bool_clickable = True # Menü elementlerinin tıklanılabilir olup olmadığını belirten boolean flag
            self.bool_page_correct = True # Tıklanılan sayfanın başarılı bir şekilde açılıp açılmadığını belirten flag
                                            # Status Code:200 olması başarılı bir şekilde sayfanın açıldığını belirtir.
                                                        
            self.initial_url = "https://kariyer.baykartech.com/tr/" # Test senaryolarında başlangıç URL'miz.
            
            for i in range(len(driver.find_elements(By.XPATH, "//nav//child::a"))):
                navbar_elems = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//nav//child::a")))
                navbar_elem = navbar_elems[i]
                try:
                    driver.execute_script("arguments[0].click();", navbar_elem) 
                    time.sleep(3.5)
                    self.bool_page_correct = self.check_http_status_code(self.driver.current_url)
                except Exception as e:
                    self.bool_clickable = False 
                
                self.test_flag = self.bool_clickable and self.bool_page_correct 
                assert self.test_flag == True, f"{navbar_elem.text} sayfasına tıklanamadı veya görüntülenemedi."

                if self.driver.current_url != self.initial_url:
                    self.driver.back()
                
                time.sleep(3.5)
                
        def check_http_status_code(self,url):
            self.resp = requests.get(url)
            return self.resp.status_code == 200
            
        
        def switch_language(self):
            # Dil değiştirme elementinin Xpath'ı ve elementin kendisi
            self.language_button_xpath = '//*[@id="home"]/nav/div/div[1]/ul/li[1]/a'
            self.language_button_elem  = self.driver.find_element(By.XPATH,self.language_button_xpath)

            
            # Eğer websitesi ilk açıldığında dil elementinin text'i 'EN' olarak gözüküyosa sitemiz Türkçedir. Çünkü 'EN' kutucuğuna
            #tıklayarak websitesini İngilizce yapacağımıza göre şimdiki dilimiz Türkçedir. 
            
            if self.language_button_elem.text == "EN":
                self.current_language = "Türkçe"
                
                #Dil değiştirme elementine tıkladıktan sonra dilimiz İngilizce olacaktır.
                WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(self.language_button_elem)).click()
                time.sleep(3.5)
                self.current_language = "İngilizce"
                
                #Sitenin dilinin İngilizce olduğunu doğrulamak için Baykar websitesinin sekme ismini (driver.title) ve 
                #URL'sini (driver.current_url) kontrol ediyoruz.
                
                self.driver_title = self.driver.title
                self.driver_url = self.driver.current_url 
                
                #İngilizce dil değiştirme bağlantısına tıkladıktan sonra Site title'ı Home Page kelimelerini içeriyorsa, URL'sinde 
                #'en' var ise ve site hata vermeden açılıyorsa test doğrulanmış olur. 
                
                assertion_flag = ("Home Page" in self.driver_title) and ("en" in self.driver_url) and (self.check_http_status_code(self.driver_url))
                assert assertion_flag == True 
            
            #Yukarıda bahsedilen durumların başlangıçta dilin Türkçe olduğu durumlar için gerekli olan kodu aşağıdaki gibidir.
            elif self.language_button_elem.text == "TR":
                self.current_language = "İngilizce"
                WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(self.language_button_elem)).click()
                time.sleep(3.5)
                self.current_language = "Türkçe"
                self.driver_title = self.driver.title 
                self.driver_url = self.driver.current_url
                assertion_flag = ("Ana Sayfa" in self.driver_title) and ("tr" in self.driver_url) and (self.check_http_status_code(self.driver_url))
                assert assertion_flag == True 
        
        @pytest.mark.language      
        def test_switching_language(self):
            # Dil'i 2 defa değiştirmek için 2 loop kullanıyorum. (Türkçe'den İngilizce'ye ve İngilizce'den Türkçeye)
            for i in range(2):
                self.switch_language()  
                
        
        def get_open_positions_elem(self):
            self.open_position_xpath = "/html/body/div[1]/a/button"
            self.open_positions_elem = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,self.open_position_xpath)))
            return self.open_positions_elem

        def click_open_positions(self):
            WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(self.get_open_positions_elem())).click()
                
        
        def clear_filters(self):
            self.clear_filter_xpath = "/html/body/div/div[2]/div/div/div[1]/div/div/div/div/div/form/div/a"
            self.clear_filter_elem = self.driver.find_element(By.XPATH,self.clear_filter_xpath)
            WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(self.clear_filter_elem)).click()
            time.sleep(2.5)
        
        def filter_units(self,unit_name):
            self.clear_filters()
            self.unit_filter_xpath = f"//input[@value='{unit_name}']"   
            self.unit_filter_elem = self.driver.find_element(By.XPATH,self.unit_filter_xpath)
            WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(self.unit_filter_elem)).click()
            time.sleep(2.5)   
         
            
        def search_positions(self,position_name):
            self.search_input_xpath = '//*[@id="myInput"]'
            self.search_input_elem = self.driver.find_element(By.XPATH,self.search_input_xpath)
            self.search_input_elem.clear()
            self.search_input_elem.send_keys(position_name)
            time.sleep(2)
            
        
            
        
        def verify_position_results(self,searched_position):
            self.all_positions_xpath = '//li[@class="liProgram"]//a'
            self.all_positions_elems = self.driver.find_elements(By.XPATH,self.all_positions_xpath)
            for position_result in self.all_positions_elems:
                assert searched_position.lower() in position_result.text.lower()
                
        def filter_and_search_positions(self,position_data):
            self.unit_to_filter = position_data["unit_to_filter"]
            self.position_to_search = position_data["position_to_search"]
            self.filter_units(self.unit_to_filter)
            self.search_positions(self.position_to_search)
            self.verify_position_results(self.position_to_search)
        
        @pytest.mark.search_and_filter    
        @pytest.mark.parametrize("position_data",[
            {"unit_to_filter":"Elektronik Sistem Geliştirme","position_to_search":"Donanım"},
            {"unit_to_filter":"Web Yazılım Teknolojileri", "position_to_search":"Uzman"},
            {"unit_to_filter":"Hafif Platformlar","position_to_search": "Uçuş"}
            
        ])
        
        def test_position_filtering_and_search_data_driven(self,position_data):
            self.click_open_positions()
            time.sleep(3)
            self.filter_and_search_positions(position_data)
            time.sleep(1.5)
        
            
            
                
            
            
                   
        

                



    