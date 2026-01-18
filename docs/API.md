# 🔌 API Reference

Complete API documentation for all modules and functions.

---

## 📚 Module Index

- [data_model](#data_model-module)
- [bank_list](#bank_list-module)
- [ingest](#ingest-module)
- [validate](#validate-module)
- [analytics](#analytics-module)

---

## data_model Module

### Functions

#### `create_empty_dataframe()`
Creates empty DataFrame with correct schema.

```python
from src.data_model import create_empty_dataframe

df = create_empty_dataframe()
# Returns: Empty DataFrame with 10 columns
```

**Returns:**
- `pd.DataFrame`: Empty DataFrame

---

#### `create_sample_data()`
Generate sample data for 5 banks in Q3 FY26.

```python
from src.data_model import create_sample_data

df = create_sample_data()
# Returns: DataFrame with 5 rows (SBI, HDFC, ICICI, AXIS, KOTAK)
```

**Returns:**
- `pd.DataFrame`: 5-row sample data

---

#### `print_schema()`
Print data schema with validation ranges.

```python
from src.data_model import print_schema

print_schema()
# Prints: Complete schema information
```

---

#### `save_csv(df, filename)`
Save DataFrame to CSV file.

```python
from src.data_model import save_csv

result = save_csv(df, 'data/bank_metrics.csv')
print(result)
# Output: "✅ Data saved to data/bank_metrics.csv (144 rows)"
```

**Parameters:**
- `df` (pd.DataFrame): DataFrame to save
- `filename` (str): Output filename

**Returns:**
- `str`: Success/error message

---

#### `load_csv(filename)`
Load CSV file into DataFrame.

```python
from src.data_model import load_csv

df = load_csv('data/bank_metrics.csv')
# Returns: Loaded DataFrame
```

**Parameters:**
- `filename` (str): Input filename

**Returns:**
- `pd.DataFrame`: Loaded data
- `None`: If file not found

---

## bank_list Module

### Functions

#### `get_bank_directory()`
Get DataFrame with all banks and metadata.

```python
from src.bank_list import get_bank_directory

df = get_bank_directory()
# Returns: DataFrame with 12 rows (one per bank)
```

**Returns:**
- `pd.DataFrame`: Bank metadata (12 rows)

**Columns:**
- bank_code, bank_name, nse_ticker, category, data_years, established, website

---

#### `get_quarters()`
Get list of 12 quarters (Q3 FY26 to Q4 FY23).

```python
from src.bank_list import get_quarters

quarters = get_quarters()
# Returns: ['Q3-FY26', 'Q2-FY26', ..., 'Q4-FY23']
```

**Returns:**
- `list`: 12 quarter identifiers

---

#### `create_collection_checklist()`
Create 144-row collection template (12 banks × 12 quarters).

```python
from src.bank_list import create_collection_checklist

df = create_collection_checklist()
# Returns: DataFrame with 144 rows
```

**Returns:**
- `pd.DataFrame`: Collection checklist template

---

## ingest Module

### Functions

#### `create_collection_template_excel()`
Create Excel template for manual data entry.

```python
from src.ingest import create_collection_template_excel

df = create_collection_template_excel()
# Returns: DataFrame with 3 example rows
```

**Returns:**
- `pd.DataFrame`: Template with examples

---

#### `load_partially_filled_data(filename)`
Load CSV or Excel file.

```python
from src.ingest import load_partially_filled_data

df = load_partially_filled_data('template.xlsx')
# Returns: Loaded DataFrame
```

**Parameters:**
- `filename` (str): CSV or Excel file

**Returns:**
- `pd.DataFrame`: Loaded data

---

#### `validate_filled_data(df)`
Basic validation of filled data.

```python
from src.ingest import validate_filled_data

results = validate_filled_data(df)
# Returns: {'total_rows': 144, 'missing_values': 0, 'errors': []}
```

**Parameters:**
- `df` (pd.DataFrame): Data to validate

**Returns:**
- `dict`: Validation results

---

## validate Module

### Class: DataValidator

#### Constructor
```python
from src.validate import DataValidator

validator = DataValidator(df)
# Creates validator instance
```

**Parameters:**
- `df` (pd.DataFrame): Data to validate

---

#### `run_all_validations()`
Run all 6 validation rules.

```python
validator.run_all_validations()
# Validates: GNPA≥NNPA, ranges, missing values
```

---

#### `get_valid_data()`
Get rows that passed all validations.

```python
df_valid = validator.get_valid_data()
# Returns: Valid rows only
```

**Returns:**
- `pd.DataFrame`: Valid rows

---

#### `print_report()`
Print validation report with errors/warnings.

```python
validator.print_report()
# Prints: Detailed validation report
```

---

### Validation Rules

```python
validator.validate_rule_1_gnpa_nnpa()  # GNPA ≥ NNPA
validator.validate_rule_2_gnpa_range() # GNPA 0-15%
validator.validate_rule_3_nnpa_range() # NNPA 0-3%
validator.validate_rule_4_nim_range()  # NIM 0.5-8%
validator.validate_rule_5_casa_range() # CASA 0-100%
validator.validate_rule_6_missing_values() # No nulls
```

---

## analytics Module

### Class: AssetQualityAnalytics

#### Constructor
```python
from src.analytics import AssetQualityAnalytics

aq = AssetQualityAnalytics(df)
```

#### Methods

##### `latest_metrics()`
Get latest GNPA, NNPA for each bank.

```python
df = aq.latest_metrics()
# Returns: DataFrame with latest values
```

**Returns:**
- `pd.DataFrame`: Latest metrics

---

##### `gnpa_trend(bank_code)`
Get 12-quarter GNPA trend for a bank.

```python
trend = aq.gnpa_trend('SBI')
# Returns: {'bank': 'SBI', 'latest': 2.45, 'min': ..., 'max': ..., 'avg': ...}
```

**Parameters:**
- `bank_code` (str): Bank identifier

**Returns:**
- `dict`: Trend statistics

---

##### `spread_analysis()`
Analyze GNPA-NNPA spread in basis points.

```python
df = aq.spread_analysis()
# Returns: DataFrame with spread_bps column
```

**Returns:**
- `pd.DataFrame`: Spread analysis

---

### Class: ProfitabilityAnalytics

#### Constructor
```python
from src.analytics import ProfitabilityAnalytics

prof = ProfitabilityAnalytics(df)
```

#### Methods

##### `nim_trends()`
Get latest NIM for each bank, ranked.

```python
df = prof.nim_trends()
# Returns: Ranked by NIM (highest first)
```

---

##### `casa_trends()`
Get latest CASA for each bank, ranked.

```python
df = prof.casa_trends()
# Returns: Ranked by CASA (highest first)
```

---

### Class: PeerComparisonAnalytics

#### Constructor
```python
from src.analytics import PeerComparisonAnalytics

pc = PeerComparisonAnalytics(df)
```

#### Methods

##### `latest_rankings()`
Get latest GNPA rankings (lowest = best).

```python
df = pc.latest_rankings()
# Returns: Ranked by GNPA (lowest first)
```

---

##### `quadrant_view()`
Classify banks into 4 quadrants (CASA vs GNPA).

```python
df = pc.quadrant_view()
# Returns: DataFrame with quadrant column (BEST/CAUTION/WATCH/WORST)
```

**Quadrants:**
- BEST: High CASA, Low GNPA
- CAUTION: High CASA, High GNPA
- WATCH: Low CASA, Low GNPA
- WORST: Low CASA, High GNPA

---

## 📝 Usage Examples

### Example 1: Load and Validate Data
```python
from src.data_model import load_csv
from src.validate import DataValidator

# Load data
df = load_csv('bank_metrics.csv')

# Validate
validator = DataValidator(df)
validator.run_all_validations()
validator.print_report()

# Get valid data
df_valid = validator.get_valid_data()
```

### Example 2: Run Analytics
```python
from src.analytics import AssetQualityAnalytics, PeerComparisonAnalytics

# Asset Quality
aq = AssetQualityAnalytics(df)
print(aq.latest_metrics())
print(aq.spread_analysis())

# Peer Comparison
pc = PeerComparisonAnalytics(df)
print(pc.latest_rankings())
print(pc.quadrant_view())
```

### Example 3: Create Sample Data
```python
from src.data_model import create_sample_data
from src.validate import DataValidator

df = create_sample_data()
validator = DataValidator(df)
validator.run_all_validations()
print(f"Valid rows: {len(validator.get_valid_data())}")
```

---

## 🔍 Return Value Formats

### DataFrame Returns
```python
df.head()
#    bank period  gnpa_pct  nnpa_pct  ...
# 0   SBI Q3-FY26     2.45      0.38  ...
# 1  HDFC Q3-FY26     1.32      0.18  ...
```

### Dictionary Returns
```python
{'bank': 'SBI', 'latest': 2.45, 'min': 1.89, 'max': 2.95, 'avg': 2.32}
```

### List Returns
```python
['Q3-FY26', 'Q2-FY26', 'Q1-FY26', ..., 'Q4-FY23']
```

---

## ⚠️ Error Handling

### Try-Catch Example
```python
from src.data_model import load_csv

try:
    df = load_csv('nonexistent.csv')
except FileNotFoundError:
    print("File not found")
```

---

## 📚 Related Documentation

- [DATA_MODEL.md](DATA_MODEL.md) - Data structure
- [USAGE.md](USAGE.md) - How to use
- [ARCHITECTURE.md](ARCHITECTURE.md) - System design

---

**API Reference Complete!** ✅

Last Updated: January 18, 2026
