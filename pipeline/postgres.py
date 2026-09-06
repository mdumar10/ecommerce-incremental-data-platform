# connection informatoin funation 

def get_connection_config(dbutils):
    """
    Build the PostgreSQL JDBC connection configuration
    using secrets stored in Databricks.
    """

    host = dbutils.secrets.get(
        scope="supabase",
        key="SUPABASE_HOST"
    )

    port = dbutils.secrets.get(
        scope="supabase",
        key="SUPABASE_PORT"
    )

    database = dbutils.secrets.get(
        scope="supabase",
        key="SUPABASE_DATABASE"
    )

    user = dbutils.secrets.get(
        scope="supabase",
        key="SUPABASE_USER"
    )

    password = dbutils.secrets.get(
        scope="supabase",
        key="SUPABASE_PASSWORD"
    )

    jdbc_url = (
        f"jdbc:postgresql://{host}:{port}/{database}"
        "?sslmode=require"
    )

    properties = {
        "user": user,
        "password": password,
        "driver": "org.postgresql.Driver"
    }

    return jdbc_url, properties



# ===============================================================================
# reading databse from the connection 


def read_table(spark, table_name, jdbc_url, properties):
    """
    Read one PostgreSQL table into a Spark DataFrame.
    """
    return(
          spark.read
          .format("jdbc")
          .option("url",jdbc_url)
          .option("dbtable",table_name)
          .options(**properties)
          .load()
    )