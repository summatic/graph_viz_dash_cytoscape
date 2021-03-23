def get_cyto_stylesheet():
    stylesheet = [
        {
            "selector": "node",
            "style": {
                "content": "data(label)",
                "background-color": "#7ea0c4",
                "border-color": "#969696",
                "border-style": "solid",
                "border-width": 3,
            },
        },
        {
            "selector": "edge",
            "style": {"curve-style": "bezier", "line-color": "#969696", "width": 0.6},
        },
        {
            "selector": "node:selected",
            "style": {
                "border-color": "#3B3B3B",
                "border-style": "solid",
                "border-width": 6,
            },
        },
        {
            "selector": "edge:selected",
            "style": {
                "line-color": "#3B3B3B",
                "width": 2,
            },
        },
        {
            "selector": ".query",
            "style": {
                "background-color": "#1b33ab",
                "border-width": 5,
                "font-size": "30px",
                "width": 80,
                "height": 80,
            },
        },
    ]
    return stylesheet
