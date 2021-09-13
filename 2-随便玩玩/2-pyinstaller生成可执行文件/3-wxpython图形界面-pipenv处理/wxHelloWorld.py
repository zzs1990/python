# -*- coding: utf-8 -*-
import wx


def main():
    app = wx.App()
    win = wx.Frame(None, title="Hello World")
    win.Show()
    app.MainLoop()


if __name__ == "__main__":
    main()
