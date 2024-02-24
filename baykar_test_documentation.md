# Baykar Kariyer Web Sitesi Manuel Test Dökümantasyonu #

1.Test Senaryo İsmi: Menü Elementlerinin Tıklanılabilirliğini ve İçeriğini Doğrula<br>
- Test Senaryo ID: TS001
- Amaç: Kullanıcının, Baykar Kariyer websitesinde yer alan menü elementlerinin tümüne tıklayabildiğini ve istenilen ekranı görüntüleyebildiğini doğrulamak.
- Ön koşullar: Baykar Kariyer websitesi erişilebilir olmalıdır ve kullanıcının geçerli bir internet bağlantısı bulunmaktadır.
- Testin Adımları:
    - Baykar Kariyer websitesini görüntüle.
    - Menüde yer alan tüm elementlere(Baykar Logosu,Kariyer,Açık Pozisyonlar,Staj,S.S.S,EN,Dashboard,vb.) tıkla.
    - Menüde yer alan tüm elementlerin herhangi bir hata vermeden tıklanılabilir olduğundan emin ol.
    - Açılan sayfalardaki web içeriklerinin menüdeki başlıklarla ilgili olduğunu doğrula.

- Fail Criteria: 
    - 1. Menü elementlerinden herhangi birinin tıklanamaması
    - 2. Tıklanılan menü elementlerinden herhangi birinin içeriğinin ilgili menü kategorisiyle eşleşmemesi

- Beklenen Sonuçlar: Kullanıcı, Baykar Kariyer websitesinde gezinme menüsünde yer alan elementleri tıklayabilmekte ve açılan sayfalarda ilgili menülere ait içeriklerle karşılaşmaktadır.

- Test Case ID: TC001 - Baykar Logosunun Tıklanabilirliği ve İçeriği
    - Amaç: Kullanıcının, gezinme menüsünde yer alan Baykar logosunun tıklayabildiğini ve tıkladıktan sonra anasayfayı görüntüleyebildiğini doğrulamak.

    - Testin adımları:
        - Baykar Kariyer websitesini görüntüle.
        - Baykar Kariyer websitesinde yer alan Baykar logosunun tıklanabilirliğini doğrula.
        - Baykar logosuna tıkladıktan sonra Baykar Kariyer websitesinin anasayfasına yönlendirildiğini doğrula. 

    - Fail Criteria: 
        - Gezinme menüsünde yer alan Baykar Logosu tıklanamamaktadır.
        - Gezinme menüsünde yer alan Baykar logosu kullanıcıyı anasayfaya yönlendirmemektedir.

    - Beklenen Sonuçlar: Kullanıcı, gezinme menüsünde yer alan Baykar logosuna başarılı bir şekilde tıklayabilmiş ve tıkladıktan sonra anasayfaya başarılı bir şekilde yönlendirilmiştir.

- Test Case ID: TC002 - Kariyer Menüsünün Tıklanabilirliği ve İçeriği 
    - Amaç: Kullanıcının gezinme menüsünde yer alan "Kariyer" isimli elemente tıklayabildiğini ve aşağı açılan menüden(drop-down menu) ilgili sayfaları başarıyla görüntüleyebildiğini doğrulamak.
    - Testin Adımları:
        - Baykar Kariyer websitesini görüntüle.
        - Gezinme menüsünden "Kariyer" isimli menünün tıklanılabilirliğini doğrula.
        - Aşağı doğru açılan menüden(drop-down) ilgili sayfaların(İstatistik,Yerleşkelerimiz,Sunduğumuz Faydalar,Sosyal Alanlar) tıklanılabilirliğini doğrula ve kullanıcının ilgili sayfayı görüntülediğinden emin ol.

    - Fail Criteria: 
        - Gezinme menüsünden "Kariyer" isimli bölüme tıklanılamaması
        - Gezinme menüsünden "Kariyer" isimli bölüme tıklandıktan sonra aşağı doğru açılan menüde(drop-down menu) ilgili sayfalara(İstatistik,Yerleşkelerimiz,Sunduğumuz Faydalar,Sosyal Alanlar) tıklanılamaması
        - Gezinme menüsünden "Kariyer" isimli bölüme tıklandıktan sonra aşağı doğru açılan menüde(drop-down menu) tıklanılan sayfaların içeriklerinin menü içerikleriyle uyuşmaması 
    - Beklenen Sonuç: Kullanıcı, gezinme menüsünde yer alan "Kariyer" isimli bölüme tıklayabilmiş ve aşağı doğru açılan menüde ilgili sayfalara başarıyla tıklayabilmiş ve sayfa içeriklerinin menü içerikleriyle uyuştuğunu görmüştür.

- Test Case ID: TC003- Açık Pozisyonlar Menüsünün Tıklanabilirliği ve İçeriği 
    - Amaç: Kullanıcının Baykar Kariyer websitesi üzerinde gezinme menüsünde yer alan "Açık Pozisyonlar" adlı bağlantıya tıklayabildiğini ve ilgili açık pozisyonlara ait içerikleri görüntüleyebildiğini doğrulamak. 
    - Test Adımları:
        - Baykar Kariyer web sitesini görüntüle.
        - Gezinme menüsünde yer alan "Açık Pozisyonlar" adlı kısmın tıklanabilirliğini doğrula.
        - "Açık Pozisyonlar" kısmına tıkladıktan sonra Baykar şirketinde yer alan açık pozisyonlar listesini görüntüleyebildiğini doğrula. 
    
    - Fail Criteria: 
        - Kulanıcının gezinme menüsünde yer alan "Açık Pozisyonlar" kısma tıklayamaması
        - Kullanıcının "Açık Pozisyonlar" kısmına tıkladıktan sonra Baykar şirketinde yer alan açık pozisyonları görüntüleyememesi 
    
    - Beklenen Sonuç: Kullanıcı, Baykar Kariyer websitesinde gezinme menüsünde yer alan "Açık Pozisyonlar" adlı bağlantıya tıklayabilmiş ve Baykar'da halihazırda bulunan açık pozisyonları görüntüleyebilmiştir. 

- Test Case ID: TC004-Staj Menüsünün Tıklanabilirliği ve İçeriği
    - Amaç: Kullanıcının gezinme menüsünde yer alan "STAJ" isimli elemente tıklayabildiğini ve aşağı açılan menüden(drop-down menu) ilgili sayfaları başarıyla görüntüleyebildiğini doğrulamak.
    - Testin Adımları:
        - Baykar Kariyer websitesini görüntüle.
        - Gezinme menüsünden "STAJ" isimli menünün tıklanılabilirliğini doğrula.
        - Aşağı doğru açılan menüden(drop-down) ilgili sayfaların(Staj Dönemleri,Staj Takvimi, Staj SSS) tıklanılabilirliğini doğrula ve kullanıcının ilgili sayfayı görüntülediğinden emin ol.
    - Fail Criteria: 
        - Gezinme menüsünden "STAJ" isimli bölüme tıklanılamaması.
        - Gezinme menüsünden "STAJ" isimli bölüme tıklandıktan sonra aşağı doğru açılan menüde(drop-down menu) ilgili sayfalara(Staj Dönemleri,Staj Takvimi,Staj SSS) tıklanılamaması.
        - Gezinme menüsünden "STAJ" isimli bölüme tıklandıktan sonra aşağı doğru açılan menüde(drop-down menu) tıklanılan sayfaların içeriklerinin menü içerikleriyle uyuşmaması.
    - Beklenen Sonuç: Kullanıcı, gezinme menüsünde yer alan "STAJ" isimli bölüme tıklayabilmiş ve aşağı doğru açılan menüde ilgili sayfalara başarıyla tıklayabilmiş ve sayfa içeriklerinin menü içerikleriyle uyuştuğunu görmüştür.
- Test Case ID: TC005- S.S.S Menüsünün Tıklanılabilirliği ve İçeriği
    - Amaç: Kullanıcının Baykar Kariyer websitesinde gezinme menüsünde yer alan S.S.S adlı bölüme tıklayabildiğini ve ilgili yere tıkladıktan sonra Baykar şirketine üyeler/kullanıcılar tarafından sıkça sorulan soruları ve Baykar şirketine özel bir mesaj atabilmek için oluşturulan İletişim formunu görüntüleyebildiğini doğrulamak. 
    - Test Adımları:
        - Baykar Kariyer websitesini görüntüle.
        - Gezinme menüsünde yer alan S.S.S adlı bağlantının tıklanılabilirliğini doğrula.
        - Gezinme menüsünde yer alan S.S.S adlı bağlantıya tıkladıktan sonra sıkça sorulan sorulara ve iletişim formuna erişimi doğrula. 
    
    - Fail Criteria: 
        - Gezinme menüsünde yer alan S.S.S adlı bağlantının tıklanılamaması
        - Gezinme menüsünde yer alan S.S.S adlı bağlantıya tıkladıktan sonra sıkça sorulan soruların ve iletişim formunun görüntülenmemesi 

    - Beklenen Sonuç: Kullanıcı, Baykar Kariyer websitesinde gezinme menüsünde S.S.S adlı bağlantıya tıklayabilmiş ve Baykar şirketine üyeler/kullanıcılar tarafından sıkça sorulan soruları ve Baykar şirketine özel bir mesaj göndermek için oluşturulan iletişim formunu görüntüleyebilmiştir.
