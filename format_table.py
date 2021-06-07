def nice_table(array_of_days):
    # Print Heading
    vac_string = 'Vacation Days'
    personal_string = 'Personal Leave Days'
    holiday_string = 'Holiday Days'
    comp_string = 'Comp Days'
    vacation_categories = [vac_string, personal_string, holiday_string,
            comp_string]

    total_string_header = ''
    for category in vacation_categories:
        total_string_header += category + ' ' * 8

    print(total_string_header)
    print('=' * (len(total_string_header) - 8))
    
    for days_saved in array_of_days:
        print(days_saved, end=(' ' * 8))

