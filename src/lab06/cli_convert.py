import argparse
from src.lab05.json_csv import json_to_csv, csv_to_json
from src.lab05.csv_xlsx import csv_to_xlsx




def main():
    parser = argparse.ArgumentParser(description="Конвертация между json и csv")
    subparsers = parser.add_subparsers(dest="command")

    # подкоманда json2csv
    parser_j2c = subparsers.add_parser("json2csv", help="Конвертация json в csv")
    parser_j2c.add_argument("--input", required=True, help="Входной json файл")
    parser_j2c.add_argument("--output", required=True, help="Финальный csv файл")

    # подкоманда csv2json
    parser_c2j = subparsers.add_parser("csv2json", help="Конвертация csv в json")
    parser_c2j.add_argument("--input", required=True, help="Входной csv файл")
    parser_c2j.add_argument("--output", required=True, help="Финальный json файл")

    # подкоманда csv2xlsx
    parser_c2x = subparsers.add_parser("csv2xlsx", help="Конвертация csv в xlsx")
    parser_c2x.add_argument("--input", required=True, help="Входной csv файл")
    parser_c2x.add_argument("--output", required=True, help="Финальный xlsx файл")

    args = parser.parse_args()

    if args.command == "json2csv":
        try:
            json_to_csv(args.input, args.output)
            print("Каонвертация завершена")
        except FileNotFoundError:
            parser.error("Входной файл не найден")
    
    elif args.command == "csv2json":
        try: 
            csv_to_json(args.input, args.output)
            print("Конвертация завершена")
        except FileNotFoundError:
            parser.error("Входной файл не найден")
    elif args.command == "csv2xlsx":
        try:
            csv_to_xlsx(args.input, args.output)
            print("Конвертация завершена")
        except FileNotFoundError:
            parser.error("Входной файл не найден")
        
if __name__ == "__main__":
    main()
    
    
