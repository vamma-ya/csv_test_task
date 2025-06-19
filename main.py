import argparse
from tabulate import tabulate
import sys
from csv_processor import read_csv, filter_data, aggregate_data

def main():
    parser = argparse.ArgumentParser(description="CSV фильтрация и агрегация")
    parser.add_argument('--file', required=True, help='Путь к CSV файлу')
    parser.add_argument('--where', help='Фильтр вида column=value, column>value, column<value')
    parser.add_argument('--aggregate', help='Агрегация вида column=avg|min|max')

    args = parser.parse_args()

    try:
        data = read_csv(args.file)
    except FileNotFoundError:
        print(f"Файл не найден: {args.file}")
        sys.exit(1)

    if args.where:
        data = filter_data(data, args.where)

    if args.aggregate:
        result = aggregate_data(data, args.aggregate)
        print(tabulate([result], headers="keys", tablefmt="grid"))
    else:
        if data:
            print(tabulate(data, headers="keys", tablefmt="grid"))
        else:
            print("Нет данных для отображения.")

if __name__ == '__main__':
    main()
