import wx
import json

from wx.lib.mixins.listctrl import CheckListCtrlMixin

# TODO: Figure out how to move my check box into the last column, and make an event for it to save my json data as True


class CheckBoxToggle(wx.ListCtrl, CheckListCtrlMixin):  # I am trying to add a checkbox with this thing
    def __init__(self, parent):
        wx.ListCtrl.__init__(self, parent, -1, style=wx.LC_REPORT)
        CheckListCtrlMixin.__init__(self)
        self.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.on_item_activated)

    def on_item_activated(self, event):
        pass


class Panel(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent, -1)  # IDK what super is...

        self.row_obj_dict = {}

        self.list_ctrl = CheckBoxToggle(self)
        main_sizer = wx.BoxSizer(wx.VERTICAL)

        # These make the columns
        #self.list_ctrl.InsertColumn(0, 'Completed')
        self.list_ctrl.InsertColumn(0, 'Assignment')
        self.list_ctrl.InsertColumn(1, 'Due Date')

        global main_list  # This probably isn't the best way to do this
        index = 0

        for key, value in main_list.items():  # This fills in the rows with my info
            self.list_ctrl.InsertItem(self.list_ctrl.GetItemCount(), value[0])
            self.list_ctrl.SetItem(index, 0, key)
            self.list_ctrl.SetItem(index, 1, value)
            index += 1

        self.list_ctrl.SetColumnWidth(0, 200)
        self.list_ctrl.SetColumnWidth(1, 200)      # Sets my column width
        #self.list_ctrl.SetColumnWidth(2, wx.LIST_AUTOSIZE)

        main_sizer.Add(self.list_ctrl, 0, wx.ALL | wx.EXPAND, 5)  # Fits everything to the screen
        # Todo: A button can go here to make changes...
        self.SetSizer(main_sizer)


class Frame(wx.Frame):  # This is my main window, the panel goes on top of it
    def __init__(self):
        super().__init__(parent=None, size=(500, 550),
                         title='Shitty to do list')
        self.panel = Panel(self)
        #self.create_menu()  # This line will give me a menu if I add a method for it
        self.Show()


# This makes a file menu tab
"""
    def create_menu(self):
        menu_bar = wx.MenuBar()
        file_menu = wx.Menu()
        open_folder_menu_item = file_menu.Append(
            wx.ID_ANY, 'Open Folder',
            'Open a folder with MP3s'
        )
        menu_bar.Append(file_menu, '&File')
        self.Bind(
            event=wx.EVT_MENU,
            handler=self.on_open_folder,
            source=open_folder_menu_item,
        )
        self.SetMenuBar(menu_bar)

    def on_open_folder(self, event):
        title = "Choose a directory:"
        dlg = wx.DirDialog(self, title,
                           style=wx.DD_DEFAULT_STYLE)
        if dlg.ShowModal() == wx.ID_OK:
            self.panel.update_mp3_listing(dlg.GetPath())
        dlg.Destroy()
"""

if __name__ == '__main__':
    with open('main_list.json', 'r') as file:
        main_list = dict(json.load(file))

    app = wx.App(False)  # IDK what this actually does... Like why the false?
    frame = Frame()
    app.MainLoop()  # This is an event loop that awaits action
