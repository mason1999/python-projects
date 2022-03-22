# a tuple stores elements which you can't change
tup = ([1], [2], [3]) # this just stores references...!

tup[0].append(3) # so we're not really changing anything when we do this. 

print(tup)

def increment(n):
    return n+1

def square(n):
    return n*n

# Example 1: 
def find_sequence(initial,goal):
    """Reports back the shortest sequence of increment and square that gives goal starting initial
    
    
    Parameters
    ----------
    initial: int
    goal:    int
    
    """
    
    # Make a list of tuples, each containing (string, int)
    candidates = [(str(initial),initial)]   
    
    # Loop over all the integers between your start and your goal.
    for i in range(1,goal-initial+1):
        
        # An empty list
        new_candidates = []
        
        # Go through each tuple in candidates,
        # For each tuple, 
        # put the string into a variable called 'action'
        # put the integer into a variable called 'result'
        for (action,result) in candidates:
            
            # a = either of the strings  : ' increment' or ' square'
            # r = either of the functions: increment' or square
            # Remember the functions are in our enviroment (aka namespace), so we can use them.
            # If we had more functions to try (eg, cube), we could put them in the list here.
            for (a,r) in [(' increment',increment),(' square',square)]:
                
                # put a new tuple on the back of the new_candidates list
                # The string 'adds' the word of the function to the list of words
                # The integer is the current function applied to the previous result.
                new_candidates.append((action+a,r(result)))
                
                # Show how we are doing so far.
                print(i,': ', new_candidates[-1])
                
                # Check if the latest is the right answer
                if new_candidates[-1][1] == goal:
                    
                    # report back the asnwer
                    return new_candidates[-1]
        
        # otherwise the list of candidates becomse where we are now. 
        candidates = new_candidates

print(find_sequence.__name__)
