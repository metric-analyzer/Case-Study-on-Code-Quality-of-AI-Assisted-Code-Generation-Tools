@echo off
setlocal enabledelayedexpansion

REM Create a directory for the output files (if it doesn't exist)
mkdir output_files 2>nul

REM Set the range of index numbers (0 to 125)
for /l %%i in (0, 1, 125) do (
    set index=%%i
    set file=generated_code_!index!.py
    set output=output_files\output_!index!.txt

    REM Run Radon commands for each file and save output to a text file
    echo Calculating Cyclomatic Complexity for !file!
    radon cc !file! -a > !output!

    echo Calculating Maintainability Index for !file!
    radon mi !file! -s >> !output!

    echo Calculating Raw Metrics for !file!
    radon raw !file! >> !output!

    echo Calculating Halstead Metrics for !file!
    radon hal !file! >> !output!
)

REM Pause to keep the console window open
pause
