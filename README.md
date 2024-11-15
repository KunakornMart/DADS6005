# DADS6005 : Data Streaming and Real Time Analytics
This project demonstrates a real-time data streaming and analytics platform, built with a series of integrated tools: **Apache Kafka**, **ksqlDB**, **Apache Pinot**, and **Streamlit**. The objective is to ingest, process, and visualize large-scale, real-time data from various sources, using a series of transformations and aggregations for meaningful insights.

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
   - The full implementation code is provided in the file `source_code_6610422020`.
   - Detailed descriptions for each component are available in the file `report_6610422020`.

## Real-Time Data Streaming and Analytics Dashboard
Here is an overview of the real-time data analytics dashboard:

![Dashboard Overview](https://drive.google.com/uc?export=view&id=1YxHnrM5-Tuw-kVxvkq2Uyk8GJs0ojJgW)

### Real-Time Dashboard Example

![Video Demonstration](https://github.com/KunakornMart/DADS6005/blob/main/Realtime-Video.gif?raw=true)


You can view the live dashboard at [http://ec2-47-129-89-174.ap-southeast-1.compute.amazonaws.com:8501/](http://ec2-47-129-89-174.ap-southeast-1.compute.amazonaws.com:8501/).



## Future Enhancements
- **Incorporate More Data Sources**: Expand the system by integrating additional data sources, such as external APIs or IoT sensor data, to enrich the data pipeline and enhance the real-time analytics capabilities.

- **Real-Time Predictive Analytics**: Integrate predictive analytics into the system by developing models that can forecast trends, such as future page views or user behaviors, based on historical data processed through Kafka and ksqlDB.

- **Integration with Third-Party Analytics Tools**: Integrate the platform with popular third-party analytics tools like Power BI, Tableau, or Grafana, allowing users to visualize the real-time data and insights through external dashboards and reporting systems.

- **Scalability Improvements**: Focus on enhancing the scalability of the system by fine-tuning the Kafka partitioning strategy, optimizing Pinot data storage, and ensuring that the platform can handle increased data volume and user load efficiently.

