from functools import partial
from tkinter import *


class Converter:

    def __init__(self):

        self.var_feedback = StringVar()
        self.var_feedback.set("")

        self.var_has_error = StringVar()
        self.var_has_error.set("no")

        self.all_calculations = []

        button_font = ("Arial", "12", "bold")
        button_fg = "#FFFFFF"
        calc_list = []

        # sets up GUI widget
        self.temp_frame = Frame(padx=5, pady=5)
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
                                font=("Arial", "14"),
                                bg="#D3D3D3")
        self.temp_entry.grid(row=2, padx=5, pady=5)

        error = "Please enter a number"
        self.output_label = Label(self.temp_frame,
                                  text=error,
                                  font=("Arial", "10", "bold"),
                                  fg="#9C0000")

        self.output_label.grid(row=3)

        self.button_frame = Frame(self.temp_frame)
        self.button_frame.grid(row=4)

        self.temp_celsius = Button(self.button_frame,
                                   text="In Celsius",
                                   width=13,
                                   font=button_font,
                                   fg=button_fg,
                                   bg="#004C99",
                                   command=lambda: self.temp_convert(-459))

        self.temp_celsius.grid(row=0, column=0, padx=5, pady=5)

        self.temp_fahrenheit = Button(self.button_frame,
                                      text="In Fahrenheit",
                                      width=13,
                                      font=button_font,
                                      fg=button_fg,
                                      bg="#d1001f",
                                      command=lambda: self.temp_convert(-273))

        self.temp_fahrenheit.grid(row=0, column=1, padx=5, pady=5)

        self.to_helpinfo = Button(self.button_frame,
                                  text="help",
                                  width=13,
                                  font=button_font,
                                  fg=button_fg,
                                  bg="#DAA520",
                                  command=self.to_help)

        self.to_helpinfo.grid(row=1, column=0, padx=5, pady=5)

        # history_port = history + export
        self.to_history_port = Button(self.button_frame,
                                      text="History/Export",
                                      width=13,
                                      font=button_font,
                                      fg=button_fg,
                                      bg="#009900",
                                      state=DISABLED,
                                      command=self.to_history)

        self.to_history_port.grid(row=1, column=1, padx=5, pady=5)

    # cehcks user input, and converts if valid
    def input_temp(self, min_temp):
        error = f"Please enter a number that is more than {min_temp}"
        has_error = ""

        temperature = self.temp_entry.get()

        try:
            temperature = float(temperature)

            if temperature < min_temp:
                has_error = "yes"

        # checks input is a integer
        except ValueError:
            has_error = "yes"

        if has_error == "yes":
            self.var_has_error.set("yes")
            self.var_feedback.set(error)
            return "invalid"

        else:
            self.var_has_error.set("no")

            # when there is at least 1 valid calculation, display error message.
            # enables the history/export button
            self.to_history_port.config(state=NORMAL)
            return temperature

    @staticmethod
    def round_ans(val):
        var_rounded = (val * 2 + 1) // 2
        return "{:.0f}".format(var_rounded)

    def temp_convert(self, min_val):

        to_convert = self.input_temp(min_val)
        deg_sign = u'\N{DEGREE SIGN}'
        set_feedback = "yes"
        temp_converted = ""
        from_to = ""

        if to_convert == "invalid":
            set_feedback = "no"

        elif min_val == -459:
            temp_converted = (to_convert - 32) * 5 / 9
            from_to = "{} F{} is {} C{}"
        else:
            temp_converted = to_convert * 1.8 + 32
            from_to = "{} C{} is {} F{}"

        if set_feedback == "yes":
            to_convert = self.round_ans(to_convert)
            temp_converted = self.round_ans(temp_converted)

            feedback = from_to.format(to_convert, deg_sign,
                                      temp_converted, deg_sign)

            self.var_feedback.set(feedback)

            self.all_calculations.append(feedback)

            print(self.all_calculations)

        self.output_answer()

    def output_answer(self):

        output = self.var_feedback.get()
        has_errors = self.var_has_error.get()

        # Checks response is not too low
        if has_errors == "yes":
            self.output_label.config(fg="#FF0024")
            self.temp_entry.config(bg="#FFB3B2")

        else:
            self.output_label.config(fg="green")
            self.temp_entry.config(bg="#D3D3D3")

        self.output_label.config(text=output)

    def to_help(self):
        Display_help(self)

    def to_history(self):
        Display_history(self)


