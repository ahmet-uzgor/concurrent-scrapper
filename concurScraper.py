import time
from pathList import *
from retailer import *
from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import concurrent.futures 
import pymysql.cursors


# Product Creation for Product Searching
palmolive_pamuk = Products('Palmolive Micellar Care Pamuk Özlü Duş Jeli 500 Ml', '8693495054270', 'HBV00000JVXND', '8693495054270')
palmolive_gul = Products('Palmolive Micellar Care Gül Özlü Duş Jeli 500 Ml', '8693495054256', 'HBV00000JVXNL', '8693495054256')
palmolive_keten = Products('Palmolive Micellar Care Keten Tohumu Özlü Duş Jeli 500 Ml', '8693495054294', 'HBV00000JVXNP', '8693495054294')


# Classes Functions
def initializer(): # It initializes and set necessary options
    driver = webdriver.Firefox()
    return driver

def thread_function(retailer_f, product_f, path_list_f): # It creates a class for scraping
    scraper = MigrosAndC4Scraper(retailer_f, product_f, path_list_f)

def scheduled_thread(): # It starts threads to scrape retailer's products
    length = len(work_list)
    while True:
        with concurrent.futures.ThreadPoolExecutor(max_workers=length) as executor:
            for i in range(length):
                executor.submit(thread_function(work_list[i][0], work_list[i][1], work_list[i][2]))
        time.sleep(100)

class MigrosAndC4Scraper():
    def __init__(self, retailer, product, path_list): # Data initialization and settings configuration
        self.retailer = retailer
        self.product = product
        self.path_list = path_list
        self.product_description = ''
        self.packshot = ''
        self.numbers_of_packshot = ''
        self.rich_content =  True
        self.brand = ''
        self.category = ''
        self.discount_rate = '%0'
        self.primary_price = ''
        self.activity_price = ''
        self.driver = initializer()
        self.run_and_scrape()

    def search_product(self): # It searches product on Migros website 
        self.driver.get(retailer_links[self.retailer])
        # Wait for loading page / it waits until search box loaded
        WebDriverWait(self.driver, 100).until(
            EC.presence_of_element_located((By.ID, self.path_list['search']))
        )
        # It finds search box
        search = self.driver.find_element_by_id(self.path_list['search'])
        # It enters searching input 
        search.clear()
        search.send_keys(self.product.getDescription())
        search.send_keys(Keys.ENTER)

    def click_to_product(self): # It waits until search completed and click product to go product page
        time.sleep(15)
        i = 1
        # WebDriverWait(self.driver, 100).until(
        #     EC.presence_of_element_located((By.XPATH, (self.path_list['result_figures'] %i)))
        # )
        # İf website shows multiple results , it looks for product that same name with searched product
        if (self.retailer == 'C4'):
            self.driver.find_element_by_xpath(self.path_list['result_figures'] %i).click()
            time.sleep(10)
        else :
            for i in range(1,5):
                try:
                    elem = self.driver.find_element_by_xpath(self.path_list['result_figures'] %i)
                    title_of_product = self.driver.find_element_by_xpath(self.path_list['result_titles'] %i).text
                    if (self.product.getDescription() == title_of_product):
                        elem.click()
                        time.sleep(10)
                        return 'Matched'
                except:
                    print('hi')
        #self.driver.find_element_by_xpath("(//div[@class='product-card product-action '])[%d]/form/div/figure" %i).click()
        

    def get_infos(self): # It finds all necessary information for given product and prints infos
        self.product_description = self.driver.find_element_by_xpath(self.path_list['product_description']).text
        self.packshot = self.driver.find_element_by_xpath(self.path_list['packshot']).get_attribute('src')
        self.numbers_of_packshot = self.packshot_counter()
        self.brand = self.driver.find_element_by_xpath(self.path_list['brand']).text
        self.category = self.driver.find_element_by_xpath(self.path_list['category']).text 
        self.primary_price = self.driver.find_element_by_xpath(self.path_list['primary_price']).text
        try:    
            self.discount_rate = self.driver.find_element_by_xpath(self.path_list['discount_rate']).text
            self.activity_price = self.driver.find_element_by_xpath(self.path_list['activity_price']).text
        except :
            print('No discount')
            self.activity_price = self.primary_price 
        # Print all infos
        print(self.product_description, self.packshot,
        self.numbers_of_packshot, self.rich_content,
        self.brand, self.category, self.discount_rate,
        self.primary_price, self.activity_price, end='\n')
        self.driver.close()

    def packshot_counter(self): # It manipulate given element and calculates packsot numbers
        count = 0
        packshots = self.driver.find_elements_by_xpath(self.path_list['numbers_of_packshot'])
        for packshot in packshots: # it calculates all packshots and give total number
            count += 1
        # return total number of packshot
        return (count+1)/2

    def write_to_mysql(self): # It connects to mysql and writes datas
        db = pymysql.connect(host='localhost',
        user='web-scraping',
        password='ahmet123',
        db='retailer_products',
        charset='utf8mb4',
        cursorclass= pymysql.cursors.DictCursor)
        # Login to mysql is settled.
        connection = db.cursor() # Mysql connection cursor
        # Insert scraped datas to Mysql tables
        result = connection.execute('INSERT INTO product_scrape VALUES(%s, %s, %s, %f, %s, %s, %s, %s, %s, %s)', 
        (self.retailer, self.product_description, self.packshot, self.numbers_of_packshot, 
        self.rich_content, self.brand, self.category, self.discount_rate, self.primary_price, self.activity_price))
        db.commit()
        print(str(result) + " product info added") # It prints when any data inserted to table

    
    def run_and_scrape(self): # It runs necessary functions respectively to scrape retailers website 
        self.search_product()
        self.click_to_product()
        self.get_infos()
        #self.write_to_mysql()
    


# Main
if __name__ == "__main__":
    scheduled_thread()


# // Options for retailers
# 'Migros
# 'C4
# 'Watsons
# 'Gratis
# 'Hepsiburada
# 'Trendyol