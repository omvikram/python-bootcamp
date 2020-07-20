dict = {"k1":100,"k2":200,"k3":300}
print(dict["k3"])

mix_dict = {"k1":111, "k2":[2,4,6,8], "k3":{"k11":1, "k22":[1,3,5,7,9]}}
print(mix_dict["k2"][2])
print(mix_dict["k3"]["k22"][2])

print(mix_dict.keys())

print(mix_dict.values())

print(mix_dict.items())