
# A file contain sequence of integers, stored one per line. Implement a class that facilitate iteration over the integers.

# file_object is stringIO object

def solution(file_object):
    while True:
        line = file_object.readline()
        if not line == '':
            try:
                line = int(line)
                if 1000000000 > line > -1000000000:
                    yield line
            except:
                pass
        else:
            return StopIteration

# Example Usage
#for i in solution(file_object):
#    print(i)
    
