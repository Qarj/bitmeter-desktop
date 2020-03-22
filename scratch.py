#!/usr/bin/env python3
import wx


class ExampleFrame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent)
        panel = wx.Panel(self)
        self.quote = wx.StaticText(panel, label="Your quote: ", pos=(20, 30))
        self.Show()


app = wx.App(False)
ExampleFrame(None)

displays = (wx.Display(i) for i in range(wx.Display.GetCount()))
for v in displays:
    print("Display", v.GetGeometry().GetSize().width)

app.MainLoop()
