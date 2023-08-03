from dash import html


def itinaryComponent(responseJson):
    raw_layout = []
    for day in responseJson['days']:
        for step in day['steps']:
            raw_layout.append(
                html.H4(step['name'])
            )
            raw_layout.append(
                html.P(step['instruction'])
            )

    return html.Div(raw_layout)
