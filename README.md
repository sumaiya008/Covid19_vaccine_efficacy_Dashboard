# Covid19 Vaccine Efficacy Dashboard

Understanding the level of protection within a population against Covid-19 is crucial. 
Two key metrics—breakthrough infection rates and the percentage of vaccines that do not offer complete protection—provide valuable insights into the susceptibility of vaccinated individuals. 
However, these metrics are significantly influenced by the efficacy of the vaccines available.

This dashboard delves into breakthrough infection rates and the percentage of vaccines that do not provide full protection across various countries. It examines these metrics concerning specific vaccine and Covid-19 variants, offering a comprehensive view of how they evolve over time. By analyzing this data, we can better understand vaccine effectiveness in different contexts, enabling informed decision-making and the implementation of necessary measures to combat the pandemic.

### Technical Details:

 - Tech Stack: Python (Dash, Plotly, Pandas), HTML/CSS
 - Process Overview:
   - Compiled data from various tables available at ourworldindata.org/covid-vaccinations
   - Exported the data as CSV files
   - Imported the CSV files into Pandas DataFrames for further analysis
   - Conducted extensive data manipulations, including imputation techniques for missing values and calculations to determine breakthrough rates, using Python
   - Visualized the data using Plotly
   - Developed a dashboard using Dash to present the visualizations
