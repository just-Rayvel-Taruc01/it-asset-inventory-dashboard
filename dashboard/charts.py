# Plotly chart functions
import plotly.express as px
import pandas as pd

def device_type_chart(df):
    return px.pie(df, names='device_type', title='Device Count by Type')

def license_status_chart(df):
    return px.bar(df, x='renewal_status', title='License Compliance Status')

def software_distribution_chart(df):
    return px.bar(df, x='vendor', y='version', title='Software Distribution by Vendor')
