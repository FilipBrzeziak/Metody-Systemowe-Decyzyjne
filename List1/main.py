import csv


def more_than_20(row):
    if float(row[20]) > 20:
        return True

    return False


def print_20(rows):
    for row in rows:
        print(
            "{: >40} {: >40} {: >40} {: >50} {: >50}  {: >50} {: >50} {: >50} {: >50} {: >50} {: >50} {: >50} {: >50} "
            "{: >50} {: >50} {: >50} {: >50} {: >50} {: >50} {: >50}".format(
                *row))


def print_21(rows):
    for row in rows:
        print(
            "{: >40} {: >40} {: >40} {: >40} {: >50} {: >50}  {: >50} {: >50} {: >50} {: >50} {: >50} {: >50} {: >50} "
            "{: >50} {: >50} {: >50} {: >50} {: >50} {: >50} {: >50} {: >50}".format(
                *row))


def print_21_formatted_string(rows):
    for row in rows:
        print("%s-%s: %s" % (row[0], row[1], row[20]))


def main():
    # Zad1

    print("Zad1")
    file = open("akutalne_dane_powiaty.csv")
    csvreader = csv.reader(file)
    header = str(next(csvreader))
    header = header.replace("['", "", 1)
    header = header.replace("']", "", 1)
    header = header.split(';')
    rows = [header]

    for i in csvreader:
        row = str(i)
        row = row.replace("['", "", 1)
        row = row.replace("']", "", 1)
        col = row.split(';')
        rows.append(col)

    file.close()
    print_20(rows)

    # Zad2

    print("Zad2")
    rows[0].append("testy_pozytywne_procent")

    for row in rows[1::]:
        result = int(row[15]) / int(row[14]) * 100
        row.append("{:.2f}".format(result))

    print_21(rows)
    print()
    print_21_formatted_string(rows)

    # Zad3
    print("Zad3")
    sorted_rows = [rows[0]]
    rows = sorted(rows[1:], key=lambda row_lamb: float(row_lamb[20]))
    sorted_rows = sorted_rows + rows
    print_21(sorted_rows)
    print()
    print_21_formatted_string(sorted_rows)

    # Zad4
    print("Zad4")
    after_filter_iterator = filter(more_than_20, rows)
    after_filter = list(after_filter_iterator)
    print_21(after_filter)
    print()
    print_21_formatted_string(after_filter)


if __name__ == '__main__':
    main()
