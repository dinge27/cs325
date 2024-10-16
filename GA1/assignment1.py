'''
This file contains the template for Assignment1. For testing it, I will place
it
in a different directory, call the function <min_num_attendees>, and check its
output.
So, you can add/remove whatever you want to/from this file. But, don't change
the name
of the file or the name/signature of the following function.
Also, I will use <python3> to run this code.
'''
def feasible(max, clubs, days):
    members = 0
    days_used = 1 

    for club in clubs:
        if members + club <= max:
            members += club
        else:
            days_used += 1
            members = club

            if days_used > days:
                return False
    
    return True

def min_num_attendees(input_file_path, output_file_path):
    with open(input_file_path, 'r') as input_file:
        days = int(input_file.readline().strip())
        line = input_file.readline().split(",")
        clubs = [int(num) for num in line]

    left = max(clubs) 
    right = sum(clubs)
    
    while left < right:
        mid = (left + right) // 2 

        if feasible(mid, clubs, days):
            right = mid
        else:
            left = mid + 1 


    with open(output_file_path, 'w') as output_file:
        output_file.write(str(left))

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
#min_num_attendees('test_cases\input6.txt', 'output')
