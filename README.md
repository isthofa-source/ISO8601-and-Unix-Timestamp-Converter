# ISO8601-to-Unix-Timestamp
The iso 8601 function _to_ unix_timestamp is a function that converts date and time formats from ISO 8601 to Unix Timestamp

# POC (Proof of Concept)
## ISO 8601 >> UNIX Timestamp
![image](https://github.com/isthofa-source/ISO8601-to-Unix-Timestamp/assets/75401288/4f860ff5-4c66-4c25-9ac9-527a9f0de705)
![image](https://github.com/isthofa-source/ISO8601-to-Unix-Timestamp/assets/75401288/f7c3fb1b-d400-462d-9a95-35f266ed150a)
![image](https://github.com/isthofa-source/ISO8601-to-Unix-Timestamp/assets/75401288/5f7a6df3-68f0-4a5d-8ce2-5c294aa8afcf)

## UNIX Timestamp >> ISO 8601
![image](https://github.com/isthofa-source/ISO8601-to-Unix-Timestamp/assets/75401288/9d84efb3-876a-480c-8748-aa62a9f6d01f)
![image](https://github.com/isthofa-source/ISO8601-to-Unix-Timestamp/assets/75401288/8d3035d7-97fe-4e9d-8630-67ccea136cf9)

# Running Test
```py
python ConvertToISO8601.py
python ConvertToUnixTimestamp.py
```

# Description
ISO 8601 is an international standard for representing date and time. The ISO 8601 format has a consistent pattern and is easy for both machines and humans to read. An example of the ISO 8601 format is "YYYY-MM-DDTHH:MM:SS+HH:MM", where "YYYY" is a four-digit year, "MM" is a two-digit month, "DD" is a two-digit date, "HH" is a two-digit hour, "MM" is a two-digit minute, "SS" is a two-digit second, and "+HH:MM" is the time difference to UTC.

The Unix Timestamp is a time representation that is calculated as the number of seconds since the UNIX Epoch reference date and time, which is January 1, 1970 00:00:00 UTC. The Unix Timestamp is often used in programming to perform time calculations.

In the given usage example, the iso8601_to_unix_timestamp function accepts a string in ISO 8601 format ("2023-05-25T16:55:00+07:00"), converts it to a datetime object, and then calculates the Unix Timestamp from that datetime object. The resulting Unix Timestamp result in the example is then printed (for example, 1702397700).

Thanks :)