- Test Case ID: TC006 - "BAYKAR" Bağlantısının Tıklanılabilirliği ve İçeriği
    - Amaç: Kullanıcın Baykar Kariyer websitesinde gezinme menüsü üzerinde bulunan "BAYKAR" adlı bağlantının tıklanılabilirliğini doğrulamak ve tıklandıktan sonra kullanıcının Baykar websitesinin anasayfasına yönlendirildiğinden emin olmak. 
    - Test Adımları:
        - Baykar Kariyer websitesini görüntüle.
        - Gezinme menüsünde yer alan "BAYKAR" adlı bağlantının tıklanabililr olduğunu doğrula.
        - "BAYKAR" adlı bağlantıya tıkladıktan sonra Baykar websitesinin anasayfasına yönlendirildiğinden emin ol.
    
    - Fail Criteria:
        - Gezinme menüsünde yer alan "BAYKAR" adlı bağlantının tıklanılamaması 
        - "BAYKAR" adlı bağlantıya tıkladıktan sonra kullanıcının Baykar websitesinin anasayfası yerine farklı bir adrese yönlendirilmesi 
    
    - Beklenen Sonuç: Kullanıcı, Baykar Kariyer websitesinde gezinme menüsü üzerinde yer alan "BAYKAR" adlı bağlantıya tıklayabilmiş ve Baykar websitesinin anasayfasına başarıyla yönlendirilmiştir. 

- Test Case ID: TC007 - "EN" Bağlantısının Tıklanılabilirliği ve İçeriği 
    - Amaç: Kullanıcının Baykar Kariyer websitesinde gezinme menüsü üzerinde yer alan "EN" isimli bağlantıya tıklayabildiğini doğrulamak ve tıkladıktan sonra Baykar Kariyer websitesinin İngilizce dil versiyonunu görüntülediğinden emin olmak. 
    - Test Adımları:
        - Baykar Kariyer websitesini görüntüle.
        - Baykar Kariyer websitesinde gezinme menüsünde yer alan "EN" adlı bağlantının tıklanılabilir olduğunu doğrula.
        - İlgili "EN" bağlantısına tıkladıktan sonra Baykar Kariyer websitesinin içeriğinin İngilizce olduğundan emin ol.

    - Fail Criteria: 
        - Gezinme menüsü üzerinde bulunan "EN" adlı bağlantıya tıklanılamaması 
        - Gezinme menüsü üzerinde bulunan "EN" adlı bağlantıya tıkladıktan sonra Baykar Kariyer websitesinin İngilizce dil versiyonunun görüntülenememesi
    
    - Beklenen Sonuç: Kullanıcı, Baykar Kariyer websitesinde gezinme menüsünde yer alan "EN" adlı bağlantıya başarıyla tıklayabilmiş ve Baykar Kariyer websitesinin İngilizce versiyonunu görüntüleyebilmiştir. 

- Test Case ID: TC008 - "GİRİŞ" Bağlantısının Tıklanılabilirliği ve İçeriği
    - Amaç: Kullanıcının Baykar Kariyer websitesinde gezinme menüsü üzerinde yer alan "GİRİŞ" adlı bağlantıya tıklayabildiğini doğrulamak ve tıkladıktan sonra Baykar Kariyer platformuna giriş yapacağı veya hesap oluşturacağı ekranı görüntüleyebildiğinden emin olmak. 

    - Testin Adımları:
        - Baykar Kariyer websitesini görüntüle.
        - Gezinme menüsü üzerinde yer alan "GİRİŞ" adlı bağlantının tıklanılabilir olduğunu doğrula.
        - "GİRİŞ" adlı bağlantıya tıkladıktan sonra Bayker Kariyer platformuna giriş yapabileceğin veya kayıt olabileceğin ekranı görüntüleyebildiğini doğrula. 
    
    - Fail Criteria: 
        - Gezinme menüsü üzerinde yer alan "GİRİŞ" adlı bağlantıya tıklanılamamasaı 
        - Gezinme menüsü üzerinde yer alan "GİRİŞ" adlı bağlantıya tıkladıktan sonra Baykar Kariyer platformuna giriş yapabileceğin veya kayıt olabileceğin ekranın görüntülenememesi 
    
    - Beklenen Sonuç: Kullanıcı, Baykar Kariyer websitesinde gezinme menüsünde yer alan "GİRİŞ" adlı bağlantıya tıklayabilmiş ve Baykar Kariyer Platformuna kayıt olabileceği veya giriş yapabileceği ekranı görüntüleyebilmiştir. 




<br><br><br>

2.Test Senaryo İsmi: Sayfalar Arasında Tutarlı Bir Gezinme Menüsünün Varlığını ve İşlevini Doğrulamak<br>
- Test Senaryo ID: TS002
- Amaç: Kullanıcının Baykar Kariyer websitesinde farklı sayfalar arasında gezinirken, gezinme menüsünü(Baykar Logosu,Kariyer,Açık Pozisyonlar,Staj,S.S.S,EN,Dashboard,vb.) tutarlı ve düzgün bir şekilde sayfasın üst bölümünde gördüğünü doğrulamak.
- Ön Koşullar: Baykar Kariyer websitesi erişilebilir olmalıdır ve kullanıcının geçerli bir internet bağlantısı bulunmaktadır.
- Testin Adımları:
    - Baykar Kariyer websitesini görüntüle.
    - Baykar Kariyer anasayfasından farklı bir sayfayı,örneğin "Staj Dönemleri" görüntüle. 
    - Açılan sayfada gezinme menüsünün varlığını ekranın üst bölümünde doğrula.
    - Gezinme menüsünün tıklanabilirliğini ve içeriğini (ref: TS001) doğrula.
    - Açılan sayfalardaki web içeriklerinin menüdeki başlıklarla ilgili olduğunu doğrula.

- Fail Criteria: 
    1. Baykar Kariyer anasayfasından farklı bir sayfayı açan kullanıcının gezinme menüsünü ekranın üst bölümünde görememesi
    2. Gezinme menüsünün tıklanabilirliğinin ve işlevinin doğrulanamaması 

- Beklenen Sonuç: Kullanıcı, anasayfadan farklı sayfalar arasında gezinirken tutarlı bir şekilde gezinme menüsünü ekranın üst tarafında görebilmiş, gezinme menüsündeki elementlere tıklayabilmiş ve ilgili sayfaları görüntüleyebilmiştir.



<br><br><br>

3.Test Senaryo İsmi: Kullanıcı Giriş İşlevini Kontrol Et 
- Test Senaryo ID: TS003
- Amaç: Kullanıcının "GİRİŞ" bağlantısına tıkladıktan sonra açılan ekranda E-Posta ve Şifre gibi bilgilerini doğru bir şekilde girdikten sonra başarılı bir şekilde Baykar Kariyer platformuna giriş yapabilmesini doğrulamak. Aynı zamanda yanlış E-posta ve/veya şifre girildiği durumlarda sistemin tepkisini test etmek. 

- Ön Koşullar: Baykar Kariyer websitesi erişilebilir olmalıdır ve kullanıcının geçerli bir internet bağlantısı bulunmaktadır.
- Testin Adımları:
    - Baykar Kariyer websitesini görüntüle.
    - Gezinme menüsü üzerinde "GİRİŞ" bağlantısına tıkla. 
    - Giriş işlemi için açılan ekranda E-Posta ve Şifre kısımlarını uygun bir şekilde doldurup "Ben Robot Değilim" seçeneğini işaretle.
    - GİRİŞ butonuna tıkla. 
    - Kontrol Panelini(Dashboard) görüntüle.

- Beklenen Sonuç: Kullanıcı, GİRİŞ ekranında yer alan E-posta ve Şifre bilgilerini doğru bir şekilde girdiği takdirde başarılı bir şekilde kendi kontrol panelini(Dashboard) görüntüleyebilmelidir. Aynı zamanda yanlış E-posta ve/veya şifre girilmesi durumunda sistemin uygun uyarı ekranı vermesi sağlanmaktadır. 

