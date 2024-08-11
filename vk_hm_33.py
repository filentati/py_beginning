import os 

text = input()

def write_and_read(text):
    my_file = os.path.join(os.path.abspath('/tmp'), 'my_file')
    open(my_file, "w").write(text)
    read_text = open(my_file, "r").read()
    return read_text
    
print(write_and_read(text))

