import turtle
# Creare una tartaruga
tartaruga = turtle.Turtle()

# Disegnare un quadrato
for _ in range(4):
    tartaruga.forward(100)  # Sposta in avanti di 100 unità
    tartaruga.left(90)      # Gira a sinistra di 90 gradi

# Chiudi la finestra al clic
turtle.exitonclick()
