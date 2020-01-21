import nose2

from qgis.testing import (start_app,
                          unittest)

start_app() # need to start before asistente_ladm_col.tests.utils

from asistente_ladm_col.config.table_mapping_config import (Names,
                                                            ILICODE,
                                                            T_ID,
                                                            DESCRIPTION,
                                                            DISPLAY_NAME)
from asistente_ladm_col.tests.utils import (get_pg_conn,
                                            restore_schema)


class TestOperationModel(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        restore_schema('test_ladm_operation_model')
        self.db_connection = get_pg_conn('test_ladm_operation_model')
        self.names = Names()

    def test_required_models(self):
        print("\nINFO: Validate if the schema for operation model...")
        result = self.db_connection.test_connection()
        self.assertTrue(result[0], 'The test connection is not working')

        self.assertTrue(self.db_connection.supplies_model_exists())
        self.assertTrue(self.db_connection.snr_data_model_exists())
        self.assertTrue(self.db_connection.supplies_integration_model_exists())
        self.assertTrue(self.db_connection.operation_model_exists())
        self.assertFalse(self.db_connection.valuation_model_exists())
        self.assertFalse(self.db_connection.cadastral_form_model_exists())
        self.assertFalse(self.db_connection.ant_model_exists())
        self.assertFalse(self.db_connection.reference_cartography_model_exists())

    def test_names_from_model(self):
        print("\nINFO: Validate names for Operation data model (the expected common DB case)...")
        result = self.db_connection.test_connection()
        self.assertTrue(result[0], 'The test connection is not working')

        dict_names = self.db_connection.get_table_and_field_names()
        self.assertEqual(len(dict_names), 144)

        expected_dict = {T_ID: 't_id',
                         ILICODE: 'ilicode',
                         DESCRIPTION: 'description',
                         DISPLAY_NAME: 'dispname',
                         'LADM_COL.LADM_Nucleo.col_masCcl': {'table_name': 'col_masccl',
                                                             'LADM_COL.LADM_Nucleo.col_masCcl.ccl_mas..Operacion.Operacion.OP_Lindero': 'ccl_mas',
                                                             'LADM_COL.LADM_Nucleo.col_masCcl.ue_mas..Operacion.Operacion.OP_Construccion': 'ue_mas_op_construccion',
                                                             'LADM_COL.LADM_Nucleo.col_masCcl.ue_mas..Operacion.Operacion.OP_ServidumbrePaso': 'ue_mas_op_servidumbrepaso',
                                                             'LADM_COL.LADM_Nucleo.col_masCcl.ue_mas..Operacion.Operacion.OP_Terreno': 'ue_mas_op_terreno',
                                                             'LADM_COL.LADM_Nucleo.col_masCcl.ue_mas..Operacion.Operacion.OP_UnidadConstruccion': 'ue_mas_op_unidadconstruccion'}}

        for k, v in expected_dict.items():
            self.assertIn(k, dict_names)
            self.assertEqual(v, dict_names[k])

    @classmethod
    def tearDownClass(self):
        self.db_connection.conn.close()


if __name__ == '__main__':
    nose2.main()

