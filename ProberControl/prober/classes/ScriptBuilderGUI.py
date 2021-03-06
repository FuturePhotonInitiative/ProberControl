#! /usr/bin/env python
#
# GUI module generated by PAGE version 4.9
# In conjunction with Tcl version 8.6
#    Dec 13, 2017 02:19:07 PM
import sys

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = 0
except ImportError:
    import tkinter.ttk as ttk
    py3 = 1

import ScriptBuilder

def vp_start_gui(Maitre):
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    ScriptBuilder.set_Tk_var()
    top = ScriptBuilderGUI(root, Maitre)
    ScriptBuilder.init(root, top, Maitre)
    root.mainloop()

w = None
def create_ScriptBuilder(w_new, Maitre, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w
    w = w_new
    ScriptBuilder.set_Tk_var()
    top = ScriptBuilderGUI (w, Maitre)
    ScriptBuilder.init(w, top, Maitre)
    return (w, top)

def destroy_ScriptBuilder():
    global w
    w.destroy()
    w = None


class ScriptBuilderGUI:
    def __init__(self, top=None, Maitre=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''

        self.Maitre = Maitre

        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#d9d9d9' # X11 color: 'gray85'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("1176x859+459+11")
        top.title("ScriptBuilder")
        top.configure(background="#d9d9d9")



        self.Scrolledtext1 = ScrolledText(top)
        self.Scrolledtext1.place(relx=0.55, rely=0.03, relheight=0.93
                , relwidth=0.43)
        self.Scrolledtext1.configure(background="white")
        self.Scrolledtext1.configure(font="TkTextFont")
        self.Scrolledtext1.configure(foreground="black")
        self.Scrolledtext1.configure(highlightbackground="#d9d9d9")
        self.Scrolledtext1.configure(highlightcolor="black")
        self.Scrolledtext1.configure(insertbackground="black")
        self.Scrolledtext1.configure(insertborderwidth="3")
        self.Scrolledtext1.configure(selectbackground="#c4c4c4")
        self.Scrolledtext1.configure(selectforeground="black")
        self.Scrolledtext1.configure(width=10)
        self.Scrolledtext1.configure(wrap=NONE)

        self.menubar = Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.file = Menu(top,tearoff=0)
        self.menubar.add_cascade(menu=self.file,
                label="File")
        self.file.add_command(
                command=ScriptBuilder.loadScript,
                label="Load Script")
        self.file.add_command(
                command=ScriptBuilder.saveScript,
                label="Save Script")
        self.file.add_command(
                command=ScriptBuilder.destroy_window,
                label="Exit")

        self.edit = Menu(top,tearoff=0)
        self.menubar.add_cascade(menu=self.edit,
                label="Edit")
        self.edit.add_command(
                command=ScriptBuilder.searchAndReplace,
                label="Search and Replace")


        self.AddMeasFrame = LabelFrame(top)
        self.AddMeasFrame.place(relx=0.03, rely=0.02, relheight=0.4
                , relwidth=0.5)
        self.AddMeasFrame.configure(relief=GROOVE)
        self.AddMeasFrame.configure(foreground="black")
        self.AddMeasFrame.configure(text='''Add Measurement''')
        self.AddMeasFrame.configure(background="#d9d9d9")
        self.AddMeasFrame.configure(width=590)

        self.MeasNameEntry = Entry(self.AddMeasFrame)
        self.MeasNameEntry.place(relx=0.02, rely=0.14, relheight=0.06
                , relwidth=0.72)
        self.MeasNameEntry.configure(background="white")
        self.MeasNameEntry.configure(disabledforeground="#a3a3a3")
        self.MeasNameEntry.configure(font="TkFixedFont")
        self.MeasNameEntry.configure(foreground="#000000")
        self.MeasNameEntry.configure(insertbackground="black")
        self.MeasNameEntry.configure(textvariable=ScriptBuilder.MeasNameVar)
        self.MeasNameEntry.configure(width=424)

        self.ProcBox = OptionMenu(self.AddMeasFrame,
        ScriptBuilder.ProcBoxVar,
        *self.Maitre.get_all_modules(),
        command = ScriptBuilder.ProcBoxChange
        )
        self.ProcBox.place(relx=0.02, rely=0.43, relheight=0.06, relwidth=0.72)
        self.ProcBox.configure(width=423)
        self.ProcBox.configure(takefocus="")

        self.StructEntry = Entry(self.AddMeasFrame)
        self.StructEntry.place(relx=0.02, rely=0.26, relheight=0.06
                , relwidth=0.72)
        self.StructEntry.configure(background="white")
        self.StructEntry.configure(disabledforeground="#a3a3a3")
        self.StructEntry.configure(font="TkFixedFont")
        self.StructEntry.configure(foreground="#000000")
        self.StructEntry.configure(insertbackground="black")
        self.StructEntry.configure(textvariable=ScriptBuilder.StructNameVar)
        self.StructEntry.configure(width=424)

        self.MeasNameLabel = Label(self.AddMeasFrame)
        self.MeasNameLabel.place(relx=0.02, rely=0.07, height=21, width=114)
        self.MeasNameLabel.configure(background="#d9d9d9")
        self.MeasNameLabel.configure(disabledforeground="#a3a3a3")
        self.MeasNameLabel.configure(foreground="#000000")
        self.MeasNameLabel.configure(text='''Measurement Name''')

        self.StructLabel = Label(self.AddMeasFrame)
        self.StructLabel.place(relx=0.02, rely=0.197, height=21, width=86)
        self.StructLabel.configure(background="#d9d9d9")
        self.StructLabel.configure(disabledforeground="#a3a3a3")
        self.StructLabel.configure(foreground="#000000")
        self.StructLabel.configure(text='''StructureName''')

        self.ProcLabel = Label(self.AddMeasFrame)
        self.ProcLabel.place(relx=0.02, rely=0.36, height=20, width=81)
        self.ProcLabel.configure(background="#d9d9d9")
        self.ProcLabel.configure(disabledforeground="#a3a3a3")
        self.ProcLabel.configure(foreground="#000000")
        self.ProcLabel.configure(text='''Procedure File''')

        self.FuncLabel = Label(self.AddMeasFrame)
        self.FuncLabel.place(relx=0.02, rely=0.52, height=21, width=142)
        self.FuncLabel.configure(background="#d9d9d9")
        self.FuncLabel.configure(disabledforeground="#a3a3a3")
        self.FuncLabel.configure(foreground="#000000")
        self.FuncLabel.configure(text='''Function to be performed''')

        self.FuncBox = OptionMenu(self.AddMeasFrame,
        ScriptBuilder.FuncBoxVar,
        *self.Maitre.get_func_name(0),
        command = ScriptBuilder.FuncBoxChange
        )
        self.FuncBox.place(relx=0.02, rely=0.58, relheight=0.06, relwidth=0.72)
        self.FuncBox.configure(width=423)
        self.FuncBox.configure(takefocus="")

        self.ArgLabel = Label(self.AddMeasFrame)
        self.ArgLabel.place(relx=0.02, rely=0.64, height=21, width=65)
        self.ArgLabel.configure(background="#d9d9d9")
        self.ArgLabel.configure(disabledforeground="#a3a3a3")
        self.ArgLabel.configure(foreground="#000000")
        self.ArgLabel.configure(text='''Arguments''')

        self.ArgEntry = Entry(self.AddMeasFrame)
        self.ArgEntry.place(relx=0.02, rely=0.78, relheight=0.06, relwidth=0.72)
        self.ArgEntry.configure(background="white")
        self.ArgEntry.configure(disabledforeground="#a3a3a3")
        self.ArgEntry.configure(font="TkFixedFont")
        self.ArgEntry.configure(foreground="#000000")
        self.ArgEntry.configure(insertbackground="black")
        self.ArgEntry.configure(textvariable=ScriptBuilder.ArgEntryVar)
        self.ArgEntry.configure(width=424)

        self.ArgShowEntry = Entry(self.AddMeasFrame)
        self.ArgShowEntry.place(relx=0.02, rely=0.7, relheight=0.06
                , relwidth=0.72)
        self.ArgShowEntry.configure(background="white")
        self.ArgShowEntry.configure(disabledforeground="#a3a3a3")
        self.ArgShowEntry.configure(font="TkFixedFont")
        self.ArgShowEntry.configure(foreground="#000000")
        self.ArgShowEntry.configure(insertbackground="black")
        self.ArgShowEntry.configure(state=DISABLED)
        self.ArgShowEntry.configure(textvariable=ScriptBuilder.ArgShowEntryVar)
        self.ArgShowEntry.configure(width=424)

        self.AddMeasButton = Button(self.AddMeasFrame)
        self.AddMeasButton.place(relx=0.02, rely=0.87, height=24, width=147)
        self.AddMeasButton.configure(activebackground="#d9d9d9")
        self.AddMeasButton.configure(activeforeground="#000000")
        self.AddMeasButton.configure(background="#d9d9d9")
        self.AddMeasButton.configure(command=ScriptBuilder.addMeasurement)
        self.AddMeasButton.configure(disabledforeground="#a3a3a3")
        self.AddMeasButton.configure(foreground="#000000")
        self.AddMeasButton.configure(highlightbackground="#d9d9d9")
        self.AddMeasButton.configure(highlightcolor="black")
        self.AddMeasButton.configure(pady="0")
        self.AddMeasButton.configure(text='''AddMeasurement''')
        self.AddMeasButton.configure(width=147)

        self.AddBlockFrame = LabelFrame(top)
        self.AddBlockFrame.place(relx=0.03, rely=0.44, relheight=0.31
                , relwidth=0.5)
        self.AddBlockFrame.configure(relief=GROOVE)
        self.AddBlockFrame.configure(foreground="black")
        self.AddBlockFrame.configure(text='''Add Block''')
        self.AddBlockFrame.configure(background="#d9d9d9")
        self.AddBlockFrame.configure(width=590)

        self.AddBlockButton = Button(self.AddBlockFrame)
        self.AddBlockButton.place(relx=0.03, rely=0.83, height=24, width=142)
        self.AddBlockButton.configure(activebackground="#d9d9d9")
        self.AddBlockButton.configure(activeforeground="#000000")
        self.AddBlockButton.configure(background="#d9d9d9")
        self.AddBlockButton.configure(command=ScriptBuilder.addBlock)
        self.AddBlockButton.configure(disabledforeground="#a3a3a3")
        self.AddBlockButton.configure(foreground="#000000")
        self.AddBlockButton.configure(highlightbackground="#d9d9d9")
        self.AddBlockButton.configure(highlightcolor="black")
        self.AddBlockButton.configure(pady="0")
        self.AddBlockButton.configure(text='''Add Block''')
        self.AddBlockButton.configure(width=142)

        self.BlockTypeLabel = Label(self.AddBlockFrame)
        self.BlockTypeLabel.place(relx=0.03, rely=0.11, height=21, width=61)
        self.BlockTypeLabel.configure(background="#d9d9d9")
        self.BlockTypeLabel.configure(disabledforeground="#a3a3a3")
        self.BlockTypeLabel.configure(foreground="#000000")
        self.BlockTypeLabel.configure(text='''BlockType''')

        self.BlockTypeBox = OptionMenu(self.AddBlockFrame,
        ScriptBuilder.BlockTypeBoxVar,
        *('','Wafer','Chip','Group'))
        self.BlockTypeBox.place(relx=0.03, rely=0.19, relheight=0.08
                , relwidth=0.16)
        self.BlockTypeBox.configure(width=93)
        self.BlockTypeBox.configure(takefocus="")

        self.BlockNameLabel = Label(self.AddBlockFrame)
        self.BlockNameLabel.place(relx=0.31, rely=0.11, height=21, width=67)
        self.BlockNameLabel.configure(background="#d9d9d9")
        self.BlockNameLabel.configure(disabledforeground="#a3a3a3")
        self.BlockNameLabel.configure(foreground="#000000")
        self.BlockNameLabel.configure(text='''BlockName''')

        self.BlockNameEntry = Entry(self.AddBlockFrame)
        self.BlockNameEntry.place(relx=0.31, rely=0.19, relheight=0.08
                , relwidth=0.28)
        self.BlockNameEntry.configure(background="white")
        self.BlockNameEntry.configure(disabledforeground="#a3a3a3")
        self.BlockNameEntry.configure(font="TkFixedFont")
        self.BlockNameEntry.configure(foreground="#000000")
        self.BlockNameEntry.configure(insertbackground="black")
        self.BlockNameEntry.configure(textvariable=ScriptBuilder.BlockNameVar)

        self.CopyCheck = Checkbutton(self.AddBlockFrame)
        self.CopyCheck.place(relx=0.32, rely=0.83, relheight=0.09, relwidth=0.42)
        self.CopyCheck.configure(activebackground="#d9d9d9")
        self.CopyCheck.configure(activeforeground="#000000")
        self.CopyCheck.configure(background="#d9d9d9")
        self.CopyCheck.configure(disabledforeground="#a3a3a3")
        self.CopyCheck.configure(foreground="#000000")
        self.CopyCheck.configure(highlightbackground="#d9d9d9")
        self.CopyCheck.configure(highlightcolor="black")
        self.CopyCheck.configure(justify=LEFT)
        self.CopyCheck.configure(text='''Copy Measurements from previous Block''')
        self.CopyCheck.configure(variable=ScriptBuilder.copyLastMeasBlock)

        self.LocalBinFuncLabel = Label(self.AddBlockFrame)
        self.LocalBinFuncLabel.place(relx=0.03, rely=0.34, height=21, width=128)
        self.LocalBinFuncLabel.configure(background="#d9d9d9")
        self.LocalBinFuncLabel.configure(disabledforeground="#a3a3a3")
        self.LocalBinFuncLabel.configure(foreground="#000000")
        self.LocalBinFuncLabel.configure(text='''Local Binning Function''')

        self.LocalBinFuncFileLabel = Label(self.AddBlockFrame)
        self.LocalBinFuncFileLabel.place(relx=0.03, rely=0.42, height=21
                , width=24)
        self.LocalBinFuncFileLabel.configure(background="#d9d9d9")
        self.LocalBinFuncFileLabel.configure(disabledforeground="#a3a3a3")
        self.LocalBinFuncFileLabel.configure(foreground="#000000")
        self.LocalBinFuncFileLabel.configure(text='''File''')

        self.LocalBinFuncFileBox = OptionMenu(self.AddBlockFrame,
        ScriptBuilder.LocalBinFuncFileBoxVar,
        *self.Maitre.get_all_modules(),
        command = ScriptBuilder.LocalBinFuncFileBoxChange
        )
        self.LocalBinFuncFileBox.place(relx=0.03, rely=0.49, relheight=0.08
                , relwidth=0.7)
        self.LocalBinFuncFileBox.configure(width=413)
        self.LocalBinFuncFileBox.configure(takefocus="")

        self.LocalBinFuncFuncLabel = Label(self.AddBlockFrame)
        self.LocalBinFuncFuncLabel.place(relx=0.03, rely=0.6, height=21
                , width=53)
        self.LocalBinFuncFuncLabel.configure(background="#d9d9d9")
        self.LocalBinFuncFuncLabel.configure(disabledforeground="#a3a3a3")
        self.LocalBinFuncFuncLabel.configure(foreground="#000000")
        self.LocalBinFuncFuncLabel.configure(text='''Function''')

        self.LocalBinFuncFuncBox = OptionMenu(self.AddBlockFrame,
        ScriptBuilder.LocalBinFuncFuncBoxVar,
        *self.Maitre.get_func_name(0)
        )
        self.LocalBinFuncFuncBox.place(relx=0.03, rely=0.68, relheight=0.08
                , relwidth=0.7)
        self.LocalBinFuncFuncBox.configure(width=413)
        self.LocalBinFuncFuncBox.configure(takefocus="")

        self.GlobalSettingsFrame = LabelFrame(top)
        self.GlobalSettingsFrame.place(relx=0.03, rely=0.77, relheight=0.19
                , relwidth=0.5)
        self.GlobalSettingsFrame.configure(relief=GROOVE)
        self.GlobalSettingsFrame.configure(foreground="black")
        self.GlobalSettingsFrame.configure(text='''Global Settings''')
        self.GlobalSettingsFrame.configure(background="#d9d9d9")
        self.GlobalSettingsFrame.configure(width=590)

        self.GroupByLabel = Label(self.GlobalSettingsFrame)
        self.GroupByLabel.place(relx=0.8, rely=0.18, height=21, width=58)
        self.GroupByLabel.configure(background="#d9d9d9")
        self.GroupByLabel.configure(disabledforeground="#a3a3a3")
        self.GroupByLabel.configure(foreground="#000000")
        self.GroupByLabel.configure(text='''Group By:''')

        self.GroupByBox = OptionMenu(self.GlobalSettingsFrame,
        ScriptBuilder.GroupByBoxVar,
        *('','Wafer','Chip','Group'))
        self.GroupByBox.place(relx=0.8, rely=0.36, relheight=0.13, relwidth=0.14)
        self.GroupByBox.configure(width=83)
        self.GroupByBox.configure(takefocus="")

        self.GlobBinFuncLabel = Label(self.GlobalSettingsFrame)
        self.GlobBinFuncLabel.place(relx=0.02, rely=0.12, height=21, width=134)
        self.GlobBinFuncLabel.configure(background="#d9d9d9")
        self.GlobBinFuncLabel.configure(disabledforeground="#a3a3a3")
        self.GlobBinFuncLabel.configure(foreground="#000000")
        self.GlobBinFuncLabel.configure(text='''Global Binning Function''')

        self.GlobBinFuncFileLabel = Label(self.GlobalSettingsFrame)
        self.GlobBinFuncFileLabel.place(relx=0.02, rely=0.24, height=21
                , width=24)
        self.GlobBinFuncFileLabel.configure(background="#d9d9d9")
        self.GlobBinFuncFileLabel.configure(disabledforeground="#a3a3a3")
        self.GlobBinFuncFileLabel.configure(foreground="#000000")
        self.GlobBinFuncFileLabel.configure(text='''File''')

        self.GlobBinFuncFileBox = OptionMenu(self.GlobalSettingsFrame,
        ScriptBuilder.GlobBinFuncFileBoxVar,
        *self.Maitre.get_all_modules(),
        command = ScriptBuilder.GlobBinFuncFileBoxChange
        )
        self.GlobBinFuncFileBox.place(relx=0.02, rely=0.36, relheight=0.13
                , relwidth=0.72)
        self.GlobBinFuncFileBox.configure(width=423)
        self.GlobBinFuncFileBox.configure(takefocus="")

        self.GlobBinFuncFuncLabel = Label(self.GlobalSettingsFrame)
        self.GlobBinFuncFuncLabel.place(relx=0.02, rely=0.48, height=21
                , width=53)
        self.GlobBinFuncFuncLabel.configure(background="#d9d9d9")
        self.GlobBinFuncFuncLabel.configure(disabledforeground="#a3a3a3")
        self.GlobBinFuncFuncLabel.configure(foreground="#000000")
        self.GlobBinFuncFuncLabel.configure(text='''Function''')

        self.GlobBinFuncFuncBox = OptionMenu(self.GlobalSettingsFrame,
        ScriptBuilder.GlobBinFuncFuncBoxVar,
        *self.Maitre.get_func_name(0)
        )
        self.GlobBinFuncFuncBox.place(relx=0.02, rely=0.61, relheight=0.13
                , relwidth=0.72)
        self.GlobBinFuncFuncBox.configure(width=423)
        self.GlobBinFuncFuncBox.configure(takefocus="")

        self.GlobalUpdateButton = Button(self.GlobalSettingsFrame)
        self.GlobalUpdateButton.place(relx=0.02, rely=0.79, height=24, width=137)
        self.GlobalUpdateButton.configure(activebackground="#d9d9d9")
        self.GlobalUpdateButton.configure(activeforeground="#000000")
        self.GlobalUpdateButton.configure(background="#d9d9d9")
        self.GlobalUpdateButton.configure(disabledforeground="#a3a3a3")
        self.GlobalUpdateButton.configure(foreground="#000000")
        self.GlobalUpdateButton.configure(highlightbackground="#d9d9d9")
        self.GlobalUpdateButton.configure(highlightcolor="black")
        self.GlobalUpdateButton.configure(pady="0")
        self.GlobalUpdateButton.configure(text='''Update''')
        self.GlobalUpdateButton.configure(width=137)
        self.GlobalUpdateButton.configure(command=ScriptBuilder.GlobalsUpdate)





# The following code is added to facilitate the Scrolled widgets you specified.
class AutoScroll(object):
    '''Configure the scrollbars for a widget.'''

    def __init__(self, master):
        #  Rozen. Added the try-except clauses so that this class
        #  could be used for scrolled entry widget for which vertical
        #  scrolling is not supported. 5/7/14.
        try:
            vsb = ttk.Scrollbar(master, orient='vertical', command=self.yview)
        except:
            pass
        hsb = ttk.Scrollbar(master, orient='horizontal', command=self.xview)

        #self.configure(yscrollcommand=_autoscroll(vsb),
        #    xscrollcommand=_autoscroll(hsb))
        try:
            self.configure(yscrollcommand=self._autoscroll(vsb))
        except:
            pass
        self.configure(xscrollcommand=self._autoscroll(hsb))

        self.grid(column=0, row=0, sticky='nsew')
        try:
            vsb.grid(column=1, row=0, sticky='ns')
        except:
            pass
        hsb.grid(column=0, row=1, sticky='ew')

        master.grid_columnconfigure(0, weight=1)
        master.grid_rowconfigure(0, weight=1)

        # Copy geometry methods of master  (taken from ScrolledText.py)
        if py3:
            methods = Pack.__dict__.keys() | Grid.__dict__.keys() \
                  | Place.__dict__.keys()
        else:
            methods = Pack.__dict__.keys() + Grid.__dict__.keys() \
                  + Place.__dict__.keys()

        for meth in methods:
            if meth[0] != '_' and meth not in ('config', 'configure'):
                setattr(self, meth, getattr(master, meth))

    @staticmethod
    def _autoscroll(sbar):
        '''Hide and show scrollbar as needed.'''
        def wrapped(first, last):
            first, last = float(first), float(last)
            if first <= 0 and last >= 1:
                sbar.grid_remove()
            else:
                sbar.grid()
            sbar.set(first, last)
        return wrapped

    def __str__(self):
        return str(self.master)

def _create_container(func):
    '''Creates a ttk Frame with a given master, and use this new frame to
    place the scrollbars and the widget.'''
    def wrapped(cls, master, **kw):
        container = ttk.Frame(master)
        return func(cls, container, **kw)
    return wrapped

class ScrolledText(AutoScroll, Text):
    '''A standard Tkinter Text widget with scrollbars that will
    automatically show/hide as needed.'''
    @_create_container
    def __init__(self, master, **kw):
        Text.__init__(self, master, **kw)
        AutoScroll.__init__(self, master)

if __name__ == '__main__':
    vp_start_gui()
