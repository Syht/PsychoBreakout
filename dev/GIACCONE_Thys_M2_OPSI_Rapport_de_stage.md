# Exploration du codage prédictif grâce au jeu vidéo

___

**Encadrants : Bruno Wicker, Laurent Perrinet**  
*Laboratoire de Neurosciences Cognitives, Equipe ACDC, UMR 7291 CNRS  
3, place Victor-Hugo 13331 - Marseille Cedex 3*  
*Ecole Centrale Marseille, Technopôle de Château-Gombert  
38, rue Frédéric Joliot Curie 13451 - Marseille Cedex 20*

**Abstract:** Nous nous intéressons à l'influence du contexte perceptuel sur les mécanismes de prise de décision via un apprentissage probabiliste. La capacité à générer des prédictions est centrale pour des systèmes adaptatifs et intelligents comme le cerveau. Celui-ci génère continuellement des prédictions sur quelles données il va recevoir par la suite en se basant sur les données actuelles et les associations de données apprises par le passé. Plus précisément, on cherche à décrire ces phénomènes grâce à un modèle d'inférence Bayésienne.



## 1. Introduction

De récentes études, comme celle de John M. Henderson *"Gaze Control as Prediction"*, font le lien entre notre contrôle du regard et les prédictions générées par notre cerveau. En effet, le cerveau semble se comporter comme un générateur de prédiction, usant de ses expériences passées et des informations présentement à sa disposition, pour tenter de déterminer les futures informations qu'il va recevoir. On appelle cette façon de considérer le cerveau comme un générateur de prédiction le Cerveau Prédictif. En se basant sur ce concept, l'intérêt de nos recherches est de réussir à construire un moyen d'explorer la prise de décision dans un environnement probabiliste, d'étudier les interactions entre perception et action - appelée inférence active.  

Si nos perceptions sont testées pour confirmer les hypothèses générées par le cerveau, alors la recherche visuelle peut être interprêtée comme une expérience générant des données sensorielles. Nous nous sommes basés sur les travaux de Karl Friston et al. dans leur papier *"Perceptions as hypotheses: saccades as experiments"* pour ce qui est du fait que le comportement saccadique du regard renseigne sur les prédictions générées par le cerveau.  


L'utilisation d'un jeu vidéo pour mener cette étude nous est portée par de nombreuses publications scientifiques - comme celles de Daphne Bavelier et al. *"How to Asses Gaming-Induced Benefits on Attention and Working Memory"* ou encore *"Video game training to improve selective visual attention in older adults"* - qui nous démontre l'intérêt de l'utilisation de jeux vidéos pour ce qui est de l'apprentissage et de l'attention. L'utilisation d'un jeu vidéo nous permet d'avoir un environnement écologique et ludique, permettant notamment l'étude de populations de différents âges dont la mâturation du cerveau prédictif peut varier, et permettant également de mettre en évidence des dysfonctionnements si jamais appliqué à des cas pathologiques.  

L'intérêt d'un jeu vidéo ne s'arrête pas là. Une fois développé, le jeu peux toujours être modifié, amélioré, afin de pouvoir être appliqué à des recherches différentes. La flexibilité du jeu vidéo en fait un outil d'une efficacité certaine, permettant un grand nombre d'applications.  


C'est donc à partir de ces considérations que l'idée d'étudier le cerveau prédictif à l'aide du jeu vidéo a vu le jour. L'intérêt de cette étude étant à terme de réussir à modéliser le fonctionnement du cerveau prédictif à l'aide d'outil de traitement du signal tels que des modèles Bayesiens d'inférence active et ainsi soutenir, voire confirmer, cette théorie du cerveau prédictif. Plusieurs objectifs ont donc été fixés afin de mener cette étude. Tout d'abord, il fallait définir le protocole expérimental - c'est-à-dire programmer le jeu - qui permettra de mettre en évidence l'apprentissage et la génération de prédictions. Le choix du langage - Python - nous a été porté par sa grande utilisation dans le monde scientifique, nous permettant de profiter de l'expérience de la communauté, et par la puissance et la flexibilité de ce langage orienté objet. De plus, Python possède un module dédié au développement de jeux vidéos - Pygame - qui rend notre choix plus évident encore.  

Le jeu ainsi programmé devra répondre à plusieurs critères afin qu'il permette, suite à l'analyse des données obtenues, de répondre à la problématique. Le jeu va donc jouer avec un contexte probabiliste et permettre un apprentissage de celui-ci par le sujet au long de la partie. Il va également permettre aux expérimentateurs d'acquérir les données et les stocker dans des fichiers spécifiques. Comme expliqué précédemment, le regard du joueur nous permet de déterminer la génération de prédiction du cerveau. C'est grâce à un système d'eye-tracking, interfacé avec le jeu au préalable, que nous récupérons cette information.  

