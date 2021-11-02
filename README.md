

pip install -r requirements.txt


Ouvrir 4 terminaux :
- dans le 1er on lance mlflow et minion : <br>
  ``bash
  docker-compose up
  ``
- dans le second on démarre  le serveur prefect : <br>
  ``bash
  prefect server start
  ``
- dans le troisième  on execute un agent prefect : <br>
  ``bash
  prefect agent local start
  ``
- dans le dernier<br>
On ajoute les deux version de la data avec DVC:<br>
  ``bash
  . dvc.sh
  ``
ouvrir prefect :<br>
``bash
http://localhost:8080
``
on peut constater dans l'interface l'agent <br>

ouvrir mlflow : <br>
``bash
http://localhost:5000
``
ouvrir minio : <br>
``bash
http://localhost:9000
``


Ensuite on enregistre le workflow dans prefect: <br>
  ``bash
  python script_mlfow.py
  ``
On peut constater le flow ajouté  dans l'interface prefect <br>

enfin on lance l'execution du workflow: <br>
  ``bash
  python scipt_flow.py
  ``
on peut suivre son execution.<br>
A la fin de son execution on peut constater l'expérimentation "gojob" les metriques obtenue. <br>

Et dans minio le model de l'experimentation   
