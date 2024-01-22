# Import necessary libraries
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# Sample chemical data (replace with your dataset)
chemical_data = pd.DataFrame({
    'Compound': ['Compound A', 'Compound B', 'Compound C'],
    'Property1': [10, 15, 8],
    'Property2': [20, 12, 18],
    'Property3': [5, 10, 15]
})

# Create Dash app
app = dash.Dash(__name__)

# App layout with movie-like styling and anime.js
app.layout = html.Div([
    # Page Title with anime.js animation
    html.H1('Chemical Data Visualization Dashboard', id='title', 
            style={'textAlign': 'center', 'color': '#FF69B4', 'fontFamily': 'Orbitron'}),
    
    # Dropdown for compound selection
    dcc.Dropdown(
        id='compound-dropdown',
        options=[{'label': compound, 'value': compound} for compound in chemical_data['Compound']],
        value=chemical_data['Compound'][0],
        multi=False,
        style={'width': '50%', 'margin': 'auto', 'marginTop': '20px', 'backgroundColor': '#1E1E1E', 'color': '#FF69B4'},
        className='dropdown'
    ),

    # Synthwave-style graph selector with anime.js animation
    html.Div([
        html.H4('Select Graph Type:', style={'color': '#FF69B4'}),
        dcc.RadioItems(
            id='graph-selector',
            options=[
                {'label': 'Scatter Plot', 'value': 'scatter'},
                {'label': 'Bar Chart', 'value': 'bar'}
            ],
            value='scatter',
            style={'color': '#FF69B4'},
            className='graph-selector'
        )
    ], style={'width': '50%', 'margin': 'auto', 'marginTop': '20px', 'opacity': 0, 'transform': 'translateY(20px)',
              'animation': 'fadeInUp 1s ease-out forwards'}),

    # Graph output with anime.js animation
    dcc.Graph(id='output-graph', style={'width': '80%', 'margin': 'auto', 'marginTop': '20px'}, className='plot')
])

# Define callback to update graph based on user selection
@app.callback(
    Output('output-graph', 'figure'),
    [Input('compound-dropdown', 'value'),
     Input('graph-selector', 'value')]
)
def update_graph(selected_compound, graph_type):
    # Filter data based on selected compound
    filtered_data = chemical_data[chemical_data['Compound'] == selected_compound]

    # Create graph based on user selection
    if graph_type == 'scatter':
        fig = px.scatter(filtered_data, x='Property1', y='Property2',
                         title=f'Scatter Plot for {selected_compound}',
                         labels={'Property1': 'X-axis Label', 'Property2': 'Y-axis Label'},
                         template='plotly_dark',
                         color_discrete_sequence=['#FF69B4'],  # Synthwave pink color
                         )
    elif graph_type == 'bar':
        fig = px.bar(filtered_data, x='Compound', y='Property3',
                     title=f'Bar Chart for {selected_compound}',
                     labels={'Property3': 'Bar Height'},
                     template='seaborn',
                     color='Compound',
                     color_discrete_sequence=px.colors.qualitative.Set3  # Use a qualitative color palette
                     )
    else:
        fig = px.scatter()  # Default to an empty scatter plot if selection is invalid

    return fig

# External CSS for dark mode and synthwave styling
external_stylesheets = ['https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css',
                        'https://codepen.io/chriddyp/pen/bWLwgP.css',
                        'https://fonts.googleapis.com/css2?family=Orbitron:wght@500&display=swap']

# External JavaScript for anime.js
external_scripts = ['https://cdn.jsdelivr.net/npm/animejs/lib/anime.min.js']

# Link the external CSS and JavaScript
app.css.append_css({"external_url": external_stylesheets})
app.scripts.append_script({'external_url': external_scripts})

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
