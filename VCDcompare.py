"""
Description: 
Author: Nicolas Gaudin
Date Created: March 19, 2024
Date Modified: April 02, 2024
Version: 1.0
Python Version: 3.10.12
Dependencies: time, sys
License: GPL-3.0 License
"""


#utilization
# 2 vcd files with same signals
# it compares consequently traces of aimed signals
# signals to be compared are declared in the variable "signals"
# if you want to analyze a signal from a bloc that is declared multiples times, only the first declared will be analyzed
# cannot compare 1-bit signal


import time, sys

start_time = time.time_ns()

old_stdout = sys.stdout
log_file = open("message.log","w")
sys.stdout = log_file


def searchOccurence(file, signal) -> int:
    F = []
    vcdtime = 0
    invcd1 = 'ffffffffffffffffff' #impossible value 

    is_in = 1
    header = 1

    # printTab(file)
    with open(file, 'r') as fvcd:
        for vcd in fvcd:
            # retrieve trigger start and stop
            if header == 0:
                if vcd.find('#',0,1) != -1:
                    vcdtime = vcd.replace("#",'')
                    vcdtime = vcdtime.replace("\n",'')
                if ((vcd.find(invcd1) != -1) and (vcd.find('b',0,1) != -1)):
                    listt = []
                    listt.append(vcdtime)
                    listt.append(vcd.replace(invcd1,'').replace(" \n",''))
                    F.append(listt)
            if vcd.find('#0',0,2) != -1:
                # print(Fore.RED + "debug")
                # print(Style.RESET_ALL)
                header = 0
            if(is_in == 1) :
                if vcd.find(signal) != -1:
                    # print(vcd)
                    test = vcd.split(' ')
                    test = list(filter(None, test))
                    # print(test)
                    if (len(test) >= 5 ):
                        if((test[4] == signal) and (len(signal) == len(test[4]))):
                            invcd1 = test[3]
                            is_in = 0
                            # printTab(invcd1)
    return F

def searchDiff(f1, f2, signals) -> int:

    for signal in signals:
        F1 = searchOccurence(f1, signal)
        F2 = searchOccurence(f2, signal)
        # print(F1)
        # print(F2)

        # print(len(F1))
        # print(len(F2))

        i = 0 
        for val1,val2 in zip(F1,F2):
            if((val1[1] != val2[1]) and i<10000) :
                if(i==0):
                    print(signal)
                    printTab(len(F1))
                    printTab(len(F2))
                time1=val1[0]
                time2=val2[0]
                bin1 = val1[1].replace('b','')
                # print(str(hex(int(bin1,2))))
                bin2 = val2[1].replace('b','')
                print(str(F1.index(val1)+1)+"\t@"+time1+" : 0x"+str(format(int(bin1,2), '08x'))+" != @"+time2+" : 0x"+str(format(int(bin2,2), '08x')))
                i+=1
        if(i !=0):
            print("\n")
    return

def printTab(*args):
    args = ("\t",)+args
    print(*args)

# signals = ["sp"]
signals = ["ra","sp","gp","tp","t0","t1","t2","s0","s1","a0","a1","a2","a3","a4","a5","a6","a7","s2","s3","s4","s5","s6","s7","s8","s9","s10","s11","t3","t4","t5","t6"]

vcdF1 = "good.vcd"
vcdF2 = "bad.vcd"

searchDiff(vcdF1, vcdF2, signals)

sys.stdout = old_stdout
log_file.close()


end_time = ((time.time_ns() - start_time)) / 1000000
print("--- %s ms ---" % end_time)

