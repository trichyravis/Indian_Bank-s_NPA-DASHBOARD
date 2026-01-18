# 📊 Data Model - Schema & Structure

Complete documentation of the data model for NPA Analysis Dashboard.

---

## 🎯 Overview

The NPA Analysis Dashboard uses a **tidy table format** with 10 columns.

**One row = One bank in one quarter**

Example:
```
bank=SBI, period=Q3-FY26, gnpa_pct=2.45, nnpa_pct=0.38, ...
```

---

## 📋 Data Schema (10 Columns)

### Column Definitions

#### 1. bank (STRING)
- **Description**: Bank identifier/code
- **Type**: String (text)
- **Examples**: SBI, HDFC, ICICI, AXIS, KOTAK
- **Required**: YES
- **Unique**: NO (appears once per quarter)

#### 2. period_type (STRING)
- **Description**: Type of period
- **Type**: String (constant)
- **Value**: 'Q' (currently only quarterly)
- **Required**: YES
- **Notes**: Future: 'M' for monthly, 'A' for annual

#### 3. period (STRING)
- **Description**: Period identifier
- **Type**: String in format Q[1-4]-FY[YY]
- **Examples**: Q3-FY26, Q2-FY26, Q1-FY25
- **Format**: Q1-Q4, FY23-FY26+
- **Required**: YES
- **Notes**: FY = Financial Year

#### 4. gnpa_pct (FLOAT)
- **Description**: Gross Non-Performing Assets percentage
- **Type**: Numeric (float/decimal)
- **Valid Range**: 0.0 - 15.0%
- **Typical Range**: 1.0 - 5.0%
- **Required**: YES
- **Validation**: GNPA ≥ NNPA (always)
- **Interpretation**: 
  - 2.45% = 2.45 out of 100 loans are non-performing
  - Lower is better

#### 5. nnpa_pct (FLOAT)
- **Description**: Net Non-Performing Assets percentage
- **Type**: Numeric (float/decimal)
- **Valid Range**: 0.0 - 3.0%
- **Typical Range**: 0.1 - 0.5%
- **Required**: YES
- **Validation**: NNPA ≤ GNPA (always)
- **Interpretation**:
  - 0.38% = After provisions, net bad loans are 0.38%
  - Lower is better

#### 6. nim_pct (FLOAT)
- **Description**: Net Interest Margin percentage
- **Type**: Numeric (float/decimal)
- **Valid Range**: 0.5 - 8.0%
- **Typical Range**: 2.5 - 4.5%
- **Required**: YES
- **Interpretation**:
  - 3.42% = Bank earns 3.42% on loans
  - Higher is better

#### 7. casa_pct (FLOAT)
- **Description**: Current Account Saving Account percentage
- **Type**: Numeric (float/decimal)
- **Valid Range**: 0 - 100%
- **Typical Range**: 30 - 50%
- **Required**: YES
- **Validation**: CASA must be 0-100% (always)
- **Interpretation**:
  - 44.2% = 44.2% of deposits are CASA
  - Higher is better (low-cost funding)

#### 8. source_url (STRING)
- **Description**: URL to source document
- **Type**: String (URL)
- **Examples**: https://nseindia.com/corporate/sbi-q3-fy26.pdf
- **Required**: YES (for audit trail)
- **Length**: Up to 500 characters

#### 9. source_doc_date (STRING)
- **Description**: Date of source document
- **Type**: String in format YYYY-MM-DD
- **Examples**: 2025-10-31, 2025-09-30
- **Required**: YES
- **Format**: ISO 8601 date format

#### 10. notes (STRING)
- **Description**: Additional notes or comments
- **Type**: String (text)
- **Examples**: "From slide 23", "Quarterly presentation"
- **Required**: NO (optional)
- **Length**: Recommended max 500 characters

---

## 📐 Data Types & Constraints

### Summary Table

| Column | Type | Min | Max | Required |
|--------|------|-----|-----|----------|
| bank | str | - | - | YES |
| period_type | str | - | - | YES |
| period | str | - | - | YES |
| gnpa_pct | float | 0 | 15 | YES |
| nnpa_pct | float | 0 | 3 | YES |
| nim_pct | float | 0.5 | 8 | YES |
| casa_pct | float | 0 | 100 | YES |
| source_url | str | - | 500 | YES |
| source_doc_date | str | - | - | YES |
| notes | str | - | 500 | NO |

