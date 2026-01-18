"""
STEP 3: DATA INGESTION - Manual-to-CSV Pipeline
================================================
Author: Prof. V. Ravichandran
Project: NPA Analysis Dashboard
Date: January 18, 2026

WORKFLOW:
1. Download investor presentations (PDF) from NSE
2. Extract metrics from "Asset Quality" slides
3. Enter into Excel/CSV template
4. Validate and save

DATA SOURCES:
- NSE: https://www.nseindia.com/corporate/financialresults
- BSE: https://www.bseindia.com/corporates/filings
- Bank IR websites: https://www.[bankname].com/investor
"""

import pandas as pd
from datetime import datetime
from pathlib import Path

# ===== INGESTION INSTRUCTIONS =====
INGESTION_GUIDE = """
HOW TO COLLECT DATA - MANUAL APPROACH
=====================================

✅ FAST & RELIABLE (1-2 weeks for 15 banks × 12 quarters)

Step 1: DOWNLOAD
  → Go to: https://www.nseindia.com/corporate/financialresults
  → Search for bank name (e.g., "SBI" or "SBIN")
  → Find quarterly result: "Q3 FY26" or "2025-Q3" or "Oct-Dec 2025"
  → Download PDF presentation or investor presentation

Step 2: EXTRACT FROM PDF
  → Open downloaded PDF
  → Find slide titled: "Asset Quality" or "Financial Performance"
  → Look for table with rows like:
     ├── Gross Advances
     ├── Gross NPAs (Amount & %)
     ├── Net NPAs (Amount & %)
     └── Provisions
  → Also find:
     ├── Net Interest Margin (NIM) %
     └── CASA Ratio %

Step 3: ENTER INTO EXCEL
  → Open: collection_checklist.csv or collection_template.xlsx
  → For each bank-quarter, fill:
     ├── gnpa_pct: Gross NPA %
     ├── nnpa_pct: Net NPA %
     ├── nim_pct: Net Interest Margin %
     └── casa_pct: CASA %
  → Also fill:
     ├── source_url: Direct URL to the PDF you downloaded
     └── source_date: Date when the PDF was released (YYYY-MM-DD)

Step 4: VALIDATE & SAVE
  → Check: GNPA ≥ NNPA (always)
  → Check: NIM between 0.5% - 8%
  → Check: CASA between 0% - 100%
  → Save as: bank_metrics.csv

EXPECTED TIME:
  Per bank: ~1-1.5 hours (12 quarters)
  15 banks: ~18-22 hours
  Spread over 2-3 weeks: Easy part-time work

TIPS:
  1. Do PSU banks first (SBI, PNB, BoB) - they're fastest
  2. Download all PDFs first, then extract in batch
  3. Use copy-paste to avoid typos
  4. Double-check GNPA and NIM values (most common errors)
  5. If quarter not available, mark as TODO and skip
"""

# ===== FILLED SAMPLE DATA (5 banks, Q3 FY26 only) =====
SAMPLE_FILLED_DATA = [
    {
        'bank_code': 'SBI',
        'bank_name': 'State Bank of India',
        'nse_ticker': 'SBIN',
        'quarter': '2025-Q3',
        'status': 'DONE',
        'gnpa_pct': 2.45,
        'nnpa_pct': 0.38,
        'nim_pct': 3.12,
        'casa_pct': 42.5,
        'source_url': 'https://www.nseindia.com/corporate/resultcompany/SBI_quarterly_2025-Q3.pdf',
        'source_date': '2026-01-15',
    },
    {
        'bank_code': 'HDFC',
        'bank_name': 'HDFC Bank',
        'nse_ticker': 'HDFCBANK',
        'quarter': '2025-Q3',
        'status': 'DONE',
        'gnpa_pct': 1.32,
        'nnpa_pct': 0.21,
        'nim_pct': 4.15,
        'casa_pct': 45.2,
        'source_url': 'https://www.nseindia.com/corporate/resultcompany/HDFC_quarterly_2025-Q3.pdf',
        'source_date': '2026-01-14',
    },
    {
        'bank_code': 'ICICI',
        'bank_name': 'ICICI Bank',
        'nse_ticker': 'ICICIBANK',
        'quarter': '2025-Q3',
        'status': 'DONE',
        'gnpa_pct': 1.28,
        'nnpa_pct': 0.19,
        'nim_pct': 4.08,
        'casa_pct': 39.8,
        'source_url': 'https://www.nseindia.com/corporate/resultcompany/ICICI_quarterly_2025-Q3.pdf',
        'source_date': '2026-01-13',
    },
    {
        'bank_code': 'AXIS',
        'bank_name': 'Axis Bank',
        'nse_ticker': 'AXISBANK',
        'quarter': '2025-Q3',
        'status': 'DONE',
        'gnpa_pct': 1.89,
        'nnpa_pct': 0.25,
        'nim_pct': 3.98,
        'casa_pct': 40.1,
        'source_url': 'https://www.nseindia.com/corporate/resultcompany/AXIS_quarterly_2025-Q3.pdf',
        'source_date': '2026-01-12',
    },
    {
        'bank_code': 'KOTAK',
        'bank_name': 'Kotak Mahindra Bank',
        'nse_ticker': 'KOTAKBANK',
        'quarter': '2025-Q3',
        'status': 'DONE',
        'gnpa_pct': 1.15,
        'nnpa_pct': 0.18,
        'nim_pct': 4.25,
        'casa_pct': 46.3,
        'source_url': 'https://www.nseindia.com/corporate/resultcompany/KOTAK_quarterly_2025-Q3.pdf',
        'source_date': '2026-01-11',
    },
]


