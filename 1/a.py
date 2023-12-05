def main():
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    all_numbers = []
    input = open('input.txt', 'r')
    lines = input.readlines()
    for line in lines:
        ltr = 0;
        rtl = 0;
        for char in line:
            try:
                char = int(char)
                if char in numbers:
                    ltr = char
                    break
            except:
                continue
        for char in reversed(line):
            try:
                char = int(char)
                if char in numbers:
                    rtl = char
                    break
            except:
                continue
        if ltr is not None and rtl is not None:
            combined_num = int(str(ltr) + str(rtl))
            all_numbers.append(combined_num)
    
    total_sum = sum(all_numbers)
    print(total_sum)

if __name__ == "__main__":
    main()
 

