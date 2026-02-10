import csv
from pathlib import Path


class CSVDataLoader:
    @staticmethod
    def load_expected_titles(csv_file: str) -> dict:
        expected = {}
        path = Path(csv_file)

        with open(path, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                expected[row["menu_item"].strip().lower()] = row["expected_title"]

        return expected