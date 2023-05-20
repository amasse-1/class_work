
def knapsack(f, max_vol):
    data_file = open(f, "r")
    items = []
    for l in data_file.readlines():         #reads lines
        l = l.split(',')                    #split at commas
        v = int(l[2]) * int(l[3]) * int(l[4])#volume is height*width*depth
        items.append([v, l[0], int(l[1]), int(l[2]), int(l[3]), int(l[4])])
    data_file.close()
    items.sort(reverse=True)                #sorting by volume high to low
    ans = []                                #the list of added items
    tot_vol = 0                             #total volume
    tot_val = 0                             #total value
    found = True
    while found:                            # until no fitting item is found
        found = False
        for x in items:                     #to search for items to add
            if((x[0] + tot_vol) <= max_vol):#check if it fits within the max volume
                tot_vol += x[0]             #add to total volume
                tot_val += x[2]             #add to total value
                ans.append([x[1],x[2], x[0]])            #add item name
                found = True
                break
        
    return ans, tot_val, tot_vol            #return the items, the total value, and total volume

def main():
    f = input('Please enter the file name(please include path if necessary): ') #get file name/path
    max_vol = int(input('Please enter the maximum volume available(in³): '))    #get maximum volume
    ans, tot_val, tot_vol = knapsack(f, max_vol)
    count = 1
    for i in ans:
        print(f'Item #{count}:')
        count +=1
        print(f'\tItem Name: {i[0]}\n\tItem Value: ${i[1]}.00\n\tItem Volume: {i[2]} in³\n')
    print(f'\nTotal Value: ${tot_val}.00\nTotal Volume: {tot_vol} in³\nTotal # of Items: {count-1}')

if __name__ == '__main__':
    main()