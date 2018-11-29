row1 = "...^^^^^..^...^...^^^^^^...^.^^^.^.^.^^.^^^.....^.^^^...^^^^^^.....^.^^...^^^^^...^.^^^.^^......^^^^"

def count_safe_tiles(row1, row_numbers):
    rows = ["." + row1 + "."]

    row = 0
    while True:
        new_row = ""
        for tile in range(1, len(rows[row])-1):
            prev = map(lambda x: x == "^", rows[row][tile-1:tile+2])
            new_row += "^" if (prev[0] and prev[1] and not prev[2]) or (prev[1] and prev[2] and not prev[0]) or (prev[0] and not prev[1] and not prev[2]) or (prev[2] and not prev[0] and not prev[1]) else "."
        rows.append("." + new_row + ".")
        row += 1
        if row == row_numbers - 1:
            break
    return ''.join([row[1:-1] for row in rows]).count(".")

print "Safe tiles in 40 rows: %s" % count_safe_tiles(row1, 40)
print "Safe tiles in 400000 rows: %s" % count_safe_tiles(row1, 400000)
