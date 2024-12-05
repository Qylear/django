# Projet Blog avec Django de roche romain MTP MIA26.2

Ce projet est une application de blog construite avec le framework Django. Il permet de créer, afficher, modifier, supprimer des articles de blog et d'ajouter des commentaires. 

## Fonctionnalités

### Liste des articles
La page d'accueil affiche une liste d'articles de blog avec des options pour :
- **Voir**, **Modifier** et **Supprimer** des articles existants.
- **Créer un nouvel article** via un formulaire simple.

### Détail de l’article
Chaque article peut être visualisé en détail avec :
- **Titre** et **Contenu** de l'article.
- Une section **Commentaires** où les utilisateurs peuvent laisser leurs avis.

Les utilisateurs peuvent :
- **Modifier** et **Supprimer** leurs commentaires.
- Ajouter de nouveaux commentaires à chaque article.

### Ajout et modification d'un article
Les utilisateurs peuvent :
- Ajouter un nouvel article via un formulaire.
- Modifier les articles existants.

### Gestion des commentaires
Les utilisateurs peuvent ajouter, modifier ou supprimer des commentaires sur les articles.

---

## URL Routes

Les URL pour l'application sont définies comme suit :

- `/` : Liste des articles de blog (Vue Liste).
- `/post/<id>/` : Détail de l’article de blog (Vue Détail).
- `/post/create/` : Créer un nouvel article de blog (Vue Créer).
- `/post/<id>/edit/` : Modifier un article de blog existant (Vue Édition).
- `/post/<id>/add_comment/` : Ajouter un commentaire à un article de blog (Vue Ajouter un commentaire).
- `/comment/<id>/edit/` : Modifier un commentaire existant (Vue Modifier le commentaire).
- `/post/<id>/delete/` : Supprimer un article de blog (Vue Supprimer l’article).
- `/comment/<id>/delete/` : Supprimer un commentaire (Vue Supprimer un commentaire).

---

## Cas de Test

Pour garantir que le projet fonctionne correctement, les tests suivants doivent être effectués :

### Tests des articles de blog
1. **Création d'un article** : Vérifier qu'un nouvel article peut être ajouté correctement.
2. **Modification d'un article** : Vérifier que les modifications d'un article existant sont enregistrées.
3. **Suppression d'un article** : Vérifier qu'un article peut être supprimé correctement.

### Tests des commentaires
4. **Ajout d'un commentaire** : Vérifier qu'un commentaire peut être ajouté à un article.
5. **Modification d'un commentaire** : Vérifier qu'un commentaire peut être modifié.
6. **Suppression d'un commentaire** : Vérifier qu'un commentaire peut être supprimé.

### Tests des vues
7. **Affichage de la liste des articles** : Vérifier que la vue de la liste des articles fonctionne et affiche les articles.
8. **Affichage des détails d'un article** : Vérifier que la vue des détails d'un article affiche correctement le titre, le contenu et les commentaires.
9. **Formulaire de création d'un article** : Vérifier que le formulaire de création d'un article soumet et sauvegarde correctement les données.
10. **Redirections** : Vérifier que toutes les redirections (création, modification, suppression) renvoient vers les bonnes vues après l'action.
