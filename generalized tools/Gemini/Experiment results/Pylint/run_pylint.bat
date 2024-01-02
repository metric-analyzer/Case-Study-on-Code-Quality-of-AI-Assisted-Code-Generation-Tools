@echo off
setlocal enabledelayedexpansion

rem Create a pylint_output folder if it doesn't exist
mkdir pylint_output

rem Loop through the index numbers from 0 to 125
for /l %%i in (0,1,125) do (
    rem Define the Python file name
    set "python_file=C:\Users\pc\Documents\Case-Study-on-Code-Quality-of-AI-Assisted-Code-Generation-Tools\generalized tools\Gemini\Generated Codes\generated_code_%%i.py"

    rem Define the output file name
    set "output_file=pylint_output\output_%%i.txt"

    rem Run pylint on the Python file and save the output
    pylint "!python_file!" > "!output_file!" 2>&1
)

endlocal