- Test Case ID: TC009 - Doğru E-Mail ve Şifre ile Birlikte "Ben Robot Değilim" Seçeneği 
    - Ön Koşullar: E-mail adresi formatı doğru şekilde girilmiştir.(örn:somebody@something.com)
    - Amaç: Kullanıcı, "GİRİŞ" ekranında var olan hesabına giriş yapabilmek için E-Posta adresini ve şifresini doğru girip "Ben Robot Değilim" seçeneğini aktifleştirdiği zaman "GİRİŞ" butonuna tıklarken kendi kontrol panelini(dashboard) görüntüleyebildiğini test etmek. 
    - Test Adımları:
        - Test Case ID: TC008-"GİRİŞ" Bağlantısının Tıklanabilirliği ve İçeriği testini uygula.
        - E-Posta adresini doğru gir.
        - Şifreni doğru gir.
        - "Ben Robot Değilim" seçeneğini aktif et.
        - "GİRİŞ" butonuna tıkla.
        - Kullanıcı kontrol panelini(Dashboard) görüntüle.
    
    - Fail Criteria: 
        - Kullanıcının kendi kontrol panelini görüntüleyememesi 
    - Beklenen Sonuçlar: Kullanıcı,kendi kontrol panelini başarıyla görüntüleyebilmiştir. 

- Test Case ID: TC010- Doğru E-Mail ve Şifre Fakat "Ben Robot Değilim" Seçeneğinin İşaretlenmemesi 
    - Ön Koşullar: E-mail adresi formatı doğru şekilde girilmiştir.(örn:somebody@something.com)
    - Amaç: Kullanıcı, "GİRİŞ" ekranında var olan hesabına giriş yapabilmek için E-Posta adresini ve şifresini doğru girip "Ben Robot Değilim" seçeneğini aktifleştirmediği zaman "GİRİŞ" butonuna tıklarken "Bu Alan zorunlu" gibi bir hata mesajı aldığını doğrulamak. 
    - Test Adımları:
        - Test Case ID: TC008-"GİRİŞ" Bağlantısının Tıklanabilirliği ve İçeriği testini uygula.
        - E-Posta adresini doğru gir.
        - Şifreni doğru gir.
        - "Ben Robot Değilim" seçeneğine tıklama
        - "GİRİŞ" butonuna tıkla.
        - "Bu alan zorunlu" sistemsel uyarı mesajını ekranda görüntüle. 
    
    - Fail Criteria:
        - Kullanıcının, "Bu alan zorunlu." sistemsel uyarı mesajıyla karşılaşmaması

    - Beklenen Sonuçlar: Kullanıcı,"Bu alan zorunlu." sistemsel uyarısıyla karşılaşmalıdır. 

- Test Case ID: TC011 - Yanlış E-Mail Adresi ve Doğru Şifre ile Birlikte "Ben Robot Değilim Seçeneği" 
    - Ön Koşullar: E-mail adresi formatı doğru şekilde girilmiştir.(örn:somebody@something.com)
    - Amaç: Kullanıcı, "GİRİŞ" ekranında var olan hesabına giriş yapabilmek için E-Posta adresini yanlış,şifresini doğru girip "Ben Robot Değilim" seçeneğini aktifleştidiği zaman "GİRİŞ" butonuna tıklarken "Girdiğiniz e-posta adresi ve/veya parola doğru değil." sistemsel uyarı mesajı aldığını test etmek. 
    - Test Adımları: 
        - Test Case ID: TC008-"GİRİŞ" Bağlantısının Tıklanabilirliği ve İçeriği testini uygula.
        - E-Posta adresini yanlış gir.
        - Şifreni doğru gir.
        - "Ben Robot Değilim" seçeneğini aktifleştir
        - "GİRİŞ" butonuna tıkla.
        - "Girdiğiniz e-posta adresi ve/veya parola doğru değil." sistemsel uyarı mesajını görüntüle. 
    
    - Fail Criteria: 
        - Kullanıcının, Girdiğiniz e-posta adresi ve/veya parola doğru değil." sistem uyarı mesajını almaması
    
    - Beklenen Sonuçlar: Kullanıcı, "Girdiğiniz e-posta adresi ve/veya parola doğru değil." sistemsel uyarı mesajını almalıdır.

- Test Case ID: TC012 - Yanlış E-Mail Adresi, Doğru Şifre Fakat "Ben Robot Değilim" Seçeneğinin İşaretlenmemesi
    - Ön Koşullar: E-mail adresi formatı doğru bir şekilde girilmiştir.(örn:somebody@something.com)
    - Amaç:Kullanıcı, "GİRİŞ" ekranında var olan hesabına giriş yapabilmek için E-Posta adresini yanlış,şifresini doğru girip "Ben Robot Değilim" seçeneğini işaretlemediği zaman "GİRİŞ" butonuna tıklarken "Bu alan zorunlu" sistemsel uyarı mesajı aldığını test etmek.
    - Test Adımları:
        - Test Case ID: TC008-"GİRİŞ" Bağlantısının Tıklanabilirliği ve İçeriği testini uygula.
        - E-Posta adresini yanlış gir.
        - Şifreni doğru gir.
        - "Ben Robot Değilim" seçeneğine tıklama.
        - "GİRİŞ" butonuna tıkla.
        - "Bu alan zorunlu." sistemsel uyarı mesajını görüntüle.
    
    - Fail Criteria:
        - Kullanıcının,"Bu alan zorunlu." sistemsel uyarı mesajını almaması 
    
    - Beklenen Sonuçlar: Kullanıcı "Bu alan zorunlu." sistemsel uyarı mesajını almalıdır.

- Test Case ID: TC013 - Doğru E-Mail Adresi,Yanlış Şifre ve "Ben Robot Değilim" Seçeneği 
    - Ön Koşullar: E-mail adresi formatı doğru şekilde girilmiştir.(örn:somebody@something.com)
    - Amaç: Kullanıcı, "GİRİŞ" ekranında var olan hesabına giriş yapabilmek için E-Posta adresini doğru,şifresini yanlış girip "Ben Robot Değilim" seçeneğini aktif ettiği zaman "GİRİŞ" butonuna tıklarken "Girdiğiniz e-posta adresi ve/veya parola doğru değil." uyarı mesajı aldığını test etmek. 
    - Test Adımları:
        - Test Case ID: TC008-"GİRİŞ" Bağlantısının Tıklanabilirliği ve İçeriği testini uygula.
        - E-Posta adresini doğru gir.
        - Şifreni yanlış gir.
        - "Ben Robot Değilim" seçeneğini aktifleştir.
        - "GİRİŞ" butonuna tıkla.
        - "Girdiğiniz e-posta adresi ve/veya parola doğru değil." sistemsel uyarı mesajını görüntüle.
    
    - Fail Criteria:
        - Kullanıcının "Girdiğiniz e-posta adresi ve/veya parola doğru değil." sistemsel uyarı mesajını almaması 
    - Beklenen Sonuçlar: Kullanıcı, "Girdiğiniz e-posta adresi ve/veya parola doğru değil." sistemsel uyarı mesajıyla karşılaşmakta ve kendi kontrol panelini görüntüleyememektedir. 


- Test Case ID: TC014 - Doğru E-Mail Adresi, Yanlış Şifre Fakat "Ben Robot Değilim" Seçeneğinin İşaretlenmemesi
    - Ön Koşullar: E-mail adresi formatı doğru şekilde girilmiştir.(örn:somebody@something.com)
    - Amaç: Kullanıcı, "GİRİŞ" ekranında var olan hesabına giriş yapabilmek için E-Posta adresini doğru,şifresini yanlış girip "Ben Robot Değilim" seçeneğini işaretlemediği zaman "GİRİŞ" butonuna tıklarken "Bu alan zorunlu." uyarı mesajı aldığını test etmek.
    - Test Adımları:
        - Test Case ID: TC008-"GİRİŞ" Bağlantısının Tıklanabilirliği ve İçeriği testini uygula.
        - E-Posta adresini doğru gir.
        - Şifreni yanlış gir.
        - "Ben Robot Değilim" seçeneğine tıklama.
        - "GİRİŞ" butonuna tıkla.
        - "Bu alan zorunlu" sistemsel uyarı mesajını görüntüle. 
    
    - Fail Criteria:
        - Kullanıcının "Bu alan zorunlu." uyarı mesajıyla karşılaşmaması 
    - Beklenen Sonuçlar: Kullanıcı, "Bu alan zorunlu." uyarı mesajıyla karşılaşmış ve kendi hesabına giriş yapamamıştır. 

