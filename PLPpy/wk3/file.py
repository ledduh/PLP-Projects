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
# Seek(0) starts at the beginning of the file

# # print(f.closed)



# with open('test.txt', 'w') as f:
#     f.write("TEST2")

# with open('tt.txt', 'r') as rf:
#     with open("ttcopy.txt", 'w') as wf:
#         for line in rf:
#             wf.write(line)

# --------------
# writing reading jpeg files
# we use binary so read 'r' becomes 'rb' read binary
# 'w' becomes 'wb' write binary

# with open ('121.jpg', 'rb') as rf:
#     with open('12_ccopy.jpg', 'wb') as wf:
#         for line in rf:
#             wf.write(line)


# with open ('121.jpg', 'rb') as rf:
#     with open('121_ccnopy.jpg', 'wb') as wf:
#         chunk_size = 4096
#         rf_chunk = rf.read(chunk_size)
#         while len(rf_chunk) > 0:
#             wf.write(rf_chunk)
#             rf_chunk = rf.read(chunk_size)
