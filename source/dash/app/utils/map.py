import dash_leaflet as dl

from source.dash.app.app import iti_df


def generate_additional_markers():
    markers = []
    for index, row in iti_df.iterrows():
        marker = dl.Marker(position=[row['end_latitude'], row['end_longitude']],
                           children=[dl.Tooltip(row['name'])])
        markers.append(marker)
    return markers
