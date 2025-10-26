from dash import html, Dash, dash_table, dcc, callback, Output, Input, State
import pandas as pd 
import plotly.express as px
import dash_bootstrap_components as dbc 
from utils import *

# Custom color palette
CUSTOM_COLORS = ['#2066ac', '#6998b5', '#92c5de', '#d1e5f0', '#fddbc7', '#dba38a', '#d6604c', '#b2172c']


# assign external style
external_stylesheets = [dbc.themes.BOOTSTRAP]
app = Dash(
    __name__, 
    external_stylesheets = external_stylesheets,
    meta_tags=[
        {'name': 'viewport', 'content': 'width=device-width, initial-scale=1.0, maximum-scale=1.2, minimum-scale=0.5'},
        {"name": "description", "content": "A dash Dashboard app provides global CO2 emission."},
        {"property": "og:title", "content": "Global Disaster Statistics Dashboard"},
        {"property": "og:description", "content": "Explore global natural disasters and their economic impacts through interactive visuals"},
        {"property": "og:image", "content": "./assets/images/dataviz-dash1.png"},
        {"property": "og:type", "content": "website"},
        {"name": "twitter:card", "content": "summary_large_image"},
        {"name": "twitter:title", "content": "Global Disaster Statistics Dashboard"},
        {"name": "twitter:description", "content": "Explore global natural disasters and their economic impacts through interactive visuals"},
        {"name": "twitter:image", "content": "./assets/images/dataviz-dash1.png"},
        ])

app.title = "Global Ki Dashboard"
server = app.server

# Loading dataset after modifying
full_data = pd.read_csv('full_data_4.csv')
full_data['Year'] = full_data['Year'].astype(str)

# Sort data for the needed filter
years = sorted(full_data['Year'].unique())
continents = sorted(full_data['Continent'].unique())
countries = sorted(full_data['Entity'].unique())

co2_avg = full_data.groupby('Entity', as_index=False)['Annual CO₂ emissions'].mean()
percent_co2 = full_data.groupby('Entity', as_index=False)['Share of global annual CO₂ emissions'].mean()

