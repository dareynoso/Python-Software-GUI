import Tkinter as tk

class Table(tk.Tk):

    def __init__(self, parent):
        tk.Tk.__init__(self, parent)
        self.parent = parent
        self.components = {}
        self.column = 0
        self.row = 0

    def __add__(self, name, component):
        lbl = tk.Label(self, text=name)
        self.components[name] = component

        lbl.grid(column=0, row=self.row)
        component.grid(column=1, row=self.row)
        self.row += 1

    def add_entry(self, name, command=None, state='normal'):
        entry = tk.Entry(self, validate='focusout', validatecommand=command, state=state)
        entry.config(width=50)
        self.__add__(name, entry)

    def add_option(self, name, options, default_index=0, command=None, state='normal'):
        var = tk.StringVar()
        var.set(options[default_index])
        option = tk.OptionMenu(self, var, *options, command=command)
        option.config(state=state, width=25)
        self.__add__(name, option)

    def add_checkbox(self, name, command=None, state='normal'):
        checkbox = tk.Checkbutton(self, state=state, command=command)
        self.__add__(name, checkbox)

class FieldDialog(Table):
    def __init__(self, parent):
        Table.__init__(self, parent)
        self.init_components()

    def init_components(self):

        self.data_types = ['None','Protocol','Boolean','UInt8','UInt16','UInt24',
                           'UInt32','UInt64','Int8', 'Int16', 'Int24', 'Int32', 'Int64',
                           'Float', 'Double', 'Absolute_Time', 'Relative_Time', 'String',
                           'StringZ', 'UInt_String', 'Ether', 'Bytes', 'UInt_Bytes', 'IPv4',
                           'IPv6', 'IPXNET', 'FRAMENUM', 'PCRE', 'GUID', 'OID', 'EUI64'
                           ]
        self.bases = ['None', 'Dec', 'Hex', 'Oct', 'Dec_Hex', 'Hex_Dec']

        self.title("Field [Abbreviation]")
        self.add_entry('Name')
        self.add_entry('Abbreviation', command=self.on_abbr_change)
        self.add_entry('Description')
        self.add_option('Reference List', options=['None'])
        self.add_option('Data Type', options=self.data_types)
        self.add_option('Base', options=self.bases)
        self.add_entry('Mask')
        self.add_entry('Value Constraint')
        self.add_checkbox('Required')

    def on_abbr_change(self):
        new_abbr = self.components['Abbreviation'].get()
        self.title("Field " + "[" + new_abbr + "]")


if __name__ == '__main__':
    form = FieldDialog(None)
    form.mainloop()