import unittest
from selenium import webdriver
import time
from pageIndex import PageIndex  #De mi archivo pageIndex importame la clase PageIndex
from pageItems import PageItems 

class SearchCases(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Chrome('chromedriver.exe')
        self.driver.get('http://automationpractice.com/index.php')
        self.indexPage = PageIndex(self.driver) #le paso el web driver a la clase PageIndex
        self.itemsPage = PageItems(self.driver)

    def test_search_no_elements(self):
        # self.driver.find_element_by_id('search_query_top').send_keys('hola')
        # self.driver.find_element_by_name('submit_search').click()
        self.indexPage.search('hola')
        time.sleep(2)
        # self.assertEqual(self.driver.find_element_by_xpath('//*[@id="center_column"]/p').text, 'No results were found for your search "hola"')
        self.assertEqual(self.itemsPage.return_no_element_text(), 'No results were found for your search "hola"')


    def test_search_find_dresses(self):
        # self.driver.find_element_by_id('search_query_top').send_keys('dress')
        # self.driver.find_element_by_name('submit_search').click()
        self.indexPage.search('dress')
        time.sleep(2)
        # self.assertTrue('DRESS' in self.driver.find_element_by_xpath('//*[@id="center_column"]/p').text)
        self.assertTrue('DRESS' in self.itemsPage.return_section_title())


    def test_search_find_tshirts(self):
        # self.driver.find_element_by_id('search_query_top').send_keys('t-shirt')
        # self.driver.find_element_by_name('submit_search').click()
        self.indexPage.search('t-shirt')
        time.sleep(2)
        # self.assertTrue('T-SHIRT' in self.driver.find_element_by_xpath('//*[@id="center_column"]/h1/span[1]').text)
        self.assertTrue('T-SHIRT' in self.itemsPage.return_section_title())

    def tearDown(self):
        self.driver.close()
        self.driver.quit() 

if __name__ == '__main__':
    unittest.main()