import mmap

# Create a binary file with some data
filename = "example.bin"
with open(filename, "wb") as f:
    f.write(b"ABCDEFGHIJKLMNOPQRSTUVWXYZ")

# Function to read and modify binary data using memoryview and mmap
def modify_binary_file(filename):
    with open(filename, "r+b") as f:
        # Memory map the file to access its content in writable mode
        with mmap.mmap(f.fileno(), 0) as mm:
            # Create a writable memoryview from the mmap object
            mv = memoryview(mm)
            
            # Print the original content
            print("Original content:", mv.tobytes())
            
            # Modify the data using memoryview
            mv[:6] = b"123456"
            
            # Print the modified content
            print("Modified content:", mv.tobytes())
            
            # Release the memoryview object
            mv.release()

modify_binary_file(filename)
