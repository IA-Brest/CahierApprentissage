---
jupyter:
  jupytext:
    formats: ipynb,md
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.13.6
  kernelspec:
    display_name: Python 3
    language: python
    name: python3
---

# Programation Orientée Objet en Python

Les classes fournissent :
- Héritage multiples
- Surcharge des méthodes
- Appel de la méthode de la classe parente éponyme.
- Crées à l'exécution et modifiable.

Les membres d'une classe ont :
- Un accès publique (protégé ou privé uniquement par convention de nommage `_membrePrive:wq`)
- des fonctions membres virtuelles
- encapsulation : pas d'accès aux membres depuis les méthodes, mais par une représentation de l'objet passé implicitement comme premier paramètre de la méthode.

Les classes sont des objets, les types natifs peuvent être étendus, et les opérateurs peuvent être redéfinis pour les instances de classes.

## Nommage des objets

Les objets sont nommés par des alias qui se comportent comme des pointeurs.
Dans le cas d'un objet passé en argument, il y a donc un passage par référance, et risque d'effet de bord.

## Portée et espace de nommage

Espace de nommage : table de correspondance entre noms et objets.
- Primitives (exceptions de base et fonctions natives) dans `builtins`
- Noms globaux dans un module (partagent le namespce des attributs), `__main__` par défaut
- Noms locaux dans une fonction
- Ensemble des attributs d'un objet

Attributs :
- modifiables ou en lecture seule
- affectation : `nom_module.nom_attribut = 42`
- suppression : `del nom_module.nom_attribut`


```python
def scope_test():
  def do_local():
    spam = "local spam"

  def do_nonlocal():
    nonlocal spam
    spam = "nonlocal spam"

  def do_global():
    global spam
    spam = "global spam"

  spam = "test spam"
  do_local()
  print("After local assignment:", spam)
  do_nonlocal()
  print("After nonlocal assignment:", spam)
  do_global()
  print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)
```

Résultat :

  After local assignment: test spam
  After nonlocal assignment: nonlocal spam
  After global assignment: nonlocal spam
  In global scope: global spam

```python

```
