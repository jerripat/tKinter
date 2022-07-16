# This function creates a fibinocchi sequence


def fib():
    startInt = 0;
    newInt = 0;
    fibseq = 0;
    for i in range(100):
        startInt = (startInt + 1)
        newInt = (startInt + i)
        fibseq = (startInt + newInt)
        print(fibseq)
    


fib()
                    