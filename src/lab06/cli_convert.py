import argparse
from src.lab05.json_csv import json_to_csv, csv_to_json

def main():
    parser = argparse.ArgumentParser(description="Конвертация между json и csv")
    subparsers = parser.add_subparsers(dest="cmd")

    # подкоманда json2csv
    parser_j2c = subparsers.add_parser("json2csv", help="Конвертация json в csv")
    parser_j2c.add_argument("--input", required=True, help="Входной json файл")
    parser_j2c.add_argument("--output", required=True, help="Финальный csv файл")

    # подкоманда csv2json
    parser_c2j = subparsers.add_parser("csv2json", help="Конвертация csv в json")
    parser_c2j.add_argument("--input", required=True, help="Входной csv файл")
    parser_c2j.add_argument("--output", required=True, help="Финальный json файл")

    # подкоманда csv2xls
    parser_c2x = subparsers.add_parser("csv2xls", help="Конвертация csv в xls")
    parser_c2x.add_argument("--input", required=True, help="Входной csv файл")
    parser_c2x.add_argument("--output", required=True, help="Финальный xls файл")

    args = parser.parse_args()


