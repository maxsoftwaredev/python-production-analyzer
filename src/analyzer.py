import pandas as pd


class ProductionAnalyzer:

    def __init__(self, file_path):
        self.df = pd.read_csv(file_path)

    def total_runtime(self):
        return self.df["runtime"].sum()

    def total_errors(self):
        return self.df["error"].sum()

    def machine_count(self):
        return len(self.df)

    def print_summary(self):
        print("=== PRODUCTION SUMMARY ===")
        print(f"Total runtime: {self.total_runtime()}")
        print(f"Total errors: {self.total_errors()}")
        print(f"Machines: {self.machine_count()}")