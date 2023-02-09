"""Run a Python script from the Terminal by passing it to the Interpreter.

Copyright (c) 2018-2021 Cisco and/or its affiliates.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

# print("Hello Python!!  ...at least I didn't say World.")
# print("Today I will learn something new.\nTomorrow I will learn some more.")

# "duplex {}".format("full")
# "interface {name}, port {port}".format(name="gigabitethernet", port="0/1")
headers1 = "device hostname ipaddress".split(" ")
headers2 = ",".join(headers1)
print(headers1,"\n",headers2)

# formatted literal strings
tool = "git clone "
host = "https://github.com/"
org = "CiscoDevNet"
repo = "/netprog_basics"
command = f"{tool}{host}{org}{repo}"
print(command)

# inputs
# num1 = int(input("What is the first number "))
# num2 = int(input("What is the second number "))
num1,num2 = 2, 4

# functions
def add(num1, num2):
     result = num1 + num2
     return result

print(add(num1, num2))

# data types()
# lists
lookup = ["ssh", "tcp", "ftp", 19.2, 20.1]
lookup[2] = "udp"
print(lookup[2])
print(lookup.append("ftp"))
print(lookup)

# tuples
territory = ("FillmoreDC", "NorthWestRegion")
print(territory[0])

# dictionaries
devicehost = {"ipv4address": "192.168.0.10", "traffic": "inbound", "port": 40044}
print(devicehost["traffic"])
devicehost["ipv4address"] = "192.168.0.111"
devicehost["alert"] = "Never"
print(devicehost)
# print(dir(devicehost)) # shows methods => in a list

# COLLECTIONS MODULES
# example 1
from collections import OrderedDict
metric_l = dict()
metric_l["finance"] = 95
metric_l["health"]= 25
metric_l["comms"] =  55
metrics = OrderedDict()
metrics["finance"] = 95
metrics["health"] = 25
metrics["comms"] = 55
print(metrics)
print("metrics_l", metric_l)
metrics["alocal"] = 5
print(metrics)

# loops
for industry, head in metrics.items():
    print("industry:= {ind}, head count:= {pax}".format(ind=industry, pax=head))