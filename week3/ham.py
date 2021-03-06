def ham(string1, string2):
    assert len(string1) == len(string2)
    return sum(st1 != st2 for st1, st2 in zip(string1, string2))


input1 = "{0:08b}".format(25)
input2 = "{0:08b}".format(30)
print(ham(str(input1),str(input2)))
print("***********************************")
input1 = "{0:08b}".format(1)
input2 = "{0:08b}".format(4)
print(ham(str(input1),str(input2)))
print("***********************************")
input1 = "{0:09b}".format(100)
input2 = "{0:09b}".format(250)
print(ham(str(input1),str(input2)))
print("***********************************")
input1 = "{0:08b}".format(1)
input2 = "{0:08b}".format(30)
print(ham(str(input1),str(input2)))
print("***********************************")
input1 = "{0:09b}".format(255)
input2 = "{0:09b}".format(0)
print(ham(str(input1),str(input2)))
