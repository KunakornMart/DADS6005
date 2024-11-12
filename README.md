# DADS6005 : Data Streaming and Real Time Analytics
This exam demonstrates a real-time data streaming and analytics platform, built with a series of integrated tools: **Apache Kafka**, **ksqlDB**, **Apache Pinot**, and **Streamlit**. The objective is to ingest, process, and visualize large-scale, real-time data from various sources, using a series of transformations and aggregations for meaningful insights.

## Project Structure
1. **Data Sources**: 
   - **Page Views**: Records of user activity on various pages.
   - **User Demographics**: User details including region and gender.
   - **Regional Data**: Static data for each region, including population and area size.

2. **Data Processing with ksqlDB**: 
   - ksqlDB streams and tables were created to process and enrich the data.
   - Operations include joining data sources, windowed aggregations (tumbling, hopping, and session windows), and data cleaning.

3. **Data Storage with Apache Pinot**:
   - Pinot tables store processed data, enabling fast analytical queries.
   - Each table corresponds to a specific transformation, e.g., **Session Window Analysis** or **Region Page Summary**.

4. **Visualization with Streamlit**:
   - The dashboard displays real-time insights, including metrics like average session length, total page visits by region, and page views over time.
   - Users can filter by region and gender, and view updated metrics every few seconds.

## Key Components and Functionality
1. **Apache Kafka**: Acts as the main data pipeline, transporting messages from different data sources to processing modules.
2. **ksqlDB**: Executes SQL-based transformations on streaming data for data enrichment and aggregations.
3. **Apache Pinot**: Serves as the backend for querying pre-aggregated data, ensuring low-latency responses.
4. **Streamlit Dashboard**: Provides an interactive and real-time visualization interface.

## Setup Instructions
1. **Environment Setup**:
    - Ensure Docker and Docker Compose are installed on your environment.
    - Clone the project repository: 
      ```bash
      git clone https://github.com/KunakornMart/DADS6005.git
      ```

2. **Run the Services**:
    - Start the services using Docker Compose:
      ```bash
      docker-compose up -d
      ```

3. **Source Code and Documentation**:
   - The full implementation code is provided in the file `source_code_6610422020.docx`.
   - Detailed descriptions for each component are available in the file `report_6610422020.docx`.

## Dashboard Screenshot
Here is an overview of the real-time data analytics dashboard:

![Dashboard Overview](https://drive.google.com/uc?export=view&id=1YxHnrM5-Tuw-kVxvkq2Uyk8GJs0ojJgW)

You can view the live dashboard at [http://ec2-47-129-89-174.ap-southeast-1.compute.amazonaws.com:8501/](http://ec2-47-129-89-174.ap-southeast-1.compute.amazonaws.com:8501/).

## Future Enhancements
- Incorporate more data sources and additional ksqlDB transformations.
- Extend Pinot schemas for more complex queries.
