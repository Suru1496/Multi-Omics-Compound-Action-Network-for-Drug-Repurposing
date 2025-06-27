# run_pipeline.py

from src import data_loading, preprocessing, network_builder, feature_extraction, model
import os

def main():
    print("🔹 Step 1: Downloading Data...")
    data_loading.download_all_data()

    print("🔹 Step 2: Preprocessing...")
    expression_df, drug_df = preprocessing.process_all()

    print("🔹 Step 3: Building Knowledge Graph...")
    G = network_builder.build_heterogeneous_graph(expression_df, drug_df)

    print("🔹 Step 4: Extracting Features...")
    node_features, labels = feature_extraction.create_node_features(G)

    print("🔹 Step 5: Training Model...")
    model.train_graph_model(G, node_features, labels)

    print("✅ Pipeline completed.")

if __name__ == "__main__":
    main()

