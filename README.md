

```
gojob/
  |___script_mlflow.py                      # script pour ajouter le workflow mlflow à prefect
  |___script_flow.py                        # script pour executer le workflow précedemment ajouté dans prefect
  |___interface.py                          # script pour ajouter les chemin du repo actuel dans la config hydra
  |___mltest.py                             # script pour run le workflow mlflow sans prefect
  |___requirements.txt                      # fichier des dependencies  à installer en local
  |___wait-for-it.sh                        # script bash utilise dans le docker-compose, il permet d'attendre qu'une connexion TCP soit disposnible 
  |___project/
  |      |___conf/                          # répertoire qui contient la config hydra
  |      |      |___ config.yaml            # conf hydra principal
  |      |      |___data/
  |      |      |     |___v1.yaml           # conf hydra pour la version  DVC de la data
  |      |      |     |___v2.yaml           #
  |      |      |___run/
  |      |      |     |___run_1.yaml        # conf hydra relative à la run ID du flow prefect
  |      |      |___dvc/
  |      |      |     |___conf1.yaml        # conf hydra relative au repo de dvc vers minio
  |      |      |___var/
  |      |            |___env.yaml          # conf hydra relative aux variables d'environnement 
  |      |
  |      |___conda.yaml                     # le fichier qui permet l'env virtuel qui va executer le workflow
  |      |___MLproject                      # le fichier ou le workflow mlflow est spécifier
  |      |___main.py                        # le script du workflow
  |      |___process_data.py                # step process_data qui lit la data en spécifiant la version dans DVC
  |      |___train.py                       # step train  qui entraine et enregistre le modèle à partir de la data  préparé 
  |___data/                                 # répertoire de la data versioné dans DVC puis entrainé par la suite  
  |      |___ ...
  |___powerpoint_presentation/              # dossier relatif aux firchier pptx de présentation
  |      |___ ...
```
<br>

```bash
conda create -n gojob python3.7
conda activate gojob
pip install -r requirements.txt
```
<br>
On supprime les parametres DVC

```bash
. rmdvc.sh
```
<br>

Déclarer les variable env <br>
```bash
export MLFLOW_TRACKING_URI=http://localhost:5000
export MLFLOW_S3_ENDPOINT_URL=http://localhost:9000
export AWS_ACCESS_KEY_ID=minio
export AWS_SECRET_ACCESS_KEY=minio123
```

Gestion des droits d'accès du script wait-for-it.sh  <br>
```bash
chmod +x wait-for-it.sh
```

Initialisation de DVC et des options cloud <br>
```bash
git init
git add .
git commit -m "First commit"
dvc init -f
git commit -m "Initialize DVC repo"

dvc remote add -d minio s3://dvc -f
dvc remote modify minio endpointurl $MLFLOW_S3_ENDPOINT_URL
dvc remote modify minio access_key_id $AWS_ACCESS_KEY_ID
dvc remote modify minio secret_access_key $AWS_SECRET_ACCESS_KEY
```
On ajoute les deux versions de la data avec DVC:<br>
d'abord on ajoute la version 1 du data
  ```bash
    dvc add data/wine-quality.csv 
    git add data/wine-quality.csv.dvc data/.gitignore

    git commit -m 'data: track'


    git tag -a 'v1' -m 'raw data'
    dvc push
  ```
On test ensuite que l'on peut bien pull les datas du bucket depuis minio : <br>
```bash
rm -rf data/wine-quality.csv
rm -rf .dvc/cache
dvc pull

```
On ajoute une version 2  en supprimant 1000 lignes:
```bash
sed -i '2,1001d' data/wine-quality.csv
dvc add data/wine-quality.csv
git add data/wine-quality.csv.dvc

git commit -m 'data : remove 1000 lines'
git tag -a 'v2'  -m 'removed 1000 lines'
dvc push
```
<br>
Ouvrir 3 terminaux de plus : <br>
- dans le 1er on lance mlflow et minio : <br>

  ```bash
  docker-compose up
  ```
acceder à l'interface mlflow : http://localhost:5000 <br>
acceder à l'interface mlflow : http://localhost:9000 ensuite se connecter avec id : minio et password : minio123 <br>
![run](/gif_readme/minio.gif)
on peut constater la présence de deux bucket respectivement pour dvc et mlflow
<br><br>
- dans le second on démarre  le serveur prefect : <br>

  ```bash
  prefect server start
  ```
acceder à l'interface prefect : http://localhost:8080 <br><br>
- dans le troisième  on execute un agent prefect : <br>

  ```bash
  prefect agent local start
  ```
<h3> retour au terminal initial</h3> 
 <br>


ensuite on set les chemins respectifs du répertoire actuel dans le répertoire  project/conf ou on a toutes les configurations : <br>
    
        python interface.py
   

<br>
Maintenant on va run le project mlflow et s'attendre à une erreur : <br>

    
        python mltest.py
    

cette étape est nécessaire car l'installation de l'environnement virtuel pour executer le workflow rentre dans une boucle infinie quand on spécifie `minio` dans le project/conda.yaml du projet <br>
Maintenant on regarde le nom de l'environnement créer : <br>

    
        conda env list
    

ensuite on active l'env et on install minio manuellement <br>

    
    conda activate {envname}
    pip install minio
    conda deactivate
    

Maintenant la command `python mltest.py`
devrait être "successful" <br><br>

dernière ligne droite :<br>

Ensuite on enregistre le workflow dans prefect: <br>
  ```bash
    python script_mlfow.py
  ```
On peut constater le flow ajouté  dans l'interface prefect à l'onglet Flow du projet gojob <br>

enfin on lance l'execution du workflow: <br>
  ```bash
    python scipt_flow.py run=run_1
  ```
on peut suivre son execution.<br>
A la fin de son execution on peut constater l'expérimentation `gojob` les metriques obtenue dans l'interface mlfow sur l'onglet de l'experiment `gojob`. <br>
 
![run](/gif_readme/flow_run.gif)

Enfin dans mlflow on peut acceder à l'experimentation et le calcul de ses metrics <br>

![run](/gif_readme/mlflowlast.gif)