---

## ✅ Validation Rules

### Rule 1: GNPA ≥ NNPA
```
Constraint: Gross NPA must always be >= Net NPA
Reason: Gross is always larger (includes provisions)
Severity: ERROR (reject row)
Example: GNPA 2.45 ≥ NNPA 0.38 ✓
```

### Rule 2: GNPA Range (0-15%)
```
Constraint: 0 ≤ GNPA ≤ 15
Reason: GNPA > 15% is extremely unusual
Severity: WARNING (log but process)
Example: GNPA 2.45 is in range ✓
```

### Rule 3: NNPA Range (0-3%)
```
Constraint: 0 ≤ NNPA ≤ 3
Reason: NNPA > 3% is very unusual
Severity: WARNING (log but process)
Example: NNPA 0.38 is in range ✓
```

### Rule 4: NIM Range (0.5-8%)
```
Constraint: 0.5 ≤ NIM ≤ 8
Reason: NIM outside this range is unusual
Severity: WARNING (log but process)
Example: NIM 3.42 is in range ✓
```

### Rule 5: CASA Range (0-100%)
```
Constraint: 0 ≤ CASA ≤ 100
Reason: Percentage can't be outside 0-100
Severity: ERROR (reject row)
Example: CASA 44.2 is in range ✓
```

### Rule 6: No Missing Core Metrics
```
Constraint: GNPA, NNPA, NIM, CASA all required
Reason: Analysis needs all 4 metrics
Severity: ERROR (reject row)
Example: All 4 present ✓
```

---

## 📊 Sample Data

### Example Row
```
bank:           SBI
period_type:    Q
period:         Q3-FY26
gnpa_pct:       2.45
nnpa_pct:       0.38
nim_pct:        3.42
casa_pct:       44.2
source_url:     https://nseindia.com/corporate/sbi-q3-fy26
source_doc_date: 2025-10-31
notes:          From Asset Quality slide 23
```

### Full Sample Dataset (5 rows)

| bank | period | gnpa_pct | nnpa_pct | nim_pct | casa_pct |
|------|--------|----------|----------|---------|----------|
| SBI | Q3-FY26 | 2.45 | 0.38 | 3.42 | 44.2 |
| HDFC | Q3-FY26 | 1.32 | 0.18 | 4.25 | 46.3 |
| ICICI | Q3-FY26 | 1.28 | 0.19 | 3.18 | 39.8 |
| AXIS | Q3-FY26 | 1.89 | 0.25 | 3.65 | 40.5 |
| KOTAK | Q3-FY26 | 1.15 | 0.18 | 3.12 | 42.1 |

---

## 🏦 Banks in Universe

### PSU Banks (5)
```
SBI    - State Bank of India
PNB    - Punjab National Bank
BOB    - Bank of Baroda
CAN    - Canara Bank
UBI    - Union Bank of India
```

### Private Banks (5)
```
HDFC   - HDFC Bank
ICICI  - ICICI Bank
AXIS   - Axis Bank
KOTAK  - Kotak Mahindra Bank
INDUSIND - IndusInd Bank
```

### Small Finance Banks (2)
```
AU     - AU Small Finance Bank
BANDHAN - Bandhan Bank
```

**Total: 12 Banks**

---

## 📅 Periods Coverage

### Quarters (12)
```
Q3-FY26  (Oct-Dec 2025)
Q2-FY26  (Jul-Sep 2025)
Q1-FY26  (Apr-Jun 2025)
Q4-FY25  (Jan-Mar 2025)
Q3-FY25  (Oct-Dec 2024)
Q2-FY25  (Jul-Sep 2024)
Q1-FY25  (Apr-Jun 2024)
Q4-FY24  (Jan-Mar 2024)
Q3-FY24  (Oct-Dec 2023)
Q2-FY24  (Jul-Sep 2023)
Q1-FY24  (Apr-Jun 2023)
Q4-FY23  (Jan-Mar 2023)
```

