# -*- coding: utf-8 -*-
# @author Wendy
# @created on 2021/1/13

import csv


def open_file():
    with open('employee_file.csv', mode='w') as employee_file:
        employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        employee_writer.writerow(['John Smith', 'Accounting', 'November'])
        employee_writer.writerow(['Erica Meyers', 'IT', 'March'])


def main():
    print('good day!')


if __name__ == '__main__':
    main()

