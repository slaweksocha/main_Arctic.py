from datetime import datetime


def log_add_line(log_line):
    timestamp = str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    today = str(datetime.now().strftime("%Y-%m-%d"))
    with open(f'log_{today}.log', 'a') as log:
        log.write(f'{timestamp} - {log_line}\n')