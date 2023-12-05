input = open("AOC1_input.txt", 'r')
l = input.readlines()

nums = {'1','2','3','4','5','6','7','8','9','0', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'}
dict = {'zero' : 0, 'one' : 1, 'two' : 2, 'three': 3, 'four' : 4, 'five' : 5, 'six' : 6, 'seven' : 7, 'eight' : 8, 'nine' : 9}

ans = 0
d1 = None
d2= None
total = 0
for str in l:
    i=0
    while i < len(str):
        if str[i] in nums:
            d1 = int(str[i])
            break

        if i+3 < len(str) and str[i:i+3] in nums:
            d1 = dict[str[i:i+3]]
            i = i+3
            break


        elif i+4< len(str) and str[i:i+4] in nums:
            d1 = dict[str[i:i+4]]
            i = i+4
            break


        elif i+5<len(str) and str[i:i+5] in nums:
            d1 = dict[str[i:i+5]]
            i = i+5
            break
            
        i += 1
    j = len(str) - 1
    while j >= 0:
        if str[j] in nums:
            d2 = int(str[j])
            break
        if j-2 > -1 and str[j-2:j+1] in nums:
            d2 = dict[str[j-2:j+1]]
            break

        elif j-3>-1  and str[j-3:j+1] in nums:
            d2 = dict[str[j-3:j+1]]
            break

        elif j-4>-1 and str[j-4:j+1] in nums:
            d2 = dict[str[j-4:j+1]]
            break
        j -= 1
    ans += (d1 * 10) + d2

print(ans)

