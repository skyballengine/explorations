class Lawnmower:

    def start(self):
        print("Ready to cut grass!")


class Movie:

    def start(self):
        print("Movie has started!")


def start_stuff():
    lm = Lawnmower()
    mv = Movie()
    start_list = [lm, mv]
    for item in start_list:
        item.start()


def main():
    start_stuff()


if __name__ == "__main__":
    main()
