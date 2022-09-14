import matplotlib.pyplot as plt

def describe(df):
    df.describe()
    
def plot_2d_graph(df):

    plt.scatter(df["Price in Mil"], df["Sqm"])

    plt.show()

def plot_3d_graph(df):
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    ax.scatter(df["Price in Mil"], df["Rooms"], df["Sqm"])
    ax.set_xlabel("Price in Mil")
    ax.set_ylabel("Rooms")
    ax.set_zlabel("Sqm")
    plt.show()