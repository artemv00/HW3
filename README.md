![workflow](https://github.com/artemv00/hw3/actions/workflows/my-program-test.yml/badge.svg)
# Technical Task 3
## How does it work?
This program opens **numbers.txt** (you may change the file in code), then it readы all numbers in the file and returns:
1. minimal number
2. maxumal numberm
3. sum of numbers
4. product of numbers

If the file contains something other than numbers, the program will return nothing.
# Tests
## The correctness tests
The correctness tests of the sum, product, minimum and maximum numbers are contained in the **test_main.py**.
Also, **test_numbers_info.py** contains an additional test that checks that this program does not return any failure if the file contains some no-numeric strings.
## Script execution time test
**test_measure_time.py**
