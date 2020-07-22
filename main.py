from tkinter import Tk, Label, Entry, Button, Radiobutton, IntVar, END

from formulas import male_bmr, female_bmr, male_calories, female_calories


def calculate():
    """Get user inputs then calculate and display BMR and calorie data."""

    # Get all input data from the GUI
    age = float(age_input.get())
    weight = float(weight_input.get())
    height = float(height_input.get())
    heartrate = float(heartrate_input.get())
    duration = float(duration_input.get())

    if gender.get() == 0:
        # Calculate data for males
        bmr = male_bmr(weight, height, age)
        gross_calories = male_calories(heartrate, weight, age, duration)
    else:
        # Calculate data for females
        bmr = female_bmr(weight, height, age)
        gross_calories = female_calories(heartrate, weight, age, duration)

    net_calories = gross_calories - (bmr / 1440 * duration)

    # Display calculated data
    bmr_output.config(text=int(bmr))
    gross_output.config(text=int(gross_calories))
    net_output.config(text=int(net_calories))


def clear():
    # Clear input fields
    bmr_output.config(text="")
    gross_output.config(text="")
    net_output.config(text="")

    # Clear output text
    age_input.delete(0, END)
    weight_input.delete(0, END)
    height_input.delete(0, END)
    heartrate_input.delete(0, END)
    duration_input.delete(0, END)


root = Tk()
root.title("Exercise Calorie Calculator")
gender = IntVar()

# Gender radio buttons
r1 = Radiobutton(root, text="Male", variable=gender, value=0)
r1.grid(row=10, column=0, pady=[10, 0])

r2 = Radiobutton(root, text="Female", variable=gender, value=1)
r2.grid(row=10, column=1, pady=[10, 0])

# Data inputs and labels
age_label = Label(root, text="Age")
age_label.grid(row=0, column=0, pady=[10, 0], columnspan=2)
age_input = Entry(root, width=10)
age_input.grid(row=1, column=0, columnspan=2)

weight_label = Label(root, text="Weight (lb)")
weight_label.grid(row=2, column=0, pady=[10, 0], columnspan=2)
weight_input = Entry(root, width=10)
weight_input.grid(row=3, column=0, columnspan=2)

height_label = Label(root, text="Height (in)")
height_label.grid(row=4, column=0, pady=[10, 0], columnspan=2)
height_input = Entry(root, width=10)
height_input.grid(row=5, column=0, columnspan=2)

duration_label = Label(root, text="Minutes")
duration_label.grid(row=6, column=0, pady=[10, 0], columnspan=2)
duration_input = Entry(root, width=10)
duration_input.grid(row=7, column=0, columnspan=2)

heartrate_label = Label(root, text="Heartrate")
heartrate_label.grid(row=8, column=0, pady=[10, 0], columnspan=2)
heartrate_input = Entry(root, width=10)
heartrate_input.grid(row=9, column=0, columnspan=2)

# Labels for text output
bmr_label = Label(root, text="BMR", font="bold")
bmr_label.grid(row=1, column=2, padx=30)
bmr_output = Label(root)
bmr_output.grid(row=2, column=2)

gross_label = Label(root, text="Gross Calories", font="bold", padx=25)
gross_label.grid(row=4, column=2)
gross_output = Label(root)
gross_output.grid(row=5, column=2)

net_label = Label(root, text="Net Calories", font="bold")
net_label.grid(row=7, column=2)
net_output = Label(root)
net_output.grid(row=8, column=2)

# Create the calculate button
calculate_button = Button(root, width=15, text="Calculate", command=calculate)
calculate_button.grid(row=11, column=0, pady=[20, 0], padx=20, columnspan=2)

# Create the clear button
clear_button = Button(root, width=15, text="Clear", command=clear)
clear_button.grid(row=11, column=2, pady=[20, 0])

# Create the exit button
exit_button = Button(root, width=20, text="Exit", command=root.quit)
exit_button.grid(row=12, column=0, pady=[20, 10], columnspan=3)

root.mainloop()
