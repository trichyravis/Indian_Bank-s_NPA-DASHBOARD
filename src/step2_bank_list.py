"""
STEP 2: BANK UNIVERSE - Define recommended bank list
====================================================
Author: Prof. V. Ravichandran
Project: NPA Analysis Dashboard
Date: January 18, 2026

Recommended 15 banks (verified for 5+ years data):
- PSU: SBI, PNB, BoB, Canara, Union (5)
- Private: HDFC, ICICI, Axis, Kotak, IndusInd (5)
- SFB: AU, Bandhan (2)
- Optional: CBI, BOI (for expansion)
"""

import pandas as pd
from datetime import datetime

# ===== BANK UNIVERSE =====
BANK_UNIVERSE = {
    'PSU': {
        'SBI': {
            'full_name': 'State Bank of India',
            'nse_ticker': 'SBIN',
            'category': 'Large PSU',
            'data_years': 25,
            'website': 'https://www.sbi.co.in'
        },
        'PNB': {
            'full_name': 'Punjab National Bank',
            'nse_ticker': 'PNB',
            'category': 'Large PSU',
            'data_years': 20,
            'website': 'https://www.pnbindia.in'
        },
        'BOB': {
            'full_name': 'Bank of Baroda',
            'nse_ticker': 'BARODA',
            'category': 'Large PSU',
            'data_years': 25,
            'website': 'https://www.bankofbaroda.in'
        },
        'CAN': {
            'full_name': 'Canara Bank',
            'nse_ticker': 'CANBK',
            'category': 'Mid-size PSU',
            'data_years': 20,
            'website': 'https://www.canarabank.com'
        },
        'UBI': {
            'full_name': 'Union Bank of India',
            'nse_ticker': 'UNIONBANK',
            'category': 'Mid-size PSU',
            'data_years': 20,
            'website': 'https://www.unionbankofindia.co.in'
        },
    },
    'Private': {
        'HDFC': {
            'full_name': 'HDFC Bank',
            'nse_ticker': 'HDFCBANK',
            'category': 'Large Private',
            'data_years': 25,
            'website': 'https://www.hdfcbank.com'
        },
        'ICICI': {
            'full_name': 'ICICI Bank',
            'nse_ticker': 'ICICIBANK',
            'category': 'Large Private',
            'data_years': 25,
            'website': 'https://www.icicibank.com'
        },
        'AXIS': {
            'full_name': 'Axis Bank',
            'nse_ticker': 'AXISBANK',
            'category': 'Large Private',
            'data_years': 19,
            'website': 'https://www.axisbank.com'
        },
        'KOTAK': {
            'full_name': 'Kotak Mahindra Bank',
            'nse_ticker': 'KOTAKBANK',
            'category': 'Large Private',
            'data_years': 23,
            'website': 'https://www.kotak.com'
        },
        'INDUSIND': {
            'full_name': 'IndusInd Bank',
            'nse_ticker': 'INDUSINDBK',
            'category': 'Large Private',
            'data_years': 20,
            'website': 'https://www.indusindbank.com'
        },
    },
    'SFB': {
        'AU': {
            'full_name': 'AU Small Finance Bank',
            'nse_ticker': 'AUBANK',
            'category': 'Small Finance',
            'data_years': 9,
            'website': 'https://www.aubank.in'
        },
        'BANDHAN': {
            'full_name': 'Bandhan Bank',
            'nse_ticker': 'BANDHANBNK',
            'category': 'Small Finance',
            'data_years': 8,
            'website': 'https://www.bandhanbank.com'
        },
    }
}

# ===== OPTIONAL EXPANSION =====
OPTIONAL_BANKS = {
    'PSU': {
        'CBI': {
            'full_name': 'Central Bank of India',
            'nse_ticker': 'CENTRALBANK',
            'category': 'Mid-size PSU',
            'data_years': 25,
        },
        'BOI': {
            'full_name': 'Bank of India',
            'nse_ticker': 'BANKINDIA',
            'category': 'Mid-size PSU',
            'data_years': 20,
        },
    }
}

# ===== QUARTERS TO COLLECT =====
QUARTERS = [
    '2025-Q3',  # Oct-Dec 2025 (Latest)
    '2025-Q2',  # Jul-Sep 2025
    '2025-Q1',  # Apr-Jun 2025
    '2024-Q4',  # Jan-Mar 2025
    '2024-Q3',  # Oct-Dec 2024
    '2024-Q2',  # Jul-Sep 2024
    '2024-Q1',  # Apr-Jun 2024
    '2023-Q4',  # Jan-Mar 2024
    '2023-Q3',  # Oct-Dec 2023
    '2023-Q2',  # Jul-Sep 2023
    '2023-Q1',  # Apr-Jun 2023
    '2022-Q4',  # Jan-Mar 2023 (12 quarters = 3 years)
]

# ===== NSE/BSE FILING URLS =====
NSE_URL_TEMPLATE = "https://www.nseindia.com/corporate/financialresults"
BSE_URL_TEMPLATE = "https://www.bseindia.com/corporates/filings"


