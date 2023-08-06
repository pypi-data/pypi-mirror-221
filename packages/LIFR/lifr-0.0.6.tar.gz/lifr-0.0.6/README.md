#LIFR
Ce module permet de générer une réponse en se basant sur une base de données de texte fournie et un début de réponse donné. Le résultat peut être une nouvelle phrase ou une réponse qui s'adapte aux données mathématiques fournies.


<p><b>Comment faire des operations avec LIFR</b></p>
Pour calculer une operation, la stocker dans une variable et afficher le résultat.<br>
[nom de la variable]=a*b=[a]*[b]=#

en premier lieu nous mettons la variable ou sera stocké la variable
ensuite nous mettons les valeurs numérique
ensuite le calcule avec les variables
ensuite le hashtag sera remplacé par la valeur du calcule

[x1]>[x2] permet de favoriser le text après, si cette condition si elle est juste
[x1]<[x2] permet de favoriser le text après, si cette condition si elle est juste
[novalue] si la chaine de charactère après cette expression n'est pas présente dans les valeurs données ou crées, favorise alors le texte après cette condition
[novalue] si la chaine de charactère après cette expression est présente dans les valeurs données ou crées, favorise alors le texte après cette condition
[break] pour arreter la generation d'un text

exemple donnont à LIFR le text suivant:
"""la valeur données [x1]>6 est donc plus grande que 6 [break]
la valeur données [x1]<6 n'est donc pas plus grande que 6 [break]
"""
par exemple:
print(LIFR.generate(({"data":"""la valeur données [x1]>6 est donc plus grande que 6 [break]\n la valeur données [x1]<6 nest donc pas plus grande que 6 [break]""","variable":{"[x1]":"2"}}))["text"])

la fonction generate renvoie un dictionnaire composé de:
	text: le text généré 
	output: des informations sur le déroulement du procésus
			divisé en 2 sous parties:
				score_output:information sur le scorage des mots et de pourquoi ils ont étaient choisis
				maths-compare:informations sur le changement des variables en nombre pour ensuite verifier une condition mathématique



On peut aussi appeler la fonction LIFR.search() pour generer une réponse approprié à la question.
print(search({"ask":"Quelles sont les dimensions rectangle dont le perimetre est egal a 34 cm et d'une aire a 60 cm2"})["text"])
	
