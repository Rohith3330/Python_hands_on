import matplotlib.pyplot as plt
def main():
    data = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]

    plt.hist(data, density=True)
    plt.title("Histogram with density (newer version)")
    # plt.show()
    plt.savefig('Matplotlib_new.png')
if __name__ == "__main__":
    main()