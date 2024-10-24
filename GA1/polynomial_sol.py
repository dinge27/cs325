def viable(max, clubs, days):
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

def calculate_min(clubs, days):
    n = len(clubs) 

    if (days >= n):
        return max(clubs)
    
    curr_sum = 0
    curr_min = sum(clubs)

    for i in range(n):
        curr_sum = clubs[i]

        j = i + 1
        for j in range(i+1, n):
            curr_sum += clubs[j]

            if (curr_sum > curr_min):
                break

            if feasible(curr_sum, clubs, days):
                curr_min = curr_sum

            j += 1
    
    return curr_min


def min_num_attendees(input_file_path, output_file_path):
    with open(input_file_path, 'r') as input_file:
        days = int(input_file.readline().strip())
        line = input_file.readline().split(",")
        clubs = [int(num) for num in line]

    ans = calculate_min(clubs, days)
    print(ans)

    with open(output_file_path, 'w') as output_file:
        output_file.write(str(ans))

min_num_attendees('test_cases\input3.txt', 'output')