# Updated app.layout with new colors
app.layout = html.Div([
    html.Div([
        html.Div([
            dbc.Spinner(
                color="black",
                fullscreen_style={"visibility":"visible", "filter": "blur(2px)"},
                children=[
                    # Row 1: Navbar + Cards
                    dbc.Row([
                        # Navbar with new background color #d1e5f0
                        dbc.Col([ 
                            dbc.Navbar(
                                dbc.Container([
                                    html.A(
                                        dbc.Row(
                                            dbc.Col(dbc.NavbarBrand("GLOBAL EMISSIONS AND ENERGY MIX", 
                                                                   className="fw-bold",
                                                                   style={'color': '#2066ac'})),  # Navbar title color
                                            align="center", className="g-0"
                                        ),
                                        href="/",
                                        style={"textDecoration": "none"},
                                    ),
                                    dbc.Row([
                                        dbc.Nav([
                                            dbc.NavItem(dbc.NavLink("Overview", href="#", id= 'open-overview', style={'color': '#2066ac'})),
                                            dbc.NavItem(dbc.NavLink("Dashboard", href="#", active=True, style={'color': '#2066ac'})),
                                            dbc.NavItem(dbc.NavLink("User Guide", href="#", id= 'open-guide', style={'color': '#2066ac'})),
                                            dbc.NavItem(dbc.NavLink("Insight", href="#", id= 'open-insight', style={'color': '#2066ac'})),
                                        ], className="ms-auto", navbar=True)
                                    ], className="flex-grow-1"),
                                ], fluid=True),
                                style={'backgroundColor': '#d1e5f0'},  # Navbar background color
                                className="mb-2"
                            ),
                            # Modals
                            dbc.Modal([
                            dbc.ModalHeader(dbc.ModalTitle("GLOBAL EMISSIONS AND ENERGY MIX — Overview")),
                            dbc.ModalBody([
                                html.P("Welcome to Dataviz 2025 !!!"),
                                html.P("This dashboard provides a comprehensive look at global emission (CO₂ and Green House Gas (GHG)) emissions across regions, sectors, and time. As well as focusing on the breakdown of energy sources. "),
                                html.P("🌍  Purpose:"),
                                html.Ul([
                                    html.Li("Visualize emission trends by country, sector, and energy source."),
                                    html.Li("Understand how regional and sectoral contributions change over time."),
                                ]),
                                html.P("📊  Key Highlights:"),
                                html.Ul([
                                    html.Li("Global CO₂ comparison map (by country and year)"),
                                    html.Li("GHG emission trends across continents"),
                                    html.Li("Energy consumption breakdown by source"),
                                    html.Li("CO₂ emissions by industrial sector"),
                                ]),
                                html.P("🧭  Goal: Explore global data on how those energy sourse vary across the world and how this is manipulating over time."),
                                html.P("Dashboard by Quynh Huong (Sylvie) Nguyen. Contact quynhhuong.nguyen@students.mq.edu.au")
                            ]),
                            dbc.ModalFooter(
                                dbc.Button("Got it!", id="close-overview", color="success", className="ms-auto", n_clicks=0)
                            ),
                        ], id="overview-modal", is_open=False),

                            # --- USER GUIDE MODAL ---
                        dbc.Modal([
                            dbc.ModalHeader(dbc.ModalTitle(" 🗺️ How to Use the Dashboard and Filter Box")),
                            dbc.ModalBody([
                                html.P("This section explains how each interactive chart behaves when you adjust filters such as continent, country, year range, and energy source."),
                                html.Hr(),

                                # --- Map Chart ---
                                html.H5("Global CO₂ Emission Map", className="fw-bold"),
                                html.P([
                                    "Use the dropdown on the right side of the map to choose the CO₂ metric you want to explore ",
                                    "(e.g., Annual CO₂ emissions, Per capita emissions, etc.). ",
                                    "The map updates automatically based on your filter selections."
                                ]),
                                html.Ul([
                                    html.Li("If you select a continent (e.g., Africa), the map highlights its countries and displays the top 5 emitters within that region."),
                                    html.Li("If you choose specific countries, the map focuses on those nations only."),
                                    html.Li("If no filters are applied, global values are shown for all countries."),
                                ]),

                                html.Hr(),

                                # --- Line Chart ---
                                html.H5("GHG Emissions Over Time (Line Chart)", className="fw-bold"),
                                html.P("This chart displays Greenhouse Gas (GHG) emissions per capita across years, adapting dynamically to your selected filters:"),
                                html.Ul([
                                    html.Li("If no continent or country is selected → The chart shows continent-level average GHG trends."),
                                    html.Li("If a country filter is applied → Each country’s emission trend is displayed as a separate line."),
                                    html.Li("If a continent filter is applied → Only the selected continents (and their countries) are plotted."),
                                    html.Li("Too many selected countries may make the chart crowded — consider refining your selection for clarity."),
                                ]),

                                html.Hr(),

                                # --- Stacked Bar Chart ---
                                html.H5("CO₂ Emission by Sector (Stacked Chart)", className="fw-bold"),
                                html.P("This horizontal stacked bar chart breaks down CO₂ emissions by sector (e.g., Buildings, Industry, Transport, etc.)."),
                                html.Ul([
                                    html.Li("Hover over each segment to view precise emission values via tooltips."),
                                    html.Li("If the global filter is active, the chart summarizes data across the selected year range."),
                                    html.Li("If animation is enabled, the chart updates dynamically to show the specific year’s emissions."),
                                ]),

                                html.Hr(),

                                # --- Area Chart ---
                                html.H5("Energy Consumption by Source (Area Chart)", className="fw-bold"),
                                html.P([
                                    "The area chart visualizes energy consumption over time by power source (e.g., Coal, Oil, Solar, Wind). ",
                                    "When you tick energy types in the checklist, the chart automatically filters to those energy sources."
                                ]),
                                html.Ul([
                                    html.Li("Filters respond to selected continent and country — showing energy trends for those regions."),
                                    html.Li("Values are aggregated per year, showing changes in energy mix over time."),
                                    html.Li("If no filters are selected, the chart displays global energy consumption trends."),
                                ]),
                                html.Hr(),

                                html.P("💡 Tip: All visuals are interconnected — modifying any filter or selection instantly updates every chart on the dashboard."),
                            ]),
                            dbc.ModalFooter(
                                dbc.Button("Back to dashboard !", id="close-guide", color="success", className="ms-auto", n_clicks=0)
                            ),
                        ], id="guide-modal", is_open=False, size="lg")
                        ,

                            # --- INSIGHT MODAL ---
                            dbc.Modal([
                                dbc.ModalHeader(dbc.ModalTitle("Key Insights & Observations")),
                                dbc.ModalBody([
                                    html.P("This section highlights the main insights derived from the global and G7 emission analysis (1990–2023)."),
                                    html.Hr(),

                                    # --- Global Energy Mix ---
                                    html.H5("🌍 Global Energy vs Electricity Mix", className="fw-bold"),
                                    html.P([
                                        "We observe a large difference between the share of low-carbon sources in the total ",
                                        html.Span("Global Energy", className="fw-semibold"),
                                        " mix compared to ",
                                        html.Span("Electricity Generation", className="fw-semibold"), ".",
                                    ]),
                                    html.Ul([
                                        html.Li("From 2015–2023, nuclear and renewables together account for about 31.97% of global electricity output."),
                                        html.Li("However, these sources make up less than 10% (≈21.9%) of total global energy consumption."),
                                        html.Li("This gap arises because major CO₂ contributors like transport and heating still rely heavily on fossil fuels."),
                                    ]),
                                    html.Hr(),

                                    # --- G7 Comparison ---
                                    html.H5("🌎 G7 CO₂ Emission Comparison", className="fw-bold"),
                                    html.P("Among G7 nations, clear emission contrasts remain despite similar levels of industrial development."),
                                    html.Ul([
                                        html.Li("🇺🇸 The United States remains the largest CO₂ emitter (≈182.8 B tonnes) — over 4× higher than Japan (40.1 B) and nearly 15× higher than Australia (12.1 B)."),
                                        html.Li("🇩🇪🇬🇧🇫🇷🇮🇹 European countries such as Germany, the UK, France, and Italy record much lower total emissions."),
                                        html.Li("🇨🇦🇦🇺 Canada and Australia, despite smaller populations, still emit significantly due to fossil-fuel-intensive economies."),
                                        html.Li("Overall, developed nations continue to produce substantial CO₂ levels, primarily from industrial activities and fossil energy dependence."),
                                    ]),
                                    html.Hr(),

                                    # --- GHG Trends Over Time ---
                                    html.H5("📈 GHG Emissions Over Time", className="fw-bold"),
                                    html.Ul([
                                        html.Li("The US and Canada exhibit the highest per-capita GHG emissions (≈15–25 tonnes per person) across the 1990–2023 period."),
                                        html.Li("European members (UK, Germany, France, Italy) show a clear downward trajectory, reflecting successful decarbonization policies and coal phase-outs."),
                                        html.Li("Japan and Australia maintain moderate emissions with gradual declines post-2010."),
                                    ]),
                                    html.Hr(),

                                    # --- Electricity Generation ---
                                    html.H5("⚡ Electricity Generation (Per Capita)", className="fw-bold"),
                                    html.Ul([
                                        html.Li("The United States leads in total electricity generation per capita — around 3,000 units — dominated by fossil fuels (≈65–70%), followed by nuclear (20%) and renewables (10–15%)."),
                                        html.Li("Canada has one of the cleanest electricity mixes, primarily hydroelectric."),
                                        html.Li("France stands out for its high nuclear share, which keeps its CO₂ emissions relatively low."),
                                        html.Li("Japan reduced nuclear use after Fukushima, increasing reliance on fossil fuels."),
                                        html.Li("Australia’s power sector remains ≈80% fossil-fuel-based, though renewables are expanding."),
                                        html.Li("Overall, renewable growth in Europe outpaces other regions, while the US, Japan, and Australia still depend heavily on fossil sources."),
                                    ]),
                                    html.Hr(),

                                    # --- Energy Consumption ---
                                    html.H5("🔋 Energy Consumption by Source", className="fw-bold"),
                                    html.Ul([
                                        html.Li("Total energy consumption among G7 countries has remained broadly stable since 2010."),
                                        html.Li("Oil and natural gas continue to dominate, though wind and solar consumption have increased noticeably in recent years."),
                                    ]),
                                    html.Hr(),

                                    # --- Sectoral Emissions ---
                                    html.H5("🏭 CO₂ Emissions by Sector", className="fw-bold"),
                                    html.Ul([
                                        html.Li("The United States leads in CO₂ output across nearly all sectors — especially Electricity & Heat and Energy Production."),
                                        html.Li("Japan records substantial emissions from its industrial and energy sectors."),
                                        html.Li("European countries exhibit more balanced emissions across sectors, driven by stronger efficiency policies."),
                                        html.Li("Australia’s emissions remain concentrated in fuel combustion due to coal and gas dominance."),
                                    ]),
                                    html.Hr(),

                                    html.P([
                                        html.Span("🌱 Overall insight:", className="fw-semibold"),
                                        " While renewables are rising, fossil fuels still dominate the global and G7 energy systems. ",
                                        "Meaningful decarbonization will depend on accelerating the clean-energy transition beyond the electricity sector — particularly in transport, heating, and heavy industry."
                                    ]),
                                ]),
                                dbc.ModalFooter(
                                    dbc.Button("Got it !", id="close-insight", color="success", className="ms-auto", n_clicks=0)
                                ),
                            ], id="insight-modal", is_open=False, size="xl")
,

                        ], xs=12, lg=6, className='mb-2 mb-lg-0'),
                        
                        # Stats Cards with new number color #b2172c
                        dbc.Col([
                            dbc.Row([
                                dbc.Col([
                                    dbc.Card([
                                        dbc.CardHeader("C02 EMISSION",className="fw-bold", style={'backgroundColor': '#dba38a'}),
                                        dbc.CardBody([
                                            html.H5(id= "card-total-co2", className="card-title fw-bold", style={'color': '#2066ac', 'textAlign': 'center'})
                                        ], className="card-stats-body"),
                                    ], outline=True, className="stats-card")
                                ], xs=6, lg=3, className="mb-2 mb-lg-0"),
                                
                                dbc.Col([
                                    dbc.Card([
                                        dbc.CardHeader("TOP EMITTER", className="fw-bold",style={'backgroundColor': '#dba38a'}),
                                        dbc.CardBody([
                                            html.H5(id= 'card-top-share', className="card-title fw-bold", style={'color': '#2066ac', 'textAlign': 'center'})
                                        ], className="card-stats-body"),
                                    ], outline=False, className="stats-card")
                                ], xs=6, lg=3, className="mb-2 mb-lg-0"),
                                
                                dbc.Col([
                                    dbc.Card([
                                        dbc.CardHeader("GLOBAL ENERGY", className="fw-bold", style={'backgroundColor': '#dba38a'}),
                                        dbc.CardBody([
                                            html.H5(id= "card-energy", className="card-title fw-bold", style={'color': '#2066ac', 'textAlign': 'center'})
                                        ], className="card-stats-body"),
                                    ], color='Warning', outline=False, className="stats-card")
                                ], xs=6, lg=3, className="mb-2 mb-lg-0"),
                                
                                dbc.Col([
                                    dbc.Card([
                                        dbc.CardHeader("ELECTRICITY only", className="fw-bold",style={'backgroundColor': '#dba38a'}),
                                        dbc.CardBody([
                                            html.H5(id= 'card-renewable', className="card-title fw-bold", style={'color': '#2066ac', 'textAlign': 'center'})
                                        ], className="card-stats-body"),
                                    ], color='Primary', outline=True, className="stats-card")
                                ], xs=6, lg=3, className="mb-2 mb-lg-0")
                            ])
                        ], xs=12, lg=6)
                    ], className="mb-3"),

                    # Row 2: Map, Line Chart, Filter
                    dbc.Row([
                        # Filter box
                        dbc.Col([
                            dbc.Card([
                                dbc.CardHeader(html.H4('Filters', id= "Filter-guilde"), style={'backgroundColor': '#d1e5f0'}),
                                dbc.Tooltip('Clicks hover on filter name to read more details about:', target= 'Filter-guilde'),
                                dbc.CardBody([
                                    html.Div([
                                        # Year slider
                                        html.Label('Year Range', className="fw-bold small", id='choose-year',
                                                    style={'cursor': 'pointer'}),
                                        dbc.Tooltip(
                                        'Dragging the slider bar to change the year period. If you want to select a single year, pull them together at the same place.',
                                        target='choose-year'
                                    ),
                                        dcc.RangeSlider(
                                            id='year-slider',
                                            min=1990, max=2023, step=1,
                                            value=[1990, 2023],
                                            marks={str(i): {'label': str(i), 'style': {'fontSize': '0.7rem'}} 
                                                   for i in range(1990, 2024, 10)},
                                            tooltip={"placement": "bottom", "always_visible": True},
                                            className="mb-3"
                                        ),
                                        
                                        # Continent
                                        html.Label('Continent', className="fw-bold small",  id='choose-continent',
                                                    style={'cursor': 'pointer'}),
                                        dbc.Tooltip(
                                        'Choosing your desired continent for futher details. Mutiple continent selection will be allowed.',
                                    target='choose-continent'
                                    ),
                                        dcc.Dropdown(
                                            id='continent-dropdown',
                                            options=[{'label': c, 'value': c} for c in continents],
                                            placeholder='Select continent(s)',
                                            multi=True,
                                            className="mb-3"
                                        ),
                                        
                                        # Countries
                                        html.Label('Countries', className="fw-bold small", id='choose-country',
                                                    style={'cursor': 'pointer'}),
                                        dbc.Tooltip(
                                        'Choosing your desired countries for futher details. MAXIMUM SELECTION will be 7.',
                                    target='choose-country'
                                    ),
                                        dcc.Dropdown(
                                            id='country-dropdown',
                                            options=[{'label': c, 'value': c} for c in countries],
                                            value = None,
                                            placeholder='Select country(ies)',
                                            multi=True,
                                            className="mb-3"
                                        ),
                                        
                                        # Power sources
                                        html.Label('Power Sources', className="fw-bold small mb-2", id='choose-source',
                                                    style={'cursor': 'pointer'}),
                                        dbc.Tooltip(
                                        'Choosing your desired power source for futher details. Mutiple sources selection will be allowed.',
                                    target='choose-sourse'
                                    ),
                                        html.Div([
                                            html.Label('Fuels', className="btn btn-danger btn-sm", htmlFor="btncheck1", style={'marginBottom': '4px', 'marginTop': '6px'}),
                                            html.Label('Renewable', className="btn btn-success btn-sm", style={'marginBottom': '6px', 'marginTop': '6px'}),
                                            html.Label('Nuclear', className="btn btn-warning btn-sm", style={'marginBottom': '6px', 'marginTop': '6px'}),
                                            html.Label('Others', className="btn btn-light btn-sm", style={'marginBottom': '6px', 'marginTop': '6px'}),
                                            dcc.Checklist(
                                                className="small",
                                                id="power-checklist",
                                                options=[
                                                    {"label": " Coal", "value": "Coal"},
                                                    {"label": " Gas", "value": "Gas"},
                                                    {"label": " Oil", "value": "Oil"},
                                                    {"label": " Hydro", "value": "Hydro"},
                                                    {"label": " Solar", "value": "Solar"},
                                                    {"label": " Wind", "value": "Wind"},
                                                    {"label": " Biofuels", "value": "Biofuels"},
                                                    {"label": " Nuclear", "value": "Nuclear"},
                                                    {"label": " Others", "value": "Others"},
                                                ],
                                                value=['Biofuels', 'Coal', 'Gas', 'Hydro', 'Nuclear', 'Wind', 'Solar', 'Oil', 'Others'],
                                                inline = True,
                                                labelStyle={'display': 'inline-block', 'marginRight': '0.5rem', 'marginBottom': '0.25rem'}, 
                                                style= {'display': 'flex', 'flexDirection': 'row', 
                                                        'flexWrap': 'wrap', 'display':'grid',
                                                        'alignItems': 'center',
                                                        'gridTemplateColumns': 'repeat(2, auto)', 'gap': '2px', 'row-gap': '8px',
                                                        'text-overflow': 'ellipsis', 'overflow': 'hidden', 'white-space': 'nowrap'}
                                            ), 
                                        ], className="power-checklist-wrapper"),
                                    ], className="filter-content-scroll")
                                ], className="filter-card-body")
                            ], className="map-card desktop-card-50")
                        ], xs=12, lg=2, className="mb-3"),
                        
                        # Map Card
                        dbc.Col([
                            dbc.Card([
                                dbc.CardHeader(html.H4('Average global CO₂ Emission Comparison'), style={'backgroundColor': '#d1e5f0'}),
                                dbc.CardBody([
                                    dbc.Row([             
                                        # Map
                                        dbc.Col([
                                            dcc.Graph(
                                                figure={}, 
                                                id='Choropleth-map',  
                                                className="mobile-graph-md desktop-graph",
                                                config={'displayModeBar': False}
                                            )
                                        ], xs=12, lg=8, className="mb-2 mb-lg-0"),
                                        
                                        # Ranking Table
                                        dbc.Col([
                                            html.H6('Select CO₂ metrics:', className="text-muted fw-bold mb-2"),
                                            dcc.Dropdown(
                                                options=[
                                                    {'label': 'Annual CO₂ emissions', 'value': 'Annual_CO2 (per tonne)'},
                                                    {'label': 'Share of global emissions', 'value': 'Share of global annual CO₂ emissions'}
                                                ],
                                                value='Annual_CO2 (per tonne)',
                                                clearable=False,
                                                id='co2-metric-dropdown', 
                                                className="mb-2"
                                            ),
                                            html.Div(id="ranking-table-container", className="ranking-table-wrapper")
                                        ], xs=12, lg=4)
                                    ])
                                ])
                            ], className="map-card desktop-card-50")
                        ], xs=12, lg=6, className="mb-3"),
                        
                        # Line Chart
                        dbc.Col([
                            dbc.Card([
                                dbc.CardHeader(html.H4('GHG Emissions Over Time'), style={'backgroundColor': '#d1e5f0'}),
                                dbc.CardBody([
                                    dcc.Graph(
                                        figure={}, 
                                        id='line-chart', 
                                        className="mobile-graph-md desktop-graph",
                                        config={'displayModeBar': False}
                                    )
                                ])
                            ], className="map-card desktop-card-50")
                        ], xs=12, lg=4, className="mb-3"),

                    ], className="desktop-row-charts"),
                    
                    # Row 3: Three bottom charts
                    dbc.Row([
                        dbc.Col([
                            dbc.Card([
                                dbc.CardHeader(html.H4('Electricity Generation (Per Capita)'), style={'backgroundColor': '#d1e5f0'}),
                                dbc.CardBody([
                                    dcc.Graph(
                                        figure={}, 
                                        id='stacked-bar-chart', 
                                        className="mobile-graph-md desktop-graph",
                                        config={'displayModeBar': False}
                                    )
                                ])
                            ], className="map-card desktop-card-40")
                        ], xs=12, lg=4, className="mb-3"),
                        
                        dbc.Col([
                            dbc.Card([
                                dbc.CardHeader(html.H4('Energy Consumption by Source'), style={'backgroundColor': '#d1e5f0'}),
                                dbc.CardBody([
                                    dcc.Graph(
                                        figure={}, 
                                        id='area-chart', 
                                        className="mobile-graph-md desktop-graph",
                                        config={'displayModeBar': False}
                                    )
                                ])
                            ], className="map-card desktop-card-40")
                        ], xs=12, lg=4, className="mb-3"),
                        
                        dbc.Col([
                            dbc.Card([
                                dbc.CardHeader(html.H4('CO₂ Emission by Sector'), style={'backgroundColor': '#d1e5f0'}),
                                dbc.CardBody([
                                    dcc.Graph(
                                        figure={}, 
                                        id='vertical-stacked-chart', 
                                        className="mobile-graph-md desktop-graph",
                                        config={'displayModeBar': False}
                                    )
                                ])
                            ], className="map-card desktop-card-40")
                        ], xs=12, lg=4, className="mb-3")
                    ], className="desktop-row-charts")
                ]
            )
        ], className="content-wrapper")
    ], className="main-container"),
    
    dcc.Store(id="store-data", storage_type='memory'),
], style={'backgroundColor': '#f0f0f1'})


