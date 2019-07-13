import wx
import json


# TODO: I need to figure out how to make a check box/toggle thing for the completed column
class Panel(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)
        main_sizer = wx.BoxSizer(wx.VERTICAL)
        self.row_obj_dict = {}

        self.list_ctrl = wx.ListCtrl(
            self, size=(-1, 800),                 # This sets up the column structure. Unsure of the size tuple meaning
            style=wx.LC_REPORT | wx.BORDER_SUNKEN
        )
        self.list_ctrl.InsertColumn(0, 'Assignment', width=250)     # These make the columns
        self.list_ctrl.InsertColumn(1, 'Day Due', width=150)
        self.list_ctrl.InsertColumn(2, 'Completed', width=100)

        global main_list    # This probably isn't the best way to do this
        index = 0

        for task, due_date in main_list.items():    # This fills in the rows with my info
            self.list_ctrl.InsertItem(index, task)
            self.list_ctrl.SetItem(index, 1, due_date)
            index += 1

        main_sizer.Add(self.list_ctrl, 0, wx.ALL | wx.EXPAND, 5)    # Fits everything to the screen
        # Todo: A button can go here to make changes...
        self.SetSizer(main_sizer)


class Frame(wx.Frame):      # This is my main window, the panel goes on top of it
    def __init__(self):
        super().__init__(parent=None, size=(500, 550),
                         title='Shitty to do list')
        self.panel = Panel(self)
        self.Show()


if __name__ == '__main__':
    with open('main_list.json', 'r') as file:
        main_list = dict(json.load(file))

    app = wx.App(False)     # IDK what this actually does... Like why the false?
    frame = Frame()
    app.MainLoop()      # This is an event loop that awaits action
