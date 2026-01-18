"""
STEP 1: DATA MODEL - Define the tidy table structure
=====================================================
Author: Prof. V. Ravichandran
Project: NPA Analysis Dashboard
Date: January 18, 2026

This module defines the core data structure:
- bank (code): e.g., 'SBI', 'HDFC', 'ICICI'
- period_type: 'FY' or 'Quarter'
- period: e.g., 'FY2025' or '2025-Q4'
- gnpa_pct: Gross NPA percentage
- nnpa_pct: Net NPA percentage
- nim_pct: Net Interest Margin percentage
- casa_pct: CASA Ratio percentage
- source_url: Direct link to filing PDF
- source_doc_date: Release date (YYYY-MM-DD)
- notes: Optional comments
"""

import pandas as pd
from datetime import datetime
from pathlib import Path

# ===== TIDY TABLE SCHEMA =====
SCHEMA = {
    'bank': str,                    # Bank code: SBI, HDFC, etc.
    'period_type': str,             # 'FY' or 'Quarter'
    'period': str,                  # 'FY2025' or '2025-Q4'
    'gnpa_pct': float,              # Gross NPA %
    'nnpa_pct': float,              # Net NPA %
    'nim_pct': float,               # Net Interest Margin %
    'casa_pct': float,              # CASA Ratio %
    'source_url': str,              # URL to source filing
    'source_doc_date': str,         # Release date (YYYY-MM-DD)
    'notes': str,                   # Optional notes/comments
}

# ===== COLUMN DESCRIPTIONS =====
COLUMN_INFO = {
    'bank': 'Bank code (e.g., SBI, HDFC, ICICI)',
    'period_type': 'Type of period: FY or Quarter',
    'period': 'Period value: FY2025 or 2025-Q4',
    'gnpa_pct': 'Gross NPA / Gross Advances × 100',
    'nnpa_pct': 'Net NPA / Net Advances × 100',
    'nim_pct': '(Net Interest Income / Average Earning Assets) × 100',
    'casa_pct': '(Current + Savings Deposits) / Total Deposits × 100',
    'source_url': 'Direct URL to NSE/BSE filing PDF',
    'source_doc_date': 'Document release date (YYYY-MM-DD format)',
    'notes': 'Any relevant notes or flags',
}

# ===== VALIDATION RANGES =====
VALIDATION_RANGES = {
    'gnpa_pct': (0, 15, 'GNPA should be 0-15%'),
    'nnpa_pct': (0, 3, 'NNPA should be 0-3%'),
    'nim_pct': (0.5, 8, 'NIM should be 0.5-8%'),
    'casa_pct': (0, 100, 'CASA should be 0-100%'),
}


def create_empty_dataframe():
    """
    Create empty DataFrame with the correct schema
    
    Returns:
        pd.DataFrame: Empty dataframe with correct column types
    """
    df = pd.DataFrame(columns=list(SCHEMA.keys()))
    for col, dtype in SCHEMA.items():
        df[col] = df[col].astype(dtype)
    return df


def save_csv(df, filepath='bank_metrics.csv'):
    """
    Save dataframe to CSV file
    
    Args:
        df (pd.DataFrame): Data to save
        filepath (str): Output file path
    """
    df.to_csv(filepath, index=False)
    print(f"✅ Saved to {filepath}")
    print(f"   Rows: {len(df)}")
    print(f"   Columns: {len(df.columns)}")


def load_csv(filepath='bank_metrics.csv'):
    """
    Load CSV into dataframe with correct schema
    
    Args:
        filepath (str): Path to CSV file
        
    Returns:
        pd.DataFrame: Loaded data
    """
    df = pd.read_csv(filepath)
    print(f"✅ Loaded from {filepath}")
    print(f"   Rows: {len(df)}")
    print(f"   Columns: {len(df.columns)}")
    return df


