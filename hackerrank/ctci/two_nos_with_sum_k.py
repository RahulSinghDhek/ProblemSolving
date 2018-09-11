
def find_numbers(array,sum):
    for number in array:
        compliment = sum - number
        if compliment in array:
            return (array.index(number)+1,array.index(compliment)+1

def main():
    no_of_test_cases = int(raw_input())
    for test in range(no_of_test_cases):
        sum =  int(raw_input())
        array = map(int,raw_input().rstrip().split())
        print find_numbers(array,sum)

if __name__ == '__main__':
    main()
