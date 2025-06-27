from rdkit import Chem
from rdkit.Chem import AllChem
import numpy as np

def smiles_to_fingerprint(smiles, radius=2, nBits=2048):
    mol = Chem.MolFromSmiles(smiles)
    if mol:
        return np.array(AllChem.GetMorganFingerprintAsBitVect(mol, radius, nBits))
    else:
        return np.zeros(nBits)

def create_node_features(G):
    node_features = {}
    labels = {}

    for node, attr in G.nodes(data=True):
        if attr["type"] == "compound":
            # Placeholder: Replace with real SMILES
            smiles = "CCO"
            node_features[node] = smiles_to_fingerprint(smiles)
        else:
            node_features[node] = np.random.rand(128)  # Omics embedding placeholder

    return node_features, labels
