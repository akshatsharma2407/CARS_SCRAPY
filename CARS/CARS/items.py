import scrapy

class QuoteItem(scrapy.Item):
    # car's primary details
    images = scrapy.Field()
    new_used = scrapy.Field()
    car_name = scrapy.Field()
    mileage = scrapy.Field()
    price = scrapy.Field()
    deal = scrapy.Field()

    # car's key specs
    fuel_type = scrapy.Field()
    mpge = scrapy.Field()
    level2_charging = scrapy.Field()
    dc_fast_charging = scrapy.Field()
    battery_capacity = scrapy.Field()
    expected_range = scrapy.Field()
    battery_rating_and_category = scrapy.Field()

    # basics
    exterior_color = scrapy.Field()
    interior_color = scrapy.Field()
    drivetrain = scrapy.Field()
    transmission = scrapy.Field()
    engine = scrapy.Field()

    # features
    convenience = scrapy.Field()
    entertainment = scrapy.Field()
    exterior = scrapy.Field()
    safety = scrapy.Field()
    seating = scrapy.Field()


    # vehicle history
    damage = scrapy.Field()
    one_owner = scrapy.Field()
    personal_use_only = scrapy.Field()

    # seller's info
    seller_name = scrapy.Field()
    seller_rating = scrapy.Field()
    seller_review = scrapy.Field()
    location = scrapy.Field()