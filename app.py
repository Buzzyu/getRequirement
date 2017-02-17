#!/usr/bin/env python3
# coding=utf-8
from bs4 import BeautifulSoup
from urllib.request import urlopen
from selenium import webdriver

import re


driver = webdriver.PhantomJS()

def main():
    driver.get('') # edit the url here
    html = BeautifulSoup(driver.page_source, 'lxml')
    jobUrls = html.findAll('a', {'href': re.compile('')})
    
    info = []
    for url in jobUrls:
        info.append(getInfo(url))

def getInfo(url):
    driver.get(url)
    html = BeautifulSoup(driver.page_source, 'lxml')
    requirement = html.findAll('div', {'id': re.compile('')})
    return requirement

if __name__ == '__main__':
    main()
