#!/usr/bin/env python3

import sys
import os

S=sys.argv
i1=S[-2]
i2=S[-1]

#sys.argv enables to recover the arguments called in the command

commands=['-d','-c','-D','-L','-l','-B']

#help block indicting the actions the user can do

if len(S)==1 or "help" in S:

    print("")
    print("netem1.0.py Options, version 1.0 - sept2022" + "<br>")
    print("----------------------------------------------------------" + "<br>")
    print("please indicate the settings you want to change" + "<br>")
    print("off      = clear all netem profiles" + "<br>")
    print("show     = show active profiles" + "<br>")
    print("itu      = enable itu spec link profile" + "<br>")
    print("-i       = show interface name" + "<br>")
    print("-d       = change delay and jitter (ms-ms)" + "<br>")
    print("-c       = change corruption (%)" + "<br>")
    print("-D       = change duplication (%)" + "<br>")
    print("-L       = change loss (%)" + "<br>")
    print("-l       = change limit" + "<br>")
    print("-r       = change reorder (%)" + "<br>")
    print("-B       = change bandwidth/burst/latency settings (m/k/bit-m/k/bit-ms)" + "<br>")
    print("")
    quit()

#off command block

#os.system enables to apply sudo commands, taskes string arguments

elif "off" in S:
    print("")
    print("Netem tc profile off <br>")
    print("")
    print("sudo tc qdisc replace dev " + i1 + " root netem <br>")
    print("sudo tc qdisc del dev " + i1 + " root netem <br>")
    print("sudo tc qdisc replace dev " + i2 + " root netem <br>")
    print("sudo tc qdisc del dev " + i2 + " root netem <br>")
    quit()

#show command block

elif "show" in S:
    print("")
    print("Show netem tc profile" + "<br>")
    print("")
    print("sudo tc qdisc show dev " + i1 + "<br>")
    print("sudo tc qdisc show dev " + i2 + "<br>")
    quit()

#itu command block

elif "itu" in S:
    print("")
    print("Applying ITU G114, Y1540/1541 ans G113 limit values" + "<br>")
    print("")
    print("sudo tc qdisc replace dev " + i1 + " root netem" + "<br>")
    quit()

elif "-i" in S:
    print("")
    print("Show netem tc interface name" + "<br>")
    print("")
    print("ip addr" + "<br>")
    quit()

else :

    #case where bandwidth setting are not the only settings that needs to be changed, in that case the bandwidth changes are being applied to one interface of the bridge and the other settings are being put on the other

    command1="sudo tc qdisc replace dev " + i1 + " root netem "
    command2=""

    if "-d" in S:
        c=S.index('-d')
        command1=command1+(" delay " + S[c+1]+ " " + S[c+2])

    if "-c" in S:
        c=S.index('-c')
        command1=command1+(" corrupt " + S[c+1])

    if "-D" in S:
        c=S.index('-D')
        command1=command1+(" duplicate " + S[c+1])


    if "-L" in S:
        c=S.index('-L')
        command1=command1+(" loss " + S[c+1])

    if "-l" in S:
        c=S.index('-l')
        command1=command1+(" limit " + S[c+1])

    if "-r" in S:
        c=S.index('-r')
        command1=command1+(" reorder " + S[c+1])

    if "-B" in S:
        c=S.index('-B')
        command2="sudo tc qdisc replace dev " + i2 + " root tbf rate "+S[c+1]+" burst "+S[c+2]+" latency "+S[c+3]

    print(command1 + "<br>" + command2)

#try: / except ValueError fonction tests if the command selected by the user makes sense, in that case it executes the command and eventually shows the interface name, in the other case it indicts the command is wrong and suggests to use help function
#tries test the two command applied to the two different interface