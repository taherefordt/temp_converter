from tkinter import *


class Converter:

    def __init__(self):

        button_font = ("Arial", "14", "bold")


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
                                font=("Arial", "14", "bold"),
                                fg="#9C0000")

        self.temp_error.grid(row=3)

        self.button_frame = Frame(self.temp_frame)
        self.button_frame.grid(row=4)

        self.temp_centigrade = Button(self.button_frame,
                                      text="To Degrees C",
                                      width=20,
                                      font=button_font,
                                      bg="#004C99",
                                      fg="#FFFFFF")
        self.temp_centigrade.grid(row=0, column=0)

        self.temp_fahrenheit = Button(self.button_frame,
                                      text="To Degrees Fahrenheit",
                                      width=20,
                                      font=button_font,
                                      bg="#d1001f",
                                      fg="#FFFFFF")
        self.temp_fahrenheit.grid(row=0, column=1)

        # helpfo = help + info
        self.temp_helpfo = Button(self.button_frame,
                                  text="Help/info",
                                  width=20,
                                  font=button_font,
                                  bg="#009900",
                                  fg="#FFFFFF")
        self.temp_helpfo.grid(row=1, column=0)

        # histport = history + export
        self.temp_histport = Button(self.button_frame,
                                    text="History/Export",
                                    width=20,
                                    font=button_font,
                                    bg="#e6cc00",
                                    fg="#FFFFFF",
                                    state=DISABLED)

        self.temp_histport.grid(row=1, column=1)

# main routine


if __name__ == "__main__":
    root = Tk()
    root.title("temperature converter")
    Converter()
    root.mainloop()
