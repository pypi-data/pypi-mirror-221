def format_time(input_time:float, time_units:str = 'seconds', max_displayed_units:int = 1,
                decimal_points:int = 5, minimum_whole_value:float = 1.0):
    '''
    Returns a convenient and easy-to-read string of a time input.
    
    input_time:float  =  input time to analyze as a float
    
    time_units:str  =  the units of measurement for input_time. accepts as input any one of the following:
        'nanoseconds', 'milliseconds', 'seconds', 'minutes', 'hours', 'days', 'weeks', 'months', 'years'
    where each month is assumed to be 30 days and each year is assumed to be 365 days. Thus, in these measurements,
    there is going to be a bit of inaccuracy so these input types are not preferred.
        
    max_displayed_units:int  =  how many units of time to display in the output
    
    displayed_units_override:bool  =  whether or not to override the number of units to output in max_displayed_units if the output
    is of a time greater than 1 day. If this is set to True, then if say for example an input is 3.5 days long, the output will instead
    be that of 3 days and 12 hours. If the input is 2.25 years, 1 day, and 3.5 hours long, the output will be 2 years, 3 months, 1 day,
    and 3.5 hours. If this is set to False and if your max_displayed_units value is set to 1, then this output will simply remain as 2.25 years.
    
    decimal_points:int  =  number of decimal points to display in the output
    
    minimum_whole_value:float  =  the minimum value of an output unit to display that unit at. For example, if this is set to 0.9 and the
    input_time is 0.8 years, then it will not display 0.8 years but instead its equivalent in months (the next biggest interval of time).
    If, however, the input_time is 0.95 years, then this function will output 0.95 years. If this value is set to 1 and the input_time is
    0.95 years, then it will not output 0.95 years but instead its equivalent in months.
    '''
    units_dict = {'nanoseconds':1000000000, 'milliseconds':1000, 'seconds':1, 'minutes':1/60, 'hours':1/3600,
                  'days':1/86400, 'weeks':1/604800, 'months':1/2592000, 'years':1/31536000}
    units_list = list(units_dict.keys())
    
    input_time = float(input_time)
    if time_units == 'nanoseconds':
        input_time /= 1000000000
    elif time_units == 'milliseconds':
        input_time /= 1000
    elif time_units == 'seconds':
        pass
    elif time_units == 'minutes':
        input_time *= 60
    elif time_units == 'hours':
        input_time *= 3600
    elif time_units == 'days':
        input_time *= 86400
    elif time_units == 'weeks':
        input_time *= 604800
    elif time_units == 'months':
        input_time *= 2592000
    elif time_units == 'years':
        input_time *= 31536000
    else:
        raise ValueError('''Please input a valid unit of time. Accepted units of time are nanoseconds,
                         milliseconds, seconds, minutes, hours, days, weeks, months, or years.''')
    
    if input_time / 31536000 >= minimum_whole_value:
        max_unit = 'years'
    elif input_time / 2592000 >= minimum_whole_value:
        max_unit = 'months'
    elif input_time / 604800 >= minimum_whole_value:
        max_unit = 'weeks'
    elif input_time / 86400 >= minimum_whole_value:
        max_unit = 'days'
    elif input_time / 3600 >= minimum_whole_value:
        max_unit = 'hours'
    elif input_time / 60 >= minimum_whole_value:
        max_unit = 'minutes'
    elif input_time >= minimum_whole_value:
        max_unit = 'seconds'
    elif input_time * 1000 >= minimum_whole_value:
        max_unit = 'milliseconds'
    else:
        max_unit = 'nanoseconds'

    included_units = []
    max_unit_index = units_list.index(max_unit)
    for index in range(max_displayed_units):
        if max_unit_index - index >= 0:
            included_units.append(units_list[max_unit_index - index])
        else:
            break
    
    output_dict = {}
    for unit in included_units:
        float_value = input_time * units_dict[unit]
        int_value = int(str(float_value).split('.')[0])
        
        if included_units[-1] != unit:
            if int_value != 0:
                output_dict[unit] = int_value
            input_time -= (int_value * 1/units_dict[unit])
        
        else:
            if float_value != 0.0:
                output_dict[unit] = round(float_value, decimal_points)
    
    output_string = []        
    for key in list(output_dict.keys())[::-1]:
        output_string.insert(0, f'{output_dict[key]} {key},')
    
    if len(output_string) >= 2:
        output_string.insert(-1, 'and')
    output_string = ' '.join(output_string)
    
    return output_string[:-1]

