from datetime import date
import re


# if filename is blank, returns default name
# otherwise checks filename and either returns
# an error or returns the filename


def get_date():
    today = date.today()

    day = today.strftime("%d")
    month = today.strftime("%m")
    year = today.strftime("%y")

    return f"{year}_{month}_{day}"


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


def filename_maker(filename):
    # default name here
    # ([TIME_FORMAT]_temperature_calculations
    if filename == "":
        filename_ok = ""
        formatted_time = get_date()
        filename = f"{formatted_time}_temperature_calculations"

    else:
        filename_ok = check_filename(filename)

    if filename_ok == "":
        filename += ".txt"

    else:
        filename = filename_ok

    return filename


# main routine
test_filenames = ["", "Test.txt", "Test it", "test"]

for item in test_filenames:
    checked = filename_maker(item)
    print(checked)
