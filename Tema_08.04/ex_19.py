"""
19. Joc ghicit zarul
Caută pe net și vezi cum se generează un număr random
Ne imaginăm ca dai cu zarul și salvăm acest număr în dice_roll
Ia numărul ghicit de la utilizator
Verifică și afișează dacă utilizatorul a ghicit
Vei avea 3 opțiuni
Ai pierdut. Ai ales un numar mai mic. Ai ales x dar a fost y.
Ai pierdut. Ai ales un numar mai mare. Ai ales x dar a fost y.
Ai ghicit. Felicitări! Ai ales x si zarul a fost y.

"""

import random
dice_roll = random.randint(0,20)
user_guess = int(input("Introdu un numar de la 0 la 20:\n"))
if user_guess < dice_roll and user_guess <= 20:
    print(f"Ai pierdut. Ai ales un numar mai mic. Ai ales {user_guess} dar a fost {dice_roll}.")
elif user_guess > dice_roll and user_guess <= 20:
    print(f"Ai pierdut. Ai ales un numar mai mare. Ai ales {user_guess} dar a fost {dice_roll}.")
elif user_guess == dice_roll:
    print(f"Ai ghicit. Felicitări! Ai ales {user_guess} si zarul a fost {dice_roll}")
# elif user_guess > 20:
else:
    print(f"Numarul {user_guess} nu este valid.")
