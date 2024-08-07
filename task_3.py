import sys
import os

def parse_log_line(line: str) -> dict:
    '''Parses a log line and returns a dictionary with the date, time, log level and message.'''
    parts = line.split(" ", 3) # Split the line into 4 parts.

    if len(parts) != 4: # Check if the line has 4 parts.
        raise ValueError(f"Неправильний формат лог-рядка: {line}")

    return {"date": parts[0], "time": parts[1], "level": parts[2], "message": parts[3]} 

def load_logs(file_path: str) -> list:
    '''Loads log lines from a file and returns a list of dictionaries with the log data.'''
    logs = [] # A list to store the log lines.
    
    with open(file_path, "r") as file:
        for line in file: 
            logs.append(parse_log_line(line.strip())) # Parse the log line and add it to the list.
    
    return logs

def filter_logs_by_level(logs: list, level: str) -> list:
    '''Filters log lines by the specified log level and returns a list of dictionaries with the log data.'''
    return [log for log in logs if log["level"] == level] 

def count_logs_by_level(logs: list) -> dict:
    '''Counts the log lines by log level and returns a dictionary with the counts.'''
    counts = {} # A dictionary to store the log counts.
    
    for log in logs: 
        level = log["level"] 
        
        if level in counts: # Check if the log level is already in the dictionary.
            counts[level] += 1 # Increment the count.
        else:
            counts[level] = 1 # Initialize the count.
    
    return counts

def display_log_counts(counts: dict):
    '''Displays the log counts in a formatted way.'''
    print("Рівень логування | Кількість")
    print("-----------------|---------")
    for level, count in counts.items(): # Iterate over the log counts.
        print(f"{level:<16} | {count}") # Display the log level and count.

def main():
    args = sys.argv[1:]
    try:
        if len(args) < 1:
            raise ValueError("Не вказано шлях до файлу з логами.")
        
        log_file = args[0]
        log_level = args[1].upper() if len(args) > 1 else None

        if not os.path.exists(log_file):
            raise FileNotFoundError(f"Файл з логами не знайдено: {log_file}")
        elif not os.path.isfile(log_file):
            raise ValueError(f"Вказаний шлях не є файлом: {log_file}")
        elif not log_file.endswith(".log"):
            raise ValueError("Файл з логами повинен мати розширення .log")
        
        logs = load_logs(log_file)

        if log_level:
            logs = filter_logs_by_level(logs, log_level)

        counts = count_logs_by_level(logs)
        display_log_counts(counts)

    except Exception as e:
        print(f"Помилка: {e}")


if __name__ == "__main__":
    main()