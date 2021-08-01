from tkinter import Tk
from MyClass import RootFrame, Bland


def main():
    bland = Bland()
    root = Tk()
    RootFrame(bland)
    root.mainloop()


if __name__ == "__main__":
    main()
