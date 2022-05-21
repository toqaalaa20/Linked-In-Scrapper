# -*- coding: utf-8 -*-
"""
Created on Fri May 20 14:42:11 2022

@author: Toqa Alaa
"""

from selenium import webdriver
from bs4 import BeautifulSoup
import time
  
def job_scrapper(email, password):
    driver= webdriver.Chrome()
    driver.get('https://www.linkedin.com')
    driver.implicitly_wait(30)
    driver.find_element_by_id('session_key').send_keys(email)
    driver.find_element_by_id('session_password').send_keys(password)
    button= driver.find_element_by_class_name('sign-in-form__submit-button')
    button.click()
    driver.get('https://www.linkedin.com/jobs/collections/recommended/?currentJobId=3063260627')
    list1= driver.find_elements_by_css_selector('.job-card-container--clickable')
    job_src = driver.page_source
    soup = BeautifulSoup(job_src, 'lxml')   
    job_titles = []
    
    for i in list1:
        i.click()
        jobs_html = soup.find_all('a', {'class': 'job-card-list__title'})
        time.sleep((5))
        print('collected')
    
    for title in jobs_html:
        job_titles.append(title.text.strip())
    print(job_titles)
    
job_scrapper('abcd@gmail.com', '1234')