Une fois les données acquises, l'analyse commence. Pour la mener à bien, l'objectif est de créer un programme complet qui permettra une analyse rapide et facile des données futures. Celui-ci sera capable de lire les fichiers de données, de tracer les figures pertinentes, de mettre en évidence les variables d'intérêts et ainsi fournir à l'expérimentateur les données nécessaires à la résolution de la problématique.  



## 2. Méthodes

Déroulé du stage.

### 2.1 Le jeu

Le jeu est un simple casse-briques programmé en langage Python à l'aide du module Pygame - module permettant de développer des jeux vidéos simples en Python. L'objectif du joueur est de finir chaque niveau en détruisant toutes les briques qui le compose. Il existe cinq couleurs de briques réparties dans un total de six niveaux.  

Le contexte probabiliste est généré par une variable cachée qui va modifier le comportement de la balle lors de la destruction d'une brique selon une probabilité associée à la couleur de la brique concernée. La balle va alors avoir une probabilité **p** de revenir sur sa trajectoire et une probabilité **(p-1)** de rebondir normalement sur la brique.  
[Insérer image rebond_brique.png]

Afin de facilité l'apprentissage, la couleur des briques provient d'une colormap (PLASMA), et les probabilités **p** leur sont associées de la manière suivante :  
 - briques **jaunes** : **p = 0**  
 - briques **oranges** : **p = 0.25**  
 - briques **saumons** : **p = 0.5**  
 - briques **violettes** : **p = 0.75**  
 - briques **bleues** : **p = 1**  

Afin de motiver les sujets et les pousser à maintenir un comportement productif durant l'expérience, des phrases d'encouragement et de reproche sont affichées à l'écran lorsque le joueur fini un niveau ou perd la balle, respectivement.

TODO: montrer un screenshot du jeu

### 2.2 TheEyeTribe : dispositif d'eye-tracking

La récolte des données du regard est faite avec TheEyeTribe, un appareil d'eye-tracking à notre disposition. Constitué d'une caméra infrarouge, le dispositif est placé sous l'écran de jeu et est calibré à l'aide du logiciel natif *EyeTribe UI*.

Afin que le programme du jeu puisse fonctionner de concert avec le dispositif d'eye-tracking, nous nous sommes muni d'un code d'interfaçage TheEyeTribe/Python écrit par *Per Baekgaard* sur son dépôt GitHub (https://github.com/baekgaard/peyetribe) et dont la licence est libre d'utilisation.

TODO: montrer une photo du dispositif experiemental?

### 2.3 Protocole expérimental

Aucune information sur la nature probabiliste des briques n'est donnée au sujet ni sur le nombre de niveaux que comporte le jeu. On explique au joueur que celui-ci va devoir finir un certain nombre de niveaux en détruisant les briques que composent chacun d'entre eux. Avant de commencer l'expérience, le joueur s'installe devant l'écran muni du dispositif d'eye-tracking et l'on utilise *EyeTribe UI* afin de le calibrer. On demande au joueur de rester le plus immobile possible durant l'expérience afin que la précision de TheEyeTribe soit optimisée.  

La raquette du casse-brique est dirigée grâce à la souris et permet de reorienter la balle, quelque soit son angle d'arrivé sur la raquette. Une balle arrivant au centre de la raquette est renvoyée perpendiculairement à celle-ci, tandis que les extrémités de la raquette vont renvoyer la balle avec des angles de respectivement 40° et 140°. Les valeurs intermédiaires suivent une loi linéaire respectant les valeurs données ci-dessus.  

Chaque niveau dure entre 2 et 4 min pour une durée totale de 12 à 24 min. Ce à quoi s'ajoute 1 à 3 min de calibrage pour une durée totale de l'expérience de 13 à 27 min.


### 2.4 Analyse des données

L'analyse des données est faite en langage Python, en utilisant Jupyter Notebook - une application open-source web qui permet de créer et partager des documents contenant du code, des équations, des graphiques et du texte explicatif - afin de faciliter l'échange et avoir un environnement de travail flexible.  

Suite au passage du sujet sur l'expérience, le programme écrit des fichiers contenant les variables d'intérêt pour chaque niveau. Ces fichiers sont classés par leur nomination qui est au format suivant : ``'année'-'mois'-'jour'_'heure''minute''seconde'_dataframe_lvl'numéro du niveau'_'sujet'.csv`` (exemple : ``2017-06-28_143211_dataframe_lvl4_remi.csv``). Ces fichiers sont des tableaux - ou dataframe - contenant les données suivantes :  

 - marque de temps du regard (en secondes)  
 - position en X du regard (pixel)  
 - position en Y du regard (pixel)  
 - marque de temps de la balle (en secondes)  
 - position en X de la balle (pixel)  
 - position en Y de la balle (pixel)  
 - marque de temps de la raquette (en secondes)  
 - position en X de la raquette (pixel)  
 - position en Y de la raquette (pixel)  

