import utils

test = utils()

formatterBinaryInt, formatterOctalInt = test.formatter(16)
formatterBinaryFloat, formatterOctalFloat = test.formatter(15.99)
formatterBinaryString, formatterOctalString = test.formatter("test")

print(test.reversed(57))
print(test.reversed(2.99))
print(test.reversed("test"))

print(f"Binary for Int: {formatterBinaryInt}, Octal for Int: {formatterOctalInt}")
print(f"Binary for Int: {formatterBinaryFloat}, Octal for Int: {formatterOctalFloat}")
print(f"Binary for Int: {formatterBinaryString}, Octal for Int: {formatterOctalString}")
