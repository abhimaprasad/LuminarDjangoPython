from collections import defaultdict
from functools import cmp_to_key

# ip_list= ['192.168.10.9', '192.168.10.4', '192.168.10.11', '192.168.10.35']

ip_list= ['192.168.10.9']

# for ip in sorted(ip_list, key = lambda ip: ( int(ip.split(".")[0])), (int(ip.split(".")[1])) ):
#     print(ip)

for ip in sorted(ip_list, key = lambda ip: \
                                    ( int(ip.split(".")[0],
                                    int(ip.split(".")[1]),
                                    int(ip.split(".")[2]),
                                    int(ip.split(".")[3])))):
    print(ip)

#
# def sorted_ip_list(ip_list, unique=False):
#     if unique:
#         ip_list = list(set(ip_list))
#         return sorted(ip_list, key=lambda ip: (
#         int(ip.split(".")[0]),
#         int(ip.split(".")[1]),
#         int(ip.split(".")[2]),
#         int(ip.split(".")[3].split(':')[0]),
#         int(ip.split(":")[1]) if ":" in ip else 0))
# print(ip_list)