'''
This file contains the template for Assignment1. For testing it, I will place
it
in a different directory, call the function <min_attendance_for_long_weekend>,
and check its output.
So, you can add/remove whatever you want to/from this file. But, don't change
the name
of the file or the name/signature of the following function.
Also, I will use <python3> to run this code.
'''

def min_attendance(clubs, n, sum1, sum2, total_sum, array, memo):

    if (memo[n][sum1][sum2] != -1):
        return

    if n == 0:
        max_val = (max(sum1, sum2, total_sum - sum1 - sum2))
        array.append(max_val)
        memo[n][sum1][sum2] = max_val
        return
    
    min_attendance(clubs, n-1, sum1, sum2, total_sum, array, memo)

    min_attendance(clubs, n-1, sum1 + clubs[n-1], sum2, total_sum, array, memo)

    min_attendance(clubs, n-1, sum1, sum2 + clubs[n-1], total_sum, array, memo)

    memo[n][sum1][sum2] = 1

def min_attendance_for_long_weekend(input_file_path, output_file_path):
    with open(input_file_path, 'r') as input_file:
        line = input_file.readline().split(",")
        clubs = [int(num) for num in line]

    n = len(clubs)
    total_sum = sum(clubs)

    array = []
    memo = [[[-1 for _ in range(total_sum + 1)] for _ in range(total_sum + 1)] for _ in range(n + 1)]

    min_attendance(clubs, n, 0, 0, total_sum, array, memo)

    answer = min(array)

    print(answer)

    with open(output_file_path, 'w') as output_file:
        output_file.write(str(answer))
'''
This function will contain your code. It wil read from the file
<input_file_path>,
and will write its output to the file <output_file_path>.
'''
pass
'''
To test your function, you can uncomment the following command with the the
input/output
files paths that you want to read from/write to. Do NOT forget to comment it
out before
submitting.
'''

min_attendance_for_long_weekend('sample_tests_ga2/tests/input6.txt', 'output')


