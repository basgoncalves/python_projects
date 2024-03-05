import tkinter as tk
import sys

def print_values():
    # Get the values from the input text boxes, drop-down menu, and checkboxes
    value1 = entry1.get()
    value2 = entry2.get()
    selected_option = dropdown.get()
    checkbox1_value = checkbox1_var.get()
    checkbox2_value = checkbox2_var.get()
    checkbox3_value = checkbox3_var.get()
    checkbox4_value = checkbox4_var.get()

    # Print the values in the terminal
    print("Value 1:", value1)
    print("Value 2:", value2)
    print("Selected Option:", selected_option)
    print("Checkbox 1:", checkbox1_value)
    print("Checkbox 2:", checkbox2_value)
    print("Checkbox 3:", checkbox3_value)
    print("Checkbox 4:", checkbox4_value)

def get_window_center(window):
    # Get the requested width and height of the window
    req_width = window.winfo_reqwidth()
    req_height = window.winfo_reqheight()

    # Get the screen size
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # Calculate the center position
    center_x = (screen_width - req_width) // 2
    center_y = (screen_height - req_height) // 2

    return center_x, center_y

# Create the main window
window = tk.Tk()
window.title("GUI Example")
myscreensize = window.winfo_screenwidth(), window.winfo_screenheight()
window_coordinates = int(myscreensize[0] // 4), int(myscreensize[1] // 4)
window.geometry(str(window_coordinates[0]) + 'x' + str(window_coordinates[1]))
window.eval('tk::PlaceWindow . center')

# Get the geometry string & parse the geometry string to extract coordinates
coordinates = get_window_center(window)
print("Coordinates:", coordinates)
print("Screen size:", myscreensize)
print("Window size:", window.winfo_geometry())
print('Window coordinates:', window_coordinates)

# Create the input text boxes
entry1 = tk.Entry(window)
entry1.pack()
entry2 = tk.Entry(window)
entry2.pack()

# Create the drop-down menu
dropdown = tk.StringVar(window)
dropdown.set("Choose option")
dropdown_menu = tk.OptionMenu(window, dropdown, "Option 1", "Option 2", "Option 3")
dropdown_menu.pack()

# Create the checkboxes
checkbox1_var = tk.IntVar()
checkbox1 = tk.Checkbutton(window, text="Checkbox 1", variable=checkbox1_var)
checkbox1.pack()
checkbox2_var = tk.IntVar()
checkbox2 = tk.Checkbutton(window, text="Checkbox 2", variable=checkbox2_var)
checkbox2.pack()
checkbox3_var = tk.IntVar()
checkbox3 = tk.Checkbutton(window, text="Checkbox 3", variable=checkbox3_var)
checkbox3.pack()
checkbox4_var = tk.IntVar()
checkbox4 = tk.Checkbutton(window, text="Checkbox 4", variable=checkbox4_var)
checkbox4.pack()

# Create the button
button = tk.Button(window, text="Print", command=print_values)
button.pack()

# Start the main loop
window.mainloop()