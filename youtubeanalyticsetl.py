import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

# Script generated for node AWS Glue Data Catalog
AWSGlueDataCatalog_node1685691356853 = glueContext.create_dynamic_frame.from_catalog(
    database="youtubeanalysis",
    table_name="cleaned_statistics_reference_data",
    transformation_ctx="AWSGlueDataCatalog_node1685691356853",
)

# Script generated for node AWS Glue Data Catalog
AWSGlueDataCatalog_node1685691390592 = glueContext.create_dynamic_frame.from_catalog(
    database="youtubeanalysis",
    table_name="raw_statistics",
    transformation_ctx="AWSGlueDataCatalog_node1685691390592",
)

# Script generated for node Join
Join_node1685691428458 = Join.apply(
    frame1=AWSGlueDataCatalog_node1685691356853,
    frame2=AWSGlueDataCatalog_node1685691390592,
    keys1=["id"],
    keys2=["category_id"],
    transformation_ctx="Join_node1685691428458",
)

# Script generated for node Amazon S3
AmazonS3_node1685691647195 = glueContext.getSink(
    path="s3://youtubeanalyticsreportingdata",
    connection_type="s3",
    updateBehavior="UPDATE_IN_DATABASE",
    partitionKeys=["region", "category_id"],
    compression="snappy",
    enableUpdateCatalog=True,
    transformation_ctx="AmazonS3_node1685691647195",
)
AmazonS3_node1685691647195.setCatalogInfo(
    catalogDatabase="db_youtube_analytics", catalogTableName="youtubeanalticsreporting"
)
AmazonS3_node1685691647195.setFormat("glueparquet")
AmazonS3_node1685691647195.writeFrame(Join_node1685691428458)
job.commit()
