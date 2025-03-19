def simulate_large_csv_file(count):
    data = []
    for i in range(count):
        data.append(f"{i},value_{i}")
    return '\n'.join(data).encode('utf-8')

def read_method(data, start, chunk_size):
    end = min(start + chunk_size, len(data))
    chunk = data[start:end]
    if not chunk:
        return None
    
    # Find the last newline character in the chunk
    last_newline = chunk.rfind(b'\n')
    if last_newline == -1:
        if end == len(data):
            return chunk, end
        else:  
            # This would not happen, we assume any log entry's length is always less than chunk_size
            print("consider increasing chunk size")
            return None

    chunk = chunk[:last_newline]
    next_start = start + last_newline + 1
    return chunk, next_start

if __name__ == "__main__":
    import random

    count = 1000000
    large_file_data = simulate_large_csv_file(count)

    test_count = 5
    for _ in range(test_count):
        chunk_size = random.randint(8192, 32768)
        start = 0
        res = []
        while start < len(large_file_data):
            chunk, start = read_method(large_file_data, start, chunk_size)
            if chunk is None:
                break
            chunk_str = chunk.decode('utf-8')
            entries = chunk_str.split('\n')
            res.extend(entries)
        
        assert len(res) == count
        for i in range(count):
            assert res[i] == f"{i},value_{i}"
        print("all entries read successfully.")
        
    print("test completed.")
