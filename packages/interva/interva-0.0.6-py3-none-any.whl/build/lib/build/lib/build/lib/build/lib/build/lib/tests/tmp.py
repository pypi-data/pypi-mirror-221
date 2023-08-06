import pytest
from pandas import concat, DataFrame, Series, read_csv
from numpy import nan
from interva.interva5 import InterVA5, get_example_input
from interva.utils import (csmf, get_indiv_cod, _get_age_group,
                           _get_age_group_all, _get_cod_with_dem,
                           _get_dem_groups, _get_sex_group)
from interva.exceptions import ArgumentException

va_data = read_csv('ova_training.csv')
iv5out = InterVA5(va_data, hiv="h", malaria="l", write=False)
iv5out.run()

out1 = csmf(iv5out, top=10, interva_rule=True, top_aggregate=None)
