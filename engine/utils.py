import networkx as nx


def get_cytoscape_elements(graph, query_node):
    elements = []
    for node_id in graph.nodes():
        node_name = graph.nodes[node_id]["name"]
        is_target = graph.nodes[node_id]["target"]
        pos_x, pos_y = 0, 0

        if node_name == query_node:
            node_class = "query"
        else:
            node_class = ""

        elements.append(
            {
                "data": {
                    "id": node_id,
                    "label": node_name,
                    "name": node_name,
                    "is_target": is_target,
                },
                "position": {"x": pos_x, "y": pos_y},
                "classes": node_class
            }
        )

    for source_id, target_id in graph.edges():
        elements.append(
            {"data": {"id": len(elements), "source": source_id, "target": target_id}}
        )

    return elements


def get_subgraph(query_node, graph):
    all_nodes = nx.descendants_at_distance(G=graph, source=query_node, distance=1)
    subgraph = nx.subgraph(G=graph, nbunch=list(all_nodes) + [query_node])
    return subgraph
