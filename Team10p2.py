import random

def exploitOnly():
    return 2000

def exploreOnly():
    return 3000

def eGreedy(e:int):
    return 2500

def simulation(t: int, e: int):
    oitind = 0
    Optimum_h = 300 * 21
    print("Optimum Happiness is " + str(Optimum_h))
    exploit = []
    exploit_tot = 0
    oit = exploitOnly()
    while oitind < t- 1:
        o = exploitOnly()
        exploit.append(o)
        oitind += 1
    for item in range(0, len(exploit)):
        exploit_tot = exploit_tot + exploit[item]
    avg_exploit = exploit_tot / len(exploit)
    exploit_reg = Optimum_h - oit
    avg_exploitr = Optimum_h - avg_exploit
    print("The average total happiness for exploitOnly for " + str(t) + " trials is " + str(avg_exploit))
    print("The total expected happiness for exploitOnly is " + str(oit))
    print("The total expected regret for exploitOnly is " + str(exploit_reg))
    print("The average total regret for exploitOnly for " + str(t) + " trials is " + str(avg_exploitr))
    oreind = 0
    explore = []
    explore_tot = 0
    ore = exploreOnly()
    while oreind < t - 1:
        o = exploreOnly()
        explore.append(o)
        oreind += 1
    for item in range(0, len(explore)):
        explore_tot = explore_tot + explore[item]
    avg_explore = explore_tot / len(explore)
    explore_reg = Optimum_h - ore
    avg_explorer = Optimum_h - avg_explore
    print("The average total happiness for exploreOnly for " + str(t) + " trials is " + str(avg_explore))
    print("The total expected happiness for exploreOnly is " + str(ore))
    print("The total expected regret for exploreOnly is " + str(explore_reg))
    print("The average total regret for exploreOnly for " + str(t) + " trials is " + str(avg_explorer))
    eedind = 0
    greed = []
    greed_tot = 0
    eed = eGreedy(e)
    while eedind < t - 1:
        o = eGreedy(e)
        greed.append(o)
        eedind += 1
    for item in range(0, len(greed)):
        greed_tot = greed_tot + greed[item]
    avg_greed = greed_tot / len(greed)
    greed_reg = Optimum_h - eed
    avg_greedr = Optimum_h - avg_greed
    print("The average total happiness for eGreedy for " + str(t) + " trials is " + str(avg_greed))
    print("The total expected happiness for eGreedy is " + str(eed))
    print("The total expected regret for eGreedy is " + str(greed_reg))
    print("The average total regret for eGreedy for " + str(t) + " trials is " + str(avg_greedr))
print(simulation(1000000, 10))
