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

        self.button_frame = Frame(self.temp_frame)
        self.button_frame.grid(row=4)

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

        # history_port = history + export
        self.to_history_port = Button(self.button_frame,
                                      text="History/Export",
                                      width=13,
                                      font=button_font,
                                      fg=button_fg,
                                      bg="#e6cc00",
                                      state=DISABLED,
                                      command=self.to_history)

        self.to_history_port.grid(row=1, column=1, padx=5, pady=5)

        self.to_history_port.config(state=NORMAL)

    def to_history(self):
        Help_export()


class Help_export:

    def __init__(self):

        backdrop = "#ffe6cc"
        label_font = ("Arial", "12")

        self.history_box = Toplevel()

        self.history_frame = Frame(self.history_box, width=300,
                                   height=200, bg=backdrop)
        self.history_frame.grid()

        self.history_heading = Label(self.history_frame, bg=backdrop,
                                     text="Help/info",
                                     font=("Arial", "14", "bold"), width=15
                                     )
        self.history_heading.grid(row=0, padx=5, pady=5)

        hisory_text = "To use this program simply enter the temperature you wish to convert," \
                    " and then choose to convert it to either celsius or fahrenheit" \
                    "\n\n" \
                    "Note that 273 degrees C" \
                    "(-459F) is absolute zero (the coldest possible temperature)." \
                    " If you try to convert anything less than -273 degrees C " \
                    "you will get an error message \n\n" \
                    "To see your calculation history and export it to a text" \
                    "file, please click the 'History/Export' button."

        self.history_text_label = Label(self.history_frame, font=label_font,
                                        text=hisory_text, wrap=250,
                                        bg=backdrop)
        self.history_text_label.grid()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("temperature converter")
    Converter()
    root.mainloop()
