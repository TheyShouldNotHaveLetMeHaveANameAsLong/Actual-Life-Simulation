import random

beginnings = ["Tauro", "Fauna", "Tri", "Broti", "Dura", "Alte", "Do", "Bi", "Exo", "Endo", "Rituso", "Felta"]
endings = ["corpus", "taurus", "lephtus", "bek", "elta", "keti", "pea", "tum", "sum", "cretus", "tus", "cephtus"]

def gen_name():
  global beginnings, endings
  name = (random.choice(beginnings)+random.choice(endings))
  return name