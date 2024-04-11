from functools import partial
from tkinter import *
from datetime import date
import re


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
                                      command=lambda: self.to_history_export(self.all_calculations))

        self.to_history_port.grid(row=1, column=1, padx=5, pady=5)

    # checks user input, and converts if valid
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

    def to_history_export(self, all_calculations):
        Display_history(self, all_calculations)


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

    def __init__(self, partner, calc_list):

        label_font = ("Arial", "10")
        backdrop = "#FFFFFF"

        max_calcs_shown = 5
        self.max_calcs = IntVar()
        self.max_calcs.set(max_calcs_shown)

        self.var_filename = StringVar()
        self.var_todays_date = StringVar()
        self.var_calc_list = StringVar()

        calcs_done = len(calc_list)
        self.calcs_done = IntVar()
        self.calcs_done.set(calcs_done)

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

        if calcs_done >= max_calcs_shown:
            calc_text = "Below are your recent calculations - " \
                        f"showing {max_calcs_shown}/{calcs_done} calculations. All calculations " \
                        "are shown to the nearest degree"
        else:
            calc_text = "Below are your recent calculations - " \
                        f"showing {calcs_done}/{calcs_done} calculations. All calculations " \
                        "are shown to the nearest degree"

        self.history_text1 = Label(self.history_frame, wrap=300,
                                   font=label_font, width=35, justify="left",
                                   text=calc_text
                                   )
        self.history_text1.grid(row=1, column=0, padx=10, pady=10)

        self.history_text2 = Label(self.history_frame, wrap=300,
                                   font=label_font, width=35, justify="left",
                                   text="Either create a custom filename in the box below "
                                        "(then push <export>),or push <export> without "
                                        "creating a custom name to save your calculations in a text file "
                                   )
        self.history_text2.grid(row=3, column=0, padx=5, pady=5)

        # ------------ #
        # CALCULATIONS #
        # ------------ #

        # separates the newest 5 calculations from the rest of the list
        new_calcs = calc_list[-5:]
        # reverses the order of items to show the recent calcs first
        new_calcs.reverse()
        # a string list of all calcs
        all_calculations = ""
        # a placeholder for the sting list of recent calcs
        recent_calculations = ""

        for item in calc_list:
            all_calculations += item + '\n'

        for item in new_calcs:
            recent_calculations += item + '\n'
        recent_calculations = recent_calculations[:-2]

        self.var_calc_list.set(all_calculations)

        self.history_past = Label(self.history_frame, width=25, bg="#FEE135",
                                  text=recent_calculations, wraplength=300, font=("Arial", "12", "bold"))

        self.history_past.grid(row=2)

        error = "filename error goes here"
        self.output_label = Label(self.history_frame,
                                  text=error,
                                  font=("Arial", "10", "bold"),
                                  fg="#9C0000",
                                  )

        # --------------- #
        # FILE NAME STUFF #
        # --------------- #
        self.file_name_entry = Entry(self.history_frame, font=("Arial", "14"),
                                     bg="#D3D3D3", width=23)
        self.file_name_entry.grid(row=4, padx=5, pady=5)

        self.filename_feedback_label = Label(self.history_frame, text="",
                                             font=("Arial", "10", "bold"),
                                             wrap=250
                                             )

        self.filename_feedback_label.grid(row=5)

        # ------- #
        # BUTTONS #
        # ------- #
        self.button_frame = Frame(self.history_frame)
        self.button_frame.grid(row=6)

        self.export = Button(self.button_frame,
                             font=("Arial", "12", "bold"),
                             text="Export",
                             width=13,
                             bg="#004C99",
                             fg="#FFFFFF",
                             command=self.make_file)
        self.export.grid(row=0, column=0, pady=10, padx=10)

        self.exit_history = Button(self.button_frame,
                                   font=("Arial", "12", "bold"),
                                   text="Dismiss",
                                   width=13,
                                   bg="red",
                                   fg="#FFFFFF",
                                   command=partial(self.close_history, partner))

        self.exit_history.grid(row=0, column=1, pady=10, padx=10)

    def make_file(self):

        filename = self.file_name_entry.get()

        filename_ok = ""
        date_part = self.get_date()

        if filename == "":

            date_part = self.get_date()
            filename = f"{date_part}_temperature_calculations"

        else:

            filename_ok = self.check_filename(filename)

        if filename_ok == "":
            filename += ".txt"
            success = "Success! Your calculation history" \
                      f"has been saved as {filename}"
            self.var_filename.set(filename)
            self.filename_feedback_label.config(text="You are OK",
                                                fg="#009900")
            self.file_name_entry.config(bg="#FFFFFF")

            self.write_to_file()

        else:
            self.filename_feedback_label.config(text=filename_ok,
                                                fg="#9C0000")
            self.file_name_entry.config(bg="#F8CECC")

    @staticmethod
    def check_filename(filename):
        problem = ""

        # expression to check the filename is valid
        valid_char = "[A-Za-z0-9_]"

        # checks each letter of the filename
        for character in filename:
            if re.match(valid_char, character):
                continue

            elif character == " ":
                problem = "sorry, no spaces allowed"

            else:
                problem = f"sorry, no {character}'s allowed"
            break

        if problem != "":
            problem = f"{problem}. Use letters / numbers / underscores only"

        return problem

    def write_to_file(self):

        # retrieve date, filename and calculation history...
        filename = self.var_filename.get()
        generated_date = self.var_todays_date.get()

        # set up strings to be written to file
        heading = "|>=+-- Temperature Calculations --+=<|\n"
        generated = "Generated: {}\n".format(generated_date)
        sub_heading = "Here is your calculation history " \
                      "(oldest to newest)...\n"

        all_calculations = self.var_calc_list.get()

        to_output_list = [heading, generated,
                          sub_heading, all_calculations]

        # write to file

        # write output to file
        text_file = open(filename, "w+")

        for item in to_output_list:
            text_file.write(item)
            text_file.write("\n")

        # close file
        text_file.close()

    def close_history(self, partner):
        # put button back to normal
        partner.to_history_port.config(state=NORMAL)
        self.history_box.destroy()

    def get_date(self):
        today = date.today()

        day = today.strftime("%d")
        month = today.strftime("%m")
        year = today.strftime("%y")

        date_today = f"{day}/{month}/{year}"
        self.var_todays_date.set(date_today)

        return f"{year}_{month}_{day}"


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("temperature converter")
    Converter()
    root.mainloop()
