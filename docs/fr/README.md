
- [English](/README.md)
- [中文](/docs/zh/README.md)
- [Français](/docs/fr/README.md)

# Blog de l'Équipe de Concours Algorithmique - Projet Open Source

Il s'agit d'une plateforme de blog basée sur Jekyll, spécialement conçue pour les équipes de concours d'algorithmique et prenant en charge le déploiement privé. Cette plateforme vise à améliorer l'efficacité d'apprentissage et la collaboration au sein des équipes, avec des fonctionnalités telles que le suivi quotidien, des notes flexibles, des modèles d'algorithmes, la génération rapide de blogs de résolution de problèmes, la visualisation des données d'entraînement (y compris le classement des contributeurs, la répartition des types de problèmes, la répartition des niveaux de difficulté des problèmes) et une page personnelle pour chaque membre.

## Fonctionnalités

### 1. Suivi Quotidien
Prend en charge la fonctionnalité de suivi automatisé quotidien, permettant de suivre les progrès d'entraînement des membres de l'équipe et de garantir que chaque membre participe activement à l'entraînement algorithmique.

### 2. Prise de Notes Flexible
Les membres de l'équipe peuvent enregistrer leurs notes personnelles sur les algorithmes, leurs idées de résolution de problèmes et leurs réflexions. Chaque membre dispose d'un espace de notes indépendant, avec prise en charge de l'édition Markdown.

### 3. Modèles d'Algorithmes
Fournit des modèles d'algorithmes courants, permettant de remplir rapidement les modèles et extraits de code, aidant les membres à résoudre des problèmes de manière plus efficace.

### 4. Génération Rapide de Blogs de Résolution de Problèmes
Prend en charge la génération rapide de blogs de résolution de problèmes via des scripts et des extensions VSCode. Les développeurs peuvent enregistrer leurs idées de résolution, implémentations de code et analyses de complexité temporelle dans VSCode. Le script remplira automatiquement ces données dans un modèle de blog, et GitHub Actions se chargera de rendre et de publier le blog final.

### 5. Visualisation des Données d'Entraînement
Affiche les données d'entraînement de chaque membre, y compris :
- **Classement des Contributeurs** : Affiche le nombre de problèmes résolus par chaque membre sur une période donnée.
- **Répartition des Types de Problèmes** : Affiche l'état de résolution des problèmes de différents types, tels que les graphes, la programmation dynamique, les algorithmes gloutons, etc.
- **Répartition des Niveaux de Difficulté des Problèmes** : Affiche l'état de résolution des problèmes selon différents niveaux de difficulté et les visualise sous forme de graphiques.

### 6. Page Personnelle
Chaque membre peut disposer d'une page personnelle affichant ses progrès d'apprentissage, ses résolutions de problèmes, ses réalisations et ses notes, avec un style d'affichage personnalisable.

## Installation et Déploiement

### Prérequis
- Compte GitHub
- Serveur auto-hébergé ou plateforme supportant GitHub Pages

### Étapes de Déploiement

1. Clonez ce projet sur votre machine locale ou serveur :

   ```bash
   git clone https://github.com/AliceAuto/AliceAuto.github.io.git
   ```