# CALLBACK & FUNCTIONS
# Callback 0: Nav items to open and close modal
@app.callback(
        Output('overview-modal', 'is_open'),
        [Input('open-overview', 'n_clicks'), 
         Input("close-overview", "n_clicks")],
        [State("overview-modal", "is_open")],
)
def toggle_modal_overview(open_click, close_click, is_open):
    if open_click or close_click:
        return  not is_open
    return is_open

@app.callback(
        Output('guide-modal', 'is_open'),
        [Input('open-guide', 'n_clicks'), 
         Input("close-guide", "n_clicks")],
        [State("guide-modal", "is_open")],
)
def toggle_modal_guide(open_click, close_click, is_open):
    if open_click or close_click:
        return  not is_open
    return is_open

@app.callback(
        Output('insight-modal', 'is_open'),
        [Input('open-insight', 'n_clicks'), 
         Input("close-insight", "n_clicks")],
        [State("insight-modal", "is_open")],
)
def toggle_modal_insight(open_click, close_click, is_open):
    if open_click or close_click:
        return  not is_open
    return is_open

# Callback 1: Store filter
@app.callback(
        Output('store-data', 'data'),
        [
            Input('year-slider', 'value'),
            Input('continent-dropdown', 'value'),
            Input('country-dropdown', 'value')
        ]
)
def stored_data(clicked_year= [1990,2023], clicked_continent=None, clicked_country= None, clicked_nonrenewable= None, clicked_renewable= None, clicked_other= None):
    filter_copy = full_data
    mask= pd.Series([True] * len(filter_copy)) 

    if clicked_year:
        mask &= (filter_copy['Year'] >= str(clicked_year[0])) & (filter_copy['Year'] <= str(clicked_year[1]))

    if clicked_continent and isinstance(clicked_continent, list):
        mask &= filter_copy['Continent'].isin(clicked_continent)

    if clicked_country and isinstance(clicked_country, list):
        mask &= filter_copy['Entity'].isin(clicked_country)

    filter_copy = filter_copy[mask]
    return filter_copy.to_dict(orient= 'records')

