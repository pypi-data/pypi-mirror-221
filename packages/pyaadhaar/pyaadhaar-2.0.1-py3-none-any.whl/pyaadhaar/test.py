from decode import AadhaarSecureQr


filename = "/home/tanmoy/Desktop/aadhar/sample/1.txt"
file = "".join(open(filename, "r").readlines())

obj = AadhaarSecureQr(int(file))
extracted_fields = obj.decodeddata()
print(extracted_fields)
print(obj.verifyMobileNumber("9333584419"))
