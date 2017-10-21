#!/usr/bin/python3


class RealEstateDeal:

    def __init__(self, title, url, category, price, location, description, other_details):
        self.title = title
        self.url = url
        self.category = category
        self.price = price
        self.location = location
        self.description = description
        self.other_details = other_details

    def __str__(self):
        return """
Title: {0}
Price: {1}
Category: {2}
Location: {3}
Description: {4}
Other Details: {5}
URL: {6}
    	""".format(self.title, self.price, self.category, self.location, self.description, self.other_details, self.url)


class JumiaDeal(RealEstateDeal):

    def __init__(self, title, url, category, price, location, description, other_details):
        super().__init__(title, url, category, price, location, description, other_details)
