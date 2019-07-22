puzzleInput = '''Step A must be finished before step I can begin.
Step M must be finished before step Q can begin.
Step B must be finished before step S can begin.
Step G must be finished before step N can begin.
Step Y must be finished before step R can begin.
Step E must be finished before step H can begin.
Step K must be finished before step L can begin.
Step H must be finished before step Z can begin.
Step C must be finished before step P can begin.
Step W must be finished before step U can begin.
Step V must be finished before step L can begin.
Step O must be finished before step N can begin.
Step U must be finished before step I can begin.
Step D must be finished before step P can begin.
Step Q must be finished before step L can begin.
Step F must be finished before step Z can begin.
Step L must be finished before step N can begin.
Step P must be finished before step S can begin.
Step I must be finished before step S can begin.
Step S must be finished before step R can begin.
Step T must be finished before step N can begin.
Step N must be finished before step X can begin.
Step Z must be finished before step J can begin.
Step R must be finished before step J can begin.
Step J must be finished before step X can begin.
Step E must be finished before step I can begin.
Step T must be finished before step R can begin.
Step I must be finished before step N can begin.
Step K must be finished before step C can begin.
Step B must be finished before step D can begin.
Step K must be finished before step T can begin.
Step E must be finished before step P can begin.
Step F must be finished before step I can begin.
Step O must be finished before step U can begin.
Step I must be finished before step J can begin.
Step S must be finished before step Z can begin.
Step L must be finished before step J can begin.
Step F must be finished before step T can begin.
Step F must be finished before step P can begin.
Step I must be finished before step T can begin.
Step G must be finished before step S can begin.
Step V must be finished before step U can begin.
Step F must be finished before step R can begin.
Step L must be finished before step R can begin.
Step Y must be finished before step D can begin.
Step M must be finished before step E can begin.
Step U must be finished before step L can begin.
Step C must be finished before step D can begin.
Step W must be finished before step N can begin.
Step S must be finished before step N can begin.
Step O must be finished before step S can begin.
Step B must be finished before step T can begin.
Step V must be finished before step T can begin.
Step S must be finished before step X can begin.
Step V must be finished before step P can begin.
Step F must be finished before step L can begin.
Step P must be finished before step R can begin.
Step D must be finished before step N can begin.
Step C must be finished before step L can begin.
Step O must be finished before step Q can begin.
Step N must be finished before step Z can begin.
Step Y must be finished before step L can begin.
Step B must be finished before step K can begin.
Step P must be finished before step Z can begin.
Step V must be finished before step Z can begin.
Step U must be finished before step J can begin.
Step Q must be finished before step S can begin.
Step H must be finished before step F can begin.
Step E must be finished before step O can begin.
Step D must be finished before step F can begin.
Step D must be finished before step X can begin.
Step L must be finished before step S can begin.
Step Z must be finished before step R can begin.
Step K must be finished before step X can begin.
Step M must be finished before step V can begin.
Step A must be finished before step M can begin.
Step B must be finished before step W can begin.
Step A must be finished before step P can begin.
Step W must be finished before step Q can begin.
Step R must be finished before step X can begin.
Step M must be finished before step H can begin.
Step F must be finished before step S can begin.
Step K must be finished before step Q can begin.
Step Y must be finished before step Q can begin.
Step W must be finished before step S can begin.
Step Q must be finished before step T can begin.
Step K must be finished before step H can begin.
Step K must be finished before step D can begin.
Step E must be finished before step T can begin.
Step Y must be finished before step E can begin.
Step A must be finished before step O can begin.
Step G must be finished before step E can begin.
Step C must be finished before step O can begin.
Step G must be finished before step H can begin.
Step Y must be finished before step I can begin.
Step V must be finished before step S can begin.
Step B must be finished before step R can begin.
Step B must be finished before step X can begin.
Step V must be finished before step I can begin.
Step N must be finished before step J can begin.
Step H must be finished before step I can begin.'''


from collections import defaultdict

def solveP1(x):
    steps = defaultdict(list)
    order = []
    workerCounter = []
    for line in x.split('\n'):
        _,prev,_,_,_,_,_,nxt,*_ = line.split(' ')          
        steps[nxt].append(prev)
        steps[prev]
    while steps.values():
        orderToDo = sorted(list(k for k,v in steps.items() if not v))
        if orderToDo:
            currentStep = orderToDo.pop(0)
            workerCounter.append([0,ord(currentStep)-64])
            order.append(currentStep)
            del steps[currentStep]
            for v in steps.values():
                if currentStep in v:
                    v.remove(currentStep) 
    return ''.join(order)
print(solveP1(puzzleInput))

def solveP2(x):
    steps = defaultdict(list)
    order = []
    counter = 0
    workerCounter = []
    for line in x.split('\n'):
        _,prev,_,_,_,_,_,nxt,*_ = line.split(' ')          
        steps[nxt].append(prev)
        steps[prev]
    while steps.values():
        orderToDo = sorted(list(k for k,v in steps.items() if not v and k not in [x[0] for x in workerCounter]))
        for _ in range(5 - len(workerCounter)):
            if orderToDo:
                currentStep = orderToDo.pop(0)
                workerCounter.append([currentStep,1,ord(currentStep)-4])
                order.append(currentStep)
        for cs,cv,v in workerCounter:
            if cv == v:
                del steps[cs]
                for values in steps.values():
                    if cs in values:
                        values.remove(cs)            
        workerCounter = [[cs,cv+1,v] for cs,cv,v in workerCounter if cv != v]
        counter += 1
    return (counter,''.join(order))
print(solveP2(puzzleInput))



