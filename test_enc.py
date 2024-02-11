from stegano import lsb
from stegano.lsb import generators
message = "Hello_word"
img = lsb.hide("car.png", message, generators.eratosthenes())
img.save("secret.png")

