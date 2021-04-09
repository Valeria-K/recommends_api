import csv
import os


def get_line_at_pos(file, pos):
    file.seek(pos)
    if pos > 0:
        skip = file.readline()
    npos = file.tell()
    line = file.readline()
    return npos, line


def binary_search(file_name, field_func, field_val):
    size = os.path.getsize(file_name)
    min_pos, max_pos, cur = 0, size, int(size / 2)
    with open(file_name) as file:
        prev_pos = -1
        while True:
            real_pos, line = get_line_at_pos(file, cur)
            val = field_func(line)
            if val >= field_val:
                max_pos = cur
                cur = int((min_pos + cur) / 2)
            else:
                min_pos = cur
                cur = int((cur + max_pos) / 2)

            if prev_pos == cur:
                break
            prev_pos = cur
    return real_pos


def get_sku_from_line(line):
    return line.split(',')[0]


def find_recommendations_in_csv(filename: str, sku: str, min_rank: float):
    err = None
    found = False
    pos = binary_search(filename, get_sku_from_line, sku)
    recommendations = []
    with open(filename, 'r', encoding='utf_8_sig') as csv_file:
        csv_file.seek(pos)
        reader = csv.reader(csv_file, delimiter=',')
        for row in reader:
            if row[0] == sku:
                if float(row[2]) >= min_rank:
                    recommendations.append(row[1])
                    found = True
            elif row[0] > sku:
                break

    if not found:
        err = 'Sku: {} not found'.format(sku)

    return recommendations, err
