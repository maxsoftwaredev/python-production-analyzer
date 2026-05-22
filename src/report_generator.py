class ReportGenerator:

    @staticmethod
    def generate(runtime, errors, machines):
        return f"""
PRODUCTION REPORT
=================
Total Runtime: {runtime}
Total Errors: {errors}
Machines: {machines}
"""