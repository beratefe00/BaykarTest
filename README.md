# Baykar Web Yazılım Test Uzmanı Pozisyonu İçin Hazırlanan Dökümantasyon
**Amaç:** Bu projede ilk olarak Baykar Kariyer websitesi için manuel testler için test senaryolarının ve test caselerin oluşturulması, bunların dökümantasyon haline getirilmesi, daha sonra
Python programlama dili kullanarak test otomasyon işleminin kullanılması amaçlanmıştır.<br><br>
**İçerik:**  
1. **Manuel test dökümü**: Baykar Kariyer websitesi için manuel test senaryoları, test caseleri ayrıntılı olarak yazılmış ve markdown dosyası olarak sunulmuştur.
    Manuel test dökümünde toplamda **9** adet test senaryosu ve **42** adet test case yer almaktadır.
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
      
           