- Test Case ID: TC015 - Yanlış E-Mail Adresi,Yanlış Şifre ve "Ben Robot Değilim" Seçeneği 
    - Ön Koşullar: E-mail adresi formatı doğru şekilde girilmiştir.(örn:somebody@something.com)
    - Amaç: Kullanıcı, "GİRİŞ" ekranında var olan hesabına giriş yapabilmek için E-Posta adresini yanlış,şifresini yanlış girip "Ben Robot Değilim" seçeneğini işaretlediği zaman "GİRİŞ" butonuna tıklarken "Girdiğiniz e-posta adresi ve/veya parola doğru değil." uyarı mesajı aldığını test etmek.

    - Test Adımları: 
        - Test Case ID: TC008-"GİRİŞ" Bağlantısının Tıklanabilirliği ve İçeriği testini uygula.
        - E-Posta adresini yanlış gir.
        - Şifreni yanlış gir.
        - "Ben Robot Değilim" seçeneğine tıkla.
        - "GİRİŞ" butonuna tıkla.
        - "Girdiğiniz e-posta adresi ve/veya parola doğru değil." sistemsel uyarı mesajını görüntüle. 

    - Fail Criteria:
        - Kullanıcının "Girdiğiniz e-posta adresi ve/veya parola doğru değil." uyarı mesajıyla karşılaşmaması

    - Beklenen Sonuç: Kullanıcı, "Girdiğiniz e-posta adresi ve/veya parola doğru değil." uyarı mesajıyla karşılaşmalı ve kontrol paneline giriş yapamamalıdır. 
    
- Test Case ID: TC016 - Yanlış E-Mail Adresi, Yanlış Şifre Fakat "Ben Robot Değilim" Seçeneğinin İşaretlenmemesi
    - Ön Koşullar: E-mail adresi formatı doğru şekilde girilmiştir.(örn:somebody@something.com)
    - Amaç: Kullanıcı, "GİRİŞ" ekranında var olan hesabına giriş yapabilmek için E-Posta adresini yanlış,şifresini yanlış girip "Ben Robot Değilim" seçeneğini aktif etmediği zaman "GİRİŞ" butonuna tıklarken "Bu alan zorunlu." uyarı mesajı aldığını test etmek.
    - Test Adımları:   
        - Test Case ID: TC008-"GİRİŞ" Bağlantısının Tıklanabilirliği ve İçeriği testini uygula.
        - E-Posta adresini yanlış gir.
        - Şifreni yanlış gir.
        - "Ben Robot Değilim" seçeneğini aktif etme.
        - "GİRİŞ" butonuna tıkla.
        - "Bu alan zorunlu." sistemsel uyarı mesajını görüntüle. 

    - Fail Criteria:
        - Kullanıcının "Bu alan zorunlu." sistemsel uyarı mesajını almaması 
        
    - Beklenen Sonuçlar: Kullanıcı "Bu alan zorunlu." uyarı mesajını görüntülemekte ve kendi kontrol paneline giriş yapamamaktadır. 

- Test Case ID: TC017 - Boş E-Mail Adresi, Doğru Şifre ve "Ben Robot Değilim" Seçeneği 
    - Amaç: Kullanıcı, "GİRİŞ" ekranında var olan hesabına giriş yapabilmek için E-Posta adresini boş bırakıp,şifresini doğru girip "Ben Robot Değilim" seçeneğini aktif ettiği zaman "GİRİŞ" butonuna tıklarken "Bu alan zorunlu." uyarı mesajı aldığını test etmek.
    - Test Adımları:
        - Test Case ID: TC008-"GİRİŞ" Bağlantısının Tıklanabilirliği ve İçeriği testini uygula.
        - E-Posta adresini boş bırak.
        - Şifreni doğru gir.
        - "Ben Robot Değilim" seçeneğini aktif et.
        - "GİRİŞ" butonuna tıkla.
        - "Bu alan zorunlu." sistemsel uyarı mesajını görüntüle. 
    - Fail Criteria:
        - E-posta adresi boş bırakıldığı halde "Bu alan zorunlu." sistemsel uyarı mesajını almamak
    - Beklenen Sonuçlar: Kullanıcı, e-posta adresini boş bıraktığı için "Bu alan zorunlu." sistemsel uyarı mesajını almıştır. 

- Test Case ID: TC018 - Boş E-Mail Adresi, Yanlış Şifre ve "Ben Robot Değilim" Seçeneği 
    - Amaç: Kullanıcı, "GİRİŞ" ekranında var olan hesabına giriş yapabilmek için E-Posta adresini boş bırakıp,şifresini yanlış girip "Ben Robot Değilim" seçeneğini aktif ettiği zaman "GİRİŞ" butonuna tıklarken "Bu alan zorunlu." uyarı mesajı aldığını test etmek.
    - Test Adımları:
        - Test Case ID: TC008-"GİRİŞ" Bağlantısının Tıklanabilirliği ve İçeriği testini uygula.
        - E-Posta adresini boş bırak.
        - Şifreni yanlış gir.
        - "Ben Robot Değilim" seçeneğini aktif et.
        - "GİRİŞ" butonuna tıkla.
        - "Bu alan zorunlu." sistemsel uyarı mesajını görüntüle. 
    - Fail Criteria:
        - E-posta adresi boş bırakıldığı halde "Bu alan zorunlu." sistemsel uyarı mesajını almamak
    - Beklenen Sonuçlar: Kullanıcı, e-posta adresini boş bıraktığı için "Bu alan zorunlu." sistemsel uyarı mesajını almıştır. 

- Test Case ID: TC019 - Boş E-Mail Adresi, Doğru Şifre ve "Ben Robot Değilim" Seçeneğinin İşaretlenmemesi 
     - Amaç: Kullanıcı, "GİRİŞ" ekranında var olan hesabına giriş yapabilmek için E-Posta adresini boş bırakıp,şifresini doğru girip "Ben Robot Değilim" seçeneğini işaretlemediği zaman "GİRİŞ" butonuna tıklarken "Bu alan zorunlu." uyarı mesajını hem e-postayı boş bıraktığı için hem de robot değilim seçeneğini aktifleştirmediği için 2 defa aldığını test etmek.
    - Test Adımları:
        - Test Case ID: TC008-"GİRİŞ" Bağlantısının Tıklanabilirliği ve İçeriği testini uygula.
        - E-Posta adresini boş bırak.
        - Şifreni doğru gir.
        - "Ben Robot Değilim" seçeneğini işaretleme.
        - "GİRİŞ" butonuna tıkla.
        - "Bu alan zorunlu." sistemsel uyarı mesajını 2 defa görüntüle. 
    - Fail Criteria:
        - Hem E-posta adresi hem de ben robot değilim seçenekleri boş bırakıldığı halde "Bu alan zorunlu." sistemsel uyarı mesajını 2 defa almamak.
    - Beklenen Sonuçlar: Kullanıcı,2 adet "Bu alan zorunlu." sistemsel uyarı mesajını ekranda görmektedir.

- Test Case ID: TC020 - Boş E-Mail Adresi, Yanlış Şifre ve "Ben Robot Değilim" Seçeneğinin İşaretlenmemesi  
    - Amaç: Kullanıcı, "GİRİŞ" ekranında var olan hesabına giriş yapabilmek için E-Posta adresini boş bırakıp,şifresini yanlış girip "Ben Robot Değilim" seçeneğini işaretlemediği zaman "GİRİŞ" butonuna tıklarken "Bu alan zorunlu." uyarı mesajını hem e-postayı boş bıraktığı için hem de robot değilim seçeneğini aktifleştirmediği için 2 defa aldığını test etmek.
    - Test Adımları:
        - Test Case ID: TC008-"GİRİŞ" Bağlantısının Tıklanabilirliği ve İçeriği testini uygula.
        - E-Posta adresini boş bırak.
        - Şifreni yanlış gir.
        - "Ben Robot Değilim" seçeneğini işaretleme.
        - "GİRİŞ" butonuna tıkla.
        - "Bu alan zorunlu." sistemsel uyarı mesajını 2 defa görüntüle. 
    - Fail Criteria:
        - Hem E-posta adresi hem de ben robot değilim seçenekleri boş bırakıldığı halde "Bu alan zorunlu." sistemsel uyarı mesajını 2 defa almamak.
    - Beklenen Sonuçlar: Kullanıcı,2 adet "Bu alan zorunlu." sistemsel uyarı mesajını ekranda görmektedir.

- Test Case ID: TC021 - Boş E-Mail Adresi, Boş Şifre ve Ben Robot Değilim Seçeneği 
    - Amaç: Kullanıcı, "GİRİŞ" ekranında var olan hesabına giriş yapabilmek için E-Posta adresini ve şifresini boş bırakıp "Ben Robot Değilim" seçeneğini işaretlediği zaman "GİRİŞ" butonuna tıklarken "Bu alan zorunlu." uyarı mesajını hem e-postayı hem de şifreyi boş bıraktığı için 2 defa aldığını test etmek.
    - Test Adımları:
        - Test Case ID: TC008-"GİRİŞ" Bağlantısının Tıklanabilirliği ve İçeriği testini uygula.
        - E-Posta adresini boş bırak.
        - Şifreni boş bırak.
        - "Ben Robot Değilim" seçeneğini aktifleştir.
        - "GİRİŞ" butonuna tıkla.
        - "Bu alan zorunlu." sistemsel uyarı mesajını 2 defa görüntüle. 
    - Fail Criteria:
        - Hem E-posta adresi hem de şifre seçenekleri boş bırakıldığı halde "Bu alan zorunlu." sistemsel uyarı mesajını 2 defa almamak.
    - Beklenen Sonuçlar: Kullanıcı,2 adet "Bu alan zorunlu." sistemsel uyarı mesajını ekranda görmektedir.

