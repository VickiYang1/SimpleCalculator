# Simple Calculator

This Python-based calculator application allows users to perform basic arithmetic operations such as addition, subtraction, multiplication, division, and more. The graphical user interface (GUI) is built using Tkinter, providing an intuitive experience.

## Features

- **Basic Operations**: Supports addition, subtraction, multiplication, division, and exponentiation.
- **Additional Functions**: Includes buttons for calculating squares, cubes, square roots, and negating values.
- **Clear and Quit**: Clear the current input or quit the application easily.

## Project Structure

### Colors and Fonts

The application is styled with a consistent color scheme, and fonts are defined for buttons and the display to make the interface visually appealing.

### Functions

1. **submit_number(number)**:
   - Adds a number or a decimal point to the display.
   - Disables the decimal button if it has already been used in the current input.

2. **operate(operator)**:
   - Stores the first number entered and the operation selected.
   - Disables all operation buttons until the calculation is completed.

3. **equal()**:
   - Performs the stored operation between the first number and the current input.
   - Handles division by zero by displaying an error message.

4. **enable_buttons()**:
   - Re-enables all operation buttons and the decimal button after a calculation.

5. **clear()**:
   - Clears the display and re-enables all buttons.

6. **square_root()**:
   - Calculates the square root of the current input and updates the display.

7. **cubed()**:
   - Calculates the cube of the current input and updates the display.

8. **square()**:
   - Calculates the square of the current input and updates the display.

9. **negate()**:
   - Negates the current input and updates the display.

### GUI Layout

- **Display Frame**: Contains the input and output field where calculations are displayed.
- **Button Frame**: Contains all the buttons for numbers, operations, and functions.

### Button Configuration

Buttons are laid out in a grid within the button frame. They are organized logically into rows for ease of use. The grid layout ensures that all buttons align properly, with specific padding to create consistent sizing.

## How to Use

1. Enter the numbers using the numerical buttons.
2. Select an operation (+, -, *, /) or a function (e.g., square root).
3. Press the "=" button to get the result.
4. Use the "CE" button to clear the display or the "Quit" button to close the application.
