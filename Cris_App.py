import random

# Exemple d'objet Python avec quelques animaux et leurs cris en français
cris_animal = [
 {"animal": "Chien", "cri": "Aboyer"},
    {"animal": "Chat", "cri": "Miauler"},
    {"animal": "Vache", "cri": "Meugler"},
    {"animal": "Mouton", "cri": "Bêler"},
    {"animal": "Cheval", "cri": "Hennir"},
    {"animal": "Cochon", "cri": "Grogner"},
    {"animal": "Canard", "cri": "Cancaner"},
    {"animal": "Poule", "cri": "Caqueter"},
    {"animal": "Lion", "cri": "Rugir"},
    {"animal": "Chaton", "cri": "Ronronner"},
    {"animal": "Dauphin", "cri": "Siffler"},
    {"animal": "Tigre", "cri": "Rugir"},
    {"animal": "Oiseau", "cri": "Chanter"},
    {"animal": "Elephant", "cri": "Barrir"},
    {"animal": "Serpent", "cri": "Siffler"},
    {"animal": "Vache", "cri": "Beugler"},
    {"animal": "Loup", "cri": "Hurler"},
    {"animal": "Aigle", "cri": "Screecher"},
    {"animal": "Panda", "cri": "Grogner"},
    {"animal": "Grenouille", "cri": "Coasser"},
    {"animal": "Crapaud", "cri": "Coasser"},
    {"animal": "Zèbre", "cri": "Hennir"},
    {"animal": "Giraffe", "cri": "Bêler"},
    {"animal": "Kangourou", "cri": "Crier"},
    {"animal": "Koala", "cri": "Grogner"},
    {"animal": "Cheetah", "cri": "Rugir"},
    {"animal": "Poule d'eau", "cri": "Cancaner"},
    {"animal": "Dromadaire", "cri": "Grogner"},
    {"animal": "Gorille", "cri": "Bourdonner"},
    {"animal": "Loutre", "cri": "Crier"},
    {"animal": "Ours", "cri": "Grogner"},
    {"animal": "Hérisson", "cri": "Grogner"},
    {"animal": "Rhinocéros", "cri": "Grogner"},
    {"animal": "Abeille", "cri": "Bourdonnement"},
    {"animal": "Mouette", "cri": "Cri"},
    {"animal": "Pélican", "cri": "Cri"},
    {"animal": "Cygne", "cri": "Siffler"},
    {"animal": "Panda géant", "cri": "Bourdonner"},
    {"animal": "Perroquet", "cri": "Crier"},
    {"animal": "Autruche", "cri": "Grogner"},
    {"animal": "Phoque", "cri": "Cri"},
    {"animal": "Papillon", "cri": "Aucun"},
    {"animal": "Chauve-souris", "cri": "Cri"},
    {"animal": "Lynx", "cri": "Rugir"},
    {"animal": "Faucon", "cri": "Cri"},
    {"animal": "Tortue", "cri": "Aucun"},
    {"animal": "Serpent boa", "cri": "Siffler"},
    {"animal": "Dragon", "cri": "Rugir"},
    {"animal": "Lama", "cri": "Grogner"},
    {"animal": "Iguane", "cri": "Aucun"},
    {"animal": "Dindon", "cri": "Glousser"},
    {"animal": "Dauphin", "cri": "Siffler"},
    {"animal": "Raton laveur", "cri": "Gratter"},
    {"animal": "Fennec", "cri": "Cri aigu"},
    {"animal": "Chinchilla", "cri": "Aucun"},
    {"animal": "Ratel", "cri": "Cri"},
    {"animal": "Aigle royal", "cri": "Cri perçant"},
    {"animal": "Marmotte", "cri": "Siffler"},
    {"animal": "Papillon de nuit", "cri": "Aucun"},
    {"animal": "Poisson", "cri": "Aucun"},
    {"animal": "Loup de mer", "cri": "Hurler"}
]
def quiz_crisA(cris_animal):
  random.shuffle(cris_animal)
  score = 0
  
  for crisA in cris_animal:
    print(f"Quel est le cris de cet animal:'{crisA['animal']}' ?")
    reponse = input("Votre réponse:").strip().lower()
    correction = crisA['cri'].lower()

    if reponse == correction:
      print("Correct!!")
      score += 1
    r
    else:
      print(f"Faux!! la bonne reponse est :'{crisA['cri']}'.\n")
  
  print(f"Fin!! ton score est:{score}/len{cris_animal}")

def main():

  print("Bienvenu sur l'application")
  input("touchez start pour commencer....")
  quiz_crisA(cris_animal)

if __name__ == "__main__":
   main()
