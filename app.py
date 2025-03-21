import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
import rasterio

# --- Streamlit App Title and Sidebar ---
st.title("Land Degradation Risk Dashboard")
st.sidebar.header("Upload Data")

# File uploader for multiple .tif files
uploaded_files = st.sidebar.file_uploader("Upload .tif Files with Land Cover Data", type=["tif"], accept_multiple_files=True)

# --- Data Processing ---
if uploaded_files:
    # Initialize an empty list to store DataFrames for each year
    df_list = []

    # Process each uploaded .tif file (one for each year)
    for uploaded_file in uploaded_files:
        year = uploaded_file.name.split('_')[-1].split('.')[0]  # Extract the year from the file name
        with rasterio.open(uploaded_file) as src:
            # Assuming degradation risk is encoded in the first band (band 1)
            band1 = src.read(1)
            transform = src.transform
            
            # Get the dimensions of the raster data
            rows, cols = band1.shape
            
            # Generate coordinates for each pixel (latitude, longitude)
            lon, lat = np.meshgrid(np.arange(0, cols), np.arange(0, rows))
            lon = lon * transform[0] + transform[2]  # Longitude calculation
            lat = lat * transform[4] + transform[5]  # Latitude calculation
            
            # Flatten the arrays to create a DataFrame
            coords = np.column_stack([lon.flatten(), lat.flatten(), band1.flatten()])
            df = pd.DataFrame(coords, columns=["Longitude", "Latitude", "Degradation_Risk"])

            # Add a column for the year based on the file name
            df["Year"] = year

            # Optionally, you can add unique region identifiers or use grid-based regions
            df["Region"] = [f"Region {i}" for i in range(1, len(df) + 1)]

            # Append the DataFrame for this year to the list
            df_list.append(df)

    # Combine all DataFrames into one (if multiple files are uploaded, or just the single file)
    full_df = pd.concat(df_list, ignore_index=True)

    # --- Risk Heatmap ---
    st.subheader("Risk Heatmap")
    fig = px.scatter_mapbox(full_df, 
                            lat="Latitude", lon="Longitude", 
                            size="Degradation_Risk", 
                            color="Degradation_Risk", 
                            hover_name="Region", 
                            color_continuous_scale="reds", 
                            size_max=15, zoom=2,
                            animation_frame="Year" if len(uploaded_files) > 1 else None)  # Only animate if multiple files
    fig.update_layout(mapbox_style="carto-positron", height=500)
    st.plotly_chart(fig)

    # --- Risk Analysis Table ---
    st.subheader("Risk Profiles by Region Over Time")
    st.dataframe(full_df.sort_values(by="Degradation_Risk", ascending=False))

    # --- Conclusion ---
    st.markdown("### Key Takeaways")
    st.markdown("- High-risk regions require urgent intervention.")
    st.markdown("- Sustainable land management strategies can mitigate risks.")
    st.markdown("- Insurance pricing can be adjusted based on real-time data insights.")

else:
    st.warning("Please upload one or more .tif files to get started.")
