import wx

class MyFrame(wx.Frame):
    def __init__(self, *args, **kw):
        super(MyFrame, self).__init__(*args, **kw)

        # Create a panel in the frame
        pnl = wx.Panel(self)

        # Create a button in the panel
        self.btn = wx.Button(pnl, label="Click Me", pos=(50, 50))
        
        # Bind the button click event to an event handler
        self.btn.Bind(wx.EVT_BUTTON, self.on_button_click)

        # Set the frame's size and title
        self.SetSize((300, 200))
        self.SetTitle("wxPython Test")

    def on_button_click(self, event):
        # Show a message dialog when the button is clicked
        wx.MessageBox("Hello, wxPython!", "Info", wx.OK | wx.ICON_INFORMATION)

class MyApp(wx.App):
    def OnInit(self):
        # Create an instance of the frame
        frame = MyFrame(None)
        frame.Show()
        return True

if __name__ == "__main__":
    # Create an instance of the application
    app = MyApp()
    # Start the application's main loop
    app.MainLoop()