def get_all_banks(include_optional=False):
    """Get all banks as flat list"""
    banks = {}
    
    # Add main universe
    for category, cat_banks in BANK_UNIVERSE.items():
        for code, info in cat_banks.items():
            banks[code] = info
    
    # Add optional if requested
    if include_optional:
        for category, cat_banks in OPTIONAL_BANKS.items():
            for code, info in cat_banks.items():
                banks[code] = info
    
    return banks


def print_bank_summary():
    """Print summary of bank universe"""
    print("\n" + "="*70)
    print("BANK UNIVERSE - RECOMMENDED 15 BANKS")
    print("="*70)
    
    total = 0
    for category, banks in BANK_UNIVERSE.items():
        print(f"\n{category} BANKS ({len(banks)}):")
        print("-" * 70)
        for code, info in banks.items():
            total += 1
            print(f"  {code:12} | {info['full_name']:25} | {info['nse_ticker']:12} | "
                  f"{info['data_years']}+ years")
    
    print("\n" + "-"*70)
    print(f"TOTAL: {total} banks")
    print(f"QUARTERS: {len(QUARTERS)} (3 years)")
    print(f"DATA POINTS: {total * len(QUARTERS)}")
    print("="*70 + "\n")


def print_collection_plan():
    """Print data collection checklist"""
    print("\n" + "="*70)
    print("DATA COLLECTION PLAN")
    print("="*70)
    
    print("\n📋 COLLECTION CHECKLIST:")
    print("-" * 70)
    
    weeks = {
        'Week 1 (PSU Big 3)': ['SBI', 'PNB', 'BOB'],
        'Week 2 (Private Big 3)': ['HDFC', 'ICICI', 'AXIS'],
        'Week 3 (Remaining 9)': ['KOTAK', 'INDUSIND', 'CAN', 'UBI', 'AU', 'BANDHAN'],
    }
    
    total_hours = 0
    for week, banks in weeks.items():
        hours = len(banks) * 1.5  # ~1.5 hours per bank
        total_hours += hours
        print(f"\n{week} (~{hours:.0f} hours):")
        for bank in banks:
            bank_data = get_all_banks().get(bank)
            if bank_data:
                print(f"  ☐ {bank:10} - {bank_data['full_name']:30} (12 quarters)")
    
    print(f"\nTOTAL EFFORT: ~{total_hours:.0f} hours = 2-3 weeks part-time")
    print("="*70 + "\n")


def create_bank_directory():
    """Create bank directory CSV"""
    banks = get_all_banks(include_optional=False)
    
    data = []
    for code, info in banks.items():
        data.append({
            'bank_code': code,
            'bank_name': info['full_name'],
            'nse_ticker': info['nse_ticker'],
            'category': info['category'],
            'data_years': info['data_years'],
            'website': info.get('website', ''),
        })
    
    df = pd.DataFrame(data)
    df = df.sort_values(['category', 'bank_code'])
    df.to_csv('bank_directory.csv', index=False)
    
    print("✅ bank_directory.csv created\n")
    return df


def create_collection_checklist():
    """Create collection checklist CSV"""
    banks = get_all_banks(include_optional=False)
    
    checklist = []
    for code, bank_info in banks.items():
        for quarter in QUARTERS:
            checklist.append({
                'bank_code': code,
                'bank_name': bank_info['full_name'],
                'nse_ticker': bank_info['nse_ticker'],
                'quarter': quarter,
                'status': 'TODO',
                'gnpa_pct': '',
                'nnpa_pct': '',
                'nim_pct': '',
                'casa_pct': '',
                'source_url': '',
                'source_date': '',
            })
    
    df = pd.DataFrame(checklist)
    df.to_csv('collection_checklist.csv', index=False)
    
    print(f"✅ collection_checklist.csv created ({len(df)} rows to fill)\n")
    return df


# ===== MAIN EXECUTION =====
if __name__ == "__main__":
    print("\n🏦 STEP 2: BANK UNIVERSE DEFINITION\n")
    
    # Print summary
    print_bank_summary()
    
    # Print collection plan
    print_collection_plan()
    
    # Create bank directory
    print("Creating bank directory...")
    df_banks = create_bank_directory()
    print(df_banks.to_string())
    
    # Create collection checklist
    print("\nCreating collection checklist template...")
    df_checklist = create_collection_checklist()
    print(f"Template created with {len(df_checklist)} rows")
    print(f"First 10 rows:")
    print(df_checklist.head(10).to_string())
    
    print("\n" + "="*70)
    print("✅ STEP 2 COMPLETE")
    print("="*70)
    print("\nFiles created:")
    print("  1. bank_directory.csv - Bank metadata")
    print("  2. collection_checklist.csv - Template to fill with data")
    print("\nNext steps:")
    print("  1. Open collection_checklist.csv")
    print("  2. Download NSE presentations for each bank")
    print("  3. Fill in metrics from 'Asset Quality' slides")
    print("  4. Run: python step4_validate.py")
    print("="*70 + "\n")