# Callback 2: Chained callback to connect continent and countries filter
@app.callback(
        Output('country-dropdown', 'options'),
        Input('continent-dropdown', 'value')
)
def set_country_options(clicked_continent):
    if clicked_continent:
        chained_country = full_data[full_data['Continent'].isin(clicked_continent)]['Entity'].unique()
    else:
        chained_country = full_data['Entity'].unique()
    return [{'label': i,'value':  i} for i in sorted(chained_country)]

# Chart 1: Line chart for per capita GHG
@app.callback(
    Output('line-chart', 'figure'),
    Input('store-data', 'data')
)
def plot_line_chart(data):
    filter_copy = pd.DataFrame(data)
    filter_copy['Year'] = pd.to_numeric(filter_copy['Year'], errors='coerce')

    if ('Continent' in filter_copy.columns) and (filter_copy['Entity'].nunique() > 10):
        df_grouped = (
            filter_copy
            .groupby(['Continent', 'Year'], as_index=False)
            ['Per capita greenhouse gas emissions in CO₂ equivalents']
            .mean()
        )

        fig = px.line(
            df_grouped,
            x='Year',
            y='Per capita greenhouse gas emissions in CO₂ equivalents',
            color='Continent',
            markers=True,
            color_discrete_sequence=CUSTOM_COLORS
        )
    else:
        fig = px.line(
            filter_copy,
            x='Year',
            y='Per capita greenhouse gas emissions in CO₂ equivalents',
            color='Entity',
            markers=True,
            color_discrete_sequence=CUSTOM_COLORS
        )

    fig.update_layout(
        xaxis_title='Year',
        yaxis_title='GHG emissions (per capita)',
        legend_title='Country / Entity',
        hovermode='x unified',
        template='plotly_white',
        legend= dict(
            orientation= "h",
            yanchor="bottom",
            y=1.0,
            xanchor="center",
            x=0.5,
            title= None,
            font=dict(size=10),
            entrywidth=40,
        ),
    )

    return fig