**Total: 12 quarters (3 years)**

---

## 📈 Data Statistics

### Dimensions
```
Banks:    12
Quarters: 12
Total rows: 144 (12 × 12)
```

### Metrics Summary
```
GNPA %  - Range: 1.15 to 2.45, Avg: 1.67
NNPA %  - Range: 0.18 to 0.38, Avg: 0.26
NIM %   - Range: 3.12 to 4.25, Avg: 3.60
CASA %  - Range: 39.8 to 46.3, Avg: 43.0
```

---

## 🔄 Data Flow

```
CSV File
   ↓
pandas.read_csv()
   ↓
DataFrame (144 rows × 10 columns)
   ↓
Validation (DataValidator)
   ↓
Analytics (3 engines)
   ↓
Streamlit Dashboard
   ↓
User Views
```

---

## 💾 File Format

### CSV Format
```csv
bank,period_type,period,gnpa_pct,nnpa_pct,nim_pct,casa_pct,source_url,source_doc_date,notes
SBI,Q,Q3-FY26,2.45,0.38,3.42,44.2,https://...,2025-10-31,From slide 23
```

### JSON Format (alternative)
```json
{
  "bank": "SBI",
  "period_type": "Q",
  "period": "Q3-FY26",
  "gnpa_pct": 2.45,
  "nnpa_pct": 0.38,
  "nim_pct": 3.42,
  "casa_pct": 44.2,
  "source_url": "https://...",
  "source_doc_date": "2025-10-31",
  "notes": "From slide 23"
}
```

---

## 🔌 SQL Schema (if using database)

```sql
CREATE TABLE bank_metrics (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    bank VARCHAR(50) NOT NULL,
    period_type CHAR(1) NOT NULL,
    period VARCHAR(10) NOT NULL,
    gnpa_pct DECIMAL(5,2) NOT NULL,
    nnpa_pct DECIMAL(5,2) NOT NULL,
    nim_pct DECIMAL(5,2) NOT NULL,
    casa_pct DECIMAL(5,2) NOT NULL,
    source_url VARCHAR(500) NOT NULL,
    source_doc_date DATE NOT NULL,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE KEY (bank, period),
    CONSTRAINT gnpa_nnpa CHECK (gnpa_pct >= nnpa_pct),
    CONSTRAINT casa_range CHECK (casa_pct >= 0 AND casa_pct <= 100)
);
```

---

## 📝 Data Loading Example

### Python
```python
import pandas as pd

# Load data
df = pd.read_csv('bank_metrics.csv')

# Display info
print(df.info())
print(df.head())

# Access column
gnpa_values = df['gnpa_pct']

# Filter
sbi_data = df[df['bank'] == 'SBI']
```

### Create Empty DataFrame
```python
from src.data_model import create_empty_dataframe

df = create_empty_dataframe()
print(df)  # Empty DataFrame with correct schema
```

### Load Sample Data
```python
from src.data_model import create_sample_data

df = create_sample_data()
print(df)  # 5-row sample data
```

---

## 🔄 Data Updates

### Adding New Quarter
1. Collect data for new quarter
2. Add 12 rows (one per bank)
3. Validate using DataValidator
4. Append to CSV
5. Dashboard auto-updates

### Adding New Bank
1. Update `src/bank_list.py`
2. Add to BANK_UNIVERSE dict
3. Update collection checklist
4. Collect 12 quarters of data
5. Add to CSV

---

## ✅ Data Quality Checklist

- [ ] All 144 rows present (12 banks × 12 quarters)
- [ ] No missing values in required columns
- [ ] GNPA ≥ NNPA for all rows
- [ ] GNPA in 0-15% range
- [ ] NNPA in 0-3% range
- [ ] NIM in 0.5-8% range
- [ ] CASA in 0-100% range
- [ ] Source URLs valid
- [ ] Dates in YYYY-MM-DD format
- [ ] No duplicate entries

---

## 📚 Related Documentation

- [USAGE.md](USAGE.md) - How to use the data
- [API.md](API.md) - API for data operations
- [FAQ.md](FAQ.md) - Common questions

---

**Data model documentation complete!** ✅

Last Updated: January 18, 2026
