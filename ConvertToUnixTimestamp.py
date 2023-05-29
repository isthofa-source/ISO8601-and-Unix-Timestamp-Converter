from datetime import datetime

# Fungsi untuk mengubah format ISO 8601 ke Unix Timestamp
def iso8601_to_unix_timestamp(iso8601_string):
    dt = datetime.fromisoformat(iso8601_string)
    timestamp = dt.timestamp()
    return int(timestamp)

# Contoh penggunaan
iso8601_string = "2023-05-29T17:10:29+07:00"
unix_timestamp = iso8601_to_unix_timestamp(iso8601_string)
print(unix_timestamp)
