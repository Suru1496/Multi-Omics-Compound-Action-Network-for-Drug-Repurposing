import networkx as nx

def build_heterogeneous_graph(expression_df, drug_df):
    G = nx.Graph()

    for gene in expression_df.columns:
        G.add_node(gene, type="gene")

    for _, row in drug_df.iterrows():
        drug = row["drug_name"]
        targets = row["targets"].split(";")

        G.add_node(drug, type="compound")
        for target in targets:
            if target in expression_df.columns:
                G.add_edge(drug, target, type="drug-target")

    return G

