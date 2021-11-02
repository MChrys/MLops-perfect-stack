

pip install -r requirements.txt


Ouvrir 4 terminaux :
- dans le 1er on lance mlflow et minion :
  ``bash
  docker-compose up
  ``
- dans le second on démarre  le serveur prefect :
  ``bash
  prefect server start
  ``
- dans le troisième  on execute un agent prefect :
  ``bash
  prefect agent local start
  ``
- dans le dernier
On ajoute les deux version de la data avec DVC:
  ``bash
  . dvc.sh
  ``
ouvrir prefect :
``bash
http://localhost:8080
``
on peut constater dans l'interface l'agent 

ouvrir mlflow :
``bash
http://localhost:5000
``
ouvrir minio :
``bash
http://localhost:9000
``


Ensuite on enregistre le workflow dans prefect: 
  ``bash
  python script_mlfow.py
  ``
On peut constater le flow ajouté  dans l'interface prefect

enfin on lance l'execution du workflow:
  ``bash
  python scipt_flow.py
  ``
on peut suivre son execution.
A la fin de son execution on peut constater l'expérimentation "gojob" les metriques obtenue.

Et dans minio le model de l'experimentation  
