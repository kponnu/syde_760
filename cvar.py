"""
Given the objective function maximize: f(x)=∑(t=1:3){2u_t+s_t}
subject to usual conservation constraints for all time periods t=1, 2, and 3.

Means of inflows in three periods are 6, 9, and 7 units and

storage is bounded between 0 and 6.

Assume inflows as i.i.d as normal with coefficient of variations of 0.5 or 1.

Calculate a frontier of means and std. deviations for the two cases from optimization

    and compare it with

        results from Monte-Carlo simulation.

Discuss and infer especially regarding the method.

Your method is simulation-optimization and the minimum number of scenarios expected is 1000.

"""

"""
for each alpha,
    obtaine the optimum DV.
    mean, std = For that DV, obtain mean and std of objectivefunction
    plot mean, std
    
    
"""

import numpy as np
from scipy.optimize import minimize


def cvar_obj(u):
    inflows = np.array(
        [np.random.normal(6, 6 * cv, N), np.random.normal(9, 9 * cv, N), np.random.normal(7, 7 * cv, N)]).T
    f = []
    for I in inflows:
        S = [2, 0, 0, 0]
        S = [S[0],
             S[0] + I[0] - u[0],  # S[1]
             S[1] + I[1] - u[1],  # S[2]
             S[2] + I[2] - u[2],  # S[3]
             ]

        f.append(2 * (u[0] + u[1] + u[2]) + (S[1] + S[2] + S[3]))
    f.sort()

    min_f = min(f)
    max_f = max(f)

    var_a = 0

    for i in np.arange(min_f, max_f, 0.001):
        if (i - min_f) / (max_f - min_f) > alfa:
            var_a = i
            break

    cvar_a = np.mean([x for x in f if x <= var_a])

    # return var_a, cvar_a, f
    return cvar_a



if __name__ == '__main__':
    N = 1000
    cv = 0.5
    alfa = 0.1
    budget = 1000
    # cvar_a = cvar_obj([2, 2, 2] , alfa, cv, N)

    initial_solution = np.array([3, 3, 3])

    # ans = NelderMeadSimplexSearch.minimize(cvar_obj, initial_solution, max_iterations=budget)

    # And variables must be positive, hence the following bounds:
    bnds = ((0, 6), (0, 6), (0, 6))

    ans2 = minimize(cvar_obj, initial_solution, method='L-BFGS-B', bounds=bnds,
                    options={'maxiter': budget, 'disp': True})

    print(ans2)
    # print("alfa=%6.3f,   var_a=%6.3f,   cvar_a=%6.3f" % (alfa, var_a, cvar_a, ))

    """
    >>> cons = ({'type': 'ineq', 'fun': lambda x:  x[0] - 2 * x[1] + 2},
    ...         {'type': 'ineq', 'fun': lambda x: -x[0] - 2 * x[1] + 6},
    ...         {'type': 'ineq', 'fun': lambda x: -x[0] + 2 * x[1] + 2})


    The optimization problem is solved using the SLSQP method as:

    >>> res = minimize(fun, (2, 0), method='SLSQP', bounds=bnds,
    ...                constraints=cons)

    It should converge to the theoretical solution (1.4 ,1.7).





    fig = plt.figure()
    fig.suptitle('bold figure suptitle', fontsize=14, fontweight='bold')

    ax = fig.add_subplot(111)
    fig.subplots_adjust(top=0.85)
    ax.set_title('axes title')

    ax.set_xlabel('Z')
    ax.set_ylabel('Frequency')

    # ax.text(3, 8, 'boxed italics text in data coords', style='italic',
    #         bbox={'facecolor':'red', 'alpha':0.5, 'pad':10})

    ax.text(var_a, -12, r'$VaR_a$', fontsize=10)
    ax.text(cvar_a-4, -12, r'$CVaR_a$', fontsize=10)



    plt.hist(f)
    plt.scatter([var_a, cvar_a], [0, 0], c='r')

    # plt.xlabel("")
    # plt.ylabel("")
    plt.show()
    """
