# # r+ open with read and write
# # r open and read (default)
# # w write to file
# # a append to file

# # without context manager
# f = open('/home/d33d/Documents/PLP-Projects/PLPpy/wk3/tt.txt', 'r')

# f.close()
# # print(f.name)
# # print(f.mode)

# # '''with context manager automatically closes the file
# # within the block'''

# with open('/home/d33d/Documents/PLP-Projects/PLPpy/wk3/tt.txt', 'r') as f:
#     # for line in f:
#     #     print(line, end='')
#     size = 100
#     print(f.read(size)) #reads first 100 characters
#     # print(f.readlines())
#     # print(f.readline())
#     while len (f.read(size)) > 0:
#         print(f.read(size), end='') 

# # f.tell() shows current position on read
# # f.seek() sends read to start at the start

# # print(f.closed)



with open('test.txt', 'w') as f:
    pass