import random
from equilibrium_solver import solve_equilibrium;

def simulate_game(start_pp, attack_probs, sucker_probs):
    k = start_pp
    turn = 1
    while k>0:
        player_attacks = random.random() < attack_probs[k]
        kingambit_attacks = random.random() < sucker_probs[k]

        if player_attacks and kingambit_attacks:
            return ("lose", None)
        elif player_attacks and not kingambit_attacks:
            return ("win", turn)
        elif not player_attacks and not kingambit_attacks:
            return ("lose", None)
        else:
            k -= 1
            turn +=1
    return ("win", turn)

def run_simulation(start_pp, trials):
    values, attack_probs, sucker_probs = solve_equilibrium(start_pp)
    wins = 0
    attack_turn_counts = {}
    for i in range(trials):
        result, turn = simulate_game(start_pp, attack_probs, sucker_probs)

        if result == "win":
            wins += 1
            attack_turn_counts[turn] = attack_turn_counts.get(turn, 0) + 1
    win_rate = wins/trials
    theory_win_rate = values[start_pp]

    return win_rate, theory_win_rate, attack_turn_counts

    


    