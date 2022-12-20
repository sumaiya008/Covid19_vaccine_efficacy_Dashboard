from dash import Dash, html, dcc, Input, Output
from utils import plot_pie, fetchAPI
import dash_bootstrap_components as dbc
import pycountry
import plotly.graph_objects as go
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

import seaborn as sns
import datetime
import warnings
from matplotlib import pyplot as plt
import numpy as np
from plotly.subplots import make_subplots

warnings.filterwarnings("ignore")

import pycountry
import plotly.express as px
import pandas as pd

df = pd.read_csv('D:\Data_Visulization\Project1\Visual_Analytics_Project_1\dfFirst.csv')
df3 = pd.read_csv('D:\Data_Visulization\Project1\Visual_Analytics_Project_1\df3.csv')
df4 = pd.read_csv('D:\Data_Visulization\Project1\Visual_Analytics_Project_1\df4.csv')

app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

eff_dropDownList = ['efficacy_ancestral_alpha_severe_', 'efficacy_ancestral_alpha_infection_',
                    'efficacy_beta_gamma_delta_severe_', 'efficacy_beta_gamma_delta_infection_',
                    'efficacy_omicron_severe_', 'efficacy_omicron_infection_']

breakThrough_dropDownList = ['breakThrough_ancestral_alpha_severe_', 'breakThrough_ancestral_alpha_infection_',
                             'breakThrough_beta_gamma_delta_severe_', 'breakThrough_beta_gamma_delta_infection_',
                             'breakThrough_omicron_severe_', 'breakThrough_omicron_infection_']

state_list = ['Alabama', 'Alaska', 'American Samoa', 'Arizona', 'Arkansas', 'California', 'Colorado',
              'Connecticut', 'Delaware', 'District of Columbia', 'Florida', 'Georgia',
              'Guam', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky',
              'Louisiana', 'Maine', 'Marshall Islands', 'Maryland', 'Massachusetts', 'Michigan', 'Micronesia',
              'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey',
              'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Northern Marianas', 'Ohio', 'Oklahoma',
              'Oregon', 'Palau', 'Pennsylvania', 'Puerto Rico', 'Rhode Island', 'South Carolina', 'South Dakota',
              'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virgin Islands', 'Virginia', 'Washington', 'West Virginia',
              'Wisconsin', 'Wyoming']

card_icon = {
    "color": "red",
    "textAlign": "center",
    "fontSize": 18,
    "margin": "auto",
}
card_icon1 = {
    "color": "purple",
    "textAlign": "center",
    "fontSize": 18,
    "margin": "auto",
}

Vaccine_dropdown = dcc.Dropdown(options=df['Vaccine_Manu'
                                           'facturer'].unique(),
                                value='Pfizer/BioNTech', style={'width': '50%', 'textAlign': 'center'},
                                placeholder='Select the vaccine Manufacturer')

Vaccine_dropdown2 = dcc.Dropdown(options=df['Vaccine_Manufacturer'].unique(),
                                 value='Pfizer/BioNTech', style={'width': '60%', 'textAlign': 'center'})

eff_dropDown = dcc.Dropdown(options=eff_dropDownList,
                            value='efficacy_ancestral_alpha_severe_', style={'width': '50%', 'textAlign': 'center'})

bT_dropDown = dcc.Dropdown(options=breakThrough_dropDownList,
                           value='breakThrough_ancestral_alpha_severe_', style={'width': '50%', 'textAlign': 'center'})

# stateDropDown = dcc.Dropdown(options=state_list,
#                            value='State List')

totalDeaths, totalCases, new_dict = fetchAPI()

