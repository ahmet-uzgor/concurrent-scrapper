from concurScraper import palmolive_gul,palmolive_pamuk,palmolive_keten
migros_path_list = {
    'result_figures': "(//div[@class='product-card product-action '])[%d]/form/div/figure",
    'result_titles': "(//h5[@class='title product-card-title'])[%d]",
    'search': "search",
    'product_description': "//h1[@class='seo title']",
    'packshot': "(//img[@id='carouselImage-0'])[1]",
    'numbers_of_packshot' : "//div[@class='image-cell']",
    'rich_content': "//li[@class='product-page-tab-list--item active']",
    'brand': "//span[@class='sup-title']/strong/a",
    'category': "//li[@class='main'][position() = last()]/a/span",
    'discount_rate': "//span[@class='wis-disc-t-27572']",
    'primary_price': "//span[@id='store-product-primary-price']",
    'activity_price': "//span[@id='store-product-primary-discounted-price']"
}

c4_path_list = {
    'result_figures': "(//span[@class='thumb'])[%d]/img",
    'result_titles': "(//span[@class='item-name'])[%d]",
    'search': "js-site-search-input",
    'product_description': "//div[@class='name']/h1",
    'packshot': "(//img[@class='lazyOwl '])[1]",
    'numbers_of_packshot' : "//div[@class='owl-item']",
    'rich_content': "//li[@id='accessibletabsnavigation0-0']/a",
    'brand': "//div[@class='brand']/span/a",
    'category': "//ol[@class='breadcrumb']/li[position()= last()-1]/a",
    'discount_rate': "//span[@class='discount-badge']",
    'activity_price': "//span[@class='priceLineThrough']",
    'primary_price': "//span[@class='item-price']"
    
}

watsons_path_list = {
    'product_description': "//h1[@class='product-detail-name my-3 mt-md-0']",
    'packshot': "(//img[@class='detail-zoom'])[1]",
    'numbers_of_packshot' : "//li[@class='mb-md-2 text-center d-inline-block d-md-block mr-1 mr-md-0']",
    'rich_content': "//a[@class='nav-link active']",
    'brand': "//h2[@class='detail-brand-name h5']",
    'category': "//ol[@class='long-breadcrumb breadcrumb m-0 rounded-0 bg-white px-0 d-none d-md-flex position-relative']/li[position() = last()-1]",
    'discount_rate': "(//div[@class='sac-badge-container'])[1]",
    'primary_price': "//s[@class='detail-price detail-old-price roboto-medium text-site-medium-gray']",
    'activity_price': "//span[@class='detail-price text-site-pink roboto-black']"
}

gratis_path_list = {
    'product_description': "//h1[@data-bind='text: displayName']",
    'packshot': "//img[@class='ccz-small img-responsive']",
    'numbers_of_packshot' : "//div[@class='col-md-3 thumbnail-container']",
    'rich_content': "//a[@class='active']",
    'brand': "//a[@class='manufacturer']",
    'category': "//ul[@class='breadcrumb']/li[position() = last() -1]",
    'discount_rate': "//div[@class='price-card__left-section list-price-card__left-section border-radius-start']/span/span",
    'primary_price': "(//div[@class='price-card__right-section list-price-card__right-section border-radius-end']/g-price/span/span[@class='gr-price__amount'])[1]",
    'activity_price': "(//div[@class='price-card__right-section list-price-card__right-section border-radius-end']/g-price/span/span[@class='gr-price__amount'])[2]"
}

hepsiburada_path_list = {
    'product_description': "//h1[@id='product-name']",
    'packshot': "//img[@class='product-image']",
    'numbers_of_packshot' : "//img[@class='product-image']",
    'rich_content': "//a[@id='productDescription']",
    'brand': "(//span[@class='brand-name']/a)[1]",
    'category': "//ul[@class='breadcrumbs']/li[position() = last() -1]",
    'discount_rate': "//span[@class='discount-amount']",
    'primary_price': "//del[@id='originalPrice']",
    'activity_price': "//span[@id='offering-price']" # .get_attribute('content')
}

trendyol_path_list = {
    'product_description': "//div[@class='pr-in-cn']/h1/div/span",
    'packshot': "//img[@class='ph-gl-img']",
    'numbers_of_packshot' : "(//div[@class='slick-track'])[1]/div",
    'rich_content': "//div[@class='pr-in-at-tl']",
    'brand': "//div[@class='pr-in-cn']/h1/a",
    'category': "//div[@class='breadcrumb full-width']/a[position() = last() -1]",
    'discount_rate': "//div[@class='dsc-prcn']",
    'primary_price': "(//span[@class='prc-org'])[1]",
    'activity_price': "(//span[@class='prc-slg'])[1]"
}

work_list = [['Migros', palmolive_pamuk, migros_path_list], 
            ['Migros', palmolive_gul, migros_path_list], 
            ['Migros', palmolive_keten, migros_path_list],
            ['C4', palmolive_pamuk, c4_path_list],
            ['C4', palmolive_gul, c4_path_list],
            ['C4', palmolive_keten, c4_path_list]]