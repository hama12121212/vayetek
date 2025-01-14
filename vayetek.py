import re

def calcul(document):
    try:
        with open(document, 'r') as fichier:
            somme = 0
            for ligne in fichier:
                ligne = ligne.strip()
                # Trouver tous les chiffres dans la ligne
                chiffres = re.findall(r'\d', ligne)
                
                if len(chiffres) == 0:
                    continue  # Passer les lignes sans chiffres
                elif len(chiffres) == 1:
                    # Si une seule chiffre, la valeur d'étalonnage est ce chiffre répété deux fois
                    valeur = int(chiffres[0] * 2)
                else:
                    # Former un nombre à deux chiffres avec le premier et le dernier chiffre
                    valeur = int(chiffres[0] + chiffres[-1])
                
                somme += valeur
            
            return somme
    except FileNotFoundError:
        print(f"Erreur : Le fichier '{document}' n'existe pas.")
        return None

# Exemple d'utilisation
if __name__ == "__main__":
    file = input("input document:")
    resultat = calcul(file)
    if resultat is not None:
        print(f"La somme des valeurs d'étalonnage est : {resultat}")


