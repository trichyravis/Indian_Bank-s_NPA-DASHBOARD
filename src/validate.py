"""
STEP 4: DATA VALIDATION - Quality checks
==========================================
Author: Prof. V. Ravichandran
Project: NPA Analysis Dashboard
Date: January 18, 2026

Quality rules:
1. GNPA ≥ NNPA (always must be true)
2. NIM range: 0.5% - 8% (flag outliers)
3. CASA range: 0% - 100% (must be valid percentage)
4. GNPA range: 0% - 15% (flag unusually high)
5. No missing core metrics
6. NNPA ≤ GNPA
"""

import pandas as pd
import sys

class DataValidator:
    """Validate bank metrics data"""
    
    def __init__(self, df):
        self.df = df.copy()
        self.issues = []
        self.errors = []
        self.warnings = []
    
    def validate_rule_1_gnpa_nnpa(self):
        """Rule 1: GNPA ≥ NNPA (must always be true)"""
        violations = self.df['gnpa_pct'] < self.df['nnpa_pct']
        
        if violations.any():
            for idx in self.df[violations].index:
                row = self.df.loc[idx]
                self.errors.append({
                    'bank': row['bank'],
                    'period': row['period'],
                    'rule': '1: GNPA < NNPA',
                    'severity': 'ERROR',
                    'detail': f"GNPA={row['gnpa_pct']:.2f}% but NNPA={row['nnpa_pct']:.2f}%"
                })
        
        return len(violations)
    
    def validate_rule_2_nim_range(self):
        """Rule 2: NIM in reasonable range (0.5-8%)"""
        violations = (self.df['nim_pct'] < 0.5) | (self.df['nim_pct'] > 8)
        
        if violations.any():
            for idx in self.df[violations].index:
                row = self.df.loc[idx]
                self.warnings.append({
                    'bank': row['bank'],
                    'period': row['period'],
                    'rule': '2: NIM out of range',
                    'severity': 'WARNING',
                    'detail': f"NIM={row['nim_pct']:.2f}% (expected 0.5-8%)"
                })
        
        return len(violations)
    
    def validate_rule_3_casa_range(self):
        """Rule 3: CASA between 0-100%"""
        violations = (self.df['casa_pct'] < 0) | (self.df['casa_pct'] > 100)
        
        if violations.any():
            for idx in self.df[violations].index:
                row = self.df.loc[idx]
                self.errors.append({
                    'bank': row['bank'],
                    'period': row['period'],
                    'rule': '3: Invalid CASA',
                    'severity': 'ERROR',
                    'detail': f"CASA={row['casa_pct']:.2f}% (must be 0-100%)"
                })
        
        return len(violations)
    
    def validate_rule_4_gnpa_range(self):
        """Rule 4: GNPA reasonably between 0-15%"""
        violations = self.df['gnpa_pct'] > 15
        
        if violations.any():
            for idx in self.df[violations].index:
                row = self.df.loc[idx]
                self.warnings.append({
                    'bank': row['bank'],
                    'period': row['period'],
                    'rule': '4: High GNPA',
                    'severity': 'WARNING',
                    'detail': f"GNPA={row['gnpa_pct']:.2f}% (unusually high, typically <15%)"
                })
        
        return len(violations)
    
    def validate_rule_5_missing_values(self):
        """Rule 5: No missing core metrics"""
        core_cols = ['gnpa_pct', 'nnpa_pct', 'nim_pct', 'casa_pct']
        missing = self.df[core_cols].isnull().any(axis=1)
        
        if missing.any():
            for idx in self.df[missing].index:
                row = self.df.loc[idx]
                missing_cols = [col for col in core_cols if pd.isnull(row[col])]
                self.errors.append({
                    'bank': row['bank'],
                    'period': row['period'],
                    'rule': '5: Missing values',
                    'severity': 'ERROR',
                    'detail': f"Missing: {', '.join(missing_cols)}"
                })
        
        return len(missing)
    
    def run_all_validations(self):
        """Run all validation rules"""
        print("\n" + "="*70)
        print("RUNNING DATA VALIDATION")
        print("="*70)
        
        counts = {
            'rule_1': self.validate_rule_1_gnpa_nnpa(),
            'rule_2': self.validate_rule_2_nim_range(),
            'rule_3': self.validate_rule_3_casa_range(),
            'rule_4': self.validate_rule_4_gnpa_range(),
            'rule_5': self.validate_rule_5_missing_values(),
        }
        
        return counts
    
    def print_report(self):
        """Print validation report"""
        print("\n" + "="*70)
        print("VALIDATION REPORT")
        print("="*70)
        
        total_rows = len(self.df)
        print(f"\nTotal rows: {total_rows}")
        
        # Summary
        print(f"\n📊 SUMMARY:")
        print(f"  ✅ PASSED: {total_rows - len(self.errors) - len(self.warnings)}")
        print(f"  ⚠️  WARNINGS: {len(self.warnings)}")
        print(f"  ❌ ERRORS: {len(self.errors)}")
        
        # Errors
        if self.errors:
            print(f"\n❌ ERRORS ({len(self.errors)} rows have critical issues):")
            print("-" * 70)
            for err in self.errors[:10]:  # Show first 10
                print(f"  {err['bank']:10} {err['period']:10} | {err['rule']:20} | {err['detail']}")
            if len(self.errors) > 10:
                print(f"  ... and {len(self.errors)-10} more errors")
        
        # Warnings
        if self.warnings:
            print(f"\n⚠️  WARNINGS ({len(self.warnings)} rows need review):")
            print("-" * 70)
            for warn in self.warnings[:10]:  # Show first 10
                print(f"  {warn['bank']:10} {warn['period']:10} | {warn['rule']:20} | {warn['detail']}")
            if len(self.warnings) > 10:
                print(f"  ... and {len(self.warnings)-10} more warnings")
        
        # Status
        print("\n" + "="*70)
        if len(self.errors) == 0:
            if len(self.warnings) == 0:
                print("✅ VALIDATION PASSED - All checks successful!")
            else:
                print("✅ VALIDATION PASSED - With warnings (review before use)")
        else:
            print(f"❌ VALIDATION FAILED - {len(self.errors)} critical issues to fix")
        print("="*70 + "\n")
    
    def get_valid_data(self):
        """Get only valid rows (errors only, exclude warnings)"""
        # Filter out error rows
        valid_df = self.df.copy()
        for err in self.errors:
            valid_df = valid_df[~((valid_df['bank'] == err['bank']) & 
                                   (valid_df['period'] == err['period']))]
        return valid_df


