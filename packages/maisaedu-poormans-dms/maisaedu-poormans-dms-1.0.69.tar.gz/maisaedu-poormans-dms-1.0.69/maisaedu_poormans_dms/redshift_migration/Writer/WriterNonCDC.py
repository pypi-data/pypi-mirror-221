from ..Types import FULL
from .GenericWriter import GenericWriter
from ..Contracts.WriterInterface import WriterInterface


class WriterNonCDC(GenericWriter, WriterInterface):
    def save_data(self, operations):
        operation = operations[0]
        url = operation.url
        load_option = operation.load_option

        self.create_table_temp_target_relation()
        self.copy_data_to_target(url, self.temp_target_relation)
        self.migrator_redshift_connector.target_conn.commit()

        if self.is_upsert is True and load_option != FULL:
            self.delete_upsert_data_from_target()
        else:
            self.delete_all_data_from_target()

        self.insert_data_from_temp_to_target()

        self.migrator_redshift_connector.target_conn.commit()

        self.drop_table_temp_target_relation()

        self.migrator_redshift_connector.target_conn.commit()
