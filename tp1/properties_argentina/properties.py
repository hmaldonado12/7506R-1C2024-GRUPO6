from pandas import DataFrame
from pyproj.utils import DataType


class Properties:
    def __init__(self, pandas):
        self.pandas = pandas

    def filter_by(self, columns: list, conditions: list, directory: str) -> DataFrame:
        data_frame = self.pandas.read_csv(directory)
        housing_type = data_frame[columns[0]].isin(conditions[0])
        is_operation_sale = data_frame[columns[1]].isin(conditions[1])
        is_property_currency_usd = data_frame[columns[2]].isin(conditions[2])
        is_place_l2_capital_federal = data_frame[columns[3]].isin(conditions[3])
        return data_frame[housing_type & is_operation_sale & is_property_currency_usd & is_place_l2_capital_federal]

    def export_csv_by(self, directory: str, data_type: DataFrame) -> None:
        data_type.to_csv(directory, index=False)