- Test Case ID: TC022 - Boş E-Mail Adresi, Boş Şifre ve Ben Robot Değilim Seçeneğinin İşaretlenmemesi 
    - Amaç: Kullanıcı, "GİRİŞ" ekranında var olan hesabına giriş yapabilmek için hem E-Posta adresini ve şifresini boş bırakıp hem de  "Ben Robot Değilim" seçeneğini işaretlemediği zaman "GİRİŞ" butonuna tıklarken "Bu alan zorunlu." uyarı mesajını hem e-postayı ve şifreyi hem de ben robot değilim seçeneğini boş bıraktığı için 3 defa aldığını test etmek.
    - Test Adımları:
        - Test Case ID: TC008-"GİRİŞ" Bağlantısının Tıklanabilirliği ve İçeriği testini uygula.
        - E-Posta adresini boş bırak.
        - Şifreni boş bırak.
        - "Ben Robot Değilim" seçeneğini boş bırak.
        - "GİRİŞ" butonuna tıkla.
        - "Bu alan zorunlu." sistemsel uyarı mesajını 3 defa görüntüle. 
    - Fail Criteria:
        - "Bu alan zorunlu." sistemsel uyarı mesajını 3 defa almamak.
    - Beklenen Sonuçlar: Kullanıcı,3 adet "Bu alan zorunlu." sistemsel uyarı mesajını ekranda görmektedir.

- Test Case ID: TC023 - E-Mail Adresinin Formatının Yanlış Girilmesi 
    - Amaç: Kullanıcı, E-mail adresi formatını yanlış girip(örneğin @ karekteri olmadan) şifresini doğru veya yanlış girilmesi farketmeksizin "Ben Robot Değilim" seçeneğini aktifleştirip "GİRİŞ" butonuna tıkladığında
    "Lütfen e-posta adresine bir '@' işareti ekleyin." sistem uyarı mesajı aldığını test etmek. 
    - Test Adımları:
        - Test Case ID: TC008-"GİRİŞ" Bağlantısının Tıklanabilirliği ve İçeriği testini uygula.
        - E-Posta adresininin formatını yanlış gir.(örneğin @ karekterini kullanma)
        - Şifreni doğru/yanlış gir veya boş bırak
        - "Ben Robot Değilim" seçeneğini işaretle veya işaretleme.
        - "GİRİŞ" butonuna tıkla.
        - "Lütfen e-posta adresine bir '@' işareti ekleyin." sistemsel uyarı mesajını görüntüle. 

    - Fail Criteria:
        - Kullanıcı "Lütfen e-posta adresine bir '@' işareti ekleyin." gibi bir uyarı mesajıyla karşılaşmadı. 
    - Beklenen Sonuçlar: Kullanıcı, yanlış formatta girilen e-posta adresi sonucunda "Lütfen e-posta adresine bir '@' işareti ekleyin." sistemsel uyarı mesajıyla karşılaştı ve kontrol paneline giriş yapamadı.  

- Test Case ID: TC024 - Giriş- Ben Robot Değilim Seçeneği Zaman Aşımı 
    - Amaç: Kullanıcı, "GİRİŞ" ekranında E-Posta ve şifre bilgilerini girip "Ben Robot Değilim" seçeneğini işaretletleyip belirli bir zaman (tipik olarak 1 dakikadan fazla) beklediğinde "Doğrulamanın süresi doldu.Onay kutusunu tekrar işeretleyin." gibi bir uyarı mesajı aldığını test etmek. 
    - Test Adımları:   
         - Test Case ID: TC008-"GİRİŞ" Bağlantısının Tıklanabilirliği ve İçeriği testini uygula.
        - E-posta adresini gir.
        - Şifreni gir.
        - "Ben Robot Değilim" seçeneğini işaretle 
        - "GİRİŞ" butonuna tıklamadan 1 dakikadan fazla bir süre boyunca bekle.
        - "Doğrulamanın süresi doldu.Onay kutusunu tekrar işaretleyin." uyarı mesajını görüntüle. 
    
    - Fail Criteria:
        - Kullanıcı 1 dakikadan fazla bir süre boyunca giriş yapmadan beklediği halde onay kutusunu tekrar işaretlemesi gerektiğini belirten sistem uyarı mesajıyla karşılaşmadı. 
    
    - Beklenen Sonuçlar: Kullanıcı "Ben robot değilim." uyarı mesajını tekrar işaretlemesini gerektiren uyarı mesajıyla karşılaştı.

<br><br><br>

4.Test Senaryo İsmi: Kullanıcı "Şifremi Unuttum" Bölümünün Tıklanılabilirliği ve İşlevi 
- Test ID: TS004
- Ön Koşullar: Baykar Kariyer websitesi erişilebilir olmalıdır ve kullanıcının geçerli bir internet bağlantısı bulunmaktadır
- Amaç: Kullanıcının,giriş ekranında yer alan "Şifremi Unuttum" bağlantısını tıklayabildiğini ve açılan sayfada E-posta adresini girip şifre sıfırlama mailini kendi mail adresinde görebildiğini test etmek. 
- Test Adımları:
    - Baykar Kariyer websitesini görüntüle.
    - Gezinme menüsünde yer alan "GİRİŞ" adlı bağlantıya tıkla.
    - Açılan sayfada "Şifremi unuttum" bağlantısına tıkla.
    - E-posta adresini gir.
    - "Ben robot değilim." seçeneğini işaretle.
    - "Sıfırlama Maili Gönder." butonuna tıkla.
    - Girmiş olduğun mail adresini kontrol et ve maildeki şifre sıfırlama bağlantısına tıkla. 
    - Yeni şifreni gir.
    - Yeni şifreni tekrar gir.
    - "Sıfırla" butonuna tıkla. 
    - Yeni şifrenle tekrar giriş yap.
- Fail Criteria: 
    - Kullanıcının mail adresine şifre sıfırlama bağlantısının gelmemesi
    - Yeni şifreyi belirledikten sonra kullanıcının yeni şifresiyle giriş yapamaması 
- Beklenen Sonuçlar: Kullanıcı, e-posta adresine gelen şifre sıfırlama bağlantısıyla yeni şifresini oluşturup başarıyla giriş yapabilmiştir. 

- Test Case ID: TC025 - Şifremi Unuttum - Boş e-posta ve boş onay kutusu
    - Amaç: Kullanıcı, Şifremi Unuttum ekranında boş bir E-posta adresi girdiğinde ve "Ben Robot" değilim seçeneğini işaretlemediği durumda 2 adet "Bu alan zorunlu." uyarı mesajı aldığını test etmek. 
    - Test Adımları:
        - Test Case ID: TC008-"GİRİŞ" Bağlantısının Tıklanabilirliği ve İçeriği testini uygula.
        - "Şifremi Unuttum" bağlantısına tıkla. 
        - E- posta adresini boş bırak. 
        - "Ben Robot Değilim." seçeneğini boş bırak.
        - "Sıfırlama Maili Gönder." butonuna tıkla.
        - 2 adet "Bu alan zorunlu." uyarı mesajını görüntüle.
    - Failure Criteria:
        - 2 adet "Bu alan zorunlu." uyarı mesajının görüntülenmemesi
    - Beklenen Sonuçlar: Kullanıcı ekranda 2 adet "Bu alan zorunlu." uyarı mesajıyla karşılaşmış ve yeni şifresini belirleyememiştir. 

- Test Case ID: TC026 - Şifremi Unuttum - Boş e-posta ve işaretlenmiş onay kutusu 
    - Amaç: Kullanıcı, Şifremi Unuttum ekranında boş bir E-posta adresi girdiğinde ve "Ben Robot" değilim seçeneğini işaretlediği durumda 1 adet "Bu alan zorunlu." uyarı mesajı aldığını test etmek. 
    - Test Adımları:
        - Test Case ID: TC008-"GİRİŞ" Bağlantısının Tıklanabilirliği ve İçeriği testini uygula.
        - "Şifremi Unuttum" bağlantısına tıkla. 
        - E- posta adresini boş bırak. 
        - "Ben Robot Değilim." seçeneğini işaretle.
        - "Sıfırlama Maili Gönder." butonuna tıkla.
        - 1 adet "Bu alan zorunlu." uyarı mesajını görüntüle.
    - Failure Criteria:
        - 1 adet "Bu alan zorunlu." uyarı mesajının görüntülenmemesi
    - Beklenen Sonuçlar: Kullanıcı ekranda 1 adet "Bu alan zorunlu." uyarı mesajıyla karşılaşmış ve yeni şifresini belirleyememiştir. 

