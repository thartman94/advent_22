def find_marker_index(data_stream):
    marker_buffer = []
    i = 0
    while i < len(data_stream):
        char = data_stream[i]
        if char in marker_buffer:
            marker_buffer = marker_buffer[marker_buffer.index(char) + 1 :]
        marker_buffer.append(char)
        i += 1
        if len(marker_buffer) == 14:
            return i


with open("./input.txt") as file:
    data_stream = file.readline()

ans = find_marker_index(data_stream)
print(ans)
