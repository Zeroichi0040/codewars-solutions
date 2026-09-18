# takes dad's age and his son's age. to identify the time the dad is twice as old as his son has already happened or not,
# multiply the son's age by 2, and if dad is still older, it has already happened in the past
# if the son's age multiplied by 2 is larger than the dad's age, it will happen in the future

def twice_as_old(dad_years_old, son_years_old):
    son_years_old *= 2
    if dad_years_old > son_years_old:
        return dad_years_old - son_years_old
    else:
        return son_years_old - dad_years_old