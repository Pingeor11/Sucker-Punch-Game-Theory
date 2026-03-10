def solve_equilibrium(max_pp):
    values = [0.0] * (max_pp+1)
    attack_probs = [0.0] * (max_pp +1)
    sucker_probs = [0.0] * (max_pp+1)
    values[0] = 1.0
    attack_probs[0] = 1.0
    sucker_probs[0] = 0

    for i in range (1, max_pp+1):
        values[i] = values[i-1]/(1+values[i-1])
        attack_probs[i] = values[i-1]/(1+values[i-1])
        sucker_probs[i] = 1/(1+values[i-1])

    return values, attack_probs, sucker_probs