def print_ingestion_guide():
    """Print data collection instructions"""
    print("\n" + INGESTION_GUIDE)


def create_collection_template_excel():
    """Create Excel template for manual data entry"""
    
    # Create empty template
    df_template = pd.read_csv('collection_checklist.csv')
    
    # Save as Excel with formatting (easier for manual entry)
    output_file = 'COLLECTION_TEMPLATE_FILL_THIS.xlsx'
    
    df_template.to_excel(output_file, index=False, sheet_name='Data Entry')
    
    print(f"✅ Excel template created: {output_file}")
    print("   Open this file and fill in the metrics\n")
    
    return output_file


def load_partially_filled_data(filepath):
    """
    Load CSV that has been partially filled
    
    Example: User fills in first 5 banks manually
    """
    df = pd.read_csv(filepath)
    
    # Show progress
    total_rows = len(df)
    filled_rows = len(df[df['status'] == 'DONE'])
    todo_rows = len(df[df['status'] == 'TODO'])
    
    print(f"\n📊 DATA COLLECTION PROGRESS")
    print("=" * 70)
    print(f"Total rows: {total_rows}")
    print(f"Filled (DONE): {filled_rows} ({(filled_rows/total_rows)*100:.1f}%)")
    print(f"To fill (TODO): {todo_rows} ({(todo_rows/total_rows)*100:.1f}%)")
    print("=" * 70 + "\n")
    
    return df


def validate_filled_data(df):
    """
    Quick validation of filled data
    Returns: DataFrame with validation_status
    """
    issues = []
    
    # Check filled rows only
    filled_df = df[df['status'] == 'DONE'].copy()
    
    if len(filled_df) == 0:
        print("⚠️ No completed rows yet. Start filling data!\n")
        return df
    
    print(f"\n🔍 VALIDATING {len(filled_df)} FILLED ROWS")
    print("=" * 70)
    
    # Rule 1: GNPA ≥ NNPA
    violations = filled_df['gnpa_pct'] < filled_df['nnpa_pct']
    if violations.any():
        print(f"❌ GNPA < NNPA violations: {violations.sum()}")
        for idx in filled_df[violations].index:
            print(f"   {filled_df.loc[idx, 'bank_code']} {filled_df.loc[idx, 'quarter']}")
        issues.append('GNPA < NNPA')
    
    # Rule 2: NIM range
    nim_invalid = (filled_df['nim_pct'] < 0.5) | (filled_df['nim_pct'] > 8)
    if nim_invalid.any():
        print(f"⚠️ NIM out of range (0.5-8%): {nim_invalid.sum()}")
        for idx in filled_df[nim_invalid].index:
            print(f"   {filled_df.loc[idx, 'bank_code']} {filled_df.loc[idx, 'quarter']}: "
                  f"{filled_df.loc[idx, 'nim_pct']}%")
    
    # Rule 3: CASA range
    casa_invalid = (filled_df['casa_pct'] < 0) | (filled_df['casa_pct'] > 100)
    if casa_invalid.any():
        print(f"❌ CASA out of range (0-100%): {casa_invalid.sum()}")
        for idx in filled_df[casa_invalid].index:
            print(f"   {filled_df.loc[idx, 'bank_code']} {filled_df.loc[idx, 'quarter']}")
        issues.append('CASA invalid')
    
    # Rule 4: GNPA reasonable
    gnpa_high = filled_df['gnpa_pct'] > 15
    if gnpa_high.any():
        print(f"⚠️ GNPA unusually high (>15%): {gnpa_high.sum()}")
        for idx in filled_df[gnpa_high].index:
            print(f"   {filled_df.loc[idx, 'bank_code']} {filled_df.loc[idx, 'quarter']}: "
                  f"{filled_df.loc[idx, 'gnpa_pct']}%")
    
    if len(issues) == 0:
        print("✅ All validations PASSED!")
    else:
        print(f"\n❌ Found {len(issues)} issues. Please fix and re-validate.")
    
    print("=" * 70 + "\n")
    
    return df


