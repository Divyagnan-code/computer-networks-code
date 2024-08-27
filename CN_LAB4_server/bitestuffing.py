FLAG = b'11111'  # String "FLAG" as the flag byte sequence
ESC = b'000000'  # String "ESC" as the escape byte sequence


def byte_stuff(data):
    stuffed_data = FLAG  # Start with the flag sequence
    for byte in data:
        if byte == FLAG[0]:  # Check if the byte matches the first byte of FLAG
            stuffed_data += ESC + b'F'
        elif byte == ESC[0]:  # Check if the byte matches the first byte of ESC
            stuffed_data += ESC + b'E'
        else:
            stuffed_data += bytes([byte])
    stuffed_data += FLAG  # End with the flag sequence
    return stuffed_data


def byte_unstuff(stuffed_data):
    unstuffed_data = b''
    i = len(FLAG)  # Skip the initial FLAG sequence
    while i < len(stuffed_data) - len(FLAG):  # Skip the final FLAG sequence
        if stuffed_data[i:i + len(ESC)] == ESC:
            if stuffed_data[i + len(ESC):i + len(ESC) + 1] == b'F':
                unstuffed_data += FLAG[0:1]
            elif stuffed_data[i + len(ESC):i + len(ESC) + 1] == b'E':
                unstuffed_data += ESC[0:1]
            i += len(ESC) + 1
        else:
            unstuffed_data += stuffed_data[i:i + 1]
            i += 1
    return unstuffed_data


# Test the implementation
data = b'This is a test message with FLAG and ESC sequences.'
stuffed = byte_stuff(data)
print(f"Stuffed Data: {stuffed}")
unstuffed = byte_unstuff(stuffed)
print(f"Unstuffed Data: {unstuffed}")

assert data == unstuffed, "Data unstuffed incorrectly!"
