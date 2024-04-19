#!/usr/bin/env python3

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

# Utilization
# 2 vcd files with same signals
# it compares consequently traces of aimed signals
# signals to be compared are declared in the variable "signals"
# if you want to analyze a signal from a bloc that is declared multiples times, only the first declared will be analyzed
# cannot compare 1-bit signal

import time, sys
import argparse

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
                header = 0
            if(is_in == 1) :
                if vcd.find(signal) != -1:
                    test = vcd.split(' ')
                    test = list(filter(None, test))
                    if (len(test) >= 5 ):
                        if((test[4] == signal) and (len(signal) == len(test[4]))):
                            invcd1 = test[3]
                            is_in = 0
    return F

def searchDiff(f1, f2, signals) -> int:

    for signal in signals:
        F1 = searchOccurence(f1, signal)
        F2 = searchOccurence(f2, signal)

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

def main():

    parser = argparse.ArgumentParser(description='VCDcompare - a tool to support when modifying an HDL module ')

    parser.add_argument('-f1', '--file1', type=str, required=True, help='First VCD file path')
    parser.add_argument('-f2', '--file2', type=str, required=True, help='Second VCD file path')
    parser.add_argument('-l', '--log', type=str, required=True, help='Log file path')
    parser.add_argument('-s', '--signals', nargs='+', type=str, required=True, help='List of signals (Example : "-s ra sp")')
    
    args = parser.parse_args()

    signals = args.signals
    print(args.signals)

    vcdF1 = args.file1
    vcdF2 = args.file2

    start_time = time.time_ns()

    old_stdout = sys.stdout
    log_file = open(args.log, "w")
    sys.stdout = log_file

    searchDiff(vcdF1, vcdF2, signals)

    sys.stdout = old_stdout
    log_file.close()


    end_time = ((time.time_ns() - start_time)) / 1000000
    print("--- %s ms ---" % end_time)

if __name__ == "__main__":
    main()