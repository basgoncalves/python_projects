Total = 958
voice =	262
guitar = 278
piano =	178
drums =	135	
saxophone =	48
violin = 57

def ratio_calc(portion,total):
    proportion = round(portion/total,2)
    percentage = round(proportion*100,0)
    return proportion, percentage


print(ratio_calc(voice,Total))
print(ratio_calc(guitar,Total))
print(ratio_calc(piano,Total))
print(ratio_calc(drums,Total))
print(ratio_calc(saxophone,Total))
print(ratio_calc(violin,Total))