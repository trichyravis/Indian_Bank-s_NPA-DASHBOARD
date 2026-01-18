"""
STEP 5: CORE ANALYTICS - Build analytics engine
================================================
Author: Prof. V. Ravichandran
Project: NPA Analysis Dashboard
Date: January 18, 2026

Analytics modules:
A) Asset Quality: GNPA/NNPA trends, YoY changes
B) Profitability: NIM, CASA trends
C) Peer Comparison: Rankings, quadrant view
"""

import pandas as pd
import numpy as np
from datetime import datetime

class AssetQualityAnalytics:
    """Asset quality analysis"""
    
    def __init__(self, df):
        self.df = df.copy()
    
    def latest_metrics(self):
        """Get latest metrics for each bank"""
        latest = self.df.loc[self.df.groupby('bank')['period'].idxmax()]
        return latest.sort_values('gnpa_pct')[['bank', 'period', 'gnpa_pct', 'nnpa_pct', 'nim_pct', 'casa_pct']]
    
    def gnpa_trend(self, bank_code):
        """Get GNPA trend for single bank"""
        bank_data = self.df[self.df['bank'] == bank_code].sort_values('period')
        
        return {
            'periods': bank_data['period'].tolist(),
            'gnpa_pct': bank_data['gnpa_pct'].tolist(),
            'nnpa_pct': bank_data['nnpa_pct'].tolist(),
            'gnpa_avg': bank_data['gnpa_pct'].mean(),
            'gnpa_min': bank_data['gnpa_pct'].min(),
            'gnpa_max': bank_data['gnpa_pct'].max(),
            'trend': 'Improving' if len(bank_data) > 1 and bank_data['gnpa_pct'].iloc[-1] < bank_data['gnpa_pct'].iloc[0] else 'Stable' if len(bank_data) <= 1 else 'Deteriorating',
        }
    
    def spread_analysis(self):
        """GNPA - NNPA spread (proxy for provision effectiveness)"""
        self.df['spread_bps'] = (self.df['gnpa_pct'] - self.df['nnpa_pct']) * 100
        
        latest = self.df.loc[self.df.groupby('bank')['period'].idxmax()]
        return latest[['bank', 'gnpa_pct', 'nnpa_pct', 'spread_bps']].sort_values('spread_bps', ascending=False)


class ProfitabilityAnalytics:
    """Profitability and funding analysis"""
    
    def __init__(self, df):
        self.df = df.copy()
    
    def nim_trends(self):
        """Latest NIM for each bank"""
        latest = self.df.loc[self.df.groupby('bank')['period'].idxmax()]
        return latest.sort_values('nim_pct', ascending=False)[['bank', 'nim_pct']]
    
    def casa_trends(self):
        """Latest CASA for each bank"""
        latest = self.df.loc[self.df.groupby('bank')['period'].idxmax()]
        return latest.sort_values('casa_pct', ascending=False)[['bank', 'casa_pct']]
    
    def profitability_vs_risk(self):
        """NIM vs GNPA scatter data"""
        latest = self.df.loc[self.df.groupby('bank')['period'].idxmax()]
        return latest[['bank', 'nim_pct', 'gnpa_pct', 'casa_pct']].sort_values('nim_pct', ascending=False)


class PeerComparisonAnalytics:
    """Peer benchmarking"""
    
    def __init__(self, df):
        self.df = df.copy()
    
    def latest_rankings(self):
        """Full rankings for latest period"""
        latest = self.df.loc[self.df.groupby('bank')['period'].idxmax()]
        rankings = latest.sort_values('gnpa_pct')[['bank', 'gnpa_pct', 'nnpa_pct', 'nim_pct', 'casa_pct']]
        rankings['gnpa_rank'] = range(1, len(rankings) + 1)
        return rankings
    
    def quadrant_view(self):
        """
        Quadrant analysis:
        X-axis: CASA (funding)
        Y-axis: GNPA (risk)
        Best: High CASA + Low GNPA (top-right)
        """
        latest = self.df.loc[self.df.groupby('bank')['period'].idxmax()]
        
        casa_median = latest['casa_pct'].median()
        gnpa_median = latest['gnpa_pct'].median()
        
        latest['quadrant'] = (
            latest.apply(lambda row:
                'BEST' if row['casa_pct'] > casa_median and row['gnpa_pct'] < gnpa_median
                else 'CAUTION' if row['casa_pct'] > casa_median and row['gnpa_pct'] >= gnpa_median
                else 'WATCH' if row['casa_pct'] <= casa_median and row['gnpa_pct'] < gnpa_median
                else 'WORST', axis=1)
        )
        
        return latest[['bank', 'casa_pct', 'gnpa_pct', 'quadrant']].sort_values('quadrant')


