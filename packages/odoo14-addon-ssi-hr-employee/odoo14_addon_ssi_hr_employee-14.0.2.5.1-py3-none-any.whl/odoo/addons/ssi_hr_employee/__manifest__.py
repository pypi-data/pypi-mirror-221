# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
# pylint: disable=locally-disabled, manifest-required-author
{
    "name": "HR Employee",
    "version": "14.0.2.5.1",
    "website": "https://simetri-sinergi.id",
    "author": "PT. Simetri Sinergi Indonesia, OpenSynergy Indonesia",
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "ssi_hr",
        "ssi_master_data_mixin",
    ],
    "data": [
        "security/res_group_data.xml",
        "security/ir.model.access.csv",
        "menu.xml",
        "views/hr_employment_status_views.xml",
        "views/hr_job_grade_category_views.xml",
        "views/hr_job_grade_views.xml",
        "views/hr_job_family_grade_views.xml",
        "views/hr_job_family_views.xml",
        "views/hr_job_family_level_views.xml",
        "views/hr_job_views.xml",
        "views/hr_employee_views.xml",
    ],
    "demo": [
        "demo/hr_employment_status_demo.xml",
        "demo/hr_job_grade_category_demo.xml",
        "demo/hr_job_grade_demo.xml",
    ],
}
