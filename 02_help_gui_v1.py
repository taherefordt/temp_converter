import tkinter
from tkinter import *


class Converter:

    def __init__(self):

        self.var_feedback = StringVar()
        self.var_feedback.set("")

        self.var_has_error = StringVar()
        self.var_has_error.set("no")

        button_font = ("Arial", "12", "bold")
        button_fg = "#FFFFFF"

        # sets up GUI widget
        self.temp_frame = Frame(padx=10, pady=10,)
        self.temp_frame.grid()

        self.temp_heading = Label(self.temp_frame,
                                  text="Help and information",
                                  font=("Arial", "16", "bold"),
                                  )
        self.temp_heading.grid(row=0)

        instructions = "Please enter a temperature below and " \
                       "then press one of the buttons to convert " \
                       "it from centigrade to fahrenheit"

        self.temp_instructions = Label(self.temp_frame,
                                       text=instructions,
                                       wrap=250, width=40,
                                       justify="left",)

        self.temp_instructions.grid(row=1)

        self.to_helpinfo = Button(self.temp_frame,
                                  text="help",
                                  width=13,
                                  font=button_font,
                                  fg=button_fg,
                                  bg="#e6cc00",
                                  command=self.to_help)

        self.to_helpinfo.grid(row=2)

    def to_help(self):
        self.to_helpinfo.config(state=DISABLED)
        Display_help()




class Display_help:

    def __init__(self):

        backdrop = "#ffe6cc"
        label_font = ("Arial", "12")

        self.help_box = Toplevel()

        self.help_frame = Frame(self.help_box, width=300,
                                height=200, bg=backdrop)
        self.help_frame.grid()

        self.help_heading = Label(self.help_frame, bg=backdrop,
                               text="Help/info",
                               font=("Arial", "14", "bold"), width=15
                               )
        self.help_heading.grid(row=0, padx=5, pady=5)

        help_text = "To use this program simply enter the temperature you wish to convert," \
                    " and then choose to convert it to either celsius or fahrenheit" \
                    "\n\n" \
                    "Note that 273 degrees C" \
                    "(-459F) is absolute zero (the coldest possible temperature)." \
                    " If you try to convert anything less than -273 degrees C " \
                    "you will get an error message \n\n" \
                    "To see your calculation history and export it to a text" \
                    "file, please click the 'History/Export' button."

        self.help_text_label = Label(self.help_frame, font=label_font,
                                     text=help_text, wrap=250,
                                     bg=backdrop)
        self.help_text_label.grid()




# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("temperature converter")
    Converter()
    root.mainloop()