# ===== MAIN EXECUTION =====
if __name__ == "__main__":
    print("\n📊 STEP 5: CORE ANALYTICS\n")
    
    # Load validated data
    try:
        df = pd.read_csv('bank_metrics_validated.csv')
        print(f"✅ Loaded {len(df)} rows from bank_metrics_validated.csv\n")
    except FileNotFoundError:
        print("❌ File not found: bank_metrics_validated.csv")
        print("   Run step4_validate.py first")
        import sys
        sys.exit(1)
    
    # Initialize analytics engines
    asset_quality = AssetQualityAnalytics(df)
    profitability = ProfitabilityAnalytics(df)
    peer = PeerComparisonAnalytics(df)
    
    # ===== A) ASSET QUALITY =====
    print("="*70)
    print("A) ASSET QUALITY ANALYSIS")
    print("="*70)
    
    print("\n📌 Latest NPA Metrics (by GNPA):")
    print("-" * 70)
    print(asset_quality.latest_metrics().to_string())
    
    print("\n📌 NPA Spread Analysis (GNPA - NNPA in bps):")
    print("-" * 70)
    spread = asset_quality.spread_analysis()
    print(spread.to_string())
    
    print("\n📌 Sample Bank Trends:")
    print("-" * 70)
    for bank in df['bank'].unique()[:2]:  # Show first 2 banks
        trend = asset_quality.gnpa_trend(bank)
        print(f"\n{bank}:")
        print(f"  Periods: {' → '.join(trend['periods'][:3])} ... {trend['periods'][-1]}")
        print(f"  GNPA Range: {trend['gnpa_min']:.2f}% - {trend['gnpa_max']:.2f}%")
        print(f"  Trend: {trend['trend']}")
    
    # ===== B) PROFITABILITY =====
    print("\n" + "="*70)
    print("B) PROFITABILITY & FUNDING ANALYSIS")
    print("="*70)
    
    print("\n📌 Latest NIM Rankings:")
    print("-" * 70)
    print(profitability.nim_trends().to_string())
    
    print("\n📌 Latest CASA Rankings:")
    print("-" * 70)
    print(profitability.casa_trends().to_string())
    
    print("\n📌 Profitability vs Risk (NIM vs GNPA):")
    print("-" * 70)
    print(profitability.profitability_vs_risk().to_string())
    
    # ===== C) PEER COMPARISON =====
    print("\n" + "="*70)
    print("C) PEER COMPARISON")
    print("="*70)
    
    print("\n📌 Latest Quarter Rankings (ALL METRICS):")
    print("-" * 70)
    print(peer.latest_rankings().to_string())
    
    print("\n📌 Quadrant View (CASA vs GNPA):")
    print("-" * 70)
    quadrant = peer.quadrant_view()
    for q in ['BEST', 'CAUTION', 'WATCH', 'WORST']:
        banks_in_q = quadrant[quadrant['quadrant'] == q]['bank'].tolist()
        if banks_in_q:
            print(f"  {q:10} : {', '.join(banks_in_q)}")
    
    # ===== SAVE ANALYTICS =====
    print("\n" + "="*70)
    print("SAVING ANALYTICS OUTPUTS")
    print("="*70)
    
    # Save rankings
    rankings = peer.latest_rankings()
    rankings.to_csv('analytics_rankings.csv', index=False)
    print("\n✅ rankings saved to: analytics_rankings.csv")
    
    # Save quadrant
    quadrant.to_csv('analytics_quadrant.csv', index=False)
    print("✅ Quadrant analysis saved to: analytics_quadrant.csv")
    
    # Save spread
    spread.to_csv('analytics_spread.csv', index=False)
    print("✅ Spread analysis saved to: analytics_spread.csv")
    
    print("\n" + "="*70)
    print("✅ STEP 5 COMPLETE")
    print("="*70)
    print("\nAnalytics outputs created:")
    print("  1. analytics_rankings.csv - Full rankings")
    print("  2. analytics_quadrant.csv - Quadrant positioning")
    print("  3. analytics_spread.csv - NPA spread analysis")
    print("\nNext steps:")
    print("  Run: streamlit run app.py")
    print("="*70 + "\n")