# Chart 2: Map cholopleth 
@app.callback(
    Output('Choropleth-map', 'figure'),
    Output('ranking-table-container', 'children'),
    [Input('co2-metric-dropdown', 'value'),
    Input('store-data', 'data')]
)
def update_charts(selected_metric, data):
    df = pd.DataFrame(data)

    if selected_metric == "Annual_CO2 (per tonne)":
        metric_col = 'Annual CO₂ emissions'
        title = 'Average Annual CO₂ Emissions by Country Over Time'
        unit = '(tonnes)'
        data = df[['Entity', 'Year', metric_col]].groupby(["Entity"])[metric_col].sum().reset_index().dropna()
    elif selected_metric == "Share of global annual CO₂ emissions":
        metric_col = 'Share of global annual CO₂ emissions'
        title = 'Global Share of Annual CO₂ Emissions Over Time'
        unit = '(%)'
        data = df[['Entity', 'Year', metric_col]].groupby(["Entity"])[metric_col].mean().reset_index().dropna()
    else:
        return px.scatter(title="Invalid selection"), html.Div("Invalid metric selected", className="text-danger")



    median = data[metric_col].median()
    # Define dynamic bins based on the value ranges
    if median < 1_000_000:
        bins = [0, 1000, 10_000, 100_000, 1_000_000, float('inf')]
        labels = ['0 - 1K', '1K - 10K', '10K - 100K', '100K - 1M', '> 1M']
    elif median < 1_000_000_000:
        bins = [0, 1_000_000, 10_000_000, 100_000_000, 1_000_000_000, float('inf')]
        labels = ['0 - 1M', '1M - 10M', '10M - 100M', '100M - 1B', '> 1B']
    else:
        bins = [0, 1_000_000_000, 10_000_000_000, 100_000_000_000, float('inf')]
        labels = ['0 - 1B', '1B - 10B', '10B - 100B', '> 100B']

    # Create a new column 'damage_category' using pd.cut
    data['category'] = pd.cut(
        data[metric_col], 
        bins=bins, labels=labels, 
        include_lowest=True
    )

    data['category'] = pd.Categorical(
        data['category'],
        categories=labels,
        ordered=True
    )


    fig = px.choropleth(
        data,
        locations='Entity',
        locationmode='country names',
        color=metric_col,
        hover_name='Entity',     
        color_continuous_scale=[[0, CUSTOM_COLORS[1]], [0.5, CUSTOM_COLORS[3]], [1, CUSTOM_COLORS[6]]],
        range_color=[data[metric_col].min(), data[metric_col].max()]
    )
    
    fig.update_geos(
        showcoastlines=True,
        fitbounds='locations',
        coastlinecolor="Black",
        showland=True, landcolor="lightgray", visible=False
    )

    fig.update_layout(
        margin=dict(r=0, t=0, l=0, b=0),
        coloraxis_colorbar=dict(
            title=None,
            orientation='h',
            yanchor="bottom",
            y=-0.1,
            xanchor="center",
            x=0.5
        )
    )

    top5 = (
        data
        .sort_values(by=metric_col, ascending=False)
        .head(5)
        .reset_index(drop=True)
    )

    table_header = html.Thead(html.Tr([
            html.Th("Rank", style={'textAlign': 'center','width': '10%'}),
            html.Th("Country", style={'textAlign': 'center','width': '35%'}),
            html.Th("Data", style={'textAlign': 'center', 'width': '55%'})
        ])
    )

    table_body = html.Tbody([
        html.Tr([
            html.Td(i + 1),
            html.Td(row['Entity']),
            html.Td(f"{format_large_value(row[metric_col])} {unit}", style={'textAlign': 'center'})
        ])
        for i, row in top5.iterrows()
    ])

    ranking_table = dbc.Table(
        [table_header, table_body],
        bordered=True,
        hover=True,
        striped=True,
        responsive=True,
        className="shadow-sm mb-0"
    )

    return fig, ranking_table


