class City:
    def __init__(self, city_name, region_name, country_name, num_citizens, zip_code, area_code):
        self.city_name = city_name
        self.region_name = region_name
        self.country_name = country_name
        self.num_citizens = num_citizens
        self.zip_code = zip_code
        self.area_code = area_code

    def full_address(self):
        print(f"The full address is: {self.city_name}, {self.region_name}, {self.country_name}, zip code:{self.zip_code}, area code:{self.area_code}")
#v metode nie je pocet obyvatelov lebo to nie je podla mna atribut adresy

address_1_ = City(city_name="Barcelona", region_name="Catalunya", country_name="Spain", num_citizens= 2000000, zip_code = 4512, area_code=47897)
address_1_.full_address()