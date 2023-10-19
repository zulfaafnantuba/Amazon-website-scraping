from amazon.api import AmazonAPI

# Replace these with your own Amazon API credentials
AMAZON_ACCESS_KEY = 'YourAccessKey'
AMAZON_SECRET_KEY = 'YourSecretKey'
AMAZON_ASSOC_TAG = 'YourAssociateTag'
AMAZON_API_REGION = 'US'  # Change this to your desired Amazon region

# Initialize the AmazonAPI
amazon = AmazonAPI(AMAZON_ACCESS_KEY, AMAZON_SECRET_KEY, AMAZON_ASSOC_TAG, region=AMAZON_API_REGION)

# Define a function to scrape product data from a URL
def scrape_product_data(url):
    try:
        # Extract ASIN (Amazon Standard Identification Number) from the URL
        asin = url.split('/')[-1]

        # Query the Amazon API to get product details
        product = amazon.lookup(ItemId=asin)
        
        return {
            'URL': url,
            'Description': product.title,
            'ASIN': asin,
            'Product Description': product.editorial_review,
            'Manufacturer': product.manufacturer
        }
    except Exception as e:
        print(f"Failed to retrieve data from {url}: {str(e)}")
        return None

# List of your 200 product URLs
product_urls = [
"https://www.amazon.com/Tetley-Green-Lemon-Honey-Bags/dp/B00MGFZGVK",
"https://www.amazon.com/Half-Moon-Laptop-Backpack-Polyester/dp/B09CMS3K2S",
"https://www.amazon.com/Impulse-Diggy-Backpack-Resistant-Green/dp/B0CJVCZZV",
"https://www.amazon.com/Bennett-Polyester-Drax-Ultrabook-Surfacepro/dp/B091NZ9MYB",
"https://www.amazon.com/Killer-Backpack-Compartments-Polyester-Waterproof/dp/B07CDD6YS2",
"https://www.amazon.com/Amazon-Brand-Presto-Oxo-Biodegradable-Garbage/dp/B0821PYKVK",
"https://www.amazon.com/Red-Lemon-Ironlook-Briefcase-Anti-Theft/dp/B09ZYMT7V1",
"https://www.amazon.com/Right-Choice-Stylish-College-Backpack/dp/B07ZVXDHCK",
"https://www.amazon.com/AmazonBasics-Vacuum-Compression-Storage-Medium/dp/B07RTJV6G4",
"https://www.amazon.com/Amazon-Brand-Presto-Oxo-Biodegradable-Garbage/dp/B0821QGBDY",
"https://www.amazon.com/TRUE-Emperor-Anti-Theft-backpack-charging/dp/B0BYB631NR",
"https://www.amazon.com/Tabelito-NEO-Backpack-Business-Compartment/dp/B0C2D2Q52R",
"https://www.amazon.com/Wildcraft-ltrs-Cms-backpack-204493566_black/dp/B07GNGG435",
"https://www.amazon.com/Murano-Casual-daybackpack-Office-College/dp/B0BX9GLFD6",
"https://www.amazon.com/Half-Moon-Laptop-Bag-Compartment/dp/B0C1NZLF67",
"https://www.amazon.com/HARISSONS-15-6-inch-Backpack-Organizers-Detachable/dp/B07M5P5LW3",
"https://www.amazon.com/s/?k=bags+for+girls&ref=sugsr_0&pd_rd_w=mof2S&content-id=amzn1.sym.1c7db1d2-1fe9-496b-8f07-8ed64c022066:amzn1.sym.1c7db1d2-1fe9-496b-8f07-8ed64c022066&pf_rd_p=1c7db1d2-1fe9-496b-8f07-8ed64c022066&pf_rd_r=KRFWJRE0T76AG24MFSBV&pd_rd_wg=3npA2&pd_rd_r=9bfe71f5-33dd-4008-97c9-87b2be49a071&qid=1697645090",
"https://www.amazon.com/gp/help/customer/display.html?nodeId=201889520",
"https://www.amazon.com/Newtone-Premium-OXO-Biodegradable-Garbage/dp/B08M5S2NQM",
"https://www.amazon.com/Shalimar-Premium-OXO-Biodegradable-Garbage/dp/B08DHSBP9S",
"https://www.amazon.com/Amazon-Basics-Laptop-College-Backpack/dp/B0C8NSJ4RD",
"https://www.amazon.com/G-1-Medium-Disposable-Garbage-Dustbin/dp/B077RJ1YMW",
"https://www.amazon.com/Half-Moon-Resistant-Backpack-Compartment/dp/B0BHX7GY16",
"https://www.amazon.com/gp/bestsellers/luggage/2917442031/ref=sr_bs_5_2917442031_1",
"https://www.amazon.com/Impulse-Diggy-Backpack-Business-Resistant/dp/B0CJHV6RTS",
"https://www.amazon.com/AirCase-C34-Laptop-Backpack-Women/dp/B07QN4KXWG",
"https://www.amazon.com/F-Gear-String-Polyester-33-cms-Black-Drawstring-Gym-Bag/dp/B07PC28YQ9",
"https://www.amazon.com/Half-Moon-Resistant-Backpack-Compartment/dp/B0BYW5SH4L",
"https://www.amazon.com/DZert-School-Polyester-Backpack-White/dp/B07GXYHFCY",
"https://www.amazon.com/ADISA-Laptop-Backpack-Office-College/dp/B09TPVD964",
"https://www.amazon.com/Laptops-College-Backpack-Charging-Anti-Theft/dp/B0C6639P8P",
"https://www.amazon.com/Shalimar-Premium-Garbage-Extra-Colour/dp/B07KSZTYWX",
"https://www.amazon.com/LOOKMUSTER-Waterproof-Backpack-College-Business/dp/B0BS6YGKMC",
"https://www.amazon.com/PUMA-Casual-Backpack-IND-Black-CASTLEROCK/dp/B08BTD8YZP",
"https://www.amazon.com/s/?k=bags+for+girls&ref=sugsr_0&pd_rd_w=b8Fxa&content-id=amzn1.sym.1c7db1d2-1fe9-496b-8f07-8ed64c022066:amzn1.sym.1c7db1d2-1fe9-496b-8f07-8ed64c022066&pf_rd_p=1c7db1d2-1fe9-496b-8f07-8ed64c022066&pf_rd_r=SQXMR1064E0178AW3DA3&pd_rd_wg=7j5Mc&pd_rd_r=e2094052-5634-4f10-8223-bd73a1e9d80d&qid=1697645092",
"https://www.amazon.com/gp/help/customer/display.html?nodeId=201889520",
"https://www.amazon.com/Purple-Tree-Canvas-Tote-Women/dp/B07PLCCQVC""/Kleeno-Cello-Clean-Garbage-Medium/dp/B09C284CTH",
"https://www.amazon.com/Amazon-Brand-Presto-Oxo-Biodegradable-Garbage/dp/B08TDCGCPK",
"https://www.amazon.com/Corduroy-Reusable-Shopping-Washable-Shoulder/dp/B0BNX437F8",
"https://www.amazon.com/ASUS-VP4700-Backpack-Reflective-Suitable/dp/B0937G637K",
"https://www.amazon.com/Stylbase-Trends-Polyester-Character-Embossed/dp/B0BNL2PBPH",
"https://www.amazon.com/SPENZ-BAGS-Backpack-Raincover-Mahogany-Brown/dp/B0C3RN6QSC",
"https://www.amazon.com/DZert-Polyester-Black-White-Backpack/dp/B07GXX2BP3",
"https://www.amazon.com/AirCase-C24-Messenger-Shoulder-Compartments/dp/B07Y3DB5YZ",
"https://www.amazon.com/Arctic-Fox-Anti-Theft-Backpack-Charging/dp/B089Q9TM16",
"https://www.amazon.com/Amazon-Brand-Reusable-Eco-Friendly-Multi-Purpose/dp/B08TTMMGYT",
"https://www.amazon.com/Wildcraft-Music-Backpack-Green-11954/dp/B07N2SBX54",
"https://www.amazon.com/American-Tourister-Backpack-Organizer-Compatible/dp/B0C8649NY8",
"https://www.amazon.com/American-Tourister-Harp-Duffle-Grey/dp/B0BTHP5LS1",
"https://www.amazon.com/Amazon-Basics-Messenger-Shoulder-MacBook/dp/B00DUGZFWY",
"https://www.amazon.com/Business-Casual-Compartment-Resistant-Backpack/dp/B08N6HSJJ5",
"https://www.amazon.com/s/?k=bags+for+girls&ref=sugsr_0&pd_rd_w=dMe42&content-id=amzn1.sym.1c7db1d2-1fe9-496b-8f07-8ed64c022066:amzn1.sym.1c7db1d2-1fe9-496b-8f07-8ed64c022066&pf_rd_p=1c7db1d2-1fe9-496b-8f07-8ed64c022066&pf_rd_r=8YVJ69GRCD291JD910JX&pd_rd_wg=XdinJ&pd_rd_r=d4053c21-92b5-48e4-b00c-06a6c5da54bd&qid=1697645095",
"https://www.amazon.com/gp/help/customer/display.html?nodeId=201889520",
"https://www.amazon.com/Lify-Womens-Shoulder-Crossbody-Handbag/dp/B09JWKDG6R",
"https://www.amazon.com/Wesley-Anti-Theft-backpack-Executive-Waterproof/dp/B08K7PCPJV",
"https://www.amazon.com/Adjustable-Waterproof-Breathable-Anti-Shock-Compatible/dp/B0C58X3CRX",
"https://www.amazon.com/Cockatoo-OXO-Biodegradable-Companion-Campaigning-Adventures/dp/B0CF9Q8HPN",
"https://www.amazon.com/Zebronics-Compartment-Backpacks-15-6-inch-Black/dp/B0C6KZS555",
"https://www.amazon.com/COSMUS-Polyester-Black-School-Backpack/dp/B078MFYJ3M",
"https://www.amazon.com/Nivia-5177BK-Polyester-String-Black/dp/B071XM6PSM",
"https://www.amazon.com/Paarsv-Tamper-Courier-Without-Jacket/dp/B018E1O6LU",
"https://www.amazon.com/POLESTAR-Backpack-Compartment-Polyester-Warranty/dp/B0BMQ2HXYP",
"https://www.amazon.com/Red-Lemon-Waterproof-Capacity-Comfortable/dp/B0C53MVJ2C",
"https://www.amazon.com/NIVIA-Polyester-Shoulder-Compartment-Accessories/dp/B07NJGW3WX",
"https://www.amazon.com/Professional-Photographers-Waterproof-Lightweight-Accessories/dp/B0C58VVFQT",
"https://www.amazon.com/DAHSHA-Bag-Business-Messenger-Shoulder/dp/B07GCLJTZF",
"https://www.amazon.com/Gear-Black-Laptop-Backpack-LBPASPIRE0104/dp/B075MK4TXP",
"https://www.amazon.com/Tabelito%C2%AE-Delta-Waterproof-Backpack-Compatible/dp/B0BLK1Z7DQ",
"https://www.amazon.com/DOUBLE-BAGS-Cotton-Shopping-Multicolour/dp/B07FKQLPDR",
"https://www.amazon.com/s/?k=bags+for+girls&ref=sugsr_0&pd_rd_w=sZEWw&content-id=amzn1.sym.1c7db1d2-1fe9-496b-8f07-8ed64c022066:amzn1.sym.1c7db1d2-1fe9-496b-8f07-8ed64c022066&pf_rd_p=1c7db1d2-1fe9-496b-8f07-8ed64c022066&pf_rd_r=3H7CMETJJ4YS64CXZAQ6&pd_rd_wg=Ht7rk&pd_rd_r=a8a64ae6-35f2-49b7-b1e0-77941b566517&qid=1697645097",
"https://www.amazon.com/gp/help/customer/display.html?nodeId=201889520",
"https://www.amazon.com/DAHSHA-Bag-Business-Messenger-Shoulder/dp/B07GCLJTZF",
"https://www.amazon.com/Gear-Black-Laptop-Backpack-LBPASPIRE0104/dp/B075MK4TXP",
"https://www.amazon.com/Tabelito%C2%AE-Delta-Waterproof-Backpack-Compatible/dp/B0BLK1Z7DQ",
"https://www.amazon.com/Black-Orange-Casual-Backpack-BKPCARYON0106/dp/B019HA8AQO",
"https://www.amazon.com/Tabelito-NEXA-Backpack-Business-Compartment/dp/B0C2D3YR7T",
"https://www.amazon.com/ZaySoo-Stylish-Backpack-College-Business/dp/B0BVZL49N8",
"https://www.amazon.com/gp/bestsellers/kitchen/1380547031/ref=sr_bs_6_1380547031_1",
"https://www.amazon.com/DOUBLE-BAGS-Cotton-Shopping-Multicolour/dp/B07FKQLPDR",
"https://www.amazon.com/Amazon-Brand-Solimo-Underbed-Storage/dp/B084MS8LTW",
"https://www.amazon.com/Artistix-Unisex-Travel-Backpack-Repellent/dp/B09B5DMGM1",
"https://www.amazon.com/Wildcraft-Typo_Blk-Casual-Backpack-11619-Typo_Blk/dp/B079MBFH5V",
"https://www.amazon.com/AirCase-C25-Messenger-Shoulder-Compartments/dp/B07X6DV3VM",
"https://www.amazon.com/AirCase-Premium-Waterproof-Neoprene-Warranty/dp/B07JBBKD5S",
"https://www.amazon.com/DAHSHA-Sling-Messenger-Bag-Grey/dp/B09CGDFNBV""/gp/bestsellers/electronics/4175441031/ref=sr_bs_14_4175441031_1",
"https://www.amazon.com/Tabelito-NEXA-Backpack-Business-Compartment/dp/B0C2D4KWQ6",
"https://www.amazon.com/s/?k=bags+for+girls&ref=sugsr_0&pd_rd_w=VtYRH&content-id=amzn1.sym.1c7db1d2-1fe9-496b-8f07-8ed64c022066:amzn1.sym.1c7db1d2-1fe9-496b-8f07-8ed64c022066&pf_rd_p=1c7db1d2-1fe9-496b-8f07-8ed64c022066&pf_rd_r=JXBX85YAWFZ8GMSBRQTG&pd_rd_wg=kR5Vz&pd_rd_r=f9a957c1-042b-4d02-a633-16368e9ddc91&qid=1697645098",
"https://www.amazon.com/gp/help/customer/display.html?nodeId=201889520",
"https://www.amazon.com/PLAYY-BAGS-Polyester-Business-Shoulder/dp/B0CJC93HDH",
"https://www.amazon.com/Red-Lemon-Business-Backpack-Waterproof/dp/B09ZYNHVKZ",
"https://www.amazon.com/Nelle-Harper-Womens-Shoulder-Ligh/dp/B07R6DRCZM",
"https://www.amazon.com/Gear-Executive-Anti-Theft-Backpack-BKPPKREXE0101/dp/B097KCMQKG",
"https://www.amazon.com/Sirona-Sanitary-Napkin-Diapers-Disposal/dp/B01NAZVN8M",
"https://www.amazon.com/Essentials-Laptop-Sleeve-13-3-Inch-Accessories/dp/B09RF47WDL",
"https://www.amazon.com/Storite-Sling-Bag-Shoulder-25-5cmx7cmx20cm/dp/B09P3RQPCG",
"https://www.amazon.com/Half-Moon-Messenger-Multi-Pocket-Adjustable/dp/B0C5CFCLLJ",
"https://www.amazon.com/HARISSONS-Backpack-Black-Grey-Repellent-Organizer/dp/B08LBLKYRY",
"https://www.amazon.com/KILLER-Polyester-Navy-Laptop-Backpack/dp/B07B51CTNF",
"https://www.amazon.com/Kuber-Industries-Biodegradable-Warehouse-Washroom/dp/B0C3QR3YJV",
"https://www.amazon.com/lynx-School-compartments-Backpack-Trending/dp/B08GJKNQ9F",
"https://www.amazon.com/POLESTAR-Backpack-compartment-polyester-warranty/dp/B09RWTQ1VW",
"https://www.amazon.com/Lavie-Womens-Closure-Satchel-Handbag_Chocolate/dp/B07DJ9Q1NY",
"https://www.amazon.com/Tabelito%C2%AE-Resistant-Business-Backpack-Notebook/dp/B0CGP32XKK",
"https://www.amazon.com/WILD-MODA-Womens-Shoulder-Turquoise/dp/B099PLT91X",
"https://www.amazon.com/s/?k=bags+for+girls&ref=sugsr_0&pd_rd_w=XYB6H&content-id=amzn1.sym.1c7db1d2-1fe9-496b-8f07-8ed64c022066:amzn1.sym.1c7db1d2-1fe9-496b-8f07-8ed64c022066&pf_rd_p=1c7db1d2-1fe9-496b-8f07-8ed64c022066&pf_rd_r=0NEXJZR01AV4DZZ53YXN&pd_rd_wg=TdFro&pd_rd_r=c724caf1-8e51-48bf-974f-978b3883ee1d&qid=1697645104",
"https://www.amazon.com/gp/help/customer/display.html?nodeId=201889520",
"https://www.amazon.com/Red-Lemon-Capacity-Backpack-Multifunctional/dp/B09RK4BRPM",
"https://www.amazon.com/Martucci-Waterproof-Backpack-College-Business/dp/B0BNSXJ2MY",
"https://www.amazon.com/s/?k=bags+for+girls&ref=sugsr_0&pd_rd_w=4FPUD&content-id=amzn1.sym.1c7db1d2-1fe9-496b-8f07-8ed64c022066:amzn1.sym.1c7db1d2-1fe9-496b-8f07-8ed64c022066&pf_rd_p=1c7db1d2-1fe9-496b-8f07-8ed64c022066&pf_rd_r=HCPH3X5VX51Z38RJAQBH&pd_rd_wg=tY5d6&pd_rd_r=41edf590-c106-44ee-8fdc-ab9eaa4b947d&qid=1697645105",
"https://www.amazon.com/gp/help/customer/display.html?nodeId=201889520",
]
    
    # Add more URLs here


# List to store the scraped data
scraped_data = []

for url in product_urls:
    data = scrape_product_data(url)
    if data:
        scraped_data.append(data)

# Export the data to a CSV file
import csv

with open('product_data.csv', 'w', newline='') as csvfile:
    fieldnames = ['URL', 'Description', 'ASIN', 'Product Description', 'Manufacturer']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for data in scraped_data:
        writer.writerow(data)
