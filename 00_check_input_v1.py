def input_temp(min_temp):
    while True:
        try:

            temperature = float(input(f"Please choose a number that is higher than {min_temp}: "))

            # Checks response is not too low
            if temperature < min_temp:
                print(f"temperature must be above {min_temp}")

            else:
                return temperature

            continue

        # checks input is a integer
        except ValueError:
            print("please enter a number")


while True:
    temp = input_temp(-273.15)
    print(temp)

