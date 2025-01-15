result=(lambda x:2*(lambda x:3)(4)*x)(5)
#P1=2*(lambda x:3)(4)*5

bottles = 99
take = 1
	
def pass_it(around):
    bottles = 98
    return take
	
remaining = bottles - pass_it(bottles)
bottles = remaining


#(1):d Each time a user-defined function is called, a new frame is created in the environment diagram. 
# This frame represents the function's execution context, including its local variables and parameters.

#(2):a The return value of pass_it(bottles) (which is 1) is assigned to the variable remaining in the global frame.

#(3):c The line bottles = 98 is inside the function pass_it(around) and only affects the local bottles variable within the function's frame.
    # It does not affect the bottles variable in the global frame.

def double(x):
      return x * 2
	
def triple(x):
    return x * 3
	
hat = double

double = triple
#hat is the name of  double function
#double is the name of triple function


def team(work):
    return t(work) - 1
def dream(work, s):
    if work(s-2):
        t = not s
    return not t
work, t = 3, abs
team = dream(team, work + 1) and t
#the parameter of dream is a function and a constant

def make_keeper(n):
    """Returns a function that takes one parameter cond and prints
    out all integers 1..i..n where calling cond(i) returns True.

    >>> def is_even(x): # Even numbers have remainder 0 when divided by 2.
    ...     return x % 2 == 0
    >>> make_keeper(5)(is_even)
    2
    4
    >>> make_keeper(5)(lambda x: True)
    1
    2
    3
    4
    5
    >>> make_keeper(5)(lambda x: False)  # Nothing is printed
    """
   
    def cond(f): 
        i=1
        while i<=n:
            if f(i) == True:
                print(i)
            i+=1
        return None
    return cond


def find_digit(k):
    """Returns a function that returns the kth digit of x.

    >>> find_digit(2)(3456)
    5
    >>> find_digit(2)(5678)
    7
    >>> find_digit(1)(10)
    0
    >>> find_digit(4)(789)
    0
    """
    assert k > 0
    def digit(x):
        i=1
        while i<=k:
            a=x%10
            if i==k:
                return a
            x=x//10
    return digit


def match_k(k):
    """Returns a function that checks if digits k apart match.

    >>> match_k(2)(1010)
    True
    >>> match_k(2)(2010)
    False
    >>> match_k(1)(1010)
    False
    >>> match_k(1)(1)
    True
    >>> match_k(1)(2111111111111111)
    False
    >>> match_k(3)(123123)
    True
    >>> match_k(2)(123123)
    False
    """
    def check(x):
        while x // (10 ** k) > 0:
            if (x%10) !=(x//(10**k))%10:
                return False
            x = x // 10
        return True
    return check
