import nose2

from qgis.testing import (start_app,
                          unittest)

start_app() # need to start before asistente_ladm_col.tests.utils

from asistente_ladm_col.tests.utils import (get_required_fields,
                                            get_required_tables)
from asistente_ladm_col.config.table_mapping_config import (ILICODE,
                                                            T_ID,
                                                            DESCRIPTION,
                                                            DISPLAY_NAME)
from asistente_ladm_col.tests.utils import (get_dbconn,
                                            restore_schema)


class TestSNRDataModel(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        restore_schema('test_ladm_snr_data')
        self.db_connection_pg = get_dbconn('test_ladm_snr_data')

    def test_required_models_pg(self):
        print("\nINFO: Validate if the schema for snr data model...")
        result = self.db_connection_pg.test_connection()
        self.assertTrue(result[0], 'The test connection is not working')
        self.check_required_models(self.db_connection_pg)

    def check_required_models(self, db_connection):
        self.assertFalse(db_connection.supplies_model_exists())
        self.assertTrue(db_connection.snr_data_model_exists())
        self.assertFalse(db_connection.supplies_integration_model_exists())
        self.assertFalse(db_connection.operation_model_exists())
        self.assertFalse(db_connection.valuation_model_exists())
        self.assertFalse(db_connection.cadastral_form_model_exists())
        self.assertFalse(db_connection.ant_model_exists())
        self.assertFalse(db_connection.reference_cartography_model_exists())

    def test_names_from_db_pg(self):
        print("\nINFO: Validate names for SNR data model (small DB case)...")
        result = self.db_connection_pg.test_connection()
        self.assertTrue(result[0], 'The test connection is not working')


        dict_names = self.db_connection_pg.get_table_and_field_names()
        self.assertEqual(len(dict_names), 15)

        expected_dict = {T_ID: 't_id',
                         ILICODE: 'ilicode',
                         DESCRIPTION: 'description',
                         DISPLAY_NAME: 'dispname',
                         'Datos_SNR.Datos_SNR.snr_titular_derecho': {'table_name': 'snr_titular_derecho',
                                                                     'Datos_SNR.Datos_SNR.snr_titular_derecho.Porcentaje_Participacion': 'porcentaje_participacion',
                                                                     'Datos_SNR.Datos_SNR.snr_titular_derecho.snr_derecho..Datos_SNR.Datos_SNR.SNR_Derecho': 'snr_derecho',
                                                                     'Datos_SNR.Datos_SNR.snr_titular_derecho.snr_titular..Datos_SNR.Datos_SNR.SNR_Titular': 'snr_titular'}}
        for k,v in expected_dict.items():
            self.assertIn(k, dict_names)
            self.assertEqual(v, dict_names[k])

    def test_required_table_names_pg(self):
        print("\nINFO: Validate minimum required tables from names...")
        result = self.db_connection_pg.test_connection()
        self.assertTrue(result[0], 'The test connection is not working')
        self.check_required_table_names(self.db_connection_pg)

    def check_required_table_names(self, db_connection):
        test_required_tables = ['SNR_RIGHT_T', 'SNR_SOURCE_RIGHT_T', 'SNR_PARCEL_REGISTRY_T', 'SNR_TITLE_HOLDER_T', 'SNR_RIGHT_TYPE_D', 'SNR_TITLE_HOLDER_DOCUMENT_T', 'SNR_SOURCE_TYPE_D', 'SNR_TITLE_HOLDER_TYPE_D', 'EXT_ARCHIVE_S']
        required_tables = get_required_tables(db_connection)

        for test_required_table in test_required_tables:
            self.assertIn(test_required_table, required_tables)

    def test_required_field_names_pg(self):
        print("\nINFO: Validate minimum required fields from names...")
        result = self.db_connection_pg.test_connection()
        self.assertTrue(result[0], 'The test connection is not working')
        self.check_required_field_names(self.db_connection_pg)

    def check_required_field_names(self, db_connection):
        test_required_fields = ['EXT_ARCHIVE_S_DATA_F', 'EXT_ARCHIVE_S_EXTRACTION_F']
        required_fields = get_required_fields(db_connection)

        for test_required_field in test_required_fields:
            self.assertIn(test_required_field, required_fields)

    @classmethod
    def tearDownClass(self):
        self.db_connection_pg.conn.close()


if __name__ == '__main__':
    nose2.main()

