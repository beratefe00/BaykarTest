# Baykar Web Yazılım Test Uzmanı Pozisyonu İçin Hazırlanan Dökümantasyon
**Amaç:** Bu projede ilk olarak Baykar Kariyer websitesi için manuel testler için test senaryolarının ve test caselerin oluşturulması, bunların dökümantasyon haline getirilmesi, daha sonra
Python programlama dili kullanarak test otomasyon işleminin kullanılması amaçlanmıştır.<br><br>
**İçerik:**  
1. **Manuel test dökümü**: Baykar Kariyer websitesi için manuel test senaryoları, test caseleri ayrıntılı olarak yazılmış ve markdown dosyası olarak sunulmuştur.
    Manuel test dökümünde toplamda **9** adet test senaryosu ve **42** adet test case yer almaktadır. İlgili manuel test dökümantasyonuna [Manuel Test](https://github.com/beratefe00/BaykarTest/blob/main/baykar_test_documentation.md) kısmından ulaşabilirsiniz.
    Test senaryoları ve test caseler için
      - Test Senaryo İsmi
      - Test Senaryo ID
      - Test Case ID
      - Amaç
      - Ön Koşullar
      - Test Adımları
      - Fail Criteria
      - Beklenen Sonuçlar
    şeklindeki tanımlamalar olabildiğince detaylı olarak aktarılmıştır.<br><br>

2. **Test Otomasyon İşleminin Uygulanması**: Baykar Kariyer websitesi için test otomasyon işlemi Python programala diliyle yazılmıştır. Web otomasyon aracı olarak Selenium, unit test işlemleri için PyTest
   framework'ü kullanılmıştır. Toplamda 3 adet test senaryosu için test scriptleri yazılmıştır. İlgili scripte [Python Automation](https://github.com/beratefe00/BaykarTest/blob/main/baykar_test_automation_final.py) ulaşabilirsiniz.<br><br>
   **Gereksinimler:**
     - **Python**
     - **Google Chrome**
     - **ChromeDriver**(Google Chrome versiyonu ile uyumlu)
     - **Selenium**:
        ```
        pip install selenium
        ```
     - **WebDriver Manager**:
       ```
        pip install webdriver_manager
       ```
     - **Pytest**
       ```
       pip install pytest
       ```
     - **Requests**
       ```
       pip install requests

    **İlgili Notlar:**<br><br>
       - Testi çalıştırmak için test otomasyon Python dosyasında yer alan **PATH_TO_CHROMEDRIVER** adlı değişken ChromeDriver'ın PATH'ini belirtir.**PATH_TO_CHROMEDRIVER** değişkenini ChromeDriver dosyasınızın bulunduğu erişim yolu(path) ile değiştirmeniz gerekmektedir. <br><br>
       - Sadece **1**.**Test senaryosunu(Ziyaretçi Baykartech sitesindeki bütün navbar elementlerine tıklayabilmeli ve sayfa sorunsuz açılmalı)** çalıştırmak için ekran konsoluna **pytest -v -m navbar baykar_test_automation_final.py** yazmanız yeterli olacaktır.<br><br>
       - Sadece **2**.**Test senaryosunu(Ziyaretçi Baykartech sitesinde sağlanan diller arasında geçiş yapabilmeli, doğru dil gösterilmeli.)** çalıştırmak için ekran konsoluna **pytest -v -m language baykar_test_automation_final.py** yazmanız yeterli olacaktır.<br><br>
       - Sadece **3**.**Test senaryosunu(Ziyaretçi/Kullanıcı kariyer.baykartech sitesinde açık pozisyonlarda birim filtreleme ve pozisyon arama yapabilmeli. Data-Driven kullanımına dikkat edilmelidir)** çalıştırmak için ekran konsoluna **pytest -v -m search_and_filter baykar_test_automation_final.py** yazmanız yeterli olacaktır<br><br>
       - Tüm test senaryolarını sırasıyla çalıştırmak için **pytest -v baykar_test_automation_final.py** yazabilirsiniz.<br><br>

3. **Performans/Yük Testinin Uygulanması:**: Python Locust modülü kullanarak Baykar Kariyer web sayfasında performans/yük testleri uygulanmıştır. Performans/yük test senaryolarının az sayıda oluşturulmasının sebebi test sırasında Baykar Kariyer websitesine çok sayıda request iletildiği için erişimin engellenmesi dolayısıyla test yapılamamasıdır. İlgili engellenme durumuna ait ekran görüntüleri ve Locust test raporu [Locust Dosyaları](https://github.com/beratefe00/BaykarTest/tree/main/LocustDosyalar%C4%B1) adlı bölümde yer almaktadır. Aynı zamanda ilgili Python koduna [Locust Python](https://github.com/beratefe00/BaykarTest/blob/main/baykar_load_test.py) linkinden erişim sağlayabilirsiniz.
       
   
      
           
