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
            self.temp_entry.config(bg="#FFFFFF")

        self.output_label.config(text=output)


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("temperature converter")
    Converter()
    root.mainloop()