def merge_filled_data(df_collected, output_file='bank_metrics.csv'):
    """
    Merge manually collected data into final CSV
    
    Input: collection_checklist.csv (partially or fully filled)
    Output: bank_metrics.csv (ready for analytics)
    """
    
    # Filter only completed rows
    df_final = df_collected[df_collected['status'] == 'DONE'].copy()
    
    # Rename columns to match tidy table
    df_final = df_final.rename(columns={
        'bank_code': 'bank',
        'quarter': 'period',
    })
    
    # Add period_type
    df_final['period_type'] = 'Quarter'
    
    # Rename source columns
    df_final = df_final.rename(columns={
        'source_url': 'source_url',
        'source_date': 'source_doc_date',
    })
    
    # Add notes column
    df_final['notes'] = 'Manually collected from NSE filings'
    
    # Select final columns in order
    final_columns = [
        'bank', 'period_type', 'period',
        'gnpa_pct', 'nnpa_pct', 'nim_pct', 'casa_pct',
        'source_url', 'source_doc_date', 'notes'
    ]
    
    df_final = df_final[final_columns]
    
    # Save
    df_final.to_csv(output_file, index=False)
    
    print(f"✅ Final dataset saved: {output_file}")
    print(f"   Rows: {len(df_final)}")
    print(f"   Columns: {len(df_final.columns)}")
    print(f"   Expected: 144 rows (12 banks × 12 quarters)\n")
    
    return df_final


# ===== MAIN EXECUTION =====
if __name__ == "__main__":
    print("\n📥 STEP 3: DATA INGESTION - MANUAL APPROACH\n")
    
    # Print guide
    print_ingestion_guide()
    
    # Create collection template
    print("\n" + "="*70)
    print("Creating collection template...")
    print("="*70)
    template_file = create_collection_template_excel()
    
    # Create sample filled data (for demonstration)
    print("Creating sample filled data (5 banks, Q3 FY26)...")
    df_sample_filled = pd.DataFrame(SAMPLE_FILLED_DATA)
    df_sample_filled.to_csv('sample_filled_data.csv', index=False)
    print(f"✅ sample_filled_data.csv created (5 rows)\n")
    print(df_sample_filled.to_string())
    
    # Demonstrate validation
    print("\n" + "="*70)
    print("Demonstrating data validation on sample...")
    print("="*70)
    validate_filled_data(df_sample_filled)
    
    # Demonstrate merge
    print("="*70)
    print("Merging sample data into final format...")
    print("="*70)
    df_final = merge_filled_data(df_sample_filled, 'bank_metrics_sample_final.csv')
    print(df_final.to_string())
    
    print("\n" + "="*70)
    print("✅ STEP 3 COMPLETE")
    print("="*70)
    print("\nFiles created:")
    print("  1. COLLECTION_TEMPLATE_FILL_THIS.xlsx - Excel for manual entry")
    print("  2. collection_checklist.csv - CSV template")
    print("  3. sample_filled_data.csv - Example of filled data")
    print("  4. bank_metrics_sample_final.csv - Final format example")
    print("\nNext steps:")
    print("  1. Download NSE presentations for each bank (12 quarters)")
    print("  2. Extract metrics from 'Asset Quality' slides")
    print("  3. Fill in COLLECTION_TEMPLATE_FILL_THIS.xlsx")
    print("  4. Save as collection_checklist.csv")
    print("  5. Run: python step4_validate.py")
    print("  6. Run: python step5_analytics.py")
    print("  7. Run: streamlit run app.py")
    print("="*70 + "\n")