class Display_help:

    def __init__(self, partner):
        backdrop = "#ffe6cc"
        label_font = ("Arial", "10")

        partner.to_helpinfo.config(state=DISABLED)

        self.help_box = Toplevel()

        self.help_box.protocol('WM_DELETE_WINDOW',
                               partial(self.close_help, partner))

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
                                     text=help_text, wrap=300,
                                     bg=backdrop)
        self.help_text_label.grid(padx=5, pady=5)

        self.exit_help = Button(self.help_frame,
                                font=("Arial", "12", "bold"),
                                text="Close",
                                width=13,
                                bg="#DAA520",
                                command=lambda: self.close_help(partner))

        self.exit_help.grid(row=3, pady=10, padx=10)

    def close_help(self, partner):
        # put button back to normal
        partner.to_helpinfo.config(state=NORMAL)
        self.help_box.destroy()


class Display_history:

    def __init__(self, partner):
        label_font = ("Arial", "10")
        backdrop = "#FFFFFF"

        # sets up history box and disables the history button
        self.history_box = Toplevel()

        partner.to_history_port.config(state=DISABLED)

        self.history_box.protocol('WM_DELETE_WINDOW',
                                  partial(self.close_history, partner))

        # setting up the history frame
        self.history_frame = Frame(self.history_box, width=10,
                                   height=200, bg=backdrop)
        self.history_frame.grid(padx=5, pady=5)

        # --------------- #
        # HEADINGS / TEXT #
        # --------------- #
        self.history_heading = Label(self.history_frame, text="History/Export",
                                     font=("Arial", "18", "bold"), width=15, justify="left"
                                     )
        self.history_heading.grid(row=0, column=0, padx=5, pady=5)

        self.history_text1 = Label(self.history_frame, wrap=300,
                                   font=label_font, width=35, justify="left",
                                   text="Below are your recent calculations - "
                                        "showing {}/{} calculations. All calculations "
                                        "are shown to the nearest degree"
                                   )
        self.history_text1.grid(row=1, column=0, padx=5, pady=5)

        self.history_text2 = Label(self.history_frame, wrap=300,
                                   font=label_font, width=35, justify="left",
                                   text="Either create a custom filename in the box below "
                                        "(then push <export>),or push <export> without "
                                        "creating a custom name to save your calculations in a text file "
                                   )
        self.history_text2.grid(row=3, column=0, padx=5, pady=5)

        error = "filename error goes here"
        self.output_label = Label(self.history_frame,
                                  text=error,
                                  font=("Arial", "10", "bold"),
                                  fg="#9C0000")

        # --------------- #
        # FILE NAME STUFF #
        # --------------- #
        self.file_name = Entry(self.history_frame, font=("Arial", "14"),
                               bg="#D3D3D3")
        self.file_name.grid(row=4, padx=5, pady=5)

        # ------- #
        # BUTTONS #
        # ------- #
        self.button_frame = Frame(self.history_frame)
        self.button_frame.grid(row=6)

        self.export = Button(self.button_frame,
                             font=("Arial", "10", "bold"),
                             text="Export",
                             width=13,
                             bg="#DAA520",
                             )
        self.export.grid(row=0, column=0, pady=10, padx=10)

        self.exit_history = Button(self.button_frame,
                                   font=("Arial", "10", "bold"),
                                   text="Dismiss",
                                   width=13,
                                   bg="#DAA520",
                                   command=partial(self.close_history, partner))

        self.exit_history.grid(row=0, column=1, pady=10, padx=10)

    def close_history(self, partner):
        # put button back to normal
        partner.to_history_port.config(state=NORMAL)
        self.history_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("temperature converter")
    Converter()
    root.mainloop()
