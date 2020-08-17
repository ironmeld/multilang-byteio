def copy(input_byte_stream, output_byte_stream, buffer_size=1000000):
    """Copy all bytes from input stream to output stream."""
    while True:
        bytes_read = input_byte_stream.read(buffer_size)
        if not bytes_read:
            return
        output_byte_stream.write(bytes_read)
