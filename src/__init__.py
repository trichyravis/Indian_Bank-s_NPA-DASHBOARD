
"""
NPA Analysis Dashboard - Main Package
======================================

A comprehensive dashboard for analyzing Non-Performing Assets (NPA)
across Indian banks using Python, Pandas, Plotly, and Streamlit.

Modules:
    - data_model: Data schema and validation
    - bank_list: Bank universe selection and management
    - ingest: Data collection and ingestion workflow
    - validate: Data quality validation rules
    - analytics: Analytics engines and calculations
    - app: Streamlit dashboard application

Author: Prof. V. Ravichandran
Version: 1.0.0
License: MIT
"""

__version__ = "1.0.0"
__author__ = "Prof. V. Ravichandran"
__license__ = "MIT"

from .data_model import (
    create_empty_dataframe,
    save_csv,
    load_csv,
    print_schema,
    create_sample_data
)

from .validate import DataValidator

from .analytics import (
    AssetQualityAnalytics,
    ProfitabilityAnalytics,
    PeerComparisonAnalytics
)

__all__ = [
    'create_empty_dataframe',
    'save_csv',
    'load_csv',
    'print_schema',
    'create_sample_data',
    'DataValidator',
    'AssetQualityAnalytics',
    'ProfitabilityAnalytics',
    'PeerComparisonAnalytics',
]
