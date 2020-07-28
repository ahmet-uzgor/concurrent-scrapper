retailer_links = {
    'Migros': 'https://www.migros.com.tr/',
    'C4': 'https://www.carrefoursa.com/tr/',
    'Watsons': 'https://www.watsons.com.tr/',
    'Gratis': 'https://www.gratis.com/tr',
    'Hepsiburada': 'https://www.hepsiburada.com/',
    'Trendyol': 'https://www.trendyol.com/'
}

class Products():
    def __init__(self, p_description, p_barcode, hepsiburada_p_code, trendyol_p_code,):
        # initialize all product information 
        self.p_decription = p_description
        self.p_barcode = p_barcode
        self.hepsiburada_p_code = hepsiburada_p_code
        self.trendyol_p_code = trendyol_p_code

    def get_all_product_info(self): # It prints all info of Products class
        print(self.p_decription, self.p_barcode, self.hepsiburada_p_code, self.trendyol_p_code, end='\n')

    def getDescription(self): # It returns only description
        return self.p_decription

    def setDescription(self, description): # It returns only description
        self.p_decription = description

    def getBarcode(self): # It returns only barcode
        return self.p_barcode

    def setBarcode(self, barcode): # Setter of Barcode
        self.p_barcode = barcode

    def getHepsiburadaCode(self): # It returns only Hepsiburada product code
        return self.hepsiburada_p_code

    def setHepsiburadaCode(self, hepsiburada_code): # Setter of Hepsiburada product code
        self.hepsiburada_p_code = hepsiburada_code

    def getTrendyolCode(self): # It returns Trendyol product code
        return self.trendyol_p_code

    def setTrendyolCode(self, trendyol_code): # Setter of Trendyol product code
        self.trendyol_p_code = trendyol_code


