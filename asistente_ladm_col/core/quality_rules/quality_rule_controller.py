"""
/***************************************************************************
                              Asistente LADM-COL
                             --------------------
        begin           : 2022-01-13
        copyright       : (C) 2022 by Germán Carrillo (SwissTierras Colombia)
        email           : gcarrillo@linuxmail.org
 ***************************************************************************/
/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License v3.0 as          *
 *   published by the Free Software Foundation.                            *
 *                                                                         *
 ***************************************************************************/
"""
import json

from qgis.PyQt.QtCore import (QCoreApplication,
                              pyqtSignal,
                              QSettings,
                              QObject)

from asistente_ladm_col.app_interface import AppInterface
from asistente_ladm_col.config.quality_rule_config import QR_IGACR3006
from asistente_ladm_col.config.general_config import DEFAULT_USE_ROADS_VALUE
from asistente_ladm_col.lib.logger import Logger
from asistente_ladm_col.core.quality_rules.quality_rule_engine import (QualityRuleEngine,
                                                                       QualityRuleResultLog)
from asistente_ladm_col.core.quality_rules.quality_rule_registry import QualityRuleRegistry
from asistente_ladm_col.logic.ladm_col.ladm_data import LADMData


class QualityRuleController(QObject):

    open_report_called = pyqtSignal(QualityRuleResultLog)  # log result
    total_progress_changed = pyqtSignal(int)  # Progress value

    def __init__(self, db):
        QObject.__init__(self)
        self.app = AppInterface()
        self.logger = Logger()
        self.__db = db

        # Hierarquical dict of qrs and qr groups
        self.__qrs_tree_data = dict()  # {type: {qr_key1: qr_obj1, ...}, ...}

        # Hierarquical dict of qrs and qr groups with general results
        self.__general_results_tree_data = dict()  # {type: {qr_obj1: qr_results1, ...}, ...}

        # Hierrchical dict of qrs and their corresponding error instances
        # feature1: {uuids, rel_uuids, error_type, nombre_ili_obj, details, values, fixed, exception, geom_fks}
        self.__error_results_data = dict()  # {qr_key1: {t_id1: feature1}}

        self.__selected_qrs = list()  # QRs to be validated (at least 1)
        self.__selected_qr = None  # QR selected by the user to show its corresponding errors (exactly 1)

        self.__qr_engine = None

        self.__point_layer = None
        self.__line_layer = None
        self.__polygon_layer = None

    def validate_qrs(self):
        self.__qr_engine = QualityRuleEngine(self.__db, self.__selected_qrs, self.app.settings.tolerance)
        self.__qr_engine.progress_changed.connect(self.total_progress_changed)
        #self.__qr_engine.qr_logger.show_message_emitted.connect(self.show_log_quality_message)
        #self.__qr_engine.qr_logger.show_button_emitted.connect(self.show_log_quality_button)
        #self.__qr_engine.qr_logger.set_initial_progress_emitted.connect(self.set_log_quality_initial_progress)
        #self.__qr_engine.qr_logger.set_final_progress_emitted.connect(self.set_log_quality_final_progress)

        use_roads = bool(QSettings().value('Asistente-LADM-COL/quality/use_roads', DEFAULT_USE_ROADS_VALUE, bool))
        options = {QR_IGACR3006: {'use_roads': use_roads}}

        res, msg, res_obj = self.__qr_engine.validate_quality_rules(options)
        self.logger.info_msg(__name__, QCoreApplication.translate("QualityRuleController",
                                                                  "All the {} quality rules were checked!").format(
            len(self.__selected_qrs)), 15)

    def all_error_layers(self):
        return [layer for qr_res in self.__res_dict.values() for layer in qr_res.error_layers if layer.featureCount()]

    def __get_qrs_per_role_and_models(self):
        return QualityRuleRegistry().get_qrs_per_role_and_models(self.__db)

    def load_tree_data(self):
        """
        Builds a hierarchical dict by qr type: {qr_type1: {qr_key1: qr_obj1, ...}, ...}

        Tree data for panel 1.
        """
        qrs = self.__get_qrs_per_role_and_models()  # Dict of qr key and qr objects.

        for qr_key, qr_obj in qrs.items():
            type = qr_obj.type()
            if type not in self.__qrs_tree_data:
                self.__qrs_tree_data[type] = {qr_key: qr_obj}
            else:
                self.__qrs_tree_data[type][qr_key] = qr_obj

    def get_qrs_tree_data(self):
        return self.__qrs_tree_data

    def set_selected_qrs(self, selected_qrs):
        # We sort them because the engine needs the QRs sorted for the PDF report
        for type, qr_dict in self.__qrs_tree_data.items():
            for qr_key, qr_obj in qr_dict.items():
                if qr_key in selected_qrs:
                    self.__selected_qrs.append(qr_key)

    def get_selected_qrs(self):
        return self.__selected_qrs

    def load_general_results_tree_data(self):
        """
        Builds a hierarchical dict by qr type: {type: {qr_obj1: qr_results1, ...}, ...}

        Tree data for panel 2.
        """
        for type, qr_dict in self.__qrs_tree_data.items():
            for qr_key, qr_obj in qr_dict.items():
                if qr_key in self.__selected_qrs:
                    if type not in self.__general_results_tree_data:
                        self.__general_results_tree_data[type] = {qr_obj: None}
                    else:
                        self.__general_results_tree_data[type][qr_obj] = None

    def get_general_results_tree_data(self):
        return self.__general_results_tree_data

    def set_qr_validation_result(self, qr, qr_result):
        """
        When a QR has its validation result after validation,
        we can store it in our custom dict by using this method.
        """
        for type, qr_dict in self.__general_results_tree_data.items():
            for k, v in qr_dict.items():
                if k == qr:
                    self.__general_results_tree_data[type][k] = qr_result

    def open_report(self):
        if self.__qr_engine:
            log_result = self.__qr_engine.qr_logger.get_log_result()
            self.open_report_called.emit(log_result)

    def set_selected_qr(self, qr_key):
        self.__selected_qr = QualityRuleRegistry().get_quality_rule(qr_key)
        return self.__selected_qr is not None  # We should not be able to continue if we don't find the QR

    def get_selected_qr(self):
        return self.__selected_qr

    def load_error_results_data(self):
        """
        Go to table and bring data to the dict.
        We should keep this dict updated with changes from the user.
        From time to time we reflect this dict changes in the original data source.
        """
        db = self.__qr_engine.get_db_quality()
        names = db.names

        layers = {names.ERR_QUALITY_ERROR_T: None,  names.ERR_RULE_TYPE_T: None}
        self.app.core.get_layers(db, layers, load=False)
        if not layers:
            self.logger.critical(__name__, "Quality error layers ('{}') not found!".format(",".join(list(layers.keys()))))
            return

        # First go for the selected quality error's t_id
        features = LADMData.get_features_from_t_ids(layers[names.ERR_RULE_TYPE_T],
                                                    names.ERR_RULE_TYPE_T_CODE_F,
                                                    [self.__selected_qr.id()])
        t_id = features[0][names.T_ID_F] if features else None
        if not t_id:
            self.logger.critical(__name__, "Quality error rule ('{}') not found!".format(self.__selected_qr.id()))
            return

        # Now go for all features that match the selected quality rule
        features = LADMData.get_features_from_t_ids(layers[names.ERR_QUALITY_ERROR_T],
                                                    names.ERR_QUALITY_ERROR_T_RULE_TYPE_F,
                                                    [t_id])

        self.__error_results_data[self.__selected_qr.id()] = {feature[names.T_ID_F]: feature for feature in features}

    def get_error_results_data(self):
        # Get the subdict {t_id1: feature1, ...} corresponding to selected qr
        return self.__error_results_data.get(self.__selected_qr.id() if self.__selected_qr else '', dict())

    def error_t_id(self, feature):
        return feature[self.__qr_engine.get_db_quality().names.T_ID_F]

    def is_fixed_error(self, feature):
        return True  # self.get_error_results_data()[feature[db.names.T_ID_F]][db.names.T_ID_F]  # TODO

    def is_error(self, feature):
        return not self.is_fixed_error(feature) and not self.is_exception(feature)

    def is_exception(self, feature):
        return True  # TODO

    def uuid_objs(self, feature):
        return "\n".join(feature[self.__qr_engine.get_db_quality().names.ERR_QUALITY_ERROR_T_OBJECT_IDS_F])

    def error_type_code_and_display(self, feature):
        db = self.__qr_engine.get_db_quality()
        names = db.names
        layer = self.app.core.get_layer(db, names.ERR_ERROR_TYPE_T, load=False)
        features = LADMData.get_features_from_t_ids(layer,
                                                    names.T_ID_F,
                                                    [feature[db.names.ERR_QUALITY_ERROR_T_ERROR_TYPE_F]])  # tid

        return features[0][names.ERR_ERROR_TYPE_T_CODE_F] if features else QCoreApplication.translate(
            "QualityRuleController", "No error type found!"), features[0][
                   names.ERR_ERROR_TYPE_T_DESCRIPTION_F] if features else QCoreApplication.translate(
            "QualityRuleController", "No error description found!")

    def error_details_and_values(self, feature):
        res = ""
        db = self.__qr_engine.get_db_quality()
        details = feature[db.names.ERR_QUALITY_ERROR_T_DETAILS_F]
        values = feature[db.names.ERR_QUALITY_ERROR_T_VALUES_F]

        if details:
            res = details
        if values:
            try:
                res_values = json.loads(values)
                if type(res_values) is dict:
                    items = ""
                    for k, v in res_values.items():
                        items = res + "{}: {}\n".format(k, v)

                    res_values = items.strip()
                else:
                    res_values = str(res_values)
            except json.decoder.JSONDecodeError as e:
                res_values = values

            res = res_values if not res else "{}\n\n{}".format(res, res_values)

        return res

    def __get_point_error_layer(self):
        if not self.__point_layer:
            db = self.__qr_engine.get_db_quality()
            self.__point_layer = self.app.core.get_layer(db, db.names.ERR_POINT_T)

        return self.__point_layer

    def __get_line_error_layer(self):
        if not self.__line_layer:
            db = self.__qr_engine.get_db_quality()
            self.__line_layer = self.app.core.get_layer(db, db.names.ERR_LINE_T)

        return self.__line_layer

    def __get_polygon_error_layer(self):
        if not self.__polygon_layer:
            db = self.__qr_engine.get_db_quality()
            self.__polygon_layer = self.app.core.get_layer(db, db.names.ERR_POLYGON_T)

        return self.__polygon_layer

    def __error_related_geometries(self, error_t_ids):
        # Prefered geometry types are polygons, lines, points, in that order
        db = self.__qr_engine.get_db_quality()
        error_data = self.get_error_results_data()
        dict_layer_fids = dict()

        for error_t_id in error_t_ids:
            feature = error_data.get(error_t_id, None)

            if feature:
                polygon = feature[db.names.ERR_QUALITY_ERROR_T_POLYGON_F]
                line = feature[db.names.ERR_QUALITY_ERROR_T_LINE_F]
                point = feature[db.names.ERR_QUALITY_ERROR_T_POINT_F]

                if polygon:
                    if 'polygon' in dict_layer_fids:
                        dict_layer_fids['polygon']['fids'].append(polygon)
                    else:
                        dict_layer_fids['polygon'] = {'layer': self.__get_polygon_error_layer(), 'fids': [polygon]}
                elif line:
                    if 'line' in dict_layer_fids:
                        dict_layer_fids['line']['fids'].append(line)
                    else:
                        dict_layer_fids['line'] = {'layer': self.__get_line_error_layer(), 'fids': [line]}
                elif point:
                    if 'point' in dict_layer_fids:
                        dict_layer_fids['point']['fids'].append(point)
                    else:
                        dict_layer_fids['point'] = {'layer': self.__get_point_error_layer(), 'fids': [point]}

        return dict_layer_fids

    def highlight_geometries(self, t_ids):
        res_geometries = self.__error_related_geometries(t_ids)
        for geom_type, dict_layer_fids in res_geometries.items():
            self.app.gui.flash_features(dict_layer_fids['layer'], dict_layer_fids['fids'])

    # def show_log_quality_message(self, msg, count):
    #     self.progress_message_bar = self.iface.messageBar().createMessage("Asistente LADM-COL", msg)
    #     self.log_quality_validation_progress = QProgressBar()
    #     self.log_quality_validation_progress.setFixedWidth(80)
    #     self.log_quality_total_rule_count = count
    #     self.log_quality_validation_progress.setMaximum(self.log_quality_total_rule_count * 10)
    #     self.progress_message_bar.layout().addWidget(self.log_quality_validation_progress)
    #     self.iface.messageBar().pushWidget(self.progress_message_bar, Qgis.Info)
    #     self.log_quality_validation_progress_count = 0
    #     self.log_quality_current_rule_count = 0
    #
    # def show_log_quality_button(self):
    #     self.button = QPushButton(self.progress_message_bar)
    #     self.button.pressed.connect(self.show_log_quality_dialog)
    #     self.button.setText(QCoreApplication.translate("LogQualityDialog", "Show Results"))
    #     self.progress_message_bar.layout().addWidget(self.button)
    #     QCoreApplication.processEvents()
    #
    # def set_log_quality_initial_progress(self, msg):
    #     self.log_quality_validation_progress_count += 2  # 20% of the current rule
    #     self.log_quality_validation_progress.setValue(self.log_quality_validation_progress_count)
    #     self.progress_message_bar.setText(
    #         QCoreApplication.translate("LogQualityDialog",
    #                                    "Checking {} out of {}: '{}'").format(
    #                                     self.log_quality_current_rule_count + 1,
    #                                     self.log_quality_total_rule_count,
    #                                     msg))
    #     QCoreApplication.processEvents()
    #
    # def set_log_quality_final_progress(self, msg):
    #     self.log_quality_validation_progress_count += 8  # 80% of the current rule
    #     self.log_quality_validation_progress.setValue(self.log_quality_validation_progress_count)
    #     self.log_quality_current_rule_count += 1
    #     if self.log_quality_current_rule_count ==  self.log_quality_total_rule_count:
    #         self.progress_message_bar.setText(QCoreApplication.translate("LogQualityDialog",
    #             "All the {} quality rules were checked! Click the button at the right-hand side to see a report.").format(self.log_quality_total_rule_count))
    #     else:
    #         self.progress_message_bar.setText(msg)
    #     QCoreApplication.processEvents()
    #