# ===== MAIN EXECUTION =====
if __name__ == "__main__":
    print("\n✅ STEP 4: DATA VALIDATION\n")
    
    # Load sample data
    try:
        df = pd.read_csv('bank_metrics_sample_final.csv')
        print(f"✅ Loaded {len(df)} rows from bank_metrics_sample_final.csv")
    except FileNotFoundError:
        print("❌ File not found: bank_metrics_sample_final.csv")
        print("   Run step3_ingest.py first")
        sys.exit(1)
    
    # Validate
    validator = DataValidator(df)
    validator.run_all_validations()
    validator.print_report()
    
    # Save valid data
    valid_df = validator.get_valid_data()
    valid_df.to_csv('bank_metrics_validated.csv', index=False)
    print(f"✅ Valid data saved to: bank_metrics_validated.csv ({len(valid_df)} rows)")
    
    # Ready for next step?
    if len(validator.errors) == 0:
        print("\n✅ READY FOR ANALYTICS!")
        print("   Run: python step5_analytics.py")
    else:
        print("\n⚠️  PLEASE FIX ERRORS BEFORE PROCEEDING")
        print("   Review and correct the issues above")
    
    print("\n" + "="*70)
    print("✅ STEP 4 COMPLETE")
    print("="*70 + "\n")
