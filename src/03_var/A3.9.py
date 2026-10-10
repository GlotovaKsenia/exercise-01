import numpy

no = [12,15,11,14,48]
print(sum(no))
print(len(no))

average = sum(no)/len(no)
print(average)
print(max(no))
print("------------------")


result = numpy.array(no).mean()
print(result)
print(numpy.array(no).max())