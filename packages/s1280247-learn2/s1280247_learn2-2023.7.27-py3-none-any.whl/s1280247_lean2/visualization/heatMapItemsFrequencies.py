import plotly.express as px

class heatMapItemsFrequencies:
    def __init__(self, items_frequencies):
        self.items_frequencies = items_frequencies

    def plot_heatmap(self):
        # Extract data from the items_frequencies dictionary
        lats = []
        lons = []
        freqs = []
        for item, freq in self.items_frequencies.items():
            lat, lon = item.split(',')
            lats.append(float(lat))
            lons.append(float(lon))
            freqs.append(freq)

        # Create the heatmap plot using Plotly Express
        fig = px.density_mapbox(
            lat=lats,
            lon=lons,
            z=freqs,
            radius=20,
            center=dict(lat=sum(lats) / len(lats), lon=sum(lons) / len(lons)),
            mapbox_style="open-street-map"
        )

        # Show the plot
        fig.show()