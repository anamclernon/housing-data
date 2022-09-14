from house_prices import load_df
from plot_graphs import describe, plot_2d_graph, plot_3d_graph, describe

URL1 = "https://www.homegate.ch/buy/apartment/city-zurich/matching-list?ac=2&ad=3.5"
URL2 = "https://www.homegate.ch/buy/apartment/city-zurich/matching-list?ep=2&ac=2&ad=3.5"

df = load_df([URL1, URL2])

describe(df)