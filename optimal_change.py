def optimal_change(item_cost, amount_paid):

    #check that change is required
    if item_cost >= amount_paid : return "You are owed no change" 
    
    #variables
    values = {100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 1: 0,.25: 0, .10: 0, .05: 0, .01: 0} #values and their count
    units = {.25: 'quarter', .10: 'dime', .05: 'nickel', .01: 'penny'} #titles of units
    ans = f'The optimal change for an item that costs ${item_cost:.2f} with an amount paid of ${amount_paid:.2f} is' #beginning of return string
    change = amount_paid - item_cost # calc required change

    #calc number of bills/coins and store in object
    while change >= .01:
        for k in values:
            if change >= k:
                values[k] = values[k] + 1
                change = round(change - k, 2)
                break

    #reduce object to exclude bills/coins not used
    values = {k: v for k, v in values.items() if v != 0}

    #print info from reduced value dict
    for i, k in enumerate(values):
        unit = 'bill' if k >=1 else units[k]
        if unit == 'penny' and values[k] > 1:
            unit = 'pennies'
        ans = ans + f" {'and ' if (len(values) > 1 and i == len(values)-1) else ''}{values[k]} {f'${k} ' if k >= 1 else ''}{unit}{'s' if (values[k] != 1 and k!=0.01) else ''}{'.' if (i == len(values)-1) else ','}"
    
    return ans