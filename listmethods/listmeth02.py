#!/usr/bin/env python3
proto = ["ssh", "http", "https"]
protoa = ["ssh", "http", "https"]
protob = ["ssh", "http", "https"]
print(proto)
proto.append("dns") # this line will add "dns" to the end of our list
protoa.append("dns") # this line will add "dns" to the end of our list
protob.append("dns") # this line will add "dns" to the end of our list
print(proto)
proto2 = [ 22, 80, 443, 53 ] # a list of common ports
proto.extend(proto2) # pass proto2 as an argument to the extend method
print(proto)
protoa.append(proto2) # pass proto2 as an argument to the append method
print(protoa)

# next bit inspired by https://stackoverflow.com/a/7946825
combined = protob + proto2 # combine both lists
print(combined)
combined[::2] = protob # assigns the elements of protob to all the even-numbered indexes of combined
print(combined)
combined[1::2] = proto2 # assigns the elements of proto2 to all the odd-numbered indexes of combined
print(combined)