# Chart 3: Stacked chart based on filter 
@app.callback(
    Output('stacked-bar-chart', 'figure'),
    Input('store-data', 'data')
)
def stacked_chart(data):
    filter_copy = pd.DataFrame(data)
    filter_copy['Year'] = pd.to_numeric(filter_copy['Year'], errors='coerce')
    
    needed_col = ['Entity',
                  'Continent',
                  'Year',
                  'Fossil fuel electricity per capita - kWh (adapted for visualization of chart per-capita-electricity-fossil-nuclear-renewables)',
                  'Nuclear electricity per capita - kWh (adapted for visualization of chart per-capita-electricity-fossil-nuclear-renewables)',
                  'Renewable electricity per capita - kWh (adapted for visualization of chart per-capita-electricity-fossil-nuclear-renewables)'                  
                  ]
    filter_copy =filter_copy[needed_col]
    filter_copy.columns = ['Entity', 'Continent', 'Year', 'Fossil fuel', 'Nuclear', 'Renewables']

    if ('Continent' in filter_copy.columns) and (filter_copy['Entity'].nunique() > 10):
        df_grouped = (
            filter_copy.groupby(['Continent', 'Year'], as_index=False)[['Fossil fuel', 'Nuclear', 'Renewables']]
            .mean()
        )
        
        df_grouped['Total'] = df_grouped[['Fossil fuel', 'Nuclear', 'Renewables']].sum(axis=1)
        for col in ['Fossil fuel', 'Nuclear', 'Renewables']:
            df_grouped[col] = (df_grouped[col] / df_grouped['Total']) * 100

        df_melted = df_grouped.melt(
            id_vars=['Continent', 'Year'],
            value_vars=['Fossil fuel', 'Nuclear', 'Renewables'],
            var_name='Source',
            value_name='Share'
        )

        fig = px.bar(
            df_melted,
            x='Share',
            y='Continent',
            color='Source',
            animation_frame='Year',
            orientation='h',
            labels={'Share': 'Percentage of total electricity generation (%)'},
            color_discrete_sequence=CUSTOM_COLORS
        )
    else:
        filter_copy['Total'] = filter_copy[['Fossil fuel', 'Nuclear', 'Renewables']].sum(axis=1)
        for col in ['Fossil fuel', 'Nuclear', 'Renewables']:
            filter_copy[col] = (filter_copy[col]/ filter_copy['Total']) * 100

        filter_copy_melted = filter_copy.melt(id_vars= ["Entity"],
                                    value_vars= ['Fossil fuel', 'Nuclear', 'Renewables'],
                                    var_name= "Source",
                                    value_name= "Share")
        
        fig= px.bar(
            filter_copy_melted, 
            x= "Share",
            y= "Entity",
            color= "Source", 
            orientation= "h",
            labels= {'Share': "Percentage of total electricity generation (%)."},
            color_discrete_sequence=CUSTOM_COLORS
        )

    fig.update_traces(hoverinfo="none", hovertemplate=None)

    fig.update_layout(
        barmode="stack",
        yaxis=dict(categoryorder="total ascending"),
        yaxis_title=None,
        legend_title_text="Energy Source:",
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.2,
            xanchor="center",
            x=0.5,
            title = None,
            font=dict(size=10),
            itemwidth=30,
        ),
        
    template="plotly_white",
    transition={'duration': 1500, 'easing': 'cubic-in-out'}
    )
    return fig

