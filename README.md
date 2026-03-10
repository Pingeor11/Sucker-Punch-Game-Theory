# The Optimal Strategy in the Sucker Punch Endgame

A small game theory project inspired by competitive Pokémon.

In Pokémon battles, the move **Sucker Punch** only works if the opponent uses an attacking move.  
This creates a classic bluffing situation:

- If you **attack**, you might get knocked out by Sucker Punch  
- If you **don’t attack**, you might waste the opponent’s limited PP  

So what is the **optimal strategy**?

This project models the late–game interaction between **Gholdengo** and **Kingambit** as a **zero-sum stochastic game** and solves it using **dynamic programming and mixed-strategy equilibrium**.

![Pokemon Battle]([https://upload.wikimedia.org/wikipedia/en/4/4c/Pokemon_Showdown.png](https://i.ytimg.com/vi/M2VI9FTzHQY/maxresdefault.jpg)
---

## The Result

If Kingambit has **k remaining Sucker Punch PP**, the optimal strategies are

Player attack probability

```
p_k = 1 / (k + 1)
```

Kingambit Sucker Punch probability

```
q_k = k / (k + 1)
```

Player win probability

```
V_k = 1 / (k + 1)
```

So from the full **8 PP**, the optimal-play win probability is

```
V_8 = 1 / 9
```

Interestingly, under optimal play the player is **equally likely to win on any possible attack turn**.

---

## Visualizing the Game

The expected payoff as a function of the mixed strategies `p` and `q`.

![Payoff Surface](payoff_surface.png)

The surface has a **saddle point**, which corresponds to the equilibrium mixed strategy.

---

## Simulation

To verify the theory, the game was simulated **100,000 times** with both players using the optimal strategies.

The simulated win rate was

```
0.11107
```

which closely matches the theoretical value

```
1 / 9 ≈ 0.11111
```

The turn on which the winning attack occurred is almost perfectly uniform:

| Turn | Wins |
|----|----|
|1|1220|
|2|1269|
|3|1244|
|4|1191|
|5|1214|
|6|1253|
|7|1254|
|8|1241|
|9|1221|

---

## Full Paper

You can read the full write-up here:

📄 **[Sucker Punch Game Theory Paper](Sucker_Punch_Kingambit.pdf)**

---

## Limitations

This model assumes both players follow the optimal mixed strategies.

In real battles, players rarely play perfectly optimally. Some may overuse Sucker Punch early, while others may be too hesitant to attack. The equilibrium therefore acts as a **benchmark for rational play**, rather than a literal description of every battle.

---

## Why this project?

Competitive games often hide elegant mathematical structures.  
This project shows how **game theory can explain strategy even in something as unexpected as Pokémon.**
