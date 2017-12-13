import wx, socket, time, os, md5
from threading import Thread
from valid import *
import DataBaseH as dh

#server
#-------------------------------------

class ServerFrame(wx.Frame):
    def __init__(self, parent, title):
        super(ServerFrame, self).__init__(parent, title=title)
        self.Maximize()
        self.Centre()
        self.Show()
        self.SetFont(wx.Font(18, wx.SWISS, wx.NORMAL, wx.NORMAL, False,'MS Shell Dlg 2'))
        #--online users--#
        self.mylabel = wx.StaticText(self, label="Online users", pos=(70,50)) 

        self.SND_BTN = wx.Button(self,size=(110,40), label='Add',pos=(340,210))
        self.SND_BTN.SetWindowStyleFlag(wx.NO_BORDER)
        self.SND_BTN.SetBackgroundColour((32,190,208))
        self.SND_BTN.Bind(wx.EVT_BUTTON, self.newUser)
        self.UserEntery = wx.TextCtrl(self, size=(250,40), pos=(340,90), value='Enter new user Name')
        self.PassEntery = wx.TextCtrl(self, size=(250,40), pos=(340,150), value='Enter password')

        self.conected_body = wx.ListCtrl(self, size=(300,480), pos=(10,90), style=wx.LC_REPORT|wx.BORDER_SUNKEN)
        self.index=0
        self.conected_body.InsertColumn(0, 'User Name')
        self.conected_body.InsertColumn(1, 'Time conected')
        
        #--users list--#

        self.REFRSH_BTN_USER = wx.Button(self,size=(60,40), label=u'\u21bb',pos=(460,210))
        self.REFRSH_BTN_USER.SetFont(wx.Font(28, wx.SWISS, wx.NORMAL, wx.NORMAL, False,'MS Shell Dlg 2'))
        self.REFRSH_BTN_USER.SetWindowStyleFlag(wx.NO_BORDER)
        self.REFRSH_BTN_USER.SetBackgroundColour((32,190,208))


        self.online_body = wx.ListCtrl(self, size=(200,300), pos=(340,270), style=wx.LC_REPORT|wx.BORDER_SUNKEN)
        self.online_body.InsertColumn(0, 'User Name')

        #---file list----#
        self.file_body = wx.ListCtrl(self, size=(430,480), pos=(610,90), style=wx.LC_REPORT|wx.BORDER_SUNKEN)
        self.file_body.InsertColumn(0, 'File Name')
        self.file_body.InsertColumn(1, 'Last changed by')
        self.file_body.InsertColumn(2, 'Type')
        self.file_body.InsertColumn(3, 'Size')

        self.REFRSH_BTN_FILE = wx.Button(self,size=(60,40), label=u'\u21bb',pos=(980,40))
        self.REFRSH_BTN_FILE.SetFont(wx.Font(28, wx.SWISS, wx.NORMAL, wx.NORMAL, False,'MS Shell Dlg 2'))
        self.REFRSH_BTN_FILE.SetWindowStyleFlag(wx.NO_BORDER)
        self.REFRSH_BTN_FILE.SetBackgroundColour((32,190,208))

        self.mylabel = wx.StaticText(self, label="Files List", pos=(770,50)) 
    def newUser(self,e):
        user_name = self.UserEntery.GetValue()
        user_pass = self.PassEntery.GetValue()
        Check = CUser(user_name)
        if isinstance(Check, bool):
            if not dh.userExists(user_name):
                Check = CPass(user_pass)
                if isinstance(Check, bool):
                    dh.addNew(user_name, user_pass)
                else:
                    print Check
        else:
            print Check
            
        
        
        
if __name__ == '__main__':
    app = wx.App()
    ServerFrame(None, 'Server')
    app.MainLoop()
