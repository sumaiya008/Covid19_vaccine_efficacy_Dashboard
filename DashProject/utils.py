import plotly.express as px
import pandas as pd
import requests


#https://dash-bootstrap-components.opensource.faculty.ai/docs/components/card/
#https://apify.com/covid-19
#https://www.macrotrends.net/countries/HRV/Bulgaria/population
url = 'https://api.apify.com/v2/key-value-stores/moxA3Q0aZh5LosewB/records/LATEST?disableRedirect=true'

def plot_pie(value, title, color, df):
    new_dict = {}
    for v in df[value].unique():
        value_count = 0
        for i in range(len(df)):
            if df[value][i] == v:
                value_count += 1
        new_dict[v] = value_count
    #     print(new_dict)
    new_df = pd.DataFrame.from_dict(new_dict, orient='index', columns=['Total'])
    if color == 'plasma':
        fig = px.pie(new_df, values='Total',
                     names=new_df.index,
                     title=title,
                     color_discrete_sequence=px.colors.sequential.Plasma,width=750, height=900)
    elif color == 'rainbow':
        fig = px.pie(new_df, values='Total',
                     names=new_df.index,
                     title=title,
                     color_discrete_sequence=px.colors.sequential.Rainbow,width=750, height=900)
    else:
        fig = px.pie(new_df, values='Total',
                     names=new_df.index,
                     title=title,width=750, height=900)
    fig.update_layout(
        title={
            'y': 0.95,
            'x': 0.5
        },
        legend_title=value, template='plotly_dark'
    )
    return fig


def fetchAPI():
    headers = {
        "X-RapidAPI-Key": "09c06425e0mshe6be6e5bba7952bp13c789jsnfa71bb8e5485",
        "X-RapidAPI-Host": "vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers)
    res = response.json()

    totalCases = res.get('totalCases')
    totalDeaths = res.get('totalDeaths')

    new_dict = {}

    for i in range(len(res['casesByState'])):
        res1 = res['casesByState'][i]
        new_dict[res1.get('name')] = res1.get('casesReported')

    return totalDeaths,totalCases,new_dict





