# **Challenge Setter: UNCCD & G20 Global Land Initiative**  
## **Sustainable Land Management and Restoration in the Sahel**  

### **Note**  
- [Draft Project Submission](https://docs.google.com/document/d/1iaRqgNmD3w2Ojq2UBqUM5K4QYVadbyZqg1DRbO_yDdI/edit?usp=sharing)

## **Team: VII Technologies**  
**Slogan**: VII Technologies | Innovate For Future
### **Members:**  
- Gerhardt Lutterodt  
- Suphawadee Bunthot  

## **Overview**  
This project aims to assess and visualize high-risk zones for land degradation, drought, and climate change in the Sahel by leveraging Earth observation data. We provide insurance agencies and stakeholders with data-driven insights to improve risk assessment and design insurance products tailored for farmers, herders, and pastoralist groups. The project integrates satellite imagery, climate data, and a **Land Degradation Risk Dashboard** to support better land management and sustainable solutions.

## **Approach**  
We utilize **satellite imagery** and **climate data** to create an **interactive risk assessment dashboard** that highlights vulnerable areas in the Sahel. This dashboard is designed to visualize degradation risk, drought susceptibility, and environmental changes, helping stakeholders make informed decisions about land management and insurance pricing.

## **Key Features**  
✅ **Interactive Risk Map** – A dynamic map displaying degradation and drought risk across regions.  
✅ **Risk Assessment Profiles** – Detailed insights on land degradation trends and climate risk.  
✅ **Land Degradation & Drought Analysis** – Visualization of historical trends, future projections, and actionable insights.

## **Methodology**  
### **Data Acquisition & Processing**  
- **MODIS Land Cover Change Data (MCD12Q1)** – Identifying desertification trends.  
- **CHIRPS Climate Precipitation Data** – Understanding drought-prone regions.  

### **Data Analysis & Visualization**  
- **Data Processing**: Using **Python** with **Pandas**, **NumPy**, **Geopandas**, and **Rasterio** for handling geospatial data and satellite imagery.  
- **Visualization**: Generating interactive **risk heatmaps** and risk profiles with **Plotly** and **Streamlit** for a user-friendly dashboard.

### **Final Implementation**  
## **Land Degradation Risk Dashboard Overview**

The **Land Degradation Risk Dashboard** is a Streamlit-based interactive tool designed to visualize land degradation risk across different regions. Users can upload .tif files containing geospatial data, and the app generates insights into degradation risk profiles using interactive maps.

### **Key Features**

- **File Upload:**
  - Upload one or multiple .tif files containing land cover data.
  - Each .tif file represents raster data for a specific year (e.g., 2010, 2011, ..., 2023).

- **Data Processing:**
  - Uses the `rasterio` library to process the uploaded .tif files.
  - Extracts geographic coordinates and degradation risk values from raster bands.

- **Visualization:**
  - **Heatmap**: Visualizes degradation risk data on an interactive Plotly map. The risk is represented by the color and size of points, with animation options if multiple files are uploaded.
  - **Risk Profiles Table**: A table that shows regions sorted by degradation risk, helping users identify high-risk areas.

- **Interactive User Interface:**
  - Users can upload .tif files via the sidebar, and the map and table automatically update.
  - Multiple file uploads enable map animation to show changes in degradation risk over time.

### **Key Insights**
- Identifies regions with the highest degradation risk, which can inform policy and intervention strategies.
- Analyzes trends in land degradation risk over time and visualizes spatial patterns.

### **Conclusion and Recommendations**
- High-risk regions require urgent intervention.
- Sustainable land management strategies can help mitigate risks.
- Insurance pricing and policy-making can be adjusted based on real-time data insights.

### **Technical Details**

- **Libraries Used:**
  - Streamlit: For building the interactive web app.
  - Plotly: For creating interactive map visualizations.
  - Pandas: For data manipulation and table creation.
  - Rasterio: For reading and processing .tif raster files.
  - Numpy: For numerical operations and array handling.

- **How It Works:**
  - The app accepts .tif files via the file uploader in the sidebar.
  - Raster data is read and processed to extract longitude, latitude, and degradation risk values.
  - The risk values are visualized on a map, with animation options for multiple files.

### **Future Enhancements**

- **Additional Data Formats:** Support for more file types (e.g., GeoTIFF, shapefiles) to enhance versatility.
- **Advanced Analytics:** Incorporate risk predictions based on historical trends to improve analytics.
- **User Feedback and Interaction:** Allow users to define regions of interest or focus on specific time periods for more tailored analysis.

### **Usage Instructions**
1. Clone or download the repository from GitHub.
2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Run the app:
    ```bash
    streamlit run app.py
    ```
4. Upload one or multiple .tif files with land cover and degradation risk data.
5. Explore the interactive heatmap and risk profiles.

### **Possible Applications**
- **Environmental Research:** A tool for researchers to analyze land degradation risk over time.
- **Policy Making:** Government agencies and organizations can identify regions needing sustainable management or conservation.
- **Insurance and Risk Assessment:** Assess land-based risk for industries like agriculture and insurance.


## **Contributions & Contact**  
Contributions are welcome! Please submit a pull request or open an issue. Feel free to contact us for any inquiries.