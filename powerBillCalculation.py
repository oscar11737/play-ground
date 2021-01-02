'''
Created on Jan 2, 2021

@author: chango
'''

from datetime import date, timedelta
from _datetime import time
from _tracemalloc import stop

class PowerBill:
    def __init__(self, stop, start, total):
        self.periods = []
        _stop = [int(x) for x in stop.split("-")]
        _start = [int(x) for x in start.split("-")]
        self.days = date(_stop[0], _stop[1], _stop[2]) - date(_start[0],
                                       _start[1], _start[2]) + timedelta(1)
        self.total = total
    
    def addPeriod(self, *args):
        for i in args:
            self.periods.append(i)

    def checkDaySum(self):
        return self.billPeriod == sum(self.periods)
    
    def calcEachPeriod(self):
        self.bill = []
        for t in self.periods:
            self.bill.append(self.total*(t.days.days/self.days.days))
        return self.bill
    
    def calcEachGroup(self, periodNum):
        print("Between {} and {}".format(self.periods[periodNum].start, 
                                         self.periods[periodNum].stop))
        billPerPax = self.bill[periodNum]/self.periods[periodNum].peopleNum
        for i in self.periods[periodNum].groups:
            print("For {}, bill is {}".format(i, billPerPax*len(i)))
            
            

class TimePeriod:
    def __init__(self, peopleNum, stop, start):
        self.peopleNum = peopleNum
        self.stop = stop
        self.start = start
        _stop = [int(x) for x in stop.split("-")]
        _start = [int(x) for x in start.split("-")]
        self.days = date(_stop[0], _stop[1], _stop[2]) - date(_start[0],
                                       _start[1], _start[2]) + timedelta(1)
        self.groups = []
        
    def addGroups(self, *args):
        for i in args:
            self.groups.append(i)
    
if __name__ == "__main__":
    t0 = TimePeriod(3, "2020-12-13", "2020-11-27")
    t0.addGroups(["Oscar", "HuaYuan"], ["Pearl"])
    t1 = TimePeriod(4, "2020-12-24", "2020-12-14")
    t1.addGroups(["Oscar", "HuaYuan", "Isaac"], ["Pearl"])
    p = PowerBill("2020-12-24", "2020-11-27", 121.61)
    p.addPeriod(t0,t1)
    bill = p.calcEachPeriod()
    p.calcEachGroup(0)
    p.calcEachGroup(1)