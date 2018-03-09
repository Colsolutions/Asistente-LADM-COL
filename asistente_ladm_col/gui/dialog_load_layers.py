# -*- coding: utf-8 -*-
"""
/***************************************************************************
                              Asistente LADM_COL
                             --------------------
        begin                : 2018-03-08
        git sha              : :%H$
        copyright            : (C) 2018 by Germán Carrillo (BSF Swissphoto)
        email                : gcarrillo@linuxmail.org
 ***************************************************************************/
/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License v3.0 as          *
 *   published by the Free Software Foundation.                            *
 *                                                                         *
 ***************************************************************************/
"""
import os

from qgis.core import QgsProject, QgsVectorLayer, Qgis
from qgis.gui import QgsMessageBar
from qgis.PyQt.QtCore import Qt, QSettings
from qgis.PyQt.QtWidgets import QDialog, QTreeWidgetItem

from ..lib.dbconnector.gpkg_connector import GPKGConnector
from ..lib.dbconnector.pg_connector import PGConnector
from ..utils import get_ui_class
from ..utils.qt_utils import make_file_selector
from ..utils.project_generator_utils import ProjectGeneratorUtils

DIALOG_UI = get_ui_class('dlg_load_layers.ui')

class DialogLoadLayers(QDialog, DIALOG_UI):
    def __init__(self, iface, db, parent=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.iface = iface
        self._db = db
        self.models_tree = {}
        self.project_generator_utils = ProjectGeneratorUtils()

        self.cbo_select_predefined_tables.clear()
        self.cbo_select_predefined_tables.addItem(self.tr('Spatial data'), 'spatial_data')
        self.cbo_select_predefined_tables.addItem(self.tr('Legal data'), 'legal_data')
        self.cbo_select_predefined_tables.currentIndexChanged.connect(self.select_predefined_changed)

        # Load layers from the db
        self.load_available_layers()

        # Set connections
        self.buttonBox.accepted.connect(self.accepted)

        # SIGNALS-SLOTS
        self.chk_show_domains.toggled.connect(self.show_domains_changed)

        # Trigger some default behaviours
        self.restore_settings()

    def load_available_layers(self):
        # Call project generator tables_info and fill the layer tree
        tables_info = self.project_generator_utils.get_tables_info_without_ignored_tables(self._db)
        self.models_tree = {}
        for record in tables_info:
            if record['model'] not in self.models_tree:
                self.models_tree[record['model']] = {
                    record['table_alias'] or record['tablename']: record}
            else:
                self.models_tree[record['model']][record['table_alias'] or record['tablename']] = record

        self.update_available_layers(self.chk_show_domains.isChecked())

    def update_available_layers(self, show_domains=False):
        self.trw_layers.clear()
        sorted_models = sorted(self.models_tree.keys())
        for model in sorted_models:
            children = []
            model_item = QTreeWidgetItem([model])
            sorted_tables = sorted(self.models_tree[model].keys())
            for table in sorted_tables:
                if self.models_tree[model][table]['is_domain'] and not show_domains:
                    continue

                table_item = QTreeWidgetItem([table])
                table_item.setData(0, Qt.UserRole, self.models_tree[model][table])
                children.append(table_item)

            model_item.addChildren(children)
            self.trw_layers.addTopLevelItem(model_item)

    def show_domains_changed(self, state):
        self.update_available_layers(self.chk_show_domains.isChecked())

    def accepted(self):
        print("Accepted!")
        self.save_settings()

    def save_settings(self):
        # Save QSettings
        # settings = QSettings(
        pass

    def restore_settings(self):
        # Restore QSettings
        # settings = QSettings()
        pass

    def select_predefined_changed(self):
        pass
