from locust import HttpUser,task,between,constant
import random


class BaykarKariyer(HttpUser):
    bekleme_suresi = constant(1)
    open_positions = "https://kariyer.baykartech.com/tr/basvuru/acik-pozisyonlar"
    register_user_url= "https://kariyer.baykartech.com/tr/hesaplar/signup/"
    home_page = "https://kariyer.baykartech.com/"
    
    @task 
    def get_homepage(self):
        self.client.get(self.home_page)
    
    @task 
    def view_open_positions(self):
        self.client.get(self.open_positions)
        
    @task
    def register_user(self):
        self.client.get(self.register_user_url)