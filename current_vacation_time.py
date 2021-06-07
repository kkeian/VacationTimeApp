from format_table import nice_table

def curr_time_saved():
    with open('timeSaved.txt') as time_saved:
        read_values = time_saved.read()

    days_saved = read_values.split(',')
    # Print out nicely formatted table 
    nice_table(days_saved)
