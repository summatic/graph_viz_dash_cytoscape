import json

import networkx as nx

from app import queue, conn
from engine import graph_loader
from engine.utils import get_subgraph, get_cytoscape_elements

github_graph = graph_loader.graph


def search_github_id(job_id, github_id):
    def _set(_status, _result):
        conn.set(name=job_id, value=json.dumps({"status": _status, "result": _result}), ex=60)

    _set(_status=None, _result=None)

    if github_id == "":
        _set(
            _status="no_input",
            _result=[{"data": {"id": 0, "label": "Enter github ID"}}],
        )
    else:
        try:

            _set(_status="searching", _result=None)
            subgraph = get_subgraph(github_id, github_graph)

            _set(_status="rendering", _result=None)
            cyto_elements = get_cytoscape_elements(subgraph, query_node=github_id)
            _set(_status="finished", _result=cyto_elements)
        except nx.exception.NetworkXError:
            _set(
                _status="not_found",
                _result=[{"data": {"id": 0, "label": "No github ID"}}],
            )


if __name__ == "__main__":
    print("Ready to work")
    while True:
        msg = queue.get()
        if msg is None:
            continue

        element = json.loads(msg.decode("utf-8"))
        print(element)
        search_github_id(**element)
