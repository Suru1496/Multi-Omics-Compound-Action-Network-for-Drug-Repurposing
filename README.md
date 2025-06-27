# 🧬 Multi-Omics–Cheminformatics Integration for Drug Repurposing

A comprehensive pipeline to integrate transcriptomic and proteomic data with chemical structure and target information to identify novel drug repurposing opportunities using a compound–gene–pathway–disease action network.

---

## 🔍 Project Objective

This project aims to discover new therapeutic uses for existing drugs by:
- Integrating **multi-omics data** (e.g., gene expression, proteomics) from public databases like GEO, LINCS, and PRIDE.
- Leveraging **cheminformatics** tools to analyze chemical structures and known drug-target interactions.
- Building a **heterogeneous knowledge graph** linking compounds, genes/proteins, biological pathways, and diseases.
- Applying **machine learning and graph neural networks (GNNs)** to predict potential repurposing candidates based on molecular action networks.

---

## 🏗️ Repository Structure

multi-omics-drug-repurposing/
│
├── data/ # Raw and processed data
│ ├── raw/ # Raw downloaded files
│ └── processed/ # Preprocessed and transformed data
│
├── notebooks/ # Jupyter notebooks for exploration and prototyping
│ ├── 01_data_download.ipynb
│ ├── 02_preprocessing.ipynb
│ ├── 03_network_building.ipynb
│ └── 04_model_training.ipynb
│
├── src/ # Core source code
│ ├── data_loading.py
│ ├── preprocessing.py
│ ├── network_builder.py
│ ├── feature_extraction.py
│ ├── model.py
│ └── utils.py
│
├── models/ # Saved model files
├── results/ # Output plots, prediction results, and evaluations
├── config/ # Configuration files (e.g., paths, constants)
│
├── run_pipeline.py # Main script to run the full pipeline
├── requirements.txt # Python package requirements
├── environment.yml # Conda environment (optional)
└── README.md # Project overview (you’re here!)


---

## 🔄 Pipeline Workflow

1. **Data Collection**  
   - Download transcriptomic, proteomic, and drug-target datasets from public repositories.

2. **Data Preprocessing**  
   - Normalize and transform omics data.
   - Extract drug target lists and molecular fingerprints (SMILES → ECFP).

3. **Knowledge Graph Construction**  
   - Build a multi-layered graph connecting compounds, genes, pathways, and diseases.

4. **Feature Extraction**  
   - Create node embeddings using chemical fingerprints and omics-derived profiles.

5. **Prediction Model**  
   - Train a graph neural network (GNN) or machine learning classifier to predict drug-disease associations.

---

## 📦 Dependencies

Install required packages using pip:

```bash
pip install -r requirements.txt
Or with Conda:

bash

💡 Example Use Cases
Identify drugs that reverse gene expression signatures in disease.

Find compounds that modulate key disease-associated pathways.

Predict new uses for FDA-approved drugs in rare or neglected diseases.

Visualize compound–gene–pathway–disease relationships using graph tools.









