import io
import gzip

# Data to be compressed and written
data = b"ullas is awesome" * 1000

# Function to write compressed data to a file
def write_compressed_file(filename, data):
    with gzip.open(filename, 'wb') as f:
        buffer = io.BytesIO(data)
        f.write(buffer.getvalue())

# Function to read compressed data from a file
def read_compressed_file(filename):
    with gzip.open(filename, 'rb') as f:
        buffer = io.BytesIO(f.read())
        return buffer.getvalue()

# Write the compressed data
compressed_filename = "example.gz"
write_compressed_file(compressed_filename, data)

# Read the compressed data
read_data = read_compressed_file(compressed_filename)

# Verify the data
print("Original data size:", len(data))
print("Compressed file size:", len(open(compressed_filename, 'rb').read()))
print("Read data size:", len(read_data))
print("Data integrity check:", data == read_data)
