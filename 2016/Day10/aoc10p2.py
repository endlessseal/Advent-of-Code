class Robit():
    def __init__(self, name, giff_low = None, giff_high = None):
        self.name = name
        self.holding = []
        self.giff_low = giff_low
        self.giff_high = giff_high
        
    def giff(self):
        if len(self.holding) == 2:
            low_value, high_value = self.holding
            if self.giff_low:
                self.giff_low.recv(low_value)
            if self.giff_high:
                self.giff_high.recv(high_value)
            self.holding = []

    def recv(self,value):
        self.holding.append(int(value))
        self.holding.sort()
        if self.giff_low and self.giff_high:
            if len(self.holding) == 2:
                self.giff()

class Output():
    def __init__(self,name):
        self.name = name
        self.values = []
        
    def recv(self,value):
        self.values.append(int(value))
    

robits = {}
outputs = {}
instructions = []
is_bot = {'output': False, 'bot':True}

with open('aoc10.txt','r') as fp:
    for each_line in fp.read().splitlines():
        each_in = each_line.split()
        
        if each_in[0] == 'value':
            _, value, _, _, _, robit_id = each_in
            robit = robits.setdefault(robit_id, Robit(robit_id))
            robit.recv(value)
            
        elif each_in[0] == 'bot':
            _, giver_bot, _, _, _, low_type, low_value_recv_id, _, _, _, high_type, high_value_recv_id = each_in
            
            if is_bot[low_type]:
                low_recv = robits.setdefault(low_value_recv_id, Robit(low_value_recv_id))
            else:
                low_recv = outputs.setdefault(low_value_recv_id, Output(low_value_recv_id))
                
            if is_bot[high_type]:
                high_recv = robits.setdefault(high_value_recv_id, Robit(high_value_recv_id))
            else:
                high_recv = outputs.setdefault(high_value_recv_id, Output(high_value_recv_id))
            giver_robit = robits.setdefault(giver_bot, Robit(giver_bot))
            
            giver_robit.giff_low = low_recv
            giver_robit.giff_high = high_recv
            did_it = giver_robit.giff()

from functools import reduce
from operator import mul

print(reduce(mul,outputs['0'].values + outputs['1'].values + outputs['2'].values))
