import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc
import numpy as np

app = dash.Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP])

generations = ['Gen Z', 'Millennials', 'Gen X', 'Boomers']
years = list(range(2018, 2024))

mental_health_data = {
    'Year': years * len(generations),
    'Generation': [gen for gen in generations for _ in years],
    'Anxiety_Level': [
        *np.random.uniform(30, 45, len(years)),
        *np.random.uniform(25, 35, len(years)),
        *np.random.uniform(20, 30, len(years)),
        *np.random.uniform(15, 25, len(years)),
    ],
    'Depression_Cases': [
        *np.random.randint(1000, 1500, len(years)),
        *np.random.randint(800, 1200, len(years)),
        *np.random.randint(600, 900, len(years)),
        *np.random.randint(400, 700, len(years)),
    ]
}

df = pd.DataFrame(mental_health_data)

area_fig = px.area(df, x='Year', y='Anxiety_Level', color='Generation',
                   title='Anxiety Levels Across Generations (2018-2023)',
                   labels={'Anxiety_Level': 'Anxiety Level (%)', 'Year': 'Year'},
                   color_discrete_sequence=['#1d3557', '#457b9d', '#a8dadc', '#f1faee'])

bar_fig = px.bar(df, x='Year', y='Depression_Cases', 
                 color='Generation', barmode='stack',
                 title='Depression Cases by Generation',
                 labels={'Depression_Cases': 'Number of Cases'},
                 color_discrete_sequence=['#1d3557', '#457b9d', '#a8dadc', '#f1faee'])

for fig in [area_fig, bar_fig]:
    fig.update_layout(
        plot_bgcolor='white',
        paper_bgcolor='white',
        font_family="Helvetica",
        title_font_family="Helvetica",
        title_font_size=20,
        title_x=0.5,
        title_y=0.95,
        font_color='#1d3557',  
        legend=dict(
            title='',
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1,
            font=dict(color='#1d3557') 
        )
    )
    fig.update_xaxes(
        showgrid=True, 
        gridwidth=1, 
        gridcolor='#a8dadc',  
        tickfont=dict(color='#1d3557')  
    )
    fig.update_yaxes(
        showgrid=True, 
        gridwidth=1, 
        gridcolor='#a8dadc',  
        tickfont=dict(color='#1d3557') 
    )


app.layout = dbc.Container([
    # Hero Section
    html.Div(className="hero-section", children=[
        html.Div(className="hero-content", children=[
            dbc.Container([
                html.Div(className="hero-grid", children=[
                    
                    html.Div(className="hero-text", children=[
                        html.H1([
                            "Mental Health ",
                            html.Span("Insights"),
                        ], className="hero-title"),
                        
                        html.P("""Discover comprehensive insights into mental health trends 
                                 across generations. This dashboard visualizes key 
                                 patterns in anxiety levels and depression cases""",
                               className="hero-description"),
                        html.Div(className="hero-stats-grid", children=[
                            html.Div(className="stat-card", children=[
                                html.Div("4", className="stat-number"),
                                html.Div("Generations", className="stat-label")
                            ]),
                            html.Div(className="stat-card", children=[
                                html.Div("6", className="stat-number"),
                                html.Div("Years", className="stat-label")
                            ]),
                            html.Div(className="stat-card", children=[
                                html.Div("3K", className="stat-number"),
                                html.Div("Cases", className="stat-label")
                            ]),
                        ])
                    ]),
                    html.Div(className="hero-image-container", children=[
                        html.Img(
                            src="/assets/mental-health.png",
                            className="hero-image",
                            alt="Mental Health Illustration"
                        )
                    ])
                ])
            ], fluid=True)
        ])
    ]),
    
    # Main
    dbc.Container([
        dbc.Row([
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        html.H4("Anxiety Trends Over Time", 
                               className="card-title"),
                        dcc.Graph(figure=area_fig)
                    ])
                ], className="mb-4 dashboard-card")
            ], width=6, className="chart-container"),
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        html.H4("Depression Cases by Generation", 
                               className="card-title"),
                        dcc.Graph(figure=bar_fig)
                    ])
                ], className="mb-4 dashboard-card")
            ], width=6, className="chart-container")
        ])
    ], className="dashboard-container", fluid=False)
], fluid=True, className="px-0")

if __name__ == '__main__':
    app.run(debug=True)