# Chart 4: Area chart based on power source filter as columns
@app.callback(
    Output('area-chart', 'figure'),
    Input('power-checklist', 'value'),
    Input('store-data','data')
)
def area_chart(selected_power, data):
    filter_copy = pd.DataFrame(data)
    
    rename_map = {
        'Biofuels consumption - TWh': 'Biofuels',
        'Coal consumption - TWh': 'Coal',
        'Gas consumption - TWh': 'Gas',
        'Hydro consumption - TWh': 'Hydro',
        'Nuclear consumption - TWh': 'Nuclear',
        'Oil consumption - TWh': 'Oil',
        'Wind consumption - TWh': 'Wind',
        'Solar consumption - TWh': 'Solar',
        'Other renewables (including geothermal and biomass) - TWh': 'Others',
    }
    filter_copy.rename(columns=rename_map, inplace=True)

    if not selected_power:
        return px.scatter(title="Invalid selection"), html.Div("Invalid metric selected", className="text-danger")
    
    if selected_power:
        based_col = ['Entity', 'Year']
        plot_col = based_col + selected_power
        data= filter_copy[plot_col].dropna()

    wise_data = pd.melt(data,
                        id_vars = ['Entity','Year'],
                        value_vars= selected_power,
                        var_name= "Energy source",
                        value_name= 'Consumption-Twh')
    wise_data = wise_data.groupby(['Year','Energy source'])['Consumption-Twh'].sum().reset_index()
    
    fig = px.area(
        wise_data,
        x= 'Year',
        y=  'Consumption-Twh',
        color= "Energy source",
        color_discrete_sequence=CUSTOM_COLORS
    )
    fig.update_layout(
        yaxis=dict(categoryorder="total ascending"),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.2,
            xanchor="center",
            x=0.5,
            title = None,
            font=dict(size=10),
            itemwidth=40,
        ),
        template="plotly_white")
    return fig

# Chart 5: Stack chart: Total co2 emission by sector
@app.callback(
    Output('vertical-stacked-chart', 'figure'),
    Input('store-data','data')
)
def stacked_chart(data):
    filter_copy = pd.DataFrame(data)
    filter_copy['Year'] = pd.to_numeric(filter_copy['Year'], errors='coerce')

    needed_cols = [
        'Entity',
        'Continent',
        'Year',
        'Carbon dioxide emissions from buildings',
        'Carbon dioxide emissions from other fuel combustion',
        'Carbon dioxide emissions from transport',
        'Carbon dioxide emissions from manufacturing and construction',
        'Fugitive emissions of carbon dioxide from energy production',
        'Carbon dioxide emissions from electricity and heat',
               ]
    filter_copy = filter_copy[needed_cols]

    rename_map = {
        'Carbon dioxide emissions from buildings': 'Buildings',
        'Carbon dioxide emissions from other fuel combustion': 'Fuel combustion',
        'Carbon dioxide emissions from transport': 'Transport',
        'Carbon dioxide emissions from manufacturing and construction': 'Construction',
        'Fugitive emissions of carbon dioxide from energy production': 'Energy production',
        'Carbon dioxide emissions from electricity and heat': 'Electricity & heat',
    }
    filter_copy.rename(columns=rename_map, inplace=True)
    
    emission_cols = [
        'Buildings', 'Fuel combustion',
        'Transport', 'Construction',
        'Energy production', 'Electricity & heat'
    ]

    if filter_copy['Entity'].nunique() > 10:
        grouped = (
            filter_copy.groupby('Continent', as_index=False)[emission_cols]
            .mean(numeric_only=True)
        )
        grouped['Label'] = grouped['Continent']
    else:
        grouped = (
            filter_copy.groupby('Entity', as_index=False)[emission_cols]
            .mean(numeric_only=True)
        )
        grouped['Label'] = grouped['Entity']

    melted = grouped.melt(
        id_vars=['Label'],
        value_vars=emission_cols,
        var_name='Emission sector',
        value_name='Emission'
    )

    fig = px.bar(
        melted,
        x='Label',
        y='Emission',
        color='Emission sector',
        orientation='v',
        labels={'Emission': 'Average CO₂ emission', 'Label': ''},
        color_discrete_sequence=CUSTOM_COLORS
    )

    fig.update_layout(
                barmode="stack",
                yaxis=dict(categoryorder="total ascending"),
                legend=dict(
                    orientation="h",
                    yanchor="bottom",
                    y=1.2,
                    xanchor="center",
                    x=0.5,
                    title = None,
                    font=dict(size=10),
                    itemwidth=30,
                ),
                template="plotly_white",
    )
    return fig

