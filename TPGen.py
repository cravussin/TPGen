import jinja2
from pygmentize import pygmentize
from json import dump, load

#   TPGen v0.1 par Charles Ravussin
#   -------------------------------
#
#   Un rapport = liste des questions + conclusion
#   Une question est un dico {'type', contenu}
#   Type = p (paragraphe: str), i (image: str), c (code: str), cl (classes:List[str], f (difficultés & conclusion: List[str])

UNITE = 'NSY102'
RAPPORT = 'TP thread'
NOM = 'RAVUSSIN'
PRENOM = 'Charles'
MATRICULE = 'FOD_XXXXXXXXX'
EMAIL = 'charles.ravussin.auditeur@lecnam.net'
questions = {}
conclusions = []

context = {'unite': UNITE, 'rapport': RAPPORT, 'prenom': PRENOM, 'nom': NOM, 'matricule': MATRICULE, 'email': EMAIL, 'questions': questions, 'conclusions': conclusions}

def help():
    print("""
    ==============
    = TPGen v0.1 =
    ==============
    
    "A nutless monkey could do your job"
        
                                - Les Grossman
    Commandes:
    ----------
    n = nouvelle question
        p = nouveau paragraphe
        c = nouveau code snippet
        i = insérer image
    f = difficultés et conclusion
    p = afficher le contenu du rapport
    g = générer le rapport
    r = restaurer un état
    h = aide
    q = quitter
    
    """)


def inputMain():

    help()
    no_question = 0
    RAPPORT = input("Nom du rapport: ")
    while True:
        entree = input("(rapport): ")
        if entree == 'n':
            no_question += 1
            questions['{}'.format(no_question)] = inputQuestion(no_question)
        elif entree == 'p':
            print(context)
        elif entree == 'f':
            conclusions.append(input("(Difficultés rencontrées): "))
            conclusions.append(input("(Conclusion): "))
        elif entree == 'q':
            quit(0)
        elif entree == 'h':
            help()
        elif entree == 'g':
            generer(context)
        elif entree == 'r':
            rest = input("Entrer le contexte à restaurer ou laisser vide: ")
            if rest != '':
                import json
                context = json.loads(rest)
            noq = input("Numéro de question à modifier: ")
            no_question = int(noq)

def mongolo():
  for range(1,12):
    print('huuh')

    
def inputQuestion(no_question):
    question = []
    classes = []
    idx_image = 1

    while True:
        entreeC = input("(question {}: classes): ".format(no_question))
        if entreeC != '':
            classes.append(entreeC)
        else:
            question.append(('cl', classes))
            break
    while True:
        entreeQ = input("(question {}): ".format(no_question))
        if entreeQ == 'p':
            paragraphe = input("(paragraphe): ")
            question.append(('p', paragraphe))
            # print(question)
        elif entreeQ == 'c':
            print("Copier / coller le code: ")
            sentinel = ''  # ends when this string is seen
            code = '\n'.join(iter(input, sentinel))
            question.append(('c', pygmentize(code)))
            # print(question[-1][-1])
        elif entreeQ == 'i':
            imgsrc = '{}_{}.png'.format(no_question, idx_image)
            question.append((entreeQ, imgsrc))
            print('{} ajoutée'.format(imgsrc))
            idx_image += 1
        elif entreeQ == '':
            return question


def generer(contexte):
    i = open("index.template.html", "r", encoding="utf-8")
    html_in = i.read()
    i.close()

    template = jinja2.Template(html_in)

    html_out = template.render(contexte)

    with open("index.html", "w", encoding="utf-8") as o:
        o.write(html_out)


def restaurer(contexte, noquestion):
    i = open("index.template.html", "r", encoding="utf-8")
    html_in = i.read()
    i.close()
    template = jinja2.Template(html_in)
    contexte = {}

    html_out = template.render(contexte)

    with open("test.html", "w", encoding="utf-8") as o:
        o.write(html_out)
    inputMain()




# find . -type f -name *.java -exec pygmentize -f html -O full,style=colorful,linenos=1   -o {}.html {} \;