app.layout = html.Div(children=[

    html.Div(
        [
            dbc.CardGroup(
                [

                    dbc.Card(
                        [
                            dbc.CardBody([
                                html.P("Total Death in United States", className="card-text", style=card_icon),
                                dbc.Button(1095074, color="danger", className="mt-auto"
                                           ), ]
                            ),

                        ],
                        style={"width": "18rem"},
                    ),

                    dbc.Card(
                        [
                            dbc.CardBody([
                                html.P("Total Cases in United States", className="card-text", ),
                                dbc.Button(99624169, color="warning", className="mt-auto"
                                           ), ]
                            ),

                        ],
                        style={"width": "18rem"},
                    ),

                    dbc.Card(
                        [
                            dbc.CardBody([
                                html.P("Total Cases In New York", className="card-text", style=card_icon1),
                                dbc.Button(new_dict.get('New York', None), color="success", className="mt-auto"
                                           ), ]
                            ),

                        ],
                        style={"width": "18rem"},
                    ),

                    dbc.Card(
                        [
                            dbc.CardBody([
                                html.P("Total Cases In New Jersey", className="card-text"),
                                dbc.Button(new_dict.get('New Jersey', None), color="success", className="mt-auto"
                                           ), ]
                            ),

                        ],
                        style={"width": "18rem"},
                    ),
                    dbc.Card(
                        [
                            dbc.CardBody([
                                html.P("Total Cases In California", className="card-text", style=card_icon1),
                                dbc.Button(new_dict.get('California', None), color="success", className="mt-auto"
                                           ), ]
                            ),

                        ],
                        style={"width": "18rem"},
                    ),

                    dbc.Card(
                        [
                            dbc.CardBody([
                                html.P("Total Cases In Connecticut", className="card-text"),
                                dbc.Button(new_dict.get('Connecticut', None), color="success", className="mt-auto"
                                           ), ]
                            ),

                        ],
                        style={"width": "18rem"},
                    ),

                ]
            )]),

    html.Div([
        html.H1(children='Vaccine Administrated Globally',style={'textAlign': 'center', 'color': 'red'}),
        html.H5(children='Select Vaccine Manufacturer'),
        Vaccine_dropdown,
        dcc.Graph(
            id='graph1',
        ),
    ]),
    html.Div([
        html.H1(children='Treemap',style={'textAlign': 'center'}),
        dcc.Graph(
            id='graph2',
        ),
    ]),
    html.Div([
        html.H1(children='Vaccine  Globally Bubble chart'),
        Vaccine_dropdown2,
        html.Div(children=[
            dcc.Graph(id="graph4", style={'display': 'inline-block'}),
            dcc.Graph(id="graph8", style={'display': 'inline-block'}),

        ]),
    ]),

    html.Div(className='row', children=[
        # html.H1(children='Efficacy and Break Through - Test')
        html.H4(children='Vaccination Over the World', style={'textAlign': 'center'}),

        html.Div(children=[
            dcc.Graph(id="graph3", style={'display': 'inline-block'}),
            dcc.Graph(id="graph7", style={'display': 'inline-block'})

        ]),
    ]),

    html.Div(className='row', children=[
        html.H1(children='Efficacy and Break Through',style={'textAlign': 'center'}),
        eff_dropDown, bT_dropDown,

        html.Div(children=[
            dcc.Graph(id="graph5", style={'display': 'inline-block'}),
            dcc.Graph(id="graph6", style={'display': 'inline-block'})

        ]),
    ]),

])


