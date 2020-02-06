import sys
import re
from bs4 import BeautifulSoup

with open('output.html', 'r') as file:
    fcontent = file.read()

sp = BeautifulSoup(fcontent, 'html.parser')

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import tournament_layout_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    root.iconbitmap('favicon.ico')
    tournament_layout_support.set_Tk_var()
    top = tournamentControlPanel (root)
    tournament_layout_support.init(root, top)
    root.mainloop()

w = None
def create_tournamentControlPanel(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    tournament_layout_support.set_Tk_var()
    top = tournamentControlPanel (w)
    tournament_layout_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_tournamentControlPanel():
    global w
    w.destroy()
    w = None

class tournamentControlPanel:
    def __init__(self, top=None):

        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font10 = "-family {Segoe UI} -size 9 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"
        font9 = "-family {Segoe UI} -size 9 -weight bold -slant roman "  \
            "-underline 0 -overstrike 0"
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("535x392+512+255")
        top.minsize(120, 1)
        top.maxsize(3204, 1061)
        top.resizable(0, 0)
        top.title("SM64 Tournament Control Panel")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.runnerOneFrame = tk.Frame(top)
        self.runnerOneFrame.place(relx=0.019, rely=0.102, relheight=0.395
                , relwidth=0.477)
        self.runnerOneFrame.configure(relief='groove')
        self.runnerOneFrame.configure(borderwidth="2")
        self.runnerOneFrame.configure(relief="groove")
        self.runnerOneFrame.configure(background="#d9d9d9")
        self.runnerOneFrame.configure(highlightbackground="#d9d9d9")
        self.runnerOneFrame.configure(highlightcolor="black")

        self.runnerOneTitle = tk.Label(self.runnerOneFrame)
        self.runnerOneTitle.place(relx=0.314, rely=0.065, height=21, width=98)
        self.runnerOneTitle.configure(activebackground="#f9f9f9")
        self.runnerOneTitle.configure(activeforeground="black")
        self.runnerOneTitle.configure(background="#d9d9d9")
        self.runnerOneTitle.configure(disabledforeground="#a3a3a3")
        self.runnerOneTitle.configure(font=font9)
        self.runnerOneTitle.configure(foreground="#000000")
        self.runnerOneTitle.configure(highlightbackground="#d9d9d9")
        self.runnerOneTitle.configure(highlightcolor="black")
        self.runnerOneTitle.configure(text='''Runner #1 (Left)''')

        self.runnerOnePlatformLabel = tk.Label(self.runnerOneFrame)
        self.runnerOnePlatformLabel.place(relx=0.039, rely=0.31, height=21
                , width=62)
        self.runnerOnePlatformLabel.configure(activebackground="#f9f9f9")
        self.runnerOnePlatformLabel.configure(activeforeground="black")
        self.runnerOnePlatformLabel.configure(background="#d9d9d9")
        self.runnerOnePlatformLabel.configure(disabledforeground="#a3a3a3")
        self.runnerOnePlatformLabel.configure(foreground="#000000")
        self.runnerOnePlatformLabel.configure(highlightbackground="#d9d9d9")
        self.runnerOnePlatformLabel.configure(highlightcolor="black")
        self.runnerOnePlatformLabel.configure(relief="groove")
        self.runnerOnePlatformLabel.configure(text='''Platform:''')

        self.runnerOnePlatformInput = ttk.Combobox(self.runnerOneFrame, state="readonly")
        self.runnerOnePlatformInput.place(relx=0.29, rely=0.31, relheight=0.135
                , relwidth=0.573)
        self.runnerOnePlatformInput.configure(takefocus="")
        self.runnerOnePlatformInput['values'] = ("Twitch", "YouTube")
        self.runnerOnePlatformInput.set("Twitch")

        self.runnerOneUsernameLabel = tk.Label(self.runnerOneFrame)
        self.runnerOneUsernameLabel.place(relx=0.039, rely=0.452, height=21
                , width=62)
        self.runnerOneUsernameLabel.configure(activebackground="#f9f9f9")
        self.runnerOneUsernameLabel.configure(activeforeground="black")
        self.runnerOneUsernameLabel.configure(background="#d9d9d9")
        self.runnerOneUsernameLabel.configure(disabledforeground="#a3a3a3")
        self.runnerOneUsernameLabel.configure(foreground="#000000")
        self.runnerOneUsernameLabel.configure(highlightbackground="#d9d9d9")
        self.runnerOneUsernameLabel.configure(highlightcolor="black")
        self.runnerOneUsernameLabel.configure(relief="groove")
        self.runnerOneUsernameLabel.configure(text='''Username:''')

        self.runnerOneUsernameInput = ttk.Entry(self.runnerOneFrame)
        self.runnerOneUsernameInput.place(relx=0.29, rely=0.452, relheight=0.135
                , relwidth=0.573)
        self.runnerOneUsernameInput.configure(takefocus="")
        # self.runnerOneUsernameInput.configure(cursor="ibeam")

        self.runnerOneScoreLabel = tk.Label(self.runnerOneFrame)
        self.runnerOneScoreLabel.place(relx=0.039, rely=0.594, height=21
                , width=62)
        self.runnerOneScoreLabel.configure(activebackground="#f9f9f9")
        self.runnerOneScoreLabel.configure(activeforeground="black")
        self.runnerOneScoreLabel.configure(background="#d9d9d9")
        self.runnerOneScoreLabel.configure(disabledforeground="#a3a3a3")
        self.runnerOneScoreLabel.configure(foreground="#000000")
        self.runnerOneScoreLabel.configure(highlightbackground="#d9d9d9")
        self.runnerOneScoreLabel.configure(highlightcolor="black")
        self.runnerOneScoreLabel.configure(relief="groove")
        self.runnerOneScoreLabel.configure(text='''Score:''')

        self.runnerOneScoreInput = tk.Spinbox(self.runnerOneFrame, from_=0, to=9)
        self.runnerOneScoreInput.place(relx=0.29, rely=0.594, relheight=0.135
                , relwidth=0.576)
        self.runnerOneScoreInput.configure(activebackground="#f9f9f9")
        self.runnerOneScoreInput.configure(background="white")
        self.runnerOneScoreInput.configure(buttonbackground="#d9d9d9")
        self.runnerOneScoreInput.configure(disabledforeground="#a3a3a3")
        self.runnerOneScoreInput.configure(font="TkDefaultFont")
        self.runnerOneScoreInput.configure(foreground="black")
        self.runnerOneScoreInput.configure(highlightbackground="black")
        self.runnerOneScoreInput.configure(highlightcolor="black")
        self.runnerOneScoreInput.configure(insertbackground="black")
        self.runnerOneScoreInput.configure(selectbackground="#c4c4c4")
        self.runnerOneScoreInput.configure(selectforeground="black")

        self.runnerTwoFrame = tk.Frame(top)
        self.runnerTwoFrame.place(relx=0.505, rely=0.102, relheight=0.395
                , relwidth=0.477)
        self.runnerTwoFrame.configure(relief='groove')
        self.runnerTwoFrame.configure(borderwidth="2")
        self.runnerTwoFrame.configure(relief="groove")
        self.runnerTwoFrame.configure(background="#d9d9d9")
        self.runnerTwoFrame.configure(highlightbackground="#d9d9d9")
        self.runnerTwoFrame.configure(highlightcolor="black")

        self.runnerTwoTitle = tk.Label(self.runnerTwoFrame)
        self.runnerTwoTitle.place(relx=0.275, rely=0.065, height=21, width=105)
        self.runnerTwoTitle.configure(activebackground="#f9f9f9")
        self.runnerTwoTitle.configure(activeforeground="black")
        self.runnerTwoTitle.configure(background="#d9d9d9")
        self.runnerTwoTitle.configure(disabledforeground="#a3a3a3")
        self.runnerTwoTitle.configure(font=font9)
        self.runnerTwoTitle.configure(foreground="#000000")
        self.runnerTwoTitle.configure(highlightbackground="#d9d9d9")
        self.runnerTwoTitle.configure(highlightcolor="black")
        self.runnerTwoTitle.configure(text='''Runner #2 (Right)''')

        self.runnerTwoPlatformLabel = tk.Label(self.runnerTwoFrame)
        self.runnerTwoPlatformLabel.place(relx=0.039, rely=0.323, height=21
                , width=62)
        self.runnerTwoPlatformLabel.configure(activebackground="#f9f9f9")
        self.runnerTwoPlatformLabel.configure(activeforeground="black")
        self.runnerTwoPlatformLabel.configure(background="#d9d9d9")
        self.runnerTwoPlatformLabel.configure(disabledforeground="#a3a3a3")
        self.runnerTwoPlatformLabel.configure(foreground="#000000")
        self.runnerTwoPlatformLabel.configure(highlightbackground="#d9d9d9")
        self.runnerTwoPlatformLabel.configure(highlightcolor="black")
        self.runnerTwoPlatformLabel.configure(relief="groove")
        self.runnerTwoPlatformLabel.configure(text='''Platform:''')

        self.runnerTwoUsernameLabel = tk.Label(self.runnerTwoFrame)
        self.runnerTwoUsernameLabel.place(relx=0.039, rely=0.465, height=21
                , width=62)
        self.runnerTwoUsernameLabel.configure(activebackground="#f9f9f9")
        self.runnerTwoUsernameLabel.configure(activeforeground="black")
        self.runnerTwoUsernameLabel.configure(background="#d9d9d9")
        self.runnerTwoUsernameLabel.configure(disabledforeground="#a3a3a3")
        self.runnerTwoUsernameLabel.configure(foreground="#000000")
        self.runnerTwoUsernameLabel.configure(highlightbackground="#d9d9d9")
        self.runnerTwoUsernameLabel.configure(highlightcolor="black")
        self.runnerTwoUsernameLabel.configure(relief="groove")
        self.runnerTwoUsernameLabel.configure(text='''Username:''')

        self.runnerTwoScoreLabel = tk.Label(self.runnerTwoFrame)
        self.runnerTwoScoreLabel.place(relx=0.039, rely=0.6, height=21, width=62)

        self.runnerTwoScoreLabel.configure(activebackground="#f9f9f9")
        self.runnerTwoScoreLabel.configure(activeforeground="black")
        self.runnerTwoScoreLabel.configure(background="#d9d9d9")
        self.runnerTwoScoreLabel.configure(disabledforeground="#a3a3a3")
        self.runnerTwoScoreLabel.configure(foreground="#000000")
        self.runnerTwoScoreLabel.configure(highlightbackground="#d9d9d9")
        self.runnerTwoScoreLabel.configure(highlightcolor="black")
        self.runnerTwoScoreLabel.configure(relief="groove")
        self.runnerTwoScoreLabel.configure(text='''Score:''')

        self.runnerTwoPlatformInput = ttk.Combobox(self.runnerTwoFrame, state="readonly")
        self.runnerTwoPlatformInput.place(relx=0.29, rely=0.323, relheight=0.135
                , relwidth=0.573)
        self.runnerTwoPlatformInput.configure(takefocus="")
        self.runnerTwoPlatformInput['values'] = ("Twitch", "YouTube")
        self.runnerTwoPlatformInput.set("Twitch")

        self.runnerTwoUsernameInput = ttk.Entry(self.runnerTwoFrame)
        self.runnerTwoUsernameInput.place(relx=0.29, rely=0.465, relheight=0.135
                , relwidth=0.573)
        self.runnerTwoUsernameInput.configure(takefocus="")
        # self.runnerTwoUsernameInput.configure(cursor="ibeam")


        self.runnerTwoScoreInput = tk.Spinbox(self.runnerTwoFrame, from_=0, to=9)
        self.runnerTwoScoreInput.place(relx=0.29, rely=0.606, relheight=0.135
                , relwidth=0.576)
        self.runnerTwoScoreInput.configure(activebackground="#f9f9f9")
        self.runnerTwoScoreInput.configure(background="white")
        self.runnerTwoScoreInput.configure(buttonbackground="#d9d9d9")
        self.runnerTwoScoreInput.configure(disabledforeground="#a3a3a3")
        self.runnerTwoScoreInput.configure(font="TkDefaultFont")
        self.runnerTwoScoreInput.configure(foreground="black")
        self.runnerTwoScoreInput.configure(highlightbackground="black")
        self.runnerTwoScoreInput.configure(highlightcolor="black")
        self.runnerTwoScoreInput.configure(insertbackground="black")
        self.runnerTwoScoreInput.configure(selectbackground="#c4c4c4")
        self.runnerTwoScoreInput.configure(selectforeground="black")

        self.casterOneFrame = tk.Frame(top)
        self.casterOneFrame.place(relx=0.019, rely=0.51, relheight=0.319
                , relwidth=0.477)
        self.casterOneFrame.configure(relief='groove')
        self.casterOneFrame.configure(borderwidth="2")
        self.casterOneFrame.configure(relief="groove")
        self.casterOneFrame.configure(background="#d9d9d9")
        self.casterOneFrame.configure(highlightbackground="#d9d9d9")
        self.casterOneFrame.configure(highlightcolor="black")

        self.casterOneTitle = tk.Label(self.casterOneFrame)
        self.casterOneTitle.place(relx=0.392, rely=0.08, height=21, width=58)
        self.casterOneTitle.configure(activebackground="#f9f9f9")
        self.casterOneTitle.configure(activeforeground="black")
        self.casterOneTitle.configure(background="#d9d9d9")
        self.casterOneTitle.configure(disabledforeground="#a3a3a3")
        self.casterOneTitle.configure(font=font9)
        self.casterOneTitle.configure(foreground="#000000")
        self.casterOneTitle.configure(highlightbackground="#d9d9d9")
        self.casterOneTitle.configure(highlightcolor="black")
        self.casterOneTitle.configure(text='''Caster #1''')

        self.casterOneUernameLabel = tk.Label(self.casterOneFrame)
        self.casterOneUernameLabel.place(relx=0.039, rely=0.368, height=21
                , width=62)
        self.casterOneUernameLabel.configure(activebackground="#f9f9f9")
        self.casterOneUernameLabel.configure(activeforeground="black")
        self.casterOneUernameLabel.configure(background="#d9d9d9")
        self.casterOneUernameLabel.configure(disabledforeground="#a3a3a3")
        self.casterOneUernameLabel.configure(foreground="#000000")
        self.casterOneUernameLabel.configure(highlightbackground="#d9d9d9")
        self.casterOneUernameLabel.configure(highlightcolor="black")
        self.casterOneUernameLabel.configure(relief="groove")
        self.casterOneUernameLabel.configure(text='''Username:''')

        self.casterOneUsernameInput = ttk.Entry(self.casterOneFrame)
        self.casterOneUsernameInput.place(relx=0.29, rely=0.368, relheight=0.168
                , relwidth=0.573)
        self.casterOneUsernameInput.configure(takefocus="")
        # self.casterOneUsernameInput.configure(cursor="ibeam")

        self.casterTwoFrame = tk.Frame(top)
        self.casterTwoFrame.place(relx=0.505, rely=0.51, relheight=0.319
                , relwidth=0.479)
        self.casterTwoFrame.configure(relief='groove')
        self.casterTwoFrame.configure(borderwidth="2")
        self.casterTwoFrame.configure(relief="groove")
        self.casterTwoFrame.configure(background="#d9d9d9")
        self.casterTwoFrame.configure(highlightbackground="#d9d9d9")
        self.casterTwoFrame.configure(highlightcolor="black")

        self.casterTwoTitle = tk.Label(self.casterTwoFrame)
        self.casterTwoTitle.place(relx=0.273, rely=0.08, height=21, width=116)
        self.casterTwoTitle.configure(activebackground="#f9f9f9")
        self.casterTwoTitle.configure(activeforeground="black")
        self.casterTwoTitle.configure(background="#d9d9d9")
        self.casterTwoTitle.configure(disabledforeground="#a3a3a3")
        self.casterTwoTitle.configure(font=font9)
        self.casterTwoTitle.configure(foreground="#000000")
        self.casterTwoTitle.configure(highlightbackground="#d9d9d9")
        self.casterTwoTitle.configure(highlightcolor="black")
        self.casterTwoTitle.configure(text='''Caster #2 (Optional)''')

        self.casterTwoUsernameLabel = tk.Label(self.casterTwoFrame)
        self.casterTwoUsernameLabel.place(relx=0.039, rely=0.4, height=21
                , width=62)
        self.casterTwoUsernameLabel.configure(activebackground="#f9f9f9")
        self.casterTwoUsernameLabel.configure(activeforeground="black")
        self.casterTwoUsernameLabel.configure(background="#d9d9d9")
        self.casterTwoUsernameLabel.configure(disabledforeground="#a3a3a3")
        self.casterTwoUsernameLabel.configure(foreground="#000000")
        self.casterTwoUsernameLabel.configure(highlightbackground="#d9d9d9")
        self.casterTwoUsernameLabel.configure(highlightcolor="black")
        self.casterTwoUsernameLabel.configure(relief="groove")
        self.casterTwoUsernameLabel.configure(text='''Username:''')

        self.casterTwoUsernameInput = ttk.Entry(self.casterTwoFrame)
        self.casterTwoUsernameInput.place(relx=0.289, rely=0.4, relheight=0.168
                , relwidth=0.57)
        self.casterTwoUsernameInput.configure(takefocus="")
        # self.casterTwoUsernameInput.configure(cursor="ibeam")

        self.casterTwoPresentCheck = tk.Checkbutton(self.casterTwoFrame)
        self.casterTwoPresentCheck.place(relx=0.352, rely=0.64, relheight=0.2
                , relwidth=0.266)
        self.casterTwoPresentCheck.configure(activebackground="#ececec")
        self.casterTwoPresentCheck.configure(activeforeground="#000000")
        self.casterTwoPresentCheck.configure(background="#d9d9d9")
        self.casterTwoPresentCheck.configure(disabledforeground="#a3a3a3")
        self.casterTwoPresentCheck.configure(foreground="#000000")
        self.casterTwoPresentCheck.configure(highlightbackground="#d9d9d9")
        self.casterTwoPresentCheck.configure(highlightcolor="black")
        self.casterTwoPresentCheck.configure(justify='left')
        self.casterTwoPresentCheck.configure(offvalue="0")
        self.casterTwoPresentCheck.configure(onvalue="1")
        self.casterTwoPresentCheck.configure(text='''Enable?''')
        self.casterTwoPresentCheck.configure(variable=tournament_layout_support.che43)

        def saveUpdateButtonPress():
            twitchIcon = './assets/twitch.png'
            youtubeIcon = './assets/youtube.png'

            sp.find(id='run-info-text').string = self.streamTitleInput.get() # Update Stream Title

            # Set Platform src location depending on user selection
            if self.runnerOnePlatformInput.get() == "Twitch":
                sp.find(id='runner-one-platform').img['src'] = twitchIcon
            elif self.runnerOnePlatformInput.get() == "YouTube":
                sp.find(id='runner-one-platform').img['src'] = youtubeIcon

            sp.find(id='runner-one-username').string = self.runnerOneUsernameInput.get() # Update Runner #1 Username
            sp.find(id='runner-one-score').string = self.runnerOneScoreInput.get() # Update Runner #1 Score

            ###

            if self.runnerTwoPlatformInput.get() == "Twitch":
                sp.find(id='runner-two-platform').img['src'] = twitchIcon
            elif self.runnerTwoPlatformInput.get() == "YouTube":
                sp.find(id='runner-two-platform').img['src'] = youtubeIcon

            sp.find(id='runner-two-username').string = self.runnerTwoUsernameInput.get() # Update Runner #2 Username
            sp.find(id='runner-two-score').string = self.runnerTwoScoreInput.get() # Update Runner #2 Score

            sp.find(id='caster-one-username').string = self.casterOneUsernameInput.get() # Update Caster #1 Username


            # Caster 2 Checkbox Visibility
            if tournament_layout_support.che43.get() == 1:
                sp.find(id='bottom-area-row-caster')['style'] = 'display: table'
                sp.find(id='caster-two-username').string = self.casterTwoUsernameInput.get() # Update Caster #2 Username
            elif tournament_layout_support.che43.get() == 0:
                sp.find(id='bottom-area-row-caster')['style'] = 'display: none'
                sp.find(id='caster-two-username').string = self.casterTwoUsernameInput.get() # Update Caster #2 Username

            with open('output.html', 'w') as fp:
                # write the current soup content
                fp.write(sp.prettify())

        self.saveUpdateButton = tk.Button(top, command=saveUpdateButtonPress)
        self.saveUpdateButton.place(relx=0.355, rely=0.842, height=34, width=167)

        self.saveUpdateButton.configure(activebackground="#ececec")
        self.saveUpdateButton.configure(activeforeground="#000000")
        self.saveUpdateButton.configure(background="#d9d9d9")
        self.saveUpdateButton.configure(disabledforeground="#a3a3a3")
        self.saveUpdateButton.configure(foreground="#000000")
        self.saveUpdateButton.configure(highlightbackground="#d9d9d9")
        self.saveUpdateButton.configure(highlightcolor="black")
        self.saveUpdateButton.configure(pady="0")
        self.saveUpdateButton.configure(text='''Save & Update''')

        self.Label8 = tk.Label(top)
        self.Label8.place(relx=0.019, rely=0.026, height=21, width=82)
        self.Label8.configure(activebackground="#f9f9f9")
        self.Label8.configure(activeforeground="black")
        self.Label8.configure(background="#d9d9d9")
        self.Label8.configure(disabledforeground="#a3a3a3")
        self.Label8.configure(font=font10)
        self.Label8.configure(foreground="#000000")
        self.Label8.configure(highlightbackground="#d9d9d9")
        self.Label8.configure(highlightcolor="black")
        self.Label8.configure(relief="groove")
        self.Label8.configure(text='''Category Title:''')

        self.streamTitleInput = ttk.Entry(top)
        self.streamTitleInput.place(relx=0.176, rely=0.026, relheight=0.054
                , relwidth=0.479)
        self.streamTitleInput.configure(takefocus="")
        # self.streamTitleInput.configure(cursor="ibeam")

        def resetButtonPress():
            scoreReset = 0

            whitespaceReset = self.streamTitleInput.get() # Update Stream Title

            self.runnerOnePlatformInput.set("Twitch");
            whitespaceReset = self.runnerOneUsernameInput.get() # Update Runner #1 Username
            scoreReset = self.runnerOneScoreInput.get() # Update Runner #1 Score

            self.runnerTwoPlatformInput.set("Twitch");
            whitespaceReset = self.runnerTwoUsernameInput.get() # Update Runner #2 Username
            scoreReset = self.runnerTwoScoreInput.get() # Update Runner #2 Score

            whitespaceReset = self.casterOneUsernameInput.get() # Update Caster #1 Username

            whitespaceReset = self.casterTwoUsernameInput.get() # Update Caster #2 Username

            # Title
            self.streamTitleInput.delete(0, tk.END)

            # Runner #1
            self.runnerOneUsernameInput.delete(0, tk.END)
            self.runnerOneScoreInput.delete(0, tk.END)
            self.runnerOneScoreInput.insert(0, 0)

            # Runner #2
            self.runnerTwoUsernameInput.delete(0, tk.END)
            self.runnerTwoScoreInput.delete(0, tk.END)
            self.runnerTwoScoreInput.insert(0, 0)

            # Caster #1
            self.casterOneUsernameInput.delete(0, tk.END)

            # Caster #2
            tournament_layout_support.che43.set(0)
            self.casterTwoUsernameInput.delete(0, tk.END)

        self.resetButton = tk.Button(top, command=resetButtonPress)
        self.resetButton.place(relx=0.83, rely=0.026, height=24, width=80)
        self.resetButton.configure(activebackground="#ececec")
        self.resetButton.configure(activeforeground="#000000")
        self.resetButton.configure(background="#d9d9d9")
        self.resetButton.configure(disabledforeground="#a3a3a3")
        self.resetButton.configure(foreground="#000000")
        self.resetButton.configure(highlightbackground="#d9d9d9")
        self.resetButton.configure(highlightcolor="black")
        self.resetButton.configure(pady="0")
        self.resetButton.configure(text='''Reset Defaults''')

        self.authorCreditsLabel = tk.Label(top)
        self.authorCreditsLabel.place(relx=0.636, rely=0.944, height=21
                , width=191)
        self.authorCreditsLabel.configure(background="#d9d9d9")
        self.authorCreditsLabel.configure(disabledforeground="#a3a3a3")
        self.authorCreditsLabel.configure(font=font9)
        self.authorCreditsLabel.configure(foreground="#000000")
        self.authorCreditsLabel.configure(text='''Written by github.com/maksrago''')

        # Additions

        streamTitle = sp.find(id='run-info-text').string

        if sp.find(id='runner-one-platform').img['src'] == './assets/twitch.png':
            runnerOnePlatform = "Twitch"
        elif sp.find(id='runner-one-platform').img['src'] == './assets/youtube.png':
            runnerOnePlatform = "YouTube"

        runnerOneUsername = sp.find(id='runner-one-username').string
        runnerOneScore = sp.find(id='runner-one-score').string

        if sp.find(id='runner-two-platform').img['src'] == './assets/twitch.png':
            runnerTwoPlatform = "Twitch"
        elif sp.find(id='runner-two-platform').img['src'] == './assets/youtube.png':
            runnerTwoPlatform = "YouTube"

        runnerTwoUsername = sp.find(id='runner-two-username').string
        runnerTwoScore = sp.find(id='runner-two-score').string

        casterOneUsername = sp.find(id='caster-one-username').string

        casterTwoUsername = sp.find(id='caster-two-username').string

        def stripWhiteSpace(messy):
            messy = re.sub("^\s+|\s+$", "", messy, flags=re.UNICODE)
            return messy

        # Clean up input whitespace from file
        streamTitle = stripWhiteSpace(streamTitle)

        runnerOneUsername = stripWhiteSpace(runnerOneUsername)
        runnerOneScore = stripWhiteSpace(runnerOneScore)

        runnerTwoUsername = stripWhiteSpace(runnerTwoUsername)
        runnerTwoScore = stripWhiteSpace(runnerTwoScore)

        casterOneUsername = stripWhiteSpace(casterOneUsername)

        casterTwoUsername = stripWhiteSpace(casterTwoUsername)

        #Set Cleaned up data up

        # Title
        self.streamTitleInput.insert(0, streamTitle)

        # Runner #1
        self.runnerOnePlatformInput.set(runnerOnePlatform)
        self.runnerOneUsernameInput.insert(0, runnerOneUsername)
        self.runnerOneScoreInput.delete(0, tk.END)
        self.runnerOneScoreInput.insert(0, runnerOneScore)

        # Runner #2
        self.runnerTwoPlatformInput.set(runnerTwoPlatform)
        self.runnerTwoUsernameInput.insert(0, runnerTwoUsername)
        self.runnerTwoScoreInput.delete(0, tk.END)
        self.runnerTwoScoreInput.insert(1, runnerTwoScore)

        # Caster #1
        self.casterOneUsernameInput.insert(0, casterOneUsername)

        # Caster #2
        self.casterTwoUsernameInput.insert(0, casterTwoUsername)


if __name__ == '__main__':
    vp_start_gui()
