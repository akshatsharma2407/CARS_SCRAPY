!pip install selenium
!pip install webdriver-manager
!sudo apt-get update
!sudo apt-get install -y wget gnupg unzip
!wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
!sudo apt-get install -y ./google-chrome-stable_current_amd64.deb


import time,random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import requests
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager



urls = [
        'https://www.cars.com/shopping/tesla-model_3/?include_shippable=false&maximum_distance=all&stock_type=all&page_size=100',
        'https://www.cars.com/shopping/tesla-model_s/?include_shippable=false&maximum_distance=all&stock_type=all&page_size=100',
        'https://www.cars.com/shopping/nissan-leaf/?include_shippable=false&maximum_distance=all&stock_type=all&page_size=100',
        'https://www.cars.com/shopping/tesla-model_y/?include_shippable=false&maximum_distance=all&stock_type=all&page_size=100',
        'https://www.cars.com/shopping/ford-mustang_mach_e/?include_shippable=false&maximum_distance=all&stock_type=all&page_size=100',
        'https://www.cars.com/shopping/ford-f_150_lightning/?include_shippable=false&maximum_distance=all&stock_type=all&page_size=100',
        'https://www.cars.com/shopping/bmw-i3/?include_shippable=false&maximum_distance=all&stock_type=all&page_size=100',
        'https://www.cars.com/shopping/volkswagen-id.4/?include_shippable=false&maximum_distance=all&stock_type=all&page_size=100',


        # 'https://www.cars.com/shopping/jeep-grand_cherokee/?include_shippable=false&maximum_distance=all&stock_type=all&page_size=100',
        # 'https://www.cars.com/shopping/toyota-4runner/?include_shippable=false&maximum_distance=all&stock_type=all&page_size=100',
        # 'https://www.cars.com/shopping/chevrolet-tahoe/?include_shippable=false&maximum_distance=all&stock_type=all&page_size=100',
        # 'https://www.cars.com/shopping/jeep-wrangler/?include_shippable=false&maximum_distance=all&stock_type=all&page_size=100',
        # 'https://www.cars.com/shopping/ford-explorer/?include_shippable=false&maximum_distance=all&stock_type=all&page_size=100',
        # 'https://www.cars.com/shopping/toyota-rav4/?include_shippable=false&maximum_distance=all&stock_type=all&page_size=100',
        # 'https://www.cars.com/shopping/jeep-wrangler_unlimited/?include_shippable=false&maximum_distance=all&stock_type=all&page_size=100',
        # 'https://www.cars.com/shopping/toyota-highlander/?include_shippable=false&maximum_distance=all&stock_type=all&page_size=100',
        # 'https://www.cars.com/shopping/ford-bronco/?include_shippable=false&maximum_distance=all&stock_type=all&page_size=100',


        # 'https://www.cars.com/shopping/toyota-camry/?include_shippable=false&maximum_distance=all&stock_type=all&page_size=100',
        # 'https://www.cars.com/shopping/honda-accord/?include_shippable=false&maximum_distance=all&stock_type=all&page_size=100',
        # 'https://www.cars.com/shopping/dodge-charger/?include_shippable=false&maximum_distance=all&stock_type=all&page_size=100',
        # 'https://www.cars.com/shopping/honda-civic/?include_shippable=false&maximum_distance=all&stock_type=all&page_size=100',
        # 'https://www.cars.com/shopping/toyota-corolla/?include_shippable=false&maximum_distance=all&stock_type=all&page_size=100',
        # 'https://www.cars.com/shopping/mercedes_benz-s_class/?include_shippable=false&maximum_distance=all&stock_type=all&page_size=100',
        # 'https://www.cars.com/shopping/nissan-altima/?include_shippable=false&maximum_distance=all&stock_type=all&page_size=100',
        # 'https://www.cars.com/shopping/chevrolet-malibu/?include_shippable=false&maximum_distance=all&stock_type=all&page_size=100',
        # 'https://www.cars.com/shopping/mercedes_benz-c_class/?include_shippable=false&maximum_distance=all&stock_type=all&page_size=100',
        

        # 'https://www.cars.com/shopping/ford-f_150/?include_shippable=false&maximum_distance=all&stock_type=all&page_size=100',
        # 'https://www.cars.com/shopping/chevrolet-silverado_1500/?include_shippable=false&maximum_distance=all&stock_type=all&page_size=100',
        # 'https://www.cars.com/shopping/gmc-sierra_1500/?include_shippable=false&maximum_distance=all&stock_type=all&page_size=100',
        # 'https://www.cars.com/shopping/toyota-tundra/?include_shippable=false&maximum_distance=all&stock_type=all&page_size=100',
        # 'https://www.cars.com/shopping/toyota-tacoma/?include_shippable=false&maximum_distance=all&stock_type=all&page_size=100',
        # 'https://www.cars.com/shopping/ford-f_250/?include_shippable=false&maximum_distance=all&stock_type=all&page_size=100',
        # 'https://www.cars.com/shopping/chevrolet-silverado_2500/?include_shippable=false&maximum_distance=all&stock_type=all&page_size=100',
        # 'https://www.cars.com/shopping/jeep-gladiator/?include_shippable=false&maximum_distance=all&stock_type=all&page_size=100',
        # 'https://www.cars.com/shopping/gmc-sierra_2500/?include_shippable=false&maximum_distance=all&stock_type=all&page_size=100',

        # 'https://www.cars.com/shopping/bmw-x5/?include_shippable=false&maximum_distance=all&stock_type=all&page_size=100',
        # 'https://www.cars.com/shopping/lexus-rx_350/?include_shippable=false&maximum_distance=all&stock_type=all&page_size=100',
        # 'https://www.cars.com/shopping/mercedes_benz-s_class/?include_shippable=false&maximum_distance=all&stock_type=all&page_size=100',
        # 'https://www.cars.com/shopping/acura-mdx/?include_shippable=false&maximum_distance=all&stock_type=all&page_size=100',
        # 'https://www.cars.com/shopping/porsche-cayenne/?include_shippable=false&maximum_distance=all&stock_type=all&page_size=100',
        # 'https://www.cars.com/shopping/mercedes_benz-e_class/?include_shippable=false&maximum_distance=all&stock_type=all&page_size=100',
        # 'https://www.cars.com/shopping/bmw-x3/?include_shippable=false&maximum_distance=all&stock_type=all&page_size=100',
        # 'https://www.cars.com/shopping/mercedes_benz-c_class/?include_shippable=false&maximum_distance=all&stock_type=all&page_size=100',
        # 'https://www.cars.com/shopping/audi-q5/?include_shippable=false&maximum_distance=all&stock_type=all&page_size=100',
        # 'https://www.cars.com/shopping/lexus-es_350/?include_shippable=false&maximum_distance=all&stock_type=all&page_size=100',

        # 'https://www.cars.com/shopping/honda-cr_v/?include_shippable=false&maximum_distance=all&stock_type=all&page_size=100',
        # 'https://www.cars.com/shopping/toyota-rav4/?include_shippable=false&maximum_distance=all&stock_type=all&page_size=100',
        # 'https://www.cars.com/shopping/toyota-highlander/?include_shippable=false&maximum_distance=all&stock_type=all&page_size=100',
        # 'https://www.cars.com/shopping/ford-escape/?include_shippable=false&maximum_distance=all&stock_type=all&page_size=100',
        # 'https://www.cars.com/shopping/honda-pilot/?include_shippable=false&maximum_distance=all&stock_type=all&page_size=100',
        # 'https://www.cars.com/shopping/nissan-rogue/?include_shippable=false&maximum_distance=all&stock_type=all&page_size=100',
        # 'https://www.cars.com/shopping/subaru-forester/?include_shippable=false&maximum_distance=all&stock_type=all&page_size=100',
        # 'https://www.cars.com/shopping/mazda-cx_5/?include_shippable=false&maximum_distance=all&stock_type=all&page_size=100',
        # 'https://www.cars.com/shopping/chevrolet-traverse/?include_shippable=false&maximum_distance=all&stock_type=all&page_size=100',
        # 'https://www.cars.com/shopping/ford-edge/?include_shippable=false&maximum_distance=all&stock_type=all&page_size=100',

        # 'https://www.cars.com/shopping/toyota-rav4_hybrid/?include_shippable=false&maximum_distance=all&stock_type=all&page_size=100',
        # 'https://www.cars.com/shopping/toyota-highlander_hybrid/?include_shippable=false&maximum_distance=all&stock_type=all&page_size=100',
        # 'https://www.cars.com/shopping/toyota-sequoia/hybrid/?include_shippable=false&maximum_distance=all&stock_type=all&page_size=100',
        # 'https://www.cars.com/shopping/toyota-sienna/hybrid/?include_shippable=false&maximum_distance=all&stock_type=all&page_size=100',
        # 'https://www.cars.com/shopping/ford-f_150/hybrid/?include_shippable=false&maximum_distance=all&stock_type=all&page_size=100',
        # 'https://www.cars.com/shopping/honda-accord_hybrid/?include_shippable=false&maximum_distance=all&stock_type=all&page_size=100',
        # 'https://www.cars.com/shopping/honda-cr_v_hybrid/?include_shippable=false&maximum_distance=all&stock_type=all&page_size=100',
        # 'https://www.cars.com/shopping/toyota-camry_hybrid/?include_shippable=false&maximum_distance=all&stock_type=all&page_size=100',
        # 'https://www.cars.com/shopping/ford-maverick/?include_shippable=false&maximum_distance=all&stock_type=all&page_size=100',
        # 'https://www.cars.com/shopping/ford-fusion_hybrid/?include_shippable=false&maximum_distance=all&stock_type=all&page_size=100',

        # 'https://www.cars.com/shopping/ford-f_250/?include_shippable=false&maximum_distance=all&stock_type=all&page_size=100',
        # 'https://www.cars.com/shopping/ford-f_350/?include_shippable=false&maximum_distance=all&stock_type=all&page_size=100',
        # 'https://www.cars.com/shopping/chevrolet-silverado_2500/?include_shippable=false&maximum_distance=all&stock_type=all&page_size=100',
        # 'https://www.cars.com/shopping/gmc-sierra_1500/?include_shippable=false&maximum_distance=all&stock_type=all&page_size=100',
        # 'https://www.cars.com/shopping/gmc-sierra_2500/?include_shippable=false&maximum_distance=all&stock_type=all&page_size=100',
        # 'https://www.cars.com/shopping/chevrolet-silverado_1500/?include_shippable=false&maximum_distance=all&stock_type=all&page_size=100',
        # 'https://www.cars.com/shopping/chevrolet-silverado_3500/?include_shippable=false&maximum_distance=all&stock_type=all&page_size=100',
        # 'https://www.cars.com/shopping/gmc-sierra_3500/?include_shippable=false&maximum_distance=all&stock_type=all&page_size=100',
        # 'https://www.cars.com/shopping/mercedes_benz-sprinter_2500/?include_shippable=false&maximum_distance=all&stock_type=all&page_size=100',
        # 'https://www.cars.com/shopping/jeep-wrangler_unlimited/?include_shippable=false&maximum_distance=all&stock_type=all&page_size=100',

        # 'https://www.cars.com/shopping/ford-mustang/?include_shippable=false&maximum_distance=all&stock_type=all&page_size=100',
        # 'https://www.cars.com/shopping/dodge-challenger/?include_shippable=false&maximum_distance=all&stock_type=all&page_size=100',
        # 'https://www.cars.com/shopping/chevrolet-corvette/?include_shippable=false&maximum_distance=all&stock_type=all&page_size=100',
        # 'https://www.cars.com/shopping/porsche-911/?include_shippable=false&maximum_distance=all&stock_type=all&page_size=100',
        # 'https://www.cars.com/shopping/chevrolet-camaro/?include_shippable=false&maximum_distance=all&stock_type=all&page_size=100',
        # 'https://www.cars.com/shopping/honda-civic/?include_shippable=false&maximum_distance=all&stock_type=all&page_size=100',
        # 'https://www.cars.com/shopping/bmw-m4/?include_shippable=false&maximum_distance=all&stock_type=all&page_size=100',
        # 'https://www.cars.com/shopping/honda-accord/?include_shippable=false&maximum_distance=all&stock_type=all&page_size=100',
        # 'https://www.cars.com/shopping/nissan-gt_r/?include_shippable=false&maximum_distance=all&stock_type=all&page_size=100',


        # 'https://www.cars.com/shopping/toyota-prius/?include_shippable=false&maximum_distance=all&stock_type=all&page_size=100',
        # 'https://www.cars.com/shopping/kia-soul/?include_shippable=false&maximum_distance=all&stock_type=all&page_size=100',
        # 'https://www.cars.com/shopping/nissan-leaf/?include_shippable=false&maximum_distance=all&stock_type=all&page_size=100',
        # 'https://www.cars.com/shopping/porsche-panamera/?include_shippable=false&maximum_distance=all&stock_type=all&page_size=100',
        # 'https://www.cars.com/shopping/honda-fit/?include_shippable=false&maximum_distance=all&stock_type=all&page_size=100',
        # 'https://www.cars.com/shopping/honda-civic/?include_shippable=false&maximum_distance=all&stock_type=all&page_size=100',
        # 'https://www.cars.com/shopping/tesla-model_s/?include_shippable=false&maximum_distance=all&stock_type=all&page_size=100',
        # 'https://www.cars.com/shopping/mazda-mazda3/?include_shippable=false&maximum_distance=all&stock_type=all&page_size=100',
        # 'https://www.cars.com/shopping/ford-focus/?include_shippable=false&maximum_distance=all&stock_type=all&page_size=100',


        # 'https://www.cars.com/shopping/chevrolet-bolt_ev/?include_shippable=false&maximum_distance=all&stock_type=all&page_size=100',
        # 'https://www.cars.com/shopping/mercedes_benz-e_class/?include_shippable=false&maximum_distance=all&stock_type=all&page_size=100',
        # 'https://www.cars.com/shopping/chrysler-pt_cruiser/?include_shippable=false&maximum_distance=all&stock_type=all&page_size=100',
        # 'https://www.cars.com/shopping/scion-xb/?include_shippable=false&maximum_distance=all&stock_type=all&page_size=100',
        # 'https://www.cars.com/shopping/mini-clubman/?include_shippable=false&maximum_distance=all&stock_type=all&page_size=100',
        # 'https://www.cars.com/shopping/audi-rs_6_avant/?include_shippable=false&maximum_distance=all&stock_type=all&page_size=100',
        # 'https://www.cars.com/shopping/toyota-prius_v/?include_shippable=false&maximum_distance=all&stock_type=all&page_size=100',
        # 'https://www.cars.com/shopping/volvo-xc70/?include_shippable=false&maximum_distance=all&stock_type=all&page_size=100',
        # 'https://www.cars.com/shopping/volkswagen-jetta_sportwagen/?include_shippable=false&maximum_distance=all&stock_type=all&page_size=100',

        # 'https://www.cars.com/shopping/ford-mustang/?include_shippable=false&maximum_distance=all&stock_type=all&page_size=100',
        # 'https://www.cars.com/shopping/chevrolet-corvette/?include_shippable=false&maximum_distance=all&stock_type=all&page_size=100',
        # 'https://www.cars.com/shopping/porsche-911/?include_shippable=false&maximum_distance=all&stock_type=all&page_size=100',
        # 'https://www.cars.com/shopping/chevrolet-camaro/?include_shippable=false&maximum_distance=all&stock_type=all&page_size=100',
        # 'https://www.cars.com/shopping/mazda-mx_5_miata/?include_shippable=false&maximum_distance=all&stock_type=all&page_size=100',
        # 'https://www.cars.com/shopping/porsche-boxster/?include_shippable=false&maximum_distance=all&stock_type=all&page_size=100',
        # 'https://www.cars.com/shopping/mercedes_benz-sl_class/?include_shippable=false&maximum_distance=all&stock_type=all&page_size=100',
        # 'https://www.cars.com/shopping/bmw-m4/?include_shippable=false&maximum_distance=all&stock_type=all&page_size=100',
        # 'https://www.cars.com/shopping/mercedes_benz-slk_class/?include_shippable=false&maximum_distance=all&stock_type=all&page_size=100',


        # 'https://www.cars.com/shopping/toyota-sienna/?include_shippable=false&maximum_distance=all&stock_type=all&page_size=100',
        # 'https://www.cars.com/shopping/honda-odyssey/?include_shippable=false&maximum_distance=all&stock_type=all&page_size=100',
        # 'https://www.cars.com/shopping/chrysler-pacifica/?include_shippable=false&maximum_distance=all&stock_type=all&page_size=100',
        # 'https://www.cars.com/shopping/dodge-grand_caravan/?include_shippable=false&maximum_distance=all&stock_type=all&page_size=100',
        # 'https://www.cars.com/shopping/chrysler-town_and_country/?include_shippable=false&maximum_distance=all&stock_type=all&page_size=100',
        # 'https://www.cars.com/shopping/kia-carnival/?include_shippable=false&maximum_distance=all&stock_type=all&page_size=100',
        # 'https://www.cars.com/shopping/kia-sedona/?include_shippable=false&maximum_distance=all&stock_type=all&page_size=100',
        # 'https://www.cars.com/shopping/chrysler-pacifica_hybrid/?include_shippable=false&maximum_distance=all&stock_type=all&page_size=100',
        # 'https://www.cars.com/shopping/ford-transit_connect/?include_shippable=false&maximum_distance=all&stock_type=all&page_size=100',
        # 'https://www.cars.com/shopping/nissan-nv200/?include_shippable=false&maximum_distance=all&stock_type=all&page_size=100',

        # 'https://www.cars.com/shopping/chevrolet-volt/?include_shippable=false&maximum_distance=all&stock_type=all&page_size=100',
        # 'https://www.cars.com/shopping/bmw-i8/?include_shippable=false&maximum_distance=all&stock_type=all&page_size=100',
        # 'https://www.cars.com/shopping/volvo-xc90_recharge_plug_in_hybrid/?include_shippable=false&maximum_distance=all&stock_type=all&page_size=100',
        # 'https://www.cars.com/shopping/bmw-330e/?include_shippable=false&maximum_distance=all&stock_type=all&page_size=100',
        # 'https://www.cars.com/shopping/porsche-cayenne/?include_shippable=false&maximum_distance=all&stock_type=all&page_size=100',
        # 'https://www.cars.com/shopping/toyota-rav4_prime/?include_shippable=false&maximum_distance=all&stock_type=all&page_size=100',
        # 'https://www.cars.com/shopping/ford-c_max_energi/?include_shippable=false&maximum_distance=all&stock_type=all&page_size=100',
        # 'https://www.cars.com/shopping/honda-clarity_plug_in_hybrid/?include_shippable=false&maximum_distance=all&stock_type=all&page_size=100',

        # 'https://www.cars.com/shopping/ford-transit_250/?include_shippable=false&maximum_distance=all&stock_type=all&page_size=100',
        # 'https://www.cars.com/shopping/mercedes_benz-sprinter_2500/?include_shippable=false&maximum_distance=all&stock_type=all&page_size=100',
        # 'https://www.cars.com/shopping/ford-transit_connect/?include_shippable=false&maximum_distance=all&stock_type=all&page_size=100',
        # 'https://www.cars.com/shopping/chevrolet-express_2500/?include_shippable=false&maximum_distance=all&stock_type=all&page_size=100',
        # 'https://www.cars.com/shopping/ford-transit_350/?include_shippable=false&maximum_distance=all&stock_type=all&page_size=100',
        # 'https://www.cars.com/shopping/ram-promaster_2500/?include_shippable=false&maximum_distance=all&stock_type=all&page_size=100',
        # 'https://www.cars.com/shopping/nissan-nv200/?include_shippable=false&maximum_distance=all&stock_type=all&page_size=100',
        # 'https://www.cars.com/shopping/gmc-savana_2500/?include_shippable=false&maximum_distance=all&stock_type=all&page_size=100',
        # 'https://www.cars.com/shopping/ram-promaster_1500/?include_shippable=false&maximum_distance=all&stock_type=all&page_size=100'
    ]

options = Options()
options.add_argument("--headless=new")   # required for Codespaces (no GUI)
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

car_details = []

# driver = webdriver.Chrome(options=options)

driver.maximize_window()

for url in set(urls):

    driver.get(url)

    wait = WebDriverWait(driver,5)

    n = 1

    while True:
        try:
            soup = BeautifulSoup(driver.page_source,'html.parser')
            for car in soup.find_all('a',attrs={'class':'vehicle-card-link js-gallery-click-link'}):
                full_link = 'https://www.cars.com/'+car.get('href')
                car_details.append(full_link)

            next_btn = wait.until(
                EC.element_to_be_clickable((By.XPATH,'//*[@id="next_paginate"]'))
            )
            if next_btn.get_attribute("disabled") is not None:
                raise KeyError 
        except:
            print('The next button is not clickable. We have navigated through all the pages')
            break
        else:
            n += 1
            print('navigating to next page : ',n)
            time.sleep(random.uniform(2,5))
            driver.execute_script("arguments[0].click();", next_btn)
            time.sleep(3)