# --- CARD STAT 
@app.callback(
    [
        Output('card-total-co2', 'children'),
        Output('card-top-share', 'children'),
        Output('card-energy', 'children'),
        Output('card-renewable', 'children')
    ],
    Input('store-data', 'data')
)
def update_cards(data):
    import numpy as np
    filtered_data = pd.DataFrame(data)
    if filtered_data.empty:
        return ["-", "-", "-", "-"]

    # --- Total CO₂ emissions ---
    total_co2_str = "N/A"
    if 'Annual CO₂ emissions' in filtered_data.columns:
        filtered_data['Annual CO₂ emissions'] = pd.to_numeric(
            filtered_data['Annual CO₂ emissions'], errors='coerce'
        )
        total_co2 = filtered_data['Annual CO₂ emissions'].sum(skipna=True)
        year_count = filtered_data['Year'].nunique()
        avg_co2 = total_co2 / year_count
        total_co2_str = f"{total_co2 / 1e9:.1f} (tons)"  # gigatonnes

    # ---Top Emitter Share (Top-1 average share) ---
    top_share_str = "N/A"
    if 'Share of global annual CO₂ emissions' in filtered_data.columns:
        share_df = (
            filtered_data.groupby('Entity', dropna=True)['Share of global annual CO₂ emissions']
            .mean()
            .sort_values(ascending=False)
            .reset_index()
        )
        if not share_df.empty:
            top_country = share_df.iloc[0]['Entity']
            top_share_str = f"{top_country}"

    # --- Energy consumption on average ---
    renewable_energy = [
        'Solar consumption - TWh', 'Wind consumption - TWh',
        'Hydro consumption - TWh', 'Nuclear consumption - TWh',
        'Other renewables (including geothermal and biomass) - TWh'
    ]
    nonrenew_energy = [
        'Gas consumption - TWh',
        'Oil consumption - TWh', 
        'Biofuels consumption - TWh',
        'Coal consumption - TWh'
    ]

    renewable_energy = [c for c in renewable_energy if c in filtered_data.columns]
    nonrenew_energy = [c for c in nonrenew_energy if c in filtered_data.columns]
    renewable_str = "N/A"

    if renewable_energy and nonrenew_energy:
        filtered_data[renewable_energy + nonrenew_energy] = filtered_data[renewable_energy + nonrenew_energy].apply(pd.to_numeric, errors='coerce')
        total_renew = filtered_data[renewable_energy].sum().sum(skipna=True)
        total_all = filtered_data[renewable_energy + nonrenew_energy].sum().sum(skipna=True)
        renew_percent = (total_renew / total_all * 100) if total_all > 0 else np.nan
        energy_str = f"{renew_percent:.2f}% (Renewable)"


    # --- Renewable share in electricity generation ---
    renewable_cols = [
        'Solar electricity per capita - kWh (adapted for visualization of chart per-capita-electricity-source-stacked)',
        'Wind electricity per capita - kWh (adapted for visualization of chart per-capita-electricity-source-stacked)',
        'Hydro electricity per capita - kWh (adapted for visualization of chart per-capita-electricity-source-stacked)'
    ]
    nonrenew_cols = [
        'Coal electricity per capita - kWh (adapted for visualization of chart per-capita-electricity-source-stacked)',
        'Gas electricity per capita - kWh (adapted for visualization of chart per-capita-electricity-source-stacked)',
        'Oil electricity per capita - kWh (adapted for visualization of chart per-capita-electricity-source-stacked)',
        'Bioenergy electricity per capita - kWh (adapted for visualization of chart per-capita-electricity-source-stacked)'
    ]

    renewable_cols = [c for c in renewable_cols if c in filtered_data.columns]
    nonrenew_cols = [c for c in nonrenew_cols if c in filtered_data.columns]

    renewable_str = "N/A"
    if renewable_cols and nonrenew_cols:
        filtered_data[renewable_cols + nonrenew_cols] = filtered_data[renewable_cols + nonrenew_cols].apply(pd.to_numeric, errors='coerce')
        total_renew = filtered_data[renewable_cols].sum().sum(skipna=True)
        total_all = filtered_data[renewable_cols + nonrenew_cols].sum().sum(skipna=True)
        renew_percent = (total_renew / total_all * 100) if total_all > 0 else np.nan
        renewable_str = f"{renew_percent:.2f}% (Renewable)"

    return total_co2_str, top_share_str, energy_str, renewable_str


    
    

if __name__ == "__main__":
    app.run(debug= True, port= 8051)