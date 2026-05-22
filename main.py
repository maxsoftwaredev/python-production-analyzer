from src.analyzer import ProductionAnalyzer
from src.report_generator import ReportGenerator
from src.utils import print_header


def main():

    analyzer = ProductionAnalyzer("data/production_log.csv")

    print_header("PRODUCTION ANALYSIS")

    analyzer.print_summary()

    report = ReportGenerator.generate(
        analyzer.total_runtime(),
        analyzer.total_errors(),
        analyzer.machine_count()
    )

    print(report)


if __name__ == "__main__":
    main()