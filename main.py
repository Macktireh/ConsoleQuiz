from typing import List, Tuple


def print_correct(text: str) -> None:
    print("\033[92m✔ " + text + "\033[0m")


def print_incorrect(text: str) -> None:
    print("\033[91m❌ " + text + "\033[0m")

def print_information(text: str) -> None:
    print("\033[94mℹ️ " + text + "\033[0m")


class Question:
    def __init__(self, titre: str, choix: Tuple[str], bonne_reponse: str) -> None:
        self.titre = titre
        self.choix = choix
        self.bonne_reponse = bonne_reponse

    def FromData(data) -> "Question":
        # ....
        q = Question(data[2], data[0], data[1])
        return q

    def poser(self) -> bool:
        print("QUESTION")
        print("  " + self.titre)
        for i, value in enumerate(self.choix):
            print("  ", i + 1, "-", value)

        print()
        resultat_response_correcte = False
        reponse_int = Question.demander_reponse_numerique_utlisateur(1, len(self.choix))
        if self.choix[reponse_int - 1].lower() == self.bonne_reponse.lower():
            print_correct("Bonne réponse")
            resultat_response_correcte = True
        else:
            print_incorrect("Mauvaise réponse")

        print()
        return resultat_response_correcte

    def demander_reponse_numerique_utlisateur(min: int, max: int) -> int:
        reponse_str = input(
            "Votre réponse (entre " + str(min) + " et " + str(max) + ") :"
        )
        try:
            reponse_int = int(reponse_str)
            if min <= reponse_int <= max:
                return reponse_int

            print("ERREUR : Vous devez rentrer un nombre entre", min, "et", max)
        except ValueError:
            print("ERREUR : Veuillez rentrer uniquement des chiffres")
        return Question.demander_reponse_numerique_utlisateur(min, max)


class Questionnaire:
    def __init__(self, questions: List[Question]) -> None:
        self.questions = questions

    def lancer(self) -> int:
        score = 0
        for question in self.questions:
            if question.poser():
                score += 1
        print_information(f"Score final : {score} sur {len(self.questions)}")
        print("Fin du questionnaire !")
        print()
        return score


questions = [
    (
        "Quelle est la capitale de la France ?",
        ("Marseille", "Nice", "Paris", "Nantes", "Lille"),
        "Paris",
    ),
    (
        "Quelle est la capitale de l'Italie ?",
        ("Rome", "Venise", "Pise", "Florence"),
        "Rome",
    ),
    (
        "Quelle est la capitale de la Belgique ?",
        ("Anvers", "Bruxelles", "Bruges", "Liège"),
        "Bruxelles",
    ),
    (
        "Quelle est la capitale de la Djibouti ?",
        ("Moscou", "Madride", "Bruges", "Djibouti"),
        "Djibouti",
    ),
    (
        "Quelle est la capitale de la Russie ?",
        ("Paris", "Madride", "Moscou", "New York"),
        "Moscou",
    ),
]

Questionnaire([Question(question[0], question[1], question[2]) for question in questions]).lancer()
