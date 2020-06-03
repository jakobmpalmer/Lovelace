import matplotlib.pyplot as plt
import array

def almostPi(N):
    result = 0
    plt.figure()
    result_line = array.array("f",(0 for i in range(0,N)))
    result_line2 = array.array("f",(0 for i in range(0,N)))
    for i in range(N):
        i = i
        print(i, '. ', result)
        ith = 4 *(((-1)**i) / ((2 * i) + 1))
        print("Ith: ", ith)    
        result += ith
        result_line[i] = result
        plt.plot(range(N+1), result)
    print("Result: ", result)
    plt.plot(result_line)
    plt.title("Finding $\pi$")
    plt.xlabel("N")
    plt.xlim([0,N])

    plt.axhline(3.14159, linestyle="--", color="tab:orange", label="$\pi$")
    plt.legend()
    plt.show()

#almostPi(25)
almostPi(1000)
