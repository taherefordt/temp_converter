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
        self.temp_frame = Frame(padx=10, pady=10)
        self.temp_frame.grid()

        self.temp_heading = Label(self.temp_frame,
                                  text="Temperature Converter",
                                  font=("Arial", "16", "bold")
                                  )
        self.temp_heading.grid(row=0)

        instructions = "Please enter a temperature below and " \
                       "then press one of the buttons to convert " \
                       "it from centigrade to fahrenheit"

        self.temp_instructions = Label(self.temp_frame,
                                       text=instructions,
                                       wrap=250, width=40,
                                       justify="left")

        self.temp_instructions.grid(row=1)

        self.temp_entry = Entry(self.temp_frame,
                                font=("Arial", "14")
                                )
        self.temp_entry.grid(row=2, padx=10, pady=10)

        error = "Please enter a number"
        self.temp_error = Label(self.temp_frame,
                                text=error,
                                font=("Arial", "10", "bold"),
                                fg="#9C0000")

        self.temp_error.grid(row=3)

        self.button_frame = Frame(self.temp_frame)
        self.button_frame.grid(row=4)

        self.temp_celsius = Button(self.button_frame,
                                   text="In Celsius",
                                   width=13,
                                   font=button_font,
                                   fg=button_fg,
                                   bg="#004C99",
                                   command=self.to_celsius)

        self.temp_celsius.grid(row=0, column=0, padx=5, pady=5)

        self.temp_fahrenheit = Button(self.button_frame,
                                      text="In Fahrenheit",
                                      width=13,
                                      font=button_font,
                                      fg=button_fg,
                                      bg="#d1001f")

        self.temp_fahrenheit.grid(row=0, column=1, padx=5, pady=5)

        # helpinfo = help + info
        self.to_helpinfo = Button(self.button_frame,
                                  text="Help/info",
                                  width=13,
                                  font=button_font,
                                  fg=button_fg,
                                  bg="#009900", )

        self.to_helpinfo.grid(row=1, column=0, padx=5, pady=5)

        # history_port = history + export
        self.to_history_port = Button(self.button_frame,
                                  text="History/Export",
                                  width=13,
                                  font=button_font,
                                  fg=button_fg,
                                  bg="#e6cc00",
                                  state=DISABLED)

        self.to_histport.grid(row=1, column=1, padx=5, pady=5)


    def input_temp(self, min_temp):
        error = f"Please enter a number that is more than {min_temp}"
        has_error = ""

        try:

            temperature = self.temp_entry.get()
            temperature = float(temperature)

            # Checks response is not too low
            if temperature < min_temp:
                self.temp_error.config(text=error, fg="#FF0024")
                self.temp_entry.config(bg="#FA8072")

            else:
                self.temp_error.config(text="valid temp", fg="blue")
                self.temp_entry.config(bg="#FFFFFF")

        # checks input is a integer
        except ValueError:
            has_error = "yes"

        if has_error == "yes":
            self.var_has_error.set("yes")
            self.var_feedback.set(error)
            return "invalid"

        else:

            # when there is at least 1 valid calculation, display error message.
            # enables the history/export button
            self.to_history_port.config(state=NORMAL)

    def to_celsius(self):
        self.input_temp(-459)


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("temperature converter")
    Converter()
    root.mainloop()
