``bash
pip install -r requirements.txt
``
Déclarer les variable env <br>
``bash
export MLFLOW_TRACKING_URI=http://localhost:5000
export MLFLOW_S3_ENDPOINT_URL=http://localhost:9000
export AWS_ACCESS_KEY_ID=minio
export AWS_SECRET_ACCESS_KEY=minio123
``

Gestion des droits d'accès du script wait-for-it.sh  <br>
``bash
chmod +x wait-for-it.sh
``

Initialisation de DVC et des options cloud <br>
``bash
git init
git add .
git commit -m "First commit"
dvc init -f
git commit -m "Initialize DVC repo"

dvc remote add -d minio s3://dvc -f
dvc remote modify minio endpointurl $MLFLOW_S3_ENDPOINT_URL
dvc remote modify minio access_key_id $AWS_ACCESS_KEY_ID
dvc remote modify minio secret_access_key $AWS_SECRET_ACCESS_KEY
``

Ouvrir 4 terminaux :
- dans le 1er on lance mlflow et minio : <br>
  ``bash
  docker-compose up
  ``
acceder à l'interface mlflow : http://localhost:5000 <br>
acceder à l'interface mlflow : http://localhost:9000 ensuite se connecter avec id : minio et password : minio123 <br>
on peut constater la présence de deux bucket respectivement pour dvc et mlflow
<br><br>
- dans le second on démarre  le serveur prefect : <br>
  ``bash
  prefect server start
  ``
acceder à l'interface prefect : http://localhost:8080 <br><br>
- dans le troisième  on execute un agent prefect : <br>
  ``bash
  prefect agent local start
  ``
- dans le dernier<br>
On ajoute les deux version de la data avec DVC:<br>
d'abord on ajoute la version 1 du data
  ``bash
dvc add data/wine-quality.csv 
git add data/wine-quality.csv.dvc data/.gitignore

git commit -m 'data: track'


git tag -a 'v1' -m 'raw data'
  ``
On test ensuite que l'on peut bien pull les data du bucket dans minio : <br>
``bash
rm -rf data/wine-quality.csv
rm -rf .dvc/cache
dvc pull

``
On ajoute une version 2 :
``bash
sed -i '2,1001d' data/wine-quality.csv

git add data/wine-quality.csv.dvc

git commit -m 'data : remove 1000 lines'
git tag -a 'v2'  -m 'removed 1000 lines'
dvc push
``

ensuite on set les chemins respectifs du répertoire actuel dans le répertoire  project/conf ou on a toutes les configurations : <br>
``bash
python interface.py
``

<br>
Maintenant on va run le project mlflow et s'attendre à une erreur : <br>
``bash
python mltest.py
``
cette étape est nécessaire car l'installation de l'environnement virtuel pour executer le workflow rentre dans une boucle infinie quand on spécifie `minio` dans le project/conda.yaml du projet <br>
Maintenant on regarde le nom de l'environnement créer : <br>
``bash
conda env list
``
ensuite on active l'env et on install minio manuellement <br>
``bash
conda activate {envname}
pip install minio
conda deactivate
``
Maintenant la comment `python mltest.py`
devrait être "successful"

dernière ligne droite :

Ensuite on enregistre le workflow dans prefect: <br>
  ``bash
  python script_mlfow.py
  ``
On peut constater le flow ajouté  dans l'interface prefect à l'onglet Flow du projet gojob <br>

enfin on lance l'execution du workflow: <br>
  ``bash
  python scipt_flow.py run=run_1
  ``
on peut suivre son execution.<br>
A la fin de son execution on peut constater l'expérimentation "gojob" les metriques obtenue. <br>

Et dans minio le model de l'experimentation   
