@echo off
setlocal enabledelayedexpansion

rem Create a test_output folder if it doesn't exist
mkdir test_output

rem Loop through the index numbers from 0 to 125
for /l %%i in (0,1,125) do (
    rem Define the Python file name
    set "python_file=generated_code_%%i.py"

    rem Define the output file name
    set "output_file=test_output\output_%%i.txt"

    rem Run the Python file and capture the output
    python "!python_file!" > "!output_file!" 2>&1

    rem Check if the Python file executed successfully
    if !errorlevel! equ 0 (
        echo Test passed > "!output_file!"
    ) else (
        echo Test failed > "!output_file!"
    )
)

endlocal
