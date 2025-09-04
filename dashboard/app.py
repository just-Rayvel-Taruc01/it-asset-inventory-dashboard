# Streamlit dashboard app

import os
import streamlit as st
import pandas as pd
from charts import device_type_chart, license_status_chart, software_distribution_chart

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def load_data(filename):
    return pd.read_csv(os.path.join(BASE_DIR, "data", filename))

def save_data(filename, df):
    df.to_csv(os.path.join(BASE_DIR, "data", filename), index=False)

def dashboard_tab(assets, licenses, software):
    st.header("Device Breakdown")
    st.plotly_chart(device_type_chart(assets))
    st.header("License Compliance Status")
    st.plotly_chart(license_status_chart(licenses))
    st.header("Software Distribution")
    st.plotly_chart(software_distribution_chart(software))

def manage_table(df, cols, filename, item_name):
    st.subheader(f"{item_name} Table")

    # Search with unique key
    search = st.text_input(f"Search {item_name}", key=f"search_{item_name}")
    if search:
        df = df[df.apply(lambda row: row.astype(str).str.contains(search, case=False).any(), axis=1)]
    st.dataframe(df)

    # Add new record
    st.subheader(f"Add New {item_name}")
    with st.form(f"add_{item_name}"):
        new_data = {}
        for col in cols:
            new_data[col] = st.text_input(col, key=f"add_{item_name}_{col}")
        submitted = st.form_submit_button("Add")
        if submitted:
            if not any([v == '' for v in new_data.values()]):
                if 'id' in cols and new_data.get('id') in df.get('id', []):
                    st.error("Duplicate ID!")
                else:
                    df = pd.concat([df, pd.DataFrame([new_data])], ignore_index=True)
                    save_data(filename, df)
                    st.success(f"{item_name} added!")
            else:
                st.error("All fields required.")

    # Edit/Delete record
    st.subheader(f"Edit/Delete {item_name}")
    selected_idx = st.number_input(
        f"Select row to edit/delete (0-{len(df)-1})",
        min_value=0, max_value=max(0, len(df)-1), step=1,
        key=f"row_selector_{item_name}"
    )

    if len(df) > 0:
        selected_row = df.iloc[selected_idx]
        with st.form(f"edit_{item_name}"):
            edit_data = {}
            for col in cols:
                edit_data[col] = st.text_input(col, value=str(selected_row[col]),
                key=f"edit_{item_name}_{col}_{selected_idx}")
            c1, c2 = st.columns(2)
            with c1:
                update = st.form_submit_button("Update")
            with c2:
                delete = st.form_submit_button("Delete")
            
            if update:
                for col in cols:
                    df.at[selected_idx, col] = edit_data[col]
                save_data(filename, df)
                st.success(f"{item_name} updated!")
            if delete:
                df = df.drop(selected_idx).reset_index(drop=True)
                save_data(filename, df)
                st.success(f"{item_name} deleted!")

def main():
    st.title("IT Asset Inventory Dashboard")
    tabs = st.tabs(["Dashboard", "Manage Assets", "Manage Licenses", "Manage Software"])

    assets = load_data('sample_assets.csv')
    licenses = load_data('sample_licenses.csv')
    software = load_data('sample_software.csv')

    with tabs[0]:
        dashboard_tab(assets, licenses, software)
    with tabs[1]:
        manage_table(assets, list(assets.columns), 'sample_assets.csv', 'Asset')
    with tabs[2]:
        manage_table(licenses, list(licenses.columns), 'sample_licenses.csv', 'License')
    with tabs[3]:
        manage_table(software, list(software.columns), 'sample_software.csv', 'Software')

if __name__ == "__main__":
    main()