def print_schema():
    """Print data model schema"""
    print("\n" + "="*70)
    print("DATA MODEL SCHEMA - TIDY TABLE")
    print("="*70)
    print("\nColumns:")
    for col, dtype in SCHEMA.items():
        desc = COLUMN_INFO.get(col, '')
        dtype_name = dtype.__name__ if hasattr(dtype, '__name__') else str(dtype)
        print(f"  {col:20} ({dtype_name:10}) - {desc}")
    
    print("\nValidation Ranges:")
    for col, (min_val, max_val, desc) in VALIDATION_RANGES.items():
        print(f"  {col:20} : {min_val}-{max_val} ({desc})")
    
    print("\nExample Row:")
    print("  bank: 'SBI'")
    print("  period_type: 'Quarter'")
    print("  period: '2025-Q3'")
    print("  gnpa_pct: 2.45")
    print("  nnpa_pct: 0.38")
    print("  nim_pct: 3.12")
    print("  casa_pct: 42.5")
    print("  source_url: 'https://www.nseindia.com/.../SBI_Q3.pdf'")
    print("  source_doc_date: '2026-01-15'")
    print("  notes: 'Verified from NSE filing'")
    print("="*70 + "\n")


def create_sample_data():
    """Create sample data for testing"""
    sample = pd.DataFrame([
        {
            'bank': 'SBI',
            'period_type': 'Quarter',
            'period': '2025-Q3',
            'gnpa_pct': 2.45,
            'nnpa_pct': 0.38,
            'nim_pct': 3.12,
            'casa_pct': 42.5,
            'source_url': 'https://www.nseindia.com/corporate/SBI_Q3FY26.pdf',
            'source_doc_date': '2026-01-15',
            'notes': 'From NSE filing'
        },
        {
            'bank': 'HDFC',
            'period_type': 'Quarter',
            'period': '2025-Q3',
            'gnpa_pct': 1.32,
            'nnpa_pct': 0.21,
            'nim_pct': 4.15,
            'casa_pct': 45.2,
            'source_url': 'https://www.nseindia.com/corporate/HDFC_Q3FY26.pdf',
            'source_doc_date': '2026-01-14',
            'notes': 'From NSE filing'
        },
        {
            'bank': 'ICICI',
            'period_type': 'Quarter',
            'period': '2025-Q3',
            'gnpa_pct': 1.28,
            'nnpa_pct': 0.19,
            'nim_pct': 4.08,
            'casa_pct': 39.8,
            'source_url': 'https://www.nseindia.com/corporate/ICICI_Q3FY26.pdf',
            'source_doc_date': '2026-01-13',
            'notes': 'From NSE filing'
        },
        {
            'bank': 'AXIS',
            'period_type': 'Quarter',
            'period': '2025-Q3',
            'gnpa_pct': 1.89,
            'nnpa_pct': 0.25,
            'nim_pct': 3.98,
            'casa_pct': 40.1,
            'source_url': 'https://www.nseindia.com/corporate/AXIS_Q3FY26.pdf',
            'source_doc_date': '2026-01-12',
            'notes': 'From NSE filing'
        },
        {
            'bank': 'KOTAK',
            'period_type': 'Quarter',
            'period': '2025-Q3',
            'gnpa_pct': 1.15,
            'nnpa_pct': 0.18,
            'nim_pct': 4.25,
            'casa_pct': 46.3,
            'source_url': 'https://www.nseindia.com/corporate/KOTAK_Q3FY26.pdf',
            'source_doc_date': '2026-01-11',
            'notes': 'From NSE filing'
        },
    ])
    return sample


# ===== MAIN EXECUTION =====
if __name__ == "__main__":
    print("\n🔧 STEP 1: DATA MODEL INITIALIZATION\n")
    
    # Print schema
    print_schema()
    
    # Create empty dataframe
    print("Creating empty dataframe...")
    df_empty = create_empty_dataframe()
    print(f"✅ Empty dataframe created")
    print(f"   Shape: {df_empty.shape}")
    print(f"   Columns: {list(df_empty.columns)}\n")
    
    # Create sample data
    print("Creating sample data (5 rows for reference)...")
    df_sample = create_sample_data()
    save_csv(df_sample, 'bank_metrics_sample.csv')
    print(f"✅ Sample data created (5 rows)\n")
    print(df_sample.to_string())
    
    print("\n" + "="*70)
    print("✅ STEP 1 COMPLETE")
    print("="*70)
    print("\nNext steps:")
    print("1. Review bank_metrics_sample.csv for structure")
    print("2. Run: python step2_bank_list.py")
    print("3. Create collection template using ingest.py")
    print("="*70 + "\n")
