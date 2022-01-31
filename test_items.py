from selenium import webdriver
import pytest
import os 
import time


#Тест для проверки запуска автотестов для разных языков интерфейса

class TestMainPage():
    def test_link(self, browser):
        link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        browser.get(link)
        time.sleep(15)  
        button = len(browser.find_elements_by_css_selector(".btn-add-to-basket"))
        assert button>0, 'Кнопка не найдена! Проверьте написание селектора.'
        
if __name__ == "__main__":
    pytest.main()