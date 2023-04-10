

def f2(tt):
    # now 3 references to 'Hey'
    print(tt)
    # once the function returns it will be 2 references
        # name tt scope is ended, but 'Hey' in memory



def f1():
    s1 = 'Hey'      # 1 reference to value 'Hey'
    s2 = s1         # 2 references to 'Hey'
    f2(s2)
    del s2          # remove the bind to 'Hey'
                    # now 1 reference to 'Hey'
    #print(s2)      UnboundLocalError

f1()
# now 'Hey' has ZERO references
