

#----Log-in-----
import wx, socket, time, os
from threading import Thread

class LoginFrame(wx.Frame):
    def __init__(self, parent, title):
        super(LoginFrame, self).__init__(parent, title=title,size=(400,300))
        self.Centre()
        self.Show()
        self.SetFont(wx.Font(18, wx.SWISS, wx.NORMAL, wx.NORMAL, False,'MS Shell Dlg 2'))
        self.enter_user = wx.TextCtrl(self, size=(280,40), pos=(10,40), value='enter user name')
        self.enter_pass = wx.TextCtrl(self, size=(280,40), pos=(10,90), value='enter password',style=wx.TE_PASSWORD)
        self.LOG_BTN = wx.Button(self,size=(110,40), label='Log-in',pos=(10,140))
        self.LOG_BTN.SetWindowStyleFlag(wx.NO_BORDER)
        self.LOG_BTN.SetBackgroundColour((32,190,208))

        self.New_user_BTN = wx.Button(self,size=(110,40), label='new user',pos=(130,140))
        self.New_user_BTN.SetWindowStyleFlag(wx.NO_BORDER)
        self.New_user_BTN.SetBackgroundColour((32,190,208))


if '__main__' == __name__:
    app=wx.App()
    LoginFrame(None, 'LoginFrame')
    app.MainLoop()
    
