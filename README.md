# Learning Synthesizability via MPNN

Synthesizability of organic molecules is crucial to drug development. Computation of synthesizability (0-10) via Molecule.one takes minutes for a single molecule, and we here speed it up ~50000x using MPNN based on Chemprop (5-10 ms). 

## Structure

<b>/Molecule.one</b> - synthesizability computed via Molecule.one, in either 0-10 format or binary (0/1) format. Binary_corrected refers to assigning known molecules (e.g. approved and investigational drugs) to be 1 instead of that computed by Molecule.one. 

/Molecule.one/Original - Synthesizability split into categories, e.g. molecules generated via random walk (100k, from /MKorablyov/LambdaZero/LambdaZero/datasets/brutal_dock/actor_dock.py), FDA approved/investigational drugs from Zinc15 database (6k), molecules from Emmanuel Bengio's RL algorithm (500). 

/Molecule.one/Attributes - Molecular weight, QED of the molecules. Calculated using rdkit.


<b>/MPNN</b> - the best performing Chemprop model to date for regression (0-10), binary classification, and binary classification with corrected synthesizability. --args.json specifies the tuned hyperparameters, --results.log specifies the performance, --verbose.log logs the training information.

To train models, see args.py in chemprop: 
```
python /path/to/chemprop/train.py --data_path <pah> --dataset_type <type> --save_dir <dir>
```

To make predictions using existing models: 
```
python /path/to/chemprop/predict.py --test_path molecules.csv --checkpoint_path /MPNN/Regression/model_0/model.pt --preds_path molecules_predicted.csv
```

<b>/Chemprop</b> - predicted synthesizability using the best performing MPNN 

## Dependencies and uses

Use SMILES strings for input, outputs either a number between 0 (non-synthesizable)-10 or 0/1. Dependent on Chemprop and rdkit. Should be importable if LambdaZero is installed.

```
conda create -n "$CONDA_ENV_NAME" -y python=3.6

conda activate "$CONDA_ENV_NAME" 
set -u 

conda install -y $torch_tensorflow pytorch::pytorch==1.4.0 pytorch::torchvision conda-forge::rdkit pandas networkx scikit-image scikit-learn numba isodate jsonschema redis-py pyyaml colorama filelock aiohttp beautifulsoup4 future lz4 tabulate fastparquet boto3 pytest pytest-cov pyarrow mlflow tqdm

pip install git+https://github.com/chemprop/chemprop.git#egg=chemprop
pip install typed-argument-parser
```
