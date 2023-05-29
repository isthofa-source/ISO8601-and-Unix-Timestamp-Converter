from datetime import datetime

# Fungsi untuk mengubah Unix Timestamp ke format ISO 8601
def unix_timestamp_to_iso8601(unix_timestamp):
    dt = datetime.fromtimestamp(unix_timestamp)
    iso8601_string = dt.isoformat()
    return iso8601_string

# Contoh penggunaan
unix_timestamp = 1685355029
iso8601_timestamp = unix_timestamp_to_iso8601(unix_timestamp)
print(iso8601_timestamp)
