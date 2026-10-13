from PyQt5 import uic

# Path to the .ui file
ui_file = "SecondHandCar.ui"
# Path for the generated .py file
py_file = "SecondHandCar.py"

# Convert the .ui file to a .py file
with open(py_file, "w", encoding="utf-8") as fout:
    uic.compileUi(ui_file, fout)