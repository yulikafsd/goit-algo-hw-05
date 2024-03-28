from pathlib import Path
from collections import defaultdict

def parse_log_line(line: str) -> dict:    # приймає рядок з логу як вхідний параметр
    date, time, level, message = line.strip().split(' ', 3)
    # повертає словник з розібраними компонентами: дата, час, рівень, повідомлення
    return {'date': date, 'time': time, 'level': level.lower(), 'message': message}

def load_logs(file_path: str) -> list:
    try:
        log_path = Path(file_path)
        if not log_path.exists() or len(file_path) < 1:
            print('This path does not exist')
            return
    except Exception as e:
        print(f'Error - {e}')
        return

    with open (log_path, 'r', encoding='utf-8') as fh:
        logs = fh.readlines()
        log_list = [parse_log_line(log) for log in logs]
        return log_list

def filter_logs_by_level(logs: list, level: str) -> list:
    level_lowered = level.lower()
    filtered_logs = list(filter(lambda log: log['level'] == level_lowered, logs))
    if len(filtered_logs) == 0:
        return 'No logs with this name!'
    # отримати всі записи логу для певного рівня логування
    print(f'Деталі логів для рівня "{level.upper()}":')
    log_details = ''
    for log in filtered_logs:
        log_details += (f'{log["date"]} {log["time"]} - {log["message"]}\n')
    return log_details

def count_logs_by_level(logs: list) -> dict:
# проходить по всім записам і підраховує кількість записів для кожного рівня логування.
    dict = defaultdict(int)
    for log in logs:
        dict[log['level']] += 1
    return dict

def display_log_counts(counts: dict):
    header = 'Рівень логування | Кількість'
    separator = f'{"-"*17}|{"-"*10}'
    body=''
    for key, value in counts.items():
        body += '{:<17}| {:<10}\n'.format(key.upper(), value)
    table = '\n'.join([header, separator, body])
    return table

def main(file_path, level = None):
    logs = load_logs(file_path)
    count = count_logs_by_level(logs)
    print(display_log_counts(count))
    if level:
        print(filter_logs_by_level(logs, level))

if __name__ == "__main__":
    main('./log_file.log')
