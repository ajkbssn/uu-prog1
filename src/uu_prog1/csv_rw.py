
#
# Example of reading a numerical (decimal valued) csv file with headers
# Author: Johan Ofverstedt
#
# Read more about csv file reading/writing here:
# https://docs.python.org/3/library/csv.html
#

import csv

# Read a csv file and store the contents as a list of lists
# [[heading1, heading2, ...], [row1_col1, row1_col2, ...], [ro2_col2]]
# with each element striped of white-space on both sides.
with open('test_data.csv', newline='\n') as f:
    reader = csv.reader(f, delimiter=',')

    rows = []
    for row in reader:
        elems = [col.strip() for col in row]
        rows.append(elems)

# Print the headers
print(f'Hdr: {rows[0]}')
for i, r in enumerate(rows[1:], start=1):
    print(f'{i:03d}: {r}')

# Function that can extracts the contents of a single named column as a list of floats
def get_column_as_float(rows, col_name):
    # Find the column of values that correspond to the column name
    # by searching through the list of headers
    col_index = rows[0].index(col_name)
    # Iterate over all the rows to construct the list of values converted to float
    c = []
    for i in range(1, len(rows)):
        valstr = rows[i][col_index]
        valfloat = float(valstr)
        c.append(valfloat)

    return c

print(get_column_as_float(rows, 'y'))

if __name__ == '__main__':
    # Import Matplotlib
    import numpy as np
    import matplotlib.pyplot as plt

    # Make a scatter plot with matplotlib
    xs = get_column_as_float(rows, 'x')
    ys = get_column_as_float(rows, 'y')
    sizes = get_column_as_float(rows, 'size')

    plt.scatter(xs, ys, s=sizes)
    plt.show()

    xs_sorted_ind = np.argsort(xs)
    xs_sorted = np.array(xs)[xs_sorted_ind]
    ys_sorted = np.array(ys)[xs_sorted_ind]
    sizes_sorted = np.array(sizes)[xs_sorted_ind]

    plt.plot(xs_sorted, ys_sorted)
    plt.plot(xs_sorted, sizes_sorted)
    plt.legend(('y', 'size'))
    plt.show()
