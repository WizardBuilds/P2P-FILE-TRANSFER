chunk_size=4096
def read_chunks(file):
    while True:
        data=file.read(chunk_size)
        if not data:
            break
        yield data
    # yield is used to send the 4kb chunk at a time
    