from airflow.hooks.postgres_hook import PostgresHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults

class DataQualityOperator(BaseOperator):

    ui_color = '#89DA59'

    @apply_defaults
    def __init__(self,
                 redshift='',
                 tables = [],
                 *args, **kwargs):

        super(DataQualityOperator, self).__init__(*args, **kwargs)
        self.redshift = redshift
        self.tables = tables

    def execute(self, context):
        self.log.info('DATAQUALITY CHECK...')

        redshift = PostgresHook(postgres_conn_id=self.redshift)

        for table in self.tables:
          ## COLUMNS
          columns = redshift.get_records("SELECT COUNT(*) FROM {}".format(table))
          if len(columns) < 1 or len(columns[0]) < 1:
            self.log.error("{} has no results". format(table))
            raise ValueError("DATAQUALITY FAILED. {} has no data.".format(table))
          
          ## RECORDS
          num_records = columns[0][0]
          if num_records == 0:
            self.log.error("DATAQUALITY FAILED. {} has no records.".format(table))
            raise ValueError("DATAQUALITY FAILED. {} has no records.".format(table))

          self.log.info("DATAQUALITY passed. Table: {} with {} records.".format(table, num_records))