@app.callback(
    [Output('graph1', 'figure'), Output('graph2', 'figure'), Output('graph3', 'figure'), Output('graph4', 'figure'),
     Output('graph5', 'figure'), Output('graph6', 'figure'), Output('graph7', 'figure'), Output('graph8', 'figure')],
    Input(component_id=Vaccine_dropdown, component_property='value'),
    Input(component_id=Vaccine_dropdown2, component_property='value'),
    Input(component_id=eff_dropDown, component_property='value'),
    Input(component_id=bT_dropDown, component_property='value')
)
def update_graph(selected_geography, Vaccine_dropdown2, eff_dropDown, bT_dropDown):
    # MAP
    df1_grouped = df.groupby('Vaccine_Manufacturer')
    vaccine_group = df1_grouped.get_group(selected_geography)
    list_countries = vaccine_group['Country'].unique().tolist()
    country_cnt = len(vaccine_group['Country'].unique())
    d_country_code = {}

    for country in list_countries:
        try:
            country_data = pycountry.countries.search_fuzzy(country)
            country_code = country_data[0].alpha_3
            d_country_code.update({country: country_code})
        except:
            print('could not add ISO 3 code for ->', country)
            d_country_code.update({country: ' '})

    for k, v in d_country_code.items():
        vaccine_group.loc[(vaccine_group.Country == k), 'iso_alpha'] = v

    fig = px.choropleth(data_frame=vaccine_group,
                        locations="iso_alpha",
                        color="Vaccine_Manufacturer",
                        color_continuous_scale=px.colors.sequential.Reds,
                        hover_name="Vaccine_Manufacturer")
    fig.update_layout(
        title_text="Countries {}".format(country_cnt), template='plotly_dark')

    # figure1 Tree
    vaccine_count = df.groupby("Vaccine_Manufacturer")["Country"].nunique()
    Vaccine_Manufacturer_count = pd.DataFrame(
        {'Vaccine_Manufacturer': vaccine_count.index, 'Count': vaccine_count.values})

    fig_1 = px.treemap(
        Vaccine_Manufacturer_count, path=["Vaccine_Manufacturer", "Count"], values="Count", template='plotly_dark')
    fig_1.update_traces(root_color="black")

    # figure2  Total Vaccination With Respect to Country and Manufacturer
    fig2 = px.bar(df3, x="Country", y="Vaccine_Wise_Max_Total_Vaccination", color="Vaccine_Manufacturer",
                  title="Total Vaccination With Respect to Country and Manufacturer", width=750, height=900,
                  template='plotly_dark')

    # figure3 Bubble chart for vaccine
    total = df.groupby(['Country', 'Vaccine_Manufacturer'])['Vaccine_Wise_Max_Total_Vaccination']
    total = total.first()
    total = total.reset_index()
    total = total.groupby('Vaccine_Manufacturer')

    Oxford = total.get_group(Vaccine_dropdown2)
    fig3 = px.scatter(Oxford, x='Country', y='Vaccine_Wise_Max_Total_Vaccination',
                      size='Vaccine_Wise_Max_Total_Vaccination', color="Country",
                      hover_name="Vaccine_Manufacturer", size_max=70, title="Vaccine Name- " + Vaccine_dropdown2,
                      template='plotly_dark', width=750, height=900)

    # figure4  Efficacy
    fig4 = px.bar(df3, y="Country", x=eff_dropDown, color='Vaccine_Manufacturer',
                  title="Efficacy With Respect to Variant", orientation='h', width=750, height=900, text=eff_dropDown,
                  template='plotly_dark')

    # figure5 Break Through
    fig5 = px.bar(df3, y="Country", x=bT_dropDown, color='Vaccine_Manufacturer',
                  title="Break through With Respect to Variant",
                  orientation='h', width=750, height=900, text=bT_dropDown, template='plotly_dark')

    # Country Wise Total Vaccination
    total = df4.groupby(['Country'])['vaccinated_pop_21'].sum().rename('vaccinated_pop_21').reset_index()
    total = total.round(2)
    fig6 = px.bar(total, y="Country", x='vaccinated_pop_21', title="Percentage of Vaccination for Year 2021", width=750, height=900,
                  text='vaccinated_pop_21',
                  orientation='h', template='plotly_dark', color='Country',
                  color_discrete_sequence=px.colors.sequential.Plasma)

    # Pie Chart
    fig7 = plot_pie('Vaccine_Manufacturer', 'Various vaccines and their uses', 'plasma', df)

    return fig, fig_1, fig2, fig3, fig4, fig5, fig6, fig7


if __name__ == '__main__':
    app.run_server(debug=True)
