import os
import sys


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    os.chdir(here)
    if here not in sys.path:
        sys.path.insert(0, here)

    import main

    app = main.App()
    app.mainloop()


if __name__ == "__main__":
    main()
