if __name__ == "__main__":
    dict = {}

    dict[4 + 4 + 4 + 4] = '4 + 4 + 4 + 4'
    dict[4 + 4 + 4 - 4] = '4 + 4 + 4 - 4'
    dict[4 + 4 + 4 * 4] = '4 + 4 + 4 * 4'
    dict[4 + 4 + 4 // 4] = '4 + 4 + 4 / 4'
    
    dict[4 + 4 - 4 + 4] = '4 + 4 - 4 + 4'
    dict[4 + 4 - 4 - 4] = '4 + 4 - 4 - 4'
    dict[4 + 4 - 4 * 4] = '4 + 4 - 4 * 4'
    dict[4 + 4 - 4 // 4] = '4 + 4 - 4 / 4'
    
    dict[4 + 4 * 4 + 4] = '4 + 4 * 4 + 4'
    dict[4 + 4 * 4 - 4] = '4 + 4 * 4 - 4'
    dict[4 + 4 * 4 * 4] = '4 + 4 * 4 * 4'
    dict[4 + 4 * 4 // 4] = '4 + 4 * 4 / 4'
    
    dict[4 + 4 // 4 + 4] = '4 + 4 / 4 + 4'
    dict[4 + 4 // 4 - 4] = '4 + 4 / 4 - 4'
    dict[4 + 4 // 4 * 4] = '4 + 4 / 4 * 4'
    dict[4 + 4 // 4 // 4] = '4 + 4 / 4 / 4'
    
    dict[4 - 4 + 4 + 4] = '4 - 4 + 4 + 4'
    dict[4 - 4 + 4 - 4] = '4 - 4 + 4 - 4'
    dict[4 - 4 + 4 * 4] = '4 - 4 + 4 * 4'
    dict[4 - 4 + 4 // 4] = '4 - 4 + 4 / 4'
    
    dict[4 - 4 - 4 + 4] = '4 - 4 - 4 + 4'
    dict[4 - 4 - 4 - 4] = '4 - 4 - 4 - 4'
    dict[4 - 4 - 4 * 4] = '4 - 4 - 4 * 4'
    dict[4 - 4 - 4 // 4] = '4 - 4 - 4 / 4'
    
    dict[4 - 4 * 4 + 4] = '4 - 4 * 4 + 4'
    dict[4 - 4 * 4 - 4] = '4 - 4 * 4 - 4'
    dict[4 - 4 * 4 * 4] = '4 - 4 * 4 * 4'
    dict[4 - 4 * 4 // 4] = '4 - 4 * 4 / 4'
    
    dict[4 - 4 // 4 + 4] = '4 - 4 / 4 + 4'
    dict[4 - 4 // 4 - 4] = '4 - 4 / 4 - 4'
    dict[4 - 4 // 4 * 4] = '4 - 4 / 4 * 4'
    dict[4 - 4 // 4 // 4] = '4 - 4 / 4 / 4'
    
    dict[4 * 4 + 4 + 4] = '4 * 4 + 4 + 4'
    dict[4 * 4 + 4 - 4] = '4 * 4 + 4 - 4'
    dict[4 * 4 + 4 * 4] = '4 * 4 + 4 * 4'
    dict[4 * 4 + 4 // 4] = '4 * 4 + 4 / 4'
    
    dict[4 * 4 - 4 + 4] = '4 * 4 - 4 + 4'
    dict[4 * 4 - 4 - 4] = '4 * 4 - 4 - 4'
    dict[4 * 4 - 4 * 4] = '4 * 4 - 4 * 4'
    dict[4 * 4 - 4 // 4] = '4 * 4 - 4 / 4'
    
    dict[4 * 4 * 4 + 4] = '4 * 4 * 4 + 4'
    dict[4 * 4 * 4 - 4] = '4 * 4 * 4 - 4'
    dict[4 * 4 * 4 * 4] = '4 * 4 * 4 * 4'
    dict[4 * 4 * 4 // 4] = '4 * 4 * 4 / 4'
    
    dict[4 * 4 // 4 + 4] = '4 * 4 / 4 + 4'
    dict[4 * 4 // 4 - 4] = '4 * 4 / 4 - 4'
    dict[4 * 4 // 4 * 4] = '4 * 4 / 4 * 4'
    dict[4 * 4 // 4 // 4] = '4 * 4 / 4 / 4'
    
    dict[4 // 4 + 4 + 4] = '4 / 4 + 4 + 4'
    dict[4 // 4 + 4 - 4] = '4 / 4 + 4 - 4'
    dict[4 // 4 + 4 * 4] = '4 / 4 + 4 * 4'
    dict[4 // 4 + 4 // 4] = '4 / 4 + 4 / 4'
    
    dict[4 // 4 - 4 + 4] = '4 / 4 - 4 + 4'
    dict[4 // 4 - 4 - 4] = '4 / 4 - 4 - 4'
    dict[4 // 4 - 4 * 4] = '4 / 4 - 4 * 4'
    dict[4 // 4 - 4 // 4] = '4 / 4 - 4 / 4'
    
    dict[4 // 4 * 4 + 4] = '4 / 4 * 4 + 4'
    dict[4 // 4 * 4 - 4] = '4 / 4 * 4 - 4'
    dict[4 // 4 * 4 * 4] = '4 / 4 * 4 * 4'
    dict[4 // 4 * 4 // 4] = '4 / 4 * 4 / 4'
    
    dict[4 // 4 // 4 + 4] = '4 / 4 / 4 + 4'
    dict[4 // 4 // 4 - 4] = '4 / 4 / 4 - 4'
    dict[4 // 4 // 4 * 4] = '4 / 4 / 4 * 4'
    dict[4 // 4 // 4 // 4] = '4 / 4 / 4 / 4'
    
    n = int(input())
    for i in range(n):
        num = int(input())
        if num in dict.keys():
            print(dict[num] + " = " + str(num))
        else:
            print("no solution")
    