- Test Case ID: TC027 - Şifremi Unuttum - Girilen E-Posta ve İşaretlenmemiş Onay Kutusu
    - Ön Koşullar: E-mail adresi formatı doğru şekilde girilmiştir.(örn:somebody@something.com)
    - Amaç: Kullanıcı, Şifremi Unuttum ekranında kendi e-posta adresi girdiğinde ve "Ben Robot" değilim seçeneğini işaretlemediği durumda 1 adet "Bu alan zorunlu." uyarı mesajı aldığını test etmek. 
    - Test Adımları:
        - Test Case ID: TC008-"GİRİŞ" Bağlantısının Tıklanabilirliği ve İçeriği testini uygula.
        - "Şifremi Unuttum" bağlantısına tıkla. 
        - E- posta adresini gir
        - "Ben Robot Değilim." seçeneğini boş bırak.
        - "Sıfırlama Maili Gönder" butonuna tıkla.
        - 1 adet "Bu alan zorunlu." uyarı mesajını görüntüle.
    - Failure Criteria:
        - 1 adet "Bu alan zorunlu." uyarı mesajının görüntülenmemesi
    - Beklenen Sonuçlar: Kullanıcı ekranda 1 adet "Bu alan zorunlu." uyarı mesajıyla karşılaşmış ve yeni şifresini belirleyememiştir. 

- Test Case ID: TC028 - Şifremi Unuttum - E-Posta Adresi Formatının Yanlış Girilmesi
    - Amaç: Kullanıcı, Şifremi Unuttum ekranında e-posta adresini yanlış bir formatta girdiğinde(örneğin @ karekteri eksik) onay kutusunun işaretlenip işaretlenmediğine bakılmaksızın "Lütfen e-posta adresine bir '@' işareti ekleyin." uyarı mesajıyla karşılaştığını test etmek
    - Test Adımları: 
        - Test Case ID: TC008-"GİRİŞ" Bağlantısının Tıklanabilirliği ve İçeriği testini uygula.
        - "Şifremi Unuttum" bağlantısına tıkla. 
        - E- posta adresinin formatını yanlış gir,örneğin '@' karekterini eksik gir.
        - "Ben Robot Değilim." seçeneğini boş bırak veya doldur.
        - "Sıfırlama Maili Gönder" butonuna tıkla.
        - 1 adet "Bu alan zorunlu." uyarı mesajını görüntüle.
        - "Lütfen e-posta adresine bir '@' işareti ekleyin." uyarı mesajını görüntüle. 
    
    - Fail Criteria:
        -"Lütfen e-posta adresine bir '@' işareti ekleyin." gibi bir uyarı mesajıyla karşılaşılmadı.
    - Beklenen Sonuçlar: Kullanıcı, ""Lütfen e-posta adresine bir '@' işareti ekleyin." gibi bir uyarı mesajı görüntüledi ve yeni şifresini oluşturamadı. 

- Test Case ID: TC029 - Şifremi Unuttum - Ben Robot Değilim Seçeneği Zaman Aşımı
    - Amaç: Kullanıcı, "Şifremi Unuttum" ekranında E-Posta bilgisini girip "Ben Robot Değilim" seçeneğini işaretletleyip belirli bir zaman (tipik olarak 1 dakikadan fazla) beklediğinde "Doğrulamanın süresi doldu.Onay kutusunu tekrar işeretleyin." gibi bir uyarı mesajı aldığını test etmek. 
    - Test Adımları:   
         - Test Case ID: TC008-"GİRİŞ" Bağlantısının Tıklanabilirliği ve İçeriği testini uygula.
        - "Şifremi Unuttum" bağlantısına tıkla.
        - E-posta bilgini gir.
        - "Ben Robot Değilim" seçeneğini işaretle 
        - "Sıfırlama Maili Gönder" butonuna tıklamadan 1 dakikadan fazla bir süre boyunca bekle.
        - "Doğrulamanın süresi doldu.Onay kutusunu tekrar işaretleyin." uyarı mesajını görüntüle. 
    
    - Fail Criteria:
        - Kullanıcı 1 dakikadan fazla bir süre boyunca giriş yapmadan beklediği halde onay kutusunu tekrar işaretlemesi gerektiğini belirten sistem uyarı mesajıyla karşılaşmadı. 
    
    - Beklenen Sonuçlar: Kullanıcı "Ben robot değilim." uyarı mesajını tekrar işaretlemesini gerektiren uyarı mesajıyla karşılaştı.


<br><br><br>


5.Test Senaryo İsmi: Baykar Kariyer Platformu Hesap Oluşturma 
- Test Senaryo ID: TS005
- Ön Koşullar:Baykar Kariyer websitesi erişilebilir olmalıdır ve kullanıcının geçerli bir internet bağlantısı bulunmaktadır.
- Amaç: Kullanıcının halihazıda bir Baykar Kariyer Platformu hesabı yoksa, E-Posta ve şifre bilgilerini girerek hesap oluşturma işlemini test etmek. 
- Testin Adımları:
    - Baykar Kariyer websitesini görüntüle.
    - Gezinme menüsünde "GİRİŞ" isimli bağlantıya tıkla.
    - Açılan giriş sayfasında "Hesap Oluştur" bağlantısına tıkla.
    - E-posta bilgisini gir.
    - Şifre bilgisini gir.
    - Şifre bilgini gir. (Tekrar)
    - "Ben robot değilim." onay kutusunu işaretle.
    - "KAYDOL" butonuna tıkla.
    - E-posta adresine gir ve onay linkine tıkla.
    - Kayıt olduğun e-mail adresin ve şifre bilgilerinle sisteme giriş yap. (Test Case ID: TC009)
 - Fail Criteria:
    - "Hesap Oluştur" bağlantısına tıklanılamaması
    - "KAYDOL" butonuna tıklanılamaması
    - Kayıt olunan mail adresine onay linkinin gelmemesi
    - Onay linkine tıkladıktan sonra kayıt olunan e-posta ve şifre bilgileriyle sisteme giriş yapılamaması 

- Beklenen Sonuç: Kullanıcı, girmiş olduğu e-posta ve şifre bilgileri sonucunda mail adresine bir onay linki teslim almış ve onay işlemi tamamlandıktan sonra belirlediği e-posta ve şifre bilgileriyle kontrol paneline giriş yapabilmiştir. 


- Test Case ID: TC030 - Şifre Uzunluğunun Test Edilmesi 
    - Ön Koşullar: 
        - E-posta adresi format olarak doğru girilmiştir.
        - "Ben robot değilim." seçeneği işaretlenmiştir.
    -Amaç: Kullanıcı hesabını oluştururken, girmiş olduğu şifre uzunluğunun 8 karekter içerip içermediği test etmek. 
    - Testin Adımları:
        - Test Case ID: TC008-"GİRİŞ" Bağlantısının Tıklanabilirliği ve İçeriği testini uygula.
        - "Hesap Oluştur" bağlantısına tıkla.
        - Şifreni 8 karekterden kısa olacak şekilde gir.
        - Şifreni 8 karekterden kısa olacak şekilde gir.(Tekrar)
        - "KAYDOL" butonuna tıkla.
        - "Bu parola çok kısa. En az 8 karakter içermek zorunda." uyarı mesajını görüntüle.
    
    - Fail Criteria:
        - Kullanıcı 8 karekterden daha küçük bir şifreye sahip olduğu halde sistem uyarı mesajını almaması 
    
    - Beklenen Sonuç: Kullanıcı, "Bu parola çok kısa. En az 8 karakter içermek zorunda." uyarı mesajını almış ve sisteme kayıt olamamıştır. 

- Test Case ID: TC031 - Şifrenin Aynı Girilmemesi
    - Ön Koşullar: 
        - E-posta adresi format olarak doğru girilmiştir.
        - "Ben robot değilim." seçeneği işaretlenmiştir.
        - Şifre en az 8 karakterlidir ve harf-sayı kombinasyonlarından oluşmaktadır.
    - Amaç: Kullanıcı hesap oluştururken girmiş olduğu şifrelerin birbirinden farklı olduğu durumlarda sistemin tepkisini test etmek 
    - Test Adımları:
        - Test Case ID: TC008-"GİRİŞ" Bağlantısının Tıklanabilirliği ve İçeriği testini uygula.
        - "Hesap Oluştur" bağlantısına tıkla.
        - İlk şifreni gir.
        - Farklı bir şifre gir.
        - "KAYDOL" butonuna tıkla.
        - "Her seferinde aynı parolayı girmelisiniz." uyarı ekranını görüntüle.
    
    - Fail Criteria:
        - Kullanıcı hesap oluştururken girdiği şifreler birbiriyle aynı olmamasına rağmen uyarı ekranıyla karşılaşmıyor.
    - Beklenen Sonuçlar: Kullanıcı, "Her seferinde aynı parolayı girmelisiniz." uyarı ekranıyla karşılaşmaktadır. 

