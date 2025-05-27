# Problem Statement:
# Write a Python script that reads a log file named server.log. Each line in the log file represents a log entry. Your script should count and print the total number of "ERROR" messages, "WARNING" messages, and "INFO" messages found in the file.

#  Assume server.log contains lines like:


# INFO: Service started successfully.
# WARNING: Disk space running low.
# ERROR: Database connection failed.
# INFO: User logged in.
# ERROR: Null pointer exception.


def count_log_messages(log_file):
    error_count = 0
    warning_count = 0
    info_count = 0

    try:
        with open(log_file) as file:
            for line in file:
                line = line.strip()
                if line.startswith("ERROR:"):
                    error_count += 1
                elif line.startswith("WARNING:"):
                    warning_count += 1
                elif line.startswith("INFO:"):
                    info_count += 1

        print(f"Total ERROR messages: {error_count}")
        print(f"Total WARNING messages: {warning_count}")
        print(f"Total INFO messages: {info_count}")

    except FileNotFoundError:
        print(f"The file {log_file} does not exist.")


if __name__ == "__main__":
    count_log_messages("server.log")