def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")

def calc_average(num_list):
    print("calc_average")
    sum = 0
    length = len(num_list)
    for num in range (0,length):
        sum = sum + num_list[num]

    average = sum/length
    return average

def get_user_input():
    print("get_user_input")
    x = input()
    Listofstr = x.split(",")
    float_list = list(map(float,Listofstr))
    return float_list

def find_min_max(num_list):
    print("find_min_max")
    min_temp = min(num_list)
    max_temp = max(num_list)
    min_max_list = [min_temp,max_temp]
    return min_max_list

def sort_temperature(num_list):
    print("sort_temperature")
    num_list.sort()
    return num_list
def calc_median_temperature(ascending_list):
    print("calc_median_temperature")
    if len(ascending_list)%2!=0:
        median = ascending_list[int(((len(ascending_list)+1)/2)-1)]
    else:
        median = (ascending_list[int((len(ascending_list)/2) + 1/2)] + ascending_list[int((len(ascending_list)/2) - 1/2)])/2

    return median
def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()
    ascending_list = sort_temperature(num_list)
    print(calc_average(num_list))
    print(find_min_max(num_list))
    print(calc_median_temperature(ascending_list))
    print(sort_temperature(num_list))

    
if __name__ == "__main__":
    main()
