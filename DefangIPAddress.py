# asks user for IP to defang
print("IP address to defang: " + address)
arr = address.split(".")
new_address = "[.]".join(arr)
print(new_address)
