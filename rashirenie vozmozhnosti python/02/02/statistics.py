from datetime import datetime

def generate_report():
    report_content = f"Ежедневный отчет за {datetime.now().strftime('%Y-%m-%d')}\n\nДанные отчета..."
    report_path = 'daily_report.txt'
    with open(report_path, 'w') as file:
        file.write(report_content)
    return report_path