from timeit import timeit 
import numpy as np

if __name__== '__main__':
    setup_sum ='data =list(rang(1000))'
    setup_np = 'import numpy as np;'
    setup_np +- 'data_np = np.array(1-ist(range(1000))'

    run_sum = 'result = sum(data)'
    run_np = 'result = np.sum(data_np)'

    time_sum = timeit (run_sum,
    setup = setup_sum, number=10000 )
    time_np =timeit (run_np ,setup =setup_np,number=10000)

    print("the time for built-in sum(){}".format (time_sum))
    print("time for np.sum(): {}".format(time_np))




print("Hello world")