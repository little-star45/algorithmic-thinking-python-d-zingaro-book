import inspect

#=== make debugger from print
original_print = print #save original print function

def debug_print(*args, **kwargs):
    #[0] - function which is currently running; [1] - function which run function [0]
    caller = inspect.stack()[1].function # get the function name which was removed from stack
    original_print(f"[{caller}] →", *args, **kwargs)

print = debug_print #replace original print

#===

#we search two identical integers in one list of values
def identify_identical_1_1(values: list[int], n: int) -> None:
    for i in range(n):
        for j in range(i+1,n):
            if values[i] == values[j]:
                print("Twin integers found.\n")
                return None
    print("No two integers are alike.\n")
    return None

def identical_right(snow1: list[int], snow2: list[int], start:int) -> int:
    #len(snow1) = 6
    i = 0
    j = start
    while i<6:
        if j == 6:
            j = 0
        if snow1[i] != snow2[j]:
            return 0
        else:
            i+=1
            j+=1
    return 1

def identical_right_1_2(snow1: list[int], snow2: list[int], start:int) -> int:
    for offset in range(6):
        if snow1[offset] != snow2[start + offset]:
            return 0
    return 1

def identical_right_1_3(snow1: list[int], snow2: list[int], start:int) -> int:

    for offset in range(6):
        snow2_index = start + offset
        if snow2_index >=6:
            snow2_index = snow2_index - 6
        if snow1[offset] != snow2[snow2_index]:
            return 0
    return 1

def identical_right_1_4(snow1: list[int], snow2: list[int], start:int) -> int:
    for offset in range(6):
        if snow1[offset] != snow2[(start + offset)%6]:
            return 0
    return 1

def identical_left(snow1: list[int], snow2: list[int], start:int) -> int:
    #len(snow1) = 6
    i = 6-1
    j = start
    while i>=0:
        if j == -1:
            j = 6-1
        print(i,j)
        if snow1[i] != snow2[j]:
            return 0
        else:
            i-=1
            j-=1
    return 1

def identical_left_1_5(snow1: list[int], snow2: list[int], start:int) -> int:
    for offset in range(6):
        snow2_index = start - offset
        if snow2_index <0:
            snow2_index = snow2_index + 6
        if snow1[offset] != snow2[snow2_index]:
            return 0
    return 1

def are_identical_1_6(snow1: list[int], snow2: list[int]) -> int:
    #snow1=[3, 4, 5, 6, 1, 2] snow2=[1, 2, 3, 4, 5, 6]

    for start in range(6):
        if identical_right_1_4(snow1,snow2,start)==1:
            print("Identical right - correct snowflake pair.")
            return 1
        if identical_left_1_5(snow1,snow2,start)==1:
            print("Identical left - correct snowflake pair.")
            return 1
    print("No correct snowflake pair.")
    return 0

def identify_identical_1_7(snowflakes: list[list[int]], n: int) -> None:
    for i in range(n):
        for j in range(n+1):
            if (are_identical_1_6(snowflakes[i], snowflakes[j])==1):
                print("Twin snowflakes found. \n")
                return
    print("No two snowflakes are like.\n")

def compare_1_9(first, second):
    snowflake1 = first
    snowflake2 = second
    if are_identical_1_6(snowflake1, snowflake2):
        return 0
    for i in range(6):
        if snowflake1[i]<snowflake2[i]:
            return -1
    return 1

def main() -> None:
    # values = (1,2,3,1,5)
    # n = 5
    # identify_identical_1_1(values, n)
    # print(identical_left_1_5([3,1,5,1,2,6], [1,2,6,3,1,5], 2))

    #4
    #[[3,4,5,6,1,2],[2,3,4,5,6,7],[4,5,6,7,8,9],[1,2,3,4,5,6]]
    # N = map(int, input().split())
    # snowflakes = [list(map(int, input().split())) for _ in range(N)]

    N = 4
    snowflakes = [[3,4,5,6,1,2],[2,3,4,5,6,7],[4,5,6,7,8,9],[1,2,3,4,5,6]]

    # identify_identical_1_7(snowflakes, N)
    print(compare_1_9(snowflakes[0], snowflakes[1]))
    return 0


if __name__ == "__main__":
    main()