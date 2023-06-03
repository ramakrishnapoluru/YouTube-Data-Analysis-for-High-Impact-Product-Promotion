# YouTube-Data-Analysis-for-High-Impact-Product-Promotion

# Introduction 

The business problem at hand revolves around effectively promoting and advertising a product that is scheduled to be launched within the next three months in the lucrative markets of the United States, Canada, and Great Britain. To achieve optimal visibility and engagement, we have identified YouTube as the primary advertising channel for our data-driven campaign. 

To tackle this challenge, we aim to leverage historical data from the past six months on YouTube. This data will serve as a valuable resource for analyzing and categorizing videos based on various metrics, including comments and statistical factors. By thoroughly examining the characteristics and trends of successful videos in these markets, we can gain valuable insights into the key factors that contribute to their popularity. 

With these insights, we can fine-tune our advertising strategy and optimize our content creation efforts. By understanding what resonates with viewers and what drives engagement, we can tailor our promotional materials to effectively capture the attention of our target audience. 

Furthermore, by employing a data-driven approach, we can make informed decisions regarding budget allocation and ad placement on YouTube. By identifying the types of videos and channels that generate high engagement and conversions, we can allocate resources strategically to maximize the return on investment. 

# Project Objectives

Data Ingestion: Construct a reliable mechanism for gathering data from diverse sources.

ETL System: Convert raw data into a standardized format through a data transformation process.

Data Lake: Establish a centralized repository to accumulate and store data obtained from multiple origins.

Scalability: Ensure that the system can seamlessly handle growing data volumes without compromising performance.

Cloud Integration: Leverage cloud computing, specifically AWS, to process substantial amounts of data that surpass the limitations of local computing resources.

Reporting: Develop a comprehensive dashboard to obtain insights and answers to the initial inquiries.

# Data Collection 

This data collection comprises six months of daily trending YouTube videos, with separate files for the United States (US), Great Britain (GB), and Canada (CA). Each file contains information on up to 200 trending videos per day. 

The dataset includes various attributes for each video, such as the title, channel title, publish time, tags, views, likes, dislikes, description, and comment count. Additionally, there is a category_id field, which varies across regions. To obtain the specific category of a video, you can refer to the associated JSON file provided for each region. 

# Architechture

An architecture leveraging various AWS services has been implemented. The project involves the utilization of Amazon S3, AWS Lambda, AWS Glue, AWS Athena, and QuickSight. 
To begin, a data lake is established in Amazon S3, serving as a central repository for the project's data. Whenever a new file is uploaded to S3, AWS Lambda functions are triggered, allowing for seamless processing. These functions convert the incoming JSON files into the efficient Parquet format, ensuring data readability and optimal performance. 
AWS Glue is employed to perform Extract, Transform, Load (ETL) operations on the data, which may be in multiple formats. This enables data harmonization and preparation for subsequent analysis and querying. The processed data is then stored and loaded back into Amazon S3, ready for further utilization. 
For querying and analysis, AWS Athena comes into play. Athena allows for the execution of SQL queries directly on the data stored in S3. This provides a convenient and scalable approach to access and retrieve insights from the processed data. 
Lastly, AWS QuickSight serves as the tool for visual-level analytics and dashboard creation. QuickSight enables the exploration and visualization of data, allowing for the creation of interactive and insightful dashboards that aid in data interpretation and decision-making. 

# Visuals in Dashboard 
![Archirechture!](https://github.com/ramakrishnapoluru/USAH1BAnalysis/assets/119472036/e4d1187a-3156-4cc2-a947-9ed363f1571b)
