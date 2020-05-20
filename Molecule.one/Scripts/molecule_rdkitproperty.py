#for proerperties (e.g. qed/molwt) of molecules from smiles

from rdkit import Chem
import pandas as pd
from rdkit.Chem import Descriptors
from rdkit.Chem import QED

input_file = sys.argv[1] #input .csv file, use molecule_output_file from moleculeone_proc.py
molwt_file = sys.argv[2] #output molwt file
qed_file = sys.argv[3] #output drug-likeness


with open(input_file, 'r') as f:
    data = f.read().splitlines()

molwt = []
qed = []

for molecule in data:
    molwt.append(Chem.Descriptors.ExactMolWt(Chem.MolFromSmiles(molecule)))
    qed.append(Chem.QED.qed(Chem.MolFromSmiles(molecule)))

molwt_result = pd.DataFrame(molwt)
molwt_result.to_csv(molwt_file, header=False, index=False)

qed_result = pd.DataFrame(qed)
qed_result.to_csv(qed_file, header=False, index=False)
