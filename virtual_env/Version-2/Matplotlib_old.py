import matplotlib.pyplot as plt
def main():
    data = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
    plt.hist(data)
    plt.title("Histogram without density (older version)")
    # plt.show()
    plt.savefig("Matplotlib_old.png")
if __name__ == "__main__":
    main()