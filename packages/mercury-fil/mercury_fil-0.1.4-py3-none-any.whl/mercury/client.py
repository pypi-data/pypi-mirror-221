from functools import cache
from typing import Optional, Tuple, Union
import google.auth
import pandas as pd
import pandas_gbq

from google.cloud import bigquery


def to_gib(bytes: float) -> str:
    """
    Given bytes, convert it to GiB.

    :param bytes: the bytes to convert
    :return: GiB formatted as string
        with a precision of 7 (i.e., 7 digits after decimal)
    """
    return f"{bytes / (1024 * 1024 * 1024):.7f} GiB"


class Client:
    """
    Client implementation handling all interactions with BigQuery.

    :attr bq_project: The GCP project ID that has
        the BigQuery project containing the Filecoin historical chain data.
    :attr dataset: The qualified dataset to use.
    """

    bq_project: str = "protocol-labs-data"
    dataset: str = "lily"

    def __init__(
        self,
    ) -> None:
        credentials, _ = google.auth.default()
        self._project = self.bq_project
        
        pandas_gbq.context.credentials = credentials
        pandas_gbq.context.project = self._project
        
        self._bqc = bigquery.Client()
        self._dry_run_config = bigquery.QueryJobConfig(
            dry_run=True, use_query_cache=False
        )

    def _generic_gbq_query(
        self,
        dataset_name: str,
        start_height: int,
        end_height: int,
        columns: Tuple,
        dry_run: bool = True,
    ) -> Union[str, pd.DataFrame]:
        """
        Generic function to fetch data from a given dataset for a given range of heights.

        :param dataset_name: the name of the dataset to fetch data from.
        :param start_height: the lower bound, i.e. start height
        :param end_height: the upper bound, i.e. end height
        :param columns: the columns to include in the result.
        :param dry_run: if set to True, doesn't run the job
            and only computes the bytes processed.
        :return: a pandas DataFrame containing the selected columns at the
            given range between start_height and end_height.
        """
        assert start_height <= end_height

        query = f"""
        SELECT {", ".join(columns)}
        FROM `{self.bq_project}.{self.dataset}.{dataset_name}`
        WHERE height between {start_height} and {end_height}
        """

        if dry_run:
            bytes = self._bqc.query(
                query, job_config=self._dry_run_config
            ).total_bytes_processed
            return to_gib(bytes)

        return pd.read_gbq(query, project_id=self.project)

    @property
    def project(self):
        return self._project

    @cache
    def fevm_contracts(
        self,
        start_height: int,
        end_height: int,
        columns: Optional[Tuple] = None,
        dry_run: bool = True,
    ) -> Union[str, pd.DataFrame]:
        """
        Returns a DataFrame containing FEVM contracts. This
        includes creation of new contracts and subsequent updates
        to existing contracts.

        :param start_height: the lower bound, i.e. start height
        :param end_height: the upper bound, i.e. end height
        :param columns: the columns to include in the result. Select only
            what is needed to optimize for performance and $ cost.
        :param dry_run: if set to True, doesn't run the job
            and only computes the bytes processed.
        :return: a pandas DataFrame containing the aforementioned columns
            at the given range between start_height and end_height.
        """
        columns = (
            ("height", "eth_address", "byte_code", "balance")
            if columns is None
            else columns
        )

        return self._generic_gbq_query(
            "fevm_contracts", start_height, end_height, columns, dry_run
        )

    @cache
    def derived_gas_outputs(
        self,
        start_height: int,
        end_height: int,
        columns: Optional[Tuple] = None,
        dry_run: bool = True,
    ) -> Union[str, pd.DataFrame]:
        """
        Returns a DataFrame containing results from derived calculations
        of a message execution in the VM. This is backed by the
        `derived_gas_outputs` table.

        :param start_height: the lower bound, i.e. start height
        :param end_height: the upper bound, i.e. end height
        :param columns: the columns to include in the result. Select only
            what is needed to optimize for performance and $ cost.
        :param dry_run: if set to True, doesn't run the job
            and only computes the bytes processed.
        :return: a pandas DataFrame containing the selected columns at the
            at the given range between start_height and end_height.
        """
        columns = (
            (
                "height",
                "`from`",
                "`to`",
                "value",
                "method",
                "gas_used",
            )
            if columns is None
            else columns
        )

        return self._generic_gbq_query(
            "derived_gas_outputs", start_height, end_height, columns, dry_run
        )

    @cache
    def miner_sector_infos(
        self,
        start_height: int,
        end_height: int,
        columns: Optional[Tuple] = None,
        dry_run: bool = True,
    ) -> Union[str, pd.DataFrame]:
        """
        Returns a DataFrame containing the latest state information
        of sectors by Storage Provider (fka Miner).

        :param start_height: the lower bound, i.e. start height
        :param end_height: the upper bound, i.e. end height
        :param columns: the columns to include in the result. Select only
            what is needed to optimize for performance and $ cost.
        :param dry_run: if set to True, doesn't run the job
            and only computes the bytes processed.
        :return: a pandas DataFrame containing the selected columns at the
            at the given range between start_height and end_height.
        """
        columns = (
            (
                "height",
                "miner_id",
                "sector_id",
                "activation_epoch",
                "expiration_epoch",
                "verified_deal_weight",
            )
            if columns is None
            else columns
        )

        return self._generic_gbq_query(
            "miner_sector_infos", start_height, end_height, columns, dry_run
        )

    @cache
    def miner_sector_events(
        self,
        start_height: int,
        end_height: int,
        columns: Optional[Tuple] = None,
        dry_run: bool = True,
    ) -> Union[str, pd.DataFrame]:
        """
        Returns a DataFrame containing the latest state events
        of sectors by Storage Provider (fka Miner) or Sector.

        :param start_height: the lower bound, i.e. start height
        :param end_height: the upper bound, i.e. end height
        :param columns: the columns to include in the result. Select only
            what is needed to optimize for performance and $ cost.
        :param dry_run: if set to True, doesn't run the job
            and only computes the bytes processed.
        :return: a pandas DataFrame containing the selected columns at the
            at the given range between start_height and end_height.
        """
        columns = (
            (
                "height",
                "miner_id",
                "sector_id",
                "event",
            )
            if columns is None
            else columns
        )

        return self._generic_gbq_query(
            "miner_sector_events", start_height, end_height, columns, dry_run
        )
