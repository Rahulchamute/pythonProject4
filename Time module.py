
##print(time.time())

import time
# %%time
# i = 0
# while i < 100000:
#     pass
#     i += 1

# %%time
# for i in range(10000):
#     print("Hi")

# print(time.time())
# print(time.gmtime(0))
# print(time.ctime(1651079337.9513185))

# start_time=time.time()
# print(start_time)
#
# end_time=time.time()
# print(end_time)

# start_time=time.time()
# for i in range(100000):
#     print(i)
#
# end_time=time.time()
#
# print("total time:-",end_time-start_time)
#
# start_time=time.time()
# i=0
# while i<100000:
#     print(i)
#     i+=1
#
# end_time=time.time()
#
# print("total time:-",end_time-start_time)


start_time=time.time()
li = [1,2,3,4,5]
for i in li:
    print(i)
    time.sleep(2)