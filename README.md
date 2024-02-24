# Personal project: Web scrapper + ETL + EDA + ML.

<img src="https://support.musicgateway.com/wp-content/uploads/2021/04/Copy-of-800-x-500-Blog-Post-5-4.png" alt="2hand" style="width:350px;"/>


## Project Description

<br>

### Data Capture and Cleaning Process Overview

## [project_1 from_web_to_csv](https://github.com/albertjimrod/personal_proj_hispasonic/blob/main/project_1/01_from_web_to_csv_togit.ipynb):

This project outlines the step-by-step process followed to capture and clean data from the Hispasonic website. Starting from scratch, the project involved understanding the necessary steps and strategies to condense advertisement information into a CSV file effectively.

### Objective

The primary objective was to gather data from the Hispasonic website and ensure it is cleaned and structured appropriately for further analysis. This involved identifying the most effective libraries and functions to achieve the desired outcome.

### Technologies Used

- **Python**: The primary programming language used for data capture and cleaning tasks.
- **Web Scraping Libraries**: Utilized for extracting data from web pages effectively.
- **Pandas**: Leveraged for data manipulation and cleaning tasks, facilitating the organization of extracted data.
- **CSV Files**: Used as the output format for storing cleaned data.

### Workflow

1. **Data Capture**: The process begins with scraping data from the Hispasonic website, extracting relevant advertisement information.
2. **Data Cleaning**: Extracted data is cleaned and standardized, ensuring consistency and removing any irrelevant or erroneous information.
3. **File Creation**: The cleaned data is then saved into a CSV file, providing a structured format for future analysis and insights.


By following a systematic approach to data capture and cleaning, the project successfully condensed advertisement information from the Hispasonic website into a CSV file. This structured dataset serves as a valuable resource for further analysis, enabling insights and decision-making processes.

<br>

### From `csv` to database `PostgreSQL`

## [project_2 from_csv_database (PostgreSQL)](https://github.com/albertjimrod/personal_proj_hispasonic/blob/main/project_2/02_from_csv_to_PostgreSQL.ipynb) :

### Project Overview

This project focuses on the initial phase of ETL (Extract, Transform, Load), specifically loading data into a PostgreSQL database. This pivotal step sets the stage for effective data management, paving the way for future transformations and advanced analysis.

### Objective

The primary objective is to extract data from various sources, transform it as needed, and load it into a PostgreSQL database. By accomplishing this, we create a structured dataset ready for further exploration and insights.

### Technologies Used

- **Jupyter Notebook**: The primary environment for executing Python code and documenting the process.
- **Python**: Utilized for data extraction, transformation, and loading tasks.
- **PostgreSQL**: The chosen database management system for storing the transformed data.

### Workflow

1. **Extraction**: Data is extracted from diverse sources, such as HTML files containing ad listings.
2. **Transformation**: Extracted data is cleaned, standardized, and organized into a structured format suitable for database storage.
3. **Loading**: The transformed data is loaded into a PostgreSQL database, ensuring it is readily accessible for future analysis.


By loading the dataset into a PostgreSQL database, we establish a solid foundation for subsequent analysis and insights. This process streamlines data management, enabling efficient transformations and facilitating advanced analytical tasks.

<br>

###  SMART Questions:

## [project_3 General guidelines in relation to the data obtained](https://github.com/albertjimrod/personal_proj_hispasonic/blob/main/project_3/Questions/SMART_Q.md):

These are the points that will be touched on in the process:

1. **Descriptive Analysis**:
   - What is the distribution of selling prices in the dataset?
   - Are there any outliers in the sales data?
   - How are sales distributed by city and product?

2. **Visualizations**:
   - How does the selling price vary by city?
   - What is the best-selling brand and its price distribution?
   - Is there any relationship between the number of views and sales by product and city?

3. **Correlation Analysis**:
   - Is there a correlation between the number of views and sales by product and city?
   - Is there any correlation between selling price and geographical location?

4. **Predictive Modeling**:
   - Is it possible to predict sales based on the date of the ad and other variables?
   - Which variables are most predictive for anticipating product sales?

5. **Data Segmentation**:
   - Can segments of sellers or buyers be identified based on their behavior?
   - Are there specific sales patterns in certain product or city segments?

6. **Temporal Analysis**:
   - How do sales vary over time?
   - Are there seasonal trends in sales activity?
   - Are there days of the week or months when sales activity is particularly active?

7. **Geographical Analysis**:
   - How are sales distributed geographically?
   - Is there any relationship between geographical location and selling price?
   - Which cities stand out in terms of sales volume or selling prices?

8. **Text Analysis**:
   - What keywords or common characteristics appear most frequently in successful ads?
   - Can the probability of sale be predicted based on the product description?
   - Is there any relationship between the quality of the product description and its success in sales?
  


### Hypothesis Development

After addressing these questions, the next step is to formulate hypotheses based on the insights gained from the data analysis. These hypotheses will guide further experimentation, testing, and decision-making in your project.

<br>


###  **ETL (Extract, Transform, Load): An Introduction**

## [project_4 ETL (Extract Transform Load) Hispasonic](https://github.com/albertjimrod/personal_proj_hispasonic/blob/main/project_4/ETL_scrapped_data_folders_to_csv.ipynb):
 

  ETL, which stands for Extract, Transform, Load, is a process commonly used in data warehousing and analytics to prepare and consolidate data from various sources for analysis and reporting purposes.

- **Extract**: In the extraction phase, data is gathered and extracted from multiple sources, which can include databases, files, APIs, and other repositories. This step involves identifying and retrieving relevant data sets needed for analysis.

- **Transform**: Once the data is extracted, it often needs to be transformed to make it suitable for analysis. Transformation involves cleaning, filtering, aggregating, and structuring the data to ensure consistency and accuracy. This step may also include enriching the data by combining it with other sources or performing calculations and derivations.

- **Load**: After the data has been extracted and transformed, it is loaded into a target destination, such as a data warehouse, database, or data lake. This final step ensures that the processed data is stored in a structured format, making it accessible for querying, analysis, and reporting.

    ETL plays a critical role in data integration and preparation, enabling organizations to centralize and harmonize disparate data sources, improve data quality, and derive valuable insights for decision-making.

<br>

###  **EDA (Exploratory Data Analysis)**

## [project_5 EDA](https://github.com/albertjimrod/personal_proj_hispasonic/blob/main/project_5/EDA_hispasonic.ipynb)


Exploratory Data Analysis (EDA) is a crucial preliminary step in the data analysis process, where the main objective is to gain insights and understand the underlying patterns, trends, and relationships within a dataset. It involves systematically examining and visualizing the data to uncover interesting features, detect anomalies, and formulate hypotheses for further investigation.

During EDA, various statistical and graphical techniques are employed to summarize the main characteristics of the data, including its distribution, central tendency, variability, and correlations between variables. Common EDA techniques include descriptive statistics, histograms, scatter plots, box plots, and correlation matrices.

The process typically begins by loading the dataset and performing basic data cleaning tasks, such as handling missing values, removing duplicates, and transforming data types if necessary. Once the data is cleaned, analysts proceed to explore individual variables and their relationships with one another.

EDA plays a critical role in guiding subsequent data modeling and hypothesis testing efforts. By understanding the structure and nature of the data, analysts can make informed decisions about which analytical techniques and algorithms are most appropriate for extracting meaningful insights and building predictive models.

In summary, EDA serves as a fundamental exploration phase that lays the groundwork for more advanced data analysis tasks. It empowers analysts to uncover hidden patterns, identify potential problems or biases in the data, and ultimately derive actionable insights to inform decision-making processes.