Ces données nous permettent d'observer le comportement du joueur vis-à-vis de son apprentissage des probabilités de rebond opposé des briques en fonction de leur couleur. Afin de quantifier ce phénomène, il nous fallait trouver comment traiter nos données, comment mettre en évidence des variables d'intérêt. Les données brutes obtenues nous permettent de visualiser les trajectoires des variables de la dataframe comme ci-dessous.  
[Mettre l'image all_trajectories.png]  

Comme il est impossible de sortir les informations recherchées de cette représentation, nous avons décidé d'observer les trajectoires dans une fenêtre temporel autour du rebond. De plus, nous avons centré toutes les trajectoires pour chaque sujet et chaque rebond. Pour dégrossir l'analyse, nous avons décidé de ne regarder que les rebonds s'opérant sur le dessous des briques. De plus, afin de s'affranchir de l'angle de rebond, nous avons tracé la position en Y en fonction du temps. Grâce à ces tracés, nous avons pu observé un comportement récurrent : une saccade du regard qui s'effectue peu après le rebond.  
[Mettre l'image saccade.png]  

Cette observation nous a permis de mettre en évidence une première variable d'intérêt que nous avons nommé "temps de latence". Cette saccade rend compte d'un comportement de suivi de la balle. La durée de celui-ci devrait donc être corrélé aux prédictions faites par le cerveau sur la trajectoire que prendra la balle après le rebond.  

Une deuxième variable d'intérêt a été choisie par la suite, découlant d'un raisonnement différent. Cette variable est la distance entre le regard et l'emplacement du rebond sur la brique. Elle serait pertinente par le fait que, plus un comportement est prédictible - ici le sens du rebond de la balle -, plus le regard peut se permettre de se trouver ailleurs, de n'observer la balle qu'avec la vision périphérique. On choisi donc d'observer l'évolution de cette distance au cours des niveaux pour chaque couleur de brique - et donc pour chaque probabilité.  


## 3. Résultats

Résultats temps de latences + graphs
Résultats distance rebond/gaze + graphs
* Résultats comportementaux => valide
* évolution des latences de 1ère saccade après le rebond
* synthèse des données en isolant les valeurs p

## 4. Discussion

* Résumé des résultats obtenus
    * jeu vidéo -> psycho
    * analyse robuste
    * marqueur psycho (latence) lié à la prédictabilité
* limites
    * variabilité des résulats du mouvement des yeux (regard périphérique) -> occlusion ?
    * temps d'acquisition
    * cadre théorique pour manipuler la valeur de prédictabilité
* Ouvertures
    * ?
    * briques sociales


___


### Références

1. Benjamin T. Vincent, *"Bayesian accounts of covert selective attention: A tutorial review"*, Atten Percept Psychophys (2015)
2. John M. Henderson, *"Gaze Control as Prediction"*, Cell Press (2017)
3. Karl Friston, Rick A. Adams, Laurent Perrinet and Michael Breakspear, *"Perceptions as hypotheses: saccades as experiments"*, edited by Lars Muckli, University of Glasgow, UK (2012)
3. Jyoti Mishra, Daphne Bavelier and Adam Gazzaley, *"How to Asses Gaming-Induced Benefits on Attention and Working Memory"*, Games for Health Journal (2012)
4. Patrícia Belchior, Michael Marsiske, Shannon M. Sisco, Anna Yam, Daphne Bavelier, Karlene Ball and William C. Mann, *"Video game training to improve selective visual attention in older adults"*, Computers in Human Behavior (2013)
5. Karl Friston, Jérémie Mattout and James Kilner, *"Action understanding and active inference"*, Europe PMC Funders Group (2012)
6. Christian Keysers and Valeria Gazzola, *"Hebbian learning and predictive neurons for actions, sensations and emotions"*, Philosophical Transactions of the Royal Society (2014)
7. Florent Meyniel, Maxime Maheu and Stanislas Dehaene, *"Human Inferences about Sequences: A Minimal Transition Probability Model"*, PLOS Computational Biology (2016)
8. Catherine Manning, James Kilner, Louise Neil, Themelis Karaminis and Elizabeth Pellicano, *"Children on the autism spectrum update their behaviour in response to a volatile environment"*, Developmental Science (2016)
9. Meltem Sevgi, Andrea O. Diaconescu, Marc Tittgemeyer and Leonhard Schilbach, *"Social Bayes: Using Bayesian Modeling to Study Autistic Trait-Related Differences in Social Cognition"*, Society of Biological Psychiatry (2016)
10. Colin J. Palmer, Rebecca P. Lawson and Jakob Hohwy, *"Bayesian Approaches to Autism: Towards Volatility, Action and Behavior"*, ResearchGate (2017)