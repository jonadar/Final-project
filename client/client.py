#client
#-------------------------------------------------
import wx, socket, time, os
from threading import Thread

class MainFrame(wx.Frame):
    def __init__(self, parent, title):
        super(MainFrame, self).__init__(parent, title=title)
        self.Maximize()
        self.Centre()
        self.Show()
        self.SetFont(wx.Font(18, wx.SWISS, wx.NORMAL, wx.NORMAL, False,'MS Shell Dlg 2'))
        #--chat--#
        
        self.SND_BTN = wx.Button(self,size=(110,40), label='Send',pos=(300,40))
        self.SND_BTN.SetWindowStyleFlag(wx.NO_BORDER)
        self.SND_BTN.SetBackgroundColour((32,190,208))

        self.Entery = wx.TextCtrl(self, size=(280,40), pos=(10,40), value='enter here!')

        self.Chat_body = wx.ListCtrl(self, size=(400,600), pos=(10,90), style=wx.LC_REPORT|wx.BORDER_SUNKEN)
        self.index=0
        self.Chat_body.InsertColumn(0, 'Name')
        self.Chat_body.InsertColumn(1, 'Message')
        #self.Chat_body.SetColumnWidth(1, 80)
        self.Chat_body.InsertColumn(2, 'Time')
        
        #--file--#
        self.UPLD_BTN = wx.Button(self,size=(110,40), label='Upload',pos=(425,40))
        self.UPLD_BTN.SetWindowStyleFlag(wx.NO_BORDER)
        self.UPLD_BTN.SetBackgroundColour((32,190,208))

        self.REFRSH_BTN = wx.Button(self,size=(110,40), label=u'\u21bb',pos=(545,40))
        self.REFRSH_BTN.SetFont(wx.Font(24, wx.SWISS, wx.NORMAL, wx.NORMAL, False,'MS Shell Dlg 2'))
        self.REFRSH_BTN.SetWindowStyleFlag(wx.NO_BORDER)
        self.REFRSH_BTN.SetBackgroundColour((32,190,208))


        self.File_body = wx.ListCtrl(self, size=(400,600), pos=(425,90), style=wx.LC_REPORT|wx.BORDER_SUNKEN)
        self.index=0
        self.File_body.InsertColumn(0, 'Last changed by')
        self.File_body.InsertColumn(1, 'File name')
        self.File_body.InsertColumn(2, 'File type')
        
if __name__ == '__main__':
    app = wx.App()
    MainFrame(None, 'Main')
    app.MainLoop()
