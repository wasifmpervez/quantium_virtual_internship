from dash import Dash, html, dcc, Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd


# ---------- Data Cleaning and Visualization ----------
sales_df = pd.read_csv("data/combined_data.csv")

# sort df
sales_df["date"] = pd.to_datetime(sales_df["date"])
sales_df = sales_df.sort_values(by=["date"])

# list for regional filtering
regions_list = [x.capitalize() for x in list(sales_df["region"].unique())]
regions_list.append("All")


# -------------------- Components --------------------
color_picker = {
    "primary": "#AA8CDB",
    "secondary": "#8CD3DB",
    "font": "#FFFFFF"
}

# app
app = Dash(__name__, external_stylesheets=[dbc.themes.LITERA])

# title
title = html.H1(
    children="Pink Morsel Sales",
    style={
        "background-color": color_picker["primary"],
        "color": color_picker["font"],
        "padding": "20px"
    },
    id="title"
)

# subtitle
subtitle = html.Div(
    children="A look at sales of Soul Foods Pink Morsel candies from 2018 to 2022.",
    style={
        "margin-left": "20px",
        "margin-top" : "15px"
    }
)

# radio button, title, wrapper
region_list_CTA = html.Div(
    children="Filter by region:",
    style={"font-weight": "bold"}
)

region_list = dcc.RadioItems(
    options=[
        {"label": "North", "value": "north"},
        {"label": "East", "value": "east"},
        {"label": "South", "value": "south"},
        {"label": "West", "value": "west"},
        {"label": "All", "value": "all"}
    ],
    value="all",
    id="regions-radio",
    inline=True,
    labelStyle={
        "margin-right": "20px"
    },
    inputStyle={
        "margin-right": "5px"
    }
)

region_list_wrapper = html.Div(
    children=[
        region_list_CTA,
        region_list
    ],
    style={
        "margin-left": "20px"
    }
)

# visualization
fig = px.line(sales_df, x="date", y="sales")
visualization = dcc.Graph(
        id="visualization"
    )

@app.callback(
    Output("visualization", "figure"),
    Input("regions-radio", "value")
)
def update_graph(selected_region):
    if selected_region == "all":
        filtered_df = sales_df
    else:
        region_filter = sales_df["region"] == selected_region.lower()
        filtered_df = sales_df[region_filter]
    
    fig = px.line(filtered_df, x="date", y="sales")
    return fig

app.layout = html.Div(
    children=[
        title,
        subtitle,
        visualization,
        region_list_wrapper
    ]
)

if __name__ == '__main__':
    app.run(debug=True)