- Test Case ID: TC032 - Tamamı Sayıdan Oluşan Şifrenin Testi 
    - Ön Koşullar:
        - E-posta adresi format olarak doğru girilmiştir.
        - "Ben robot değilim." seçeneği işaretlenmiştir.
    - Amaç: Kullanıcı hesap oluştururken girmiş olduğu şifrenin tamamının sayı olması durumunda sistemin tepkisini test etmektir. 
    - Test Adımları:
        - Test Case ID: TC008-"GİRİŞ" Bağlantısının Tıklanabilirliği ve İçeriği testini uygula.
        - "Hesap Oluştur" bağlantısına tıkla.
        - Şifreni tamamı sayılardan oluşacak şekilde gir.
        - Oluşturduğun şifreyi tekrardan gir.
        - "KAYDOL" butonuna tıkla.
        - "Bu parola çok geneldir.Bu parola tamamıyla sayısaldır." uyarı ekranını görüntüle.

    - Fail Criteria:
        - Kullanıcı tamamı sayılardan oluşan şifre seçtiği halde uyarı mesajı almamaktadır.

    - Beklenen Sonuç: Kullanıcı,"Bu parola çok geneldir.Bu parola tamamıyla sayısaldır." gibi bir uyarı mesajı görüntülemektedir.


<br><br><br>

6.Test Senaryo İsmi: Açık Pozisyonlarda Birim Arama İşlevi 
- Test Senaryo ID: TS006
- Ön Koşullar:Baykar Kariyer websitesi erişilebilir olmalıdır ve kullanıcının geçerli bir internet bağlantısı bulunmaktadır.
- Amaç: Bu test senaryosu,kullanıcının Baykar Kariyer websitesinde "Açık Pozisyonlar" sayfasında birim arama işlevini test etmektedir. Kullacının girmiş olduğu arama sözcüğüne göre uygun birimlerin çıktısı doğrulanmaktadır. 
- Test Adımları:
    - Baykar Kariyer websitesini görüntüle.
    - "AÇIK POZİSYONLAR" bağlantısına tıkla.
    - Sol tarafta yer alan "Birimler" bölümünde arama kutucuğuna aranmak istenen birim ismini yaz.
    - Aranan kelime ile çıktının birbiriyle uyumluluğunu doğrula.

- Fail Criteria:
    - Arama kutucuğuna istenen birimin kullanıcı tarafından yazılamaması
    - Arama kutucuğunda aranan birimin ile arama sonucu gösterilen birimin birbiriyle uyuşmaması

- Beklenen Sonuçlar: Kullanıcı,birim arama kutucuğuna yazdığı kelimelerle istediği birime ait açık pozisyonları görebilmektedir. 


- Test Case ID:TC033 - Birim Arama Kutucuğuna Hiçbir Şey Yazılmaması 
    - Ön Koşullar: Kullanıcı herhangi bir birimi manuel olarak filtrelememiştir.
    - Amaç: Kullanıcı, Açık Pozisyonlar bölümünde yer alan birim arama kutucuğuna hiçbir şey yazmadığı durumda sistemin vermiş olduğu tepki test edilmektedir. 
    - Test Adımları:
        - Test Case ID: TC003- Açık Pozisyonlar Menüsünün Tıklanabilirliği ve İçeriği testini uygula.
        - Ekranın sol tarafında bulunan birim arama kutucuğuna hiçbir şey yazmadan var olan iş birimlerini incele.

    - Fail Criteria:
        - Kullanıcının herhangi bir iş birimini görüntüleyememesi
    
    - Beklenen Sonuç: Kullanıcı, var olan tüm iş birimlerini görüntüleyebilmiştir.

- Test Case ID: TC034 - Birim Arama Kutucuğuna Belirli Bir İş Biriminin Yazılması
    - Ön Koşullar:
        - Kullanıcının aradığı birimin halihazırda en az bir adet pozisyonu bulunmaktadır.
    - Amaç: Kullanıcının Açık Pozisyonlar sayfasında yer alan birim arama kutucuğuna halihazırda açık pozisyon bulunan birimlerden birini aratmasıyla sadece istenilen birimlere ait çıktıların gösterilmesi test edilmektedir.
    - Test Adımları:
        - Test Case ID: TC003- Açık Pozisyonlar Menüsünün Tıklanabilirliği ve İçeriği testini uygula.
        - Ekranın sol tarafında yer alan birim arama kutucuğuna birim ismini yaz.
        - Sadece ilgili birim ismini içeren iş birimlerini görüntülediğini doğrula.
    
    - Fail Criteria:
        - Kullanıcının aramış olduğu birime dair herhangi bir iş birimi sonucunun gösterilmemesi
    - Beklenen Sonuç: Kullanıcı, aramış olduğu birim ismini içeren tüm iş birimlerini görüntülemektedir.

- Test Case ID: TC035 - Birim Arama Kutucuğuna Açık Pozisyonu Bulunmayan Birim Adının Yazılması
    - Ön Koşullar:
        - Kullanıcının aramakta olduğu birimin halihazırda açık bir pozisyonu bulunmamaktadır.
    - Amaç: Kullanıcının Açık Pozisyonlar sayfasında yer alan birim arama kutucuğuna halihazırda açık pozisyon bulunmayan bir birim ismini yazması sonucunda sistemin verdiği çıktıyı test etmek 
    - Test Adımları:
        - Test Case ID: TC003- Açık Pozisyonlar Menüsünün Tıklanabilirliği ve İçeriği  testini uygula.
        - Ekranın sol tarafında yer alan birim arama kutucuğuna aranmak istenen birim ismini yaz
        - Sistemin herhangi bir çıktı vermediğini doğrula.

    - Fail Criteria:
        - Kullanıcının girdiği birim ismine göre herhangi bir açık pozisyon olmamasına rağmen sistemin en az bir adet birim arama sonucunu göstermesi
    - Beklenen Sonuçlar: Kullanıcı,halihazırda açık pozisyonu bulunmayan bir birim ismi arattığında herhangi bir iş birimi sonucu gösterilmeyecektir.


<br><br><br>

Test Senaryo İsmi: Açık Pozisyonlar Filtreleme Özelliğinin Test Edilmesi 
- Test Senaryo ID: TS007
- Ön Koşullar:Baykar Kariyer websitesi erişilebilir olmalıdır ve kullanıcının geçerli bir internet bağlantısı bulunmaktadır.
- Amaç: Bu test senaryosunda Açık Pozisyonlar sayfasında yer alan iş birimlerinin filtrelenme özelliği test edilmektedir.
- Test Adımları:
    - Baykar Kariyer websitesini görüntüle.
    - "AÇIK POZİSYONLAR" adlı bağlantıya tıkla.
    - Ekranın sol tarafında yer alan filtreme özelliğini kullanarak iş birimlerini filtrele
    - Ekranın sağ tarafında yer alan iş ilanlarını görüntüle

- Fail Criteria:
    - Kullanıcının filtrelediği iş birimlerine ait iş ilanlarının doğru bir şekilde gösterilememesi

- Beklenen Sonuçlar: Kullanıcı başarılı bir şekilde iş birimine göre filtreleme yapmış ve bu filtreleme sonucuna göre iş ilanları sayfada görüntülenmiştir.


- Test Case ID: TC036 - Herhangi Bir Filtreleme İşleminin Yapılmaması
- Ön Koşullar:
    - Kullanıcı birim arama kutucuğuna herhangi bir birim ismi yazmamıştır.
- Amaç: Kullanıcının  Açık Pozisyonlar sayfasında yer alan birim filtreleme özelliğini kullanmadığı durumda sistemin çıktısını test etmek

- Test Adımları:
    - Test Case ID: TC003- Açık Pozisyonlar Menüsünün Tıklanabilirliği ve İçeriği  testini uygula.

    - Ekranın sol tarafında yer alan iş birimi filtrelerinden herhangi bir iş birimini filtreleme özelliğini kullanma. 
    
    - Ekranın sağ tarafındaki iş ilanları sonuçlarını görüntüle.

- Fail Criteria:
    - Kullanıcı herhangi bir filtreleme işlemi yapmamasına rağmen tüm iş ilanlarının gözükmemesi 
- Beklenen Sonuçlar: Kullanıcı halihazırda var olan tüm iş ilanlarını görmektedir.

- Test Case ID: TC037 - Bir Adet Filtreleme İşleminin Yapılması
- Ön Koşullar:
    - Kullanıcı birim arama kutucuğuna herhangi bir birim ismi yazmamıştır.
- Amaç: Kullanıcının Açık Pozisyonlar sayfasında ekranın sol bölümünde yer alan filtreleme özelliklerinden bir tanesini kullandığı durumda sistemin çıktısını test etmek

- Test Adımları:
    - Test Case ID: TC003- Açık Pozisyonlar Menüsünün Tıklanabilirliği ve İçeriği  testini uygula.
    - Ekranın sol bölümünde yer alan iş birimi filtrelerinden sadece bir tanesini kullan.
    - Ekranın sağ bölümünde iş ilanlarını incele.

