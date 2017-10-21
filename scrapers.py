import requests
from bs4 import BeautifulSoup
from resources import JumiaDeal


def getJumiaDeal(dealUrl, categoryName):
    # For offline pages
    dealPage = open(dealUrl, 'r')
    dpage = dealPage.read()
    dealSoup = BeautifulSoup(dpage, 'html.parser')

    # For live page requests
    # dealPage = requests.get(dealUrl)
    # dealSoup = BeautifulSoup(dealPage.content, 'html.parser')
    if (categoryName == "Rent and Sales"):
        title = dealSoup.find("h1", class_="detail-property-title").get_text().strip()
        location = dealSoup.find(
            "div", id="property-location-container").find("span", class_="icon-location").get_text().strip()
        price = dealSoup.find(
            "div", id="property-price-container").find("span", class_="price").get_text().strip()
        description = dealSoup.find(
            "section", class_="description").find("p").get_text().strip().title()
        details = []
        for table in dealSoup.find("section", class_="details").find_all("table"):
            for det in table.get_text().strip().split("\n\n"):
                details.append(det.strip())

    elif (categoryName == "New Developments"):
        title = dealSoup.find("title").get_text().strip()
        location = dealSoup.find("div", class_="location-description").find("p").get_text().strip()
        price = dealSoup.find("div", class_="price-amount").get_text().strip()
        description = dealSoup.find("section", class_="description").find(
            "p").get_text().strip().title()
        details = []
        for table in dealSoup.find("section", class_="details development-details-attributes").find_all("table"):
            for det in table.get_text().strip().split("\n\n"):
                details.append(det.strip())

    deal = JumiaDeal(
        title=title,
        url=dealUrl,
        category=categoryName,
        location=location,
        price=price,
        description=description,
        other_details=details
    )
    print(deal)


def getJumiaDealLinks(baseUrl):
    linksList = []
    propertyList = []

    # To be used with offline pages
    basePage = open(baseUrl, 'r')
    page = basePage.read()
    baseSoup = BeautifulSoup(page, 'html.parser')

    # To be used with live requests
    # basePage = requests.get(baseUrl)
    # baseSoup = BeautifulSoup(basePage.content,'html.parser')

    for link in baseSoup.find_all("a", class_="FeaturedItem-showDetails-link"):
        linksList.append(link.get("href"))
    return print("\n".join(linksList))

    '''
    # For live requests pages
    for item in linksList:
    	getJumiaDeal(item)
    	propertyList.append(deal)
    '''
