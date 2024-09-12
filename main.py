from pyguiadapter.adapter import GUIAdapter

from qrcode_maker.qrcode import make_qrcode


def main():
    adapter = GUIAdapter()
    adapter.add(make_qrcode)
    adapter.run()


if __name__ == "__main__":
    main()