- Fail Criteria:
    - Kullanıcının seçmiş olduğu iş birimi filtresine göre iş ilanlarının gösterilmemesi
- Beklenen Sonuç: Kullanıcı,sadece filtrelediği iş birimiyle alakalı iş ilanlarını görüntülemektedir.


- Test Case ID: TC038 - Birden Fazla Filtreleme İşleminin Yapılması
    - Ön Koşullar: Kullanıcı birim arama kutucuğuna herhangi bir birim ismi yazmamıştır.
    - Amaç: Kullanıcının Açık Pozisyonlar sayfasında ekranın sol bölümünde yer alan filtreleme özelliklerinden çok sayıda kullandığı durumda sistemin çıktısını test etmek. 
    - Test Adımları:
        - Test Case ID: TC003- Açık Pozisyonlar Menüsünün Tıklanabilirliği ve İçeriği  testini uygula.
        - Ekranın sol bölümünde yer alan iş birimi filtrelerinden birden fazla kullan.
        - Ekranın sağ bölümünde iş ilanlarını incele.

- Fail Criteria:
    - Kullanıcının seçmiş olduğu iş birimi filtresine göre iş ilanlarının gösterilmemesi
- Beklenen Sonuç: Kullanıcı, sadece filtrelediği iş birimleriyle alakalı iş ilanlarını görüntülemektedir.

         
- Test Case ID: TC039 Hem Filtreleme Hem Birim Arama Özelliğinin Kullanılması 
    - Ön Koşullar:
        - Kullanıcının aramış olduğu birim ismine ait birden fazla birim görüntülenmektedir. Örneğin "Elektro" sözcüğü için Elektro Optik Sistemler, Elektronik Sistem Geliştirme ve Elektronik İmalat ve Entegrasyon iş birimlerinin gösterilmesi
        
    - Amaç: Kullanıcının Açık Pozisyonlar sayfasında hem iş birimi arama özelliğini hem de iş birimi filtreleme özelliğini kullanarak iş ilanlarını görüntülediği durumlarda sistem çıktısını test etmektedir.
    - Test Adımları:
        - Test Case ID: TC003- Açık Pozisyonlar Menüsünün Tıklanabilirliği ve İçeriği  testini uygula.
        - Ekranın sol bölümünde yer alan birim arama kutucuğuna aranmak istenen birimi yaz.
        - Ekranda çıkan sonuçlardan bir tanesi veya daha fazlası için filtreleme yap.
        - Ekranın sağ bölümündeki iş ilanlarını incele
    
    - Fail Criteria:
        - Kullanıcının birim arama ve filtreleme özelliklerine göre istenilen iş ilanlarını görüntüleyememesi

    - Beklenen Sonuçlar: Kullanıcı birim arama ve filtreleme özelliklerine göre halihazırda açık pozisyonu bulunan iş ilanlarını görüntüleyebilmektedir.

<br><br><br>

8.Test Senaryo İsmi: İş İlanı Arama İşlevinin Test Edilmesi
- Test Senaryo ID: TS008 
- Ön Koşullar:Baykar Kariyer websitesi erişilebilir olmalıdır ve kullanıcının geçerli bir internet bağlantısı bulunmaktadır.
- Amaç: Kullanıcının Açık Pozisyonlar sayfasında yer alan iş ilanı arama kutucuğuna girmiş olduğu iş alanı anahtar kelimesine göre iş ilanlarını görüntüleyebildiğini test etmek.
- Test Adımları:
    - Baykar Kariyer web sitesini görüntüle.
    - "AÇIK POZİSYONLAR" adlı bağlantıya tıkla.
    - Ekranın sağ bölümünde yer alan "İş İlanı Ara..." kutucuğuna aranmak istenen iş ilanını yaz.
    - İş ilanlarını görüntüle.

- Fail Criteria:
    - Kullanıcının girmiş olduğu iş ilanı kelimesine göre doğru bir şekilde iş ilanları listenememektedir.
- Beklenen Sonuçlar: Kullanıcı, aramak istediği iş ilanına göre iş ilanları listesinii görüntülemektedir.

- Test Case ID: TC040 - Herhangi bir İş İlanı Arama Sözcüğünün Girilmemesi
- Ön Koşullar:
    - Kullanıcı herhangi bir birim filtreleme özelliğini kullanmamıştır.
    - Kullanıcı birim arama kutucuğunu kullanmamıştır.
- Amaç: Kullanıcının Açık Pozisyonlar sayfasında yer alan iş arama kutucuğunda herhangi bir arama işlemi yapmaması sonucunda sistemin çıktısı test edilmektedir.
- Test Adımları:
    - Test Case ID: TC003- Açık Pozisyonlar Menüsünün Tıklanabilirliği ve İçeriği  testini uygula.
    - İş ilanı arama kutucuğunda herhangi bir işlemde bulunma.
    - İş ilanları listesini görüntüle 
- Fail Criteria:
    - Kullanıcı tüm iş ilanlarını görüntüleyememektedir.
- Beklenen Sonuçlar: Kullanıcı tüm iş ilanlarını görüntüleyebilmektedir.

- Test Case ID: TC041 - İş İlanı Arama Sözcüğünün Kullanılması 
    - Ön Koşullar:
        - Kullanıcı herhangi bir birim filtreleme işlemi yapmamıştır.
        - Kullanıcı herhangi bir birim arama sözcüğünü kullanmamıştır.
        - Kullanıcının aramış olduğuı iş alanı sözcüğü halihazırda iş ilanlarında yer almaktadır.
    - Amaç: Kullanıcının iş ilanı arama kutucuğunu kullanarak iş ilanı aradığı durumlarda sistemin çıktısını test etmek

    - Test Adımları:
        - Test Case ID: TC003- Açık Pozisyonlar Menüsünün Tıklanabilirliği ve İçeriği  testini uygula.
        - İş ilanı arama kutucuğuna istenilen sözcükleri yaz.
        - İş ilanlarını görüntüle.
    
    - Fail Criteria:
        - Kullanıcı aramakta olduğu iş ilanlarını görüntüleyememektedir.
    
    - Beklenen Sonuçlar: Kullanıcı aramakta olduğu iş ilanları listesini görüntülemektedir.

- Test Case ID: TC042 - Kullanıcının İş İlanı Bulunmayan Sözcükleri Aratması 
- Ön Koşullar:
    - Kullanıcı herhangi bir birim filtrelemesi yapmamıştır.
    - Kullanıcı birim arama kutucuğunu kullanmamıştır.
    - Kullanıcının iş ilanı arama kutucuğuna yazdığı sözcükle ilgili bir iş ilanı halihazırda bulunmamaktadır.

- Amaç: Kullanıcının iş ilanı arama kutusuna yazmış olduğu sözcükle ilgili halihazırda bir iş ilanının bulunmadığı durumlarda sistemin çıktısı test edilmektedir.

- Test Adımları:
    - Test Case ID: TC003- Açık Pozisyonlar Menüsünün Tıklanabilirliği ve İçeriği  testini uygula.
    - İş ilanı arama kutucuğuna aranmak istenen işi yaz.
    - İş ilanlarını görüntüle.

- Fail Criteria:  
    - Kullanıcının aramış olduğu sözcükle ilgili iş ilanları olmamasına rağmen iş ilanlarında alakasız bir iş ilanının görüntülenmesi
- Beklenen Sonuçlar: Kullanıcı herhangi bir iş ilanı görüntülememektedir.

<br><br><br>

9.Test Senaryo İsmi: İş Birimi Filtrelerinin Temizlenmesi İşleminin Test Edilmesi 
- Test ID: TS009 
- Ön Koşullar:
    - Baykar Kariyer websitesi erişilebilir olmalıdır ve kullanıcının geçerli bir internet bağlantısı bulunmaktadır.

- Amaç: Kullanıcının iş birimleri filtreleme özelliğini kullandıktan sonra "Filtreleri Temizle" butonuna tıklamasıyla var olan tüm filtrelerin temizlenmesi işleminin test edilmesi amaçlanmaktadır.

- Test Adımları:
    - Baykar Kariyer websitesini görüntüle.
    - "AÇIK POZİSYONLAR" adlı bağlantıya tıkla.
    - Sayfanın sol tarafında yer alan iş birimi filtreleme özelliklerinden bir veya birden fazlasını kullan.
    - İş ilanlarını görüntüle.
    - "Filtreleri Temizle" butonuna tıkla.
    - Filtrelerin temizlendiğini doğrula.
    - Tekrardan iş ilanlarını görüntüle.

- Fail Criteria:
    - Filtrelerin temizlenmemesi
    - Tüm iş ilanlarının görüntülenmemesi
- Beklenen Sonuçlar: Kullanıcı, halihazırda seçilmiş olan birim filtreleri temizlemiş ve tüm iş ilanlarını görüntülemiştir.

    









