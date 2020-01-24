# -*- coding: utf-8 -*-


class DefaultValuesPipeline(object):
    def process_item(self, item, spider):
        for field in item.fields:
            item.setdefault(field, "NULL")
        return item


class CheapTripsPipeline(object):
    def process_item(self, item, spider):
        if item["price"] < 2000:
            print("\n\n Cheap Trip Found !!!")
            print("Name: ", item["name"])
            print("Price: ", item["price"])
            print("Operator: ", item["operator"])
            print("Next Departure Date: ", item["next_departure_date"])
        return item
