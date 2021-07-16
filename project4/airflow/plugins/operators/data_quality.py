from airflow.hooks.postgres_hook import PostgresHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults

class DataQualityOperator(BaseOperator):

    ui_color = '#89DA59'

    @apply_defaults
    def __init__(self,
                 redshift='',
                 dq_checks = [],
                 *args, **kwargs):

        super(DataQualityOperator, self).__init__(*args, **kwargs)
        self.redshift = redshift
        self.dq_checks = dq_checks

    def execute(self, context):
        self.log.info('DATA QUALITY CHECK - STARTED')

        redshift = PostgresHook(postgres_conn_id=self.redshift)
      
        ## LOOP THROUGH VALIDATIONS
        tests_with_error = []
        for dq_check in self.dq_checks:                
            sql = dq_check.get('check_sql')
            expected_result = dq_check.get('expected_result')
            description = dq_check.get('description')

            self.log.info(f"DATA QUALITY CHECK - TEST: {sql} / {expected_result}")

            ## RESULT
            result = redshift.get_records(sql)[0]
            if expected_result != result[0]:
                tests_with_error.append(
                  "ASSERT {}. EXPECTED {} instead got {}".format(
                    description, 
                    expected_result,
                    result[0])
                )
            else:
              self.log.info("DATA QUALITY CHECK - PASSED. SQL: {} with {} records.".format(sql, result[0]))

        if len(tests_with_error) > 0:
          self.log.error("TESTS WITH ERROR")
          self.log.error(tests_with_error)
          raise ValueError("DATA QUALITY FAILED.")

        self.log.info("DATA QUALITY CHECK - COMPLETED")

