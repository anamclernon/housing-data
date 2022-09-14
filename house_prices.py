import pandas as pd
import requests
from bs4 import BeautifulSoup

classPrice = "ListItemPrice_price_1o0i3"
classRooms = "ListItemRoomNumber_value_Hpn8O"
classSqm = "ListItemLivingSpace_value_2zFir"
classData = "ListItem_data_18_z_"

def process_price(price):
    num = ""
    for s in price:
        if s.isnumeric():
            num += s
    if num:
        return float(num)
    else:
        return None

def get_price(item):

    raw_price = item.find("span", {"class": classPrice}).contents[1].contents[0]

    return process_price(raw_price) / 1000000

def get_rooms(item):

    raw_rooms = item.find("span", {"class": classRooms}).contents[0]

    return float(raw_rooms)

def get_sqm(item):

    raw_sqm = item.find("span", {"class": classSqm}).contents[0]

    return float(raw_sqm)

def house_data(URL):

    soup = BeautifulSoup(requests.get(URL).content, 'html.parser')
    
    list = soup.find_all("div", {"class": classData})

    rooms_price = [(get_rooms(item), get_price(item), get_sqm(item)) for item in list]
    
    return rooms_price

def load_df(URL_list):
    data = []
    for URL in URL_list:
        data.append(house_data(URL))

    df = pd.DataFrame(data, columns = ["Rooms", "Price in Mil", "Sqm"])

    return df

