def race(x, y):
    """The tortoise always walks x feet per minute, while the hare repeatedly
    runs y feet per minute for 5 minutes, then rests for 5 minutes. Return how
    many minutes pass until the tortoise first catches up to the hare.

    >>> race(5, 7)  # After 7 minutes, both have gone 35 steps
    7
    >>> race(2, 4) # After 10 minutes, both have gone 20 steps
    10
    """
    assert y > x and y <= 2 * x, 'the hare must be fast but not too fast'
    tortoise, hare, minutes = 0, 0, 0
    while minutes == 0 or (tortoise - hare)!=0:
        tortoise += x
        if minutes % 10 < 5:
            hare += y
        minutes += 1
        print(tortoise,hare,minutes)
    return minutes
#Two bugs:

    1.0
    #The value of race(x, y) is incorrect when it is not the first time the tortoise passes the hare.
    #The return value is incorrect when the time that the tortoise first passes the hare is not an integer number of minutes .
    # (e.g., for race(2, 3) the tortoise passes the hare after 7.5 minutes), but there is some (larger) integer number of minutes after which both animals have gone the same distance.

    2.0
    #you can find a case where tortoise has become larger than hare, but the expression tortoise - hare was not zero when it happened.  
    #The race function will run forever if the only times that the tortoise and hare have gone the same distance are not integers 
    # (e.g., for race(4, 5) the tortoise passes the hare after 6.2 minutes, and the hare never catches up).


def fizzbuzz(n):
    """
    >>> result = fizzbuzz(16)
    1
    2
    fizz
    4
    buzz
    fizz
    7
    8
    fizz
    buzz
    11
    fizz
    13
    14
    fizzbuzz
    16
    >>> print(result)
    None
    """
    i=1
    while i<=n:
        if i%3==0 and i%5==0:
            print("fizzbuzz")
        elif i%3==0 and i%5!=0:
            print("fizz")
        elif i%3!=0 and i%5==0:
            print("buzz")
        else :
            print(i)
        i=i+1
#fizzbuzz(50)

def is_prime(n):
    """
    >>> is_prime(10)
    False
    >>> is_prime(7)
    True
    >>> is_prime(1) # one is not a prime number!!
    False
    """
    if n==1:
        return False
    if n==2 :
        return True
    k=2
    while k<n:
        if n%k==0:
            return False
        k=k+1
    return True

#print(is_prime(120))

def unique_digits(n):
    """Return the number of unique digits in positive integer n.

    >>> unique_digits(8675309) # All are unique
    7
    >>> unique_digits(13173131) # 1, 3, and 7
    3
    >>> unique_digits(101) # 0 and 1
    2
    """
    k=0
    num=0
    while k>=0 and k<10:
        if has_digit(n,k)==True:
            num=num+1
            #print(k)
        k=k+1
    return num

def has_digit(n, k):
    """Returns whether k is a digit in n.

    >>> has_digit(10, 1)
    True
    >>> has_digit(12, 7)
    False
    """
    assert k >= 0 and k < 10
    while n>=1:
        if(n-(n//10)*10==k):
            return True
        n=n//10
    return False


#print(has_digit(105649,6))
#print(unique_digits(54681615))

def ordered_digits(x):
    """Return True if the (base 10) digits of X>0 are in non-decreasing
    order, and False otherwise.

    >>> ordered_digits(5)
    True
    >>> ordered_digits(11)
    True
    >>> ordered_digits(127)
    True
    >>> ordered_digits(1357)
    True
    >>> ordered_digits(21)
    False
    >>> result = ordered_digits(1375) # Return, don't print
    >>> result
    False

    """
    while x>1:
        k=x%10
        x=x//10
        q=x%10
        print(f"last={k},front={q}")
        if k<q:
            return False
        x=x//10
    return True
print(ordered_digits(268798545648952131))