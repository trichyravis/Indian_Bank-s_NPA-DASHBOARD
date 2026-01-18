# 🏗️ Architecture - System Design

Complete overview of the NPA Analysis Dashboard architecture.

---

## 🎯 System Overview

```
┌─────────────────────────────────────────────────────┐
│         NPA ANALYSIS DASHBOARD - ARCHITECTURE       │
└─────────────────────────────────────────────────────┘

Data Layer
├── CSV Files (raw data)
└── Validation Rules

Processing Layer
├── Data Model (schema)
├── Validation Engine
├── Analytics Engines
│   ├── Asset Quality Analytics
│   ├── Profitability Analytics
│   └── Peer Comparison Analytics
└── Bank Universe Management

Presentation Layer
└── Streamlit Dashboard (4 pages)
    ├── Page 1: Overview
    ├── Page 2: Bank Deep Dive
    ├── Page 3: Peer Comparison
    └── Page 4: Data & Sources

User Layer
└── Web Browser (any device)
```

---

## 📦 Module Structure

### src/ Directory (6 modules)

```
src/
├── __init__.py              (Package initialization)
├── data_model.py            (Data schema - STEP 1)
├── bank_list.py             (Bank universe - STEP 2)
├── ingest.py                (Data collection - STEP 3)
├── validate.py              (Validation - STEP 4)
├── analytics.py             (Analytics - STEP 5)
└── app.py                   (Dashboard - STEP 6)
```

---

## 🔄 Data Flow

### 1. Data Collection Flow

```
NSE Presentations (PDFs)
        ↓
    Manual Extraction
        ↓
Collection Template (CSV/Excel)
        ↓
    CSV File Saved
        ↓
bank_metrics.csv
```

### 2. Processing Flow

```
bank_metrics.csv
        ↓
    Load with Pandas
        ↓
    data_model.py (schema validation)
        ↓
    validate.py (5 quality rules)
        ↓
    bank_metrics_validated.csv
        ↓
    analytics.py (3 engines)
        ↓
Analytics Output
├── rankings.csv
├── quadrants.csv
└── spreads.csv
```

### 3. Presentation Flow

```
Validated Data
        ↓
    app.py (Streamlit)
        ↓
    4 Pages Rendered
├── Overview (KPIs + Trends)
├── Deep Dive (Selected Bank)
├── Peer Compare (Rankings)
└── Data & Sources (Raw)
        ↓
    Web Browser
        ↓
    User Views Dashboard
```

---

## 🏛️ Layer Architecture

### Layer 1: Data Layer
**Purpose**: Store and manage data  
**Components**:
- CSV files (raw data)
- Bank directory
- Collection checklist

**Responsibilities**:
- Data persistence
- Data organization
- Audit trail

### Layer 2: Validation Layer
**Purpose**: Ensure data quality  
**Components**:
- DataValidator class (5 rules)
- Error/warning classification
- Data quality reports

**Responsibilities**:
- Validate against 5 rules
- Reject/flag errors
- Generate quality metrics

### Layer 3: Analytics Layer
**Purpose**: Extract insights from data  
**Components**:
- AssetQualityAnalytics
- ProfitabilityAnalytics
- PeerComparisonAnalytics

**Responsibilities**:
- Calculate metrics
- Produce rankings
- Generate quadrants
- Compute trends

### Layer 4: Presentation Layer
**Purpose**: Display data to users  
**Components**:
- Streamlit app.py
- 4 interactive pages
- Charts and tables

**Responsibilities**:
- Render UI
- Handle user interactions
- Display visualizations
- Enable downloads

### Layer 5: User Layer
**Purpose**: Interact with system  
**Components**:
- Web browser
- User input (dropdown, buttons)
- Display output

**Responsibilities**:
- View data
- Make selections
- Download reports

---

## 📊 Class Diagram

```
DATA LAYER
├── DataFrame (pandas)
│   └── 10 columns × 144 rows
└── Bank Universe
    └── 12 banks × 12 quarters

VALIDATION LAYER
└── DataValidator
    ├── validate_rule_1_gnpa_nnpa()
    ├── validate_rule_2_gnpa_range()
    ├── validate_rule_3_nnpa_range()
    ├── validate_rule_4_nim_range()
    ├── validate_rule_5_casa_range()
    ├── validate_rule_6_missing_values()
    └── run_all_validations()

ANALYTICS LAYER
├── AssetQualityAnalytics
│   ├── latest_metrics()
│   ├── gnpa_trend()
│   └── spread_analysis()
├── ProfitabilityAnalytics
│   ├── nim_trends()
│   ├── casa_trends()
│   └── profitability_vs_risk()
└── PeerComparisonAnalytics
    ├── latest_rankings()
    └── quadrant_view()

PRESENTATION LAYER
└── Streamlit App
    ├── page_overview()
    ├── page_bank_deep_dive()
    ├── page_peer_comparison()
    └── page_data_sources()
```

---

## 🔌 Component Interactions

### Data → Validation → Analytics → Presentation

```
Step 1: Load Data
  df = load_csv('bank_metrics.csv')
  Result: 144 rows × 10 columns

Step 2: Validate Data
  validator = DataValidator(df)
  validator.run_all_validations()
  Result: Valid rows (errors rejected)

Step 3: Run Analytics
  aq = AssetQualityAnalytics(df)
  rankings = aq.latest_metrics()
  Result: Processed metrics

Step 4: Display in Dashboard
  streamlit.run(app.py)
  Result: Interactive web app
```

---

## 🎯 Design Patterns

### 1. Model-View-Controller (MVC)

```
Model (Data Layer)
├── data_model.py (schema)
├── bank_list.py (universe)
└── validate.py (validation)

View (Presentation Layer)
└── app.py (Streamlit pages)

Controller (Analytics Layer)
├── ingest.py (data collection)
├── validate.py (processing)
└── analytics.py (calculations)
```

### 2. Single Responsibility Principle

```
data_model.py    → Defines data structure only
bank_list.py     → Manages bank universe only
ingest.py        → Handles data collection only
validate.py      → Performs validation only
analytics.py     → Calculates analytics only
app.py           → Displays dashboard only
```

### 3. Separation of Concerns

```
Data (what)      → data_model.py
Rules (how)      → validate.py
Insights (why)   → analytics.py
Presentation     → app.py
```

---

## 📈 Scalability Considerations

### Current Scale
- Banks: 12
- Quarters: 12
- Total rows: 144

### Scaling Options

#### Option 1: More Banks
```
Current: 12 banks
Scalable to: 35+ banks (all NSE-listed)
Impact: 12 × 35 = 420 rows
```

#### Option 2: More Quarters
```
Current: 12 quarters (3 years)
Scalable to: 40+ quarters (10 years)
Impact: 12 × 40 = 480 rows
```

#### Option 3: More Metrics
```
Current: 4 metrics (GNPA, NNPA, NIM, CASA)
Add: ROA, ROE, CAR, CRR, etc.
Impact: Expand columns
```

---

## 🔐 Security Considerations

### Data Security
- ✅ CSV files (plain text) - OK for public data
- ✅ Source URLs - Public NSE filings
- ✅ No sensitive/confidential data
- ⚠️ For production: Use database + encryption

### Access Control
- ✅ Public dashboard (read-only)
- ✅ No authentication needed
- ⚠️ For production: Add user authentication

### Data Validation
- ✅ 5 validation rules enforce data quality
- ✅ Invalid rows rejected
- ✅ Error logging for audit trail

---

## ⚡ Performance Optimization

### Current Performance
- Dashboard load: < 2 seconds
- Page navigation: < 1 second
- Chart rendering: < 1 second

### Caching Strategy
```python
@st.cache_data
def load_data():
    return pd.read_csv('bank_metrics.csv')
```

### Optimization Techniques
1. **Data caching** - Load data once, reuse
2. **Lazy loading** - Load only when needed
3. **Chart optimization** - Use Plotly for efficiency
4. **Minimal data** - Only 144 rows (fast processing)

---

## 🔄 Extensibility

### Easy to Add

#### New Bank
```python
# Step 1: Edit src/bank_list.py
BANK_UNIVERSE['PSU_BANKS']['NEWBANK'] = {...}

# Step 2: Collect data
# New rows added to CSV

# Step 3: Dashboard auto-updates
```

#### New Metric
```python
# Step 1: Edit src/data_model.py
# Add column to schema

# Step 2: Edit src/validate.py
# Add validation rule

# Step 3: Edit src/analytics.py
# Add calculation

# Step 4: Edit src/app.py
# Add chart
```

#### New Page
```python
# Step 1: Create function in src/app.py
def page_new_feature():
    st.write("New content")

# Step 2: Add to sidebar navigation
```

---

## 📚 Technology Stack

### Backend
- **Python 3.7+** - Programming language
- **Pandas** - Data manipulation
- **NumPy** - Numerical computing
- **Pytest** - Testing framework

### Frontend
- **Streamlit** - Web framework
- **Plotly** - Interactive charts
- **HTML/CSS** - (handled by Streamlit)

### Data Storage
- **CSV files** - Data persistence
- **Optional**: SQLite, PostgreSQL, MySQL

### Deployment
- **Streamlit Cloud** - Free hosting
- **AWS/GCP/Azure** - Enterprise hosting
- **Docker** - Containerization

---

## 🧪 Testing Architecture

### Unit Tests
```
tests/
├── test_data_model.py
├── test_validation.py
├── test_analytics.py
└── test_app.py
```

### Test Coverage
- Data loading: ✅
- Validation rules: ✅
- Analytics calculations: ✅
- Dashboard rendering: ✅

### Running Tests
```bash
pytest tests/ -v
```

---

## 🚀 Deployment Architecture

### Development
```
Local Machine
├── Python environment
├── Source code
├── CSV data files
└── Streamlit dashboard (localhost:8501)
```

### Production
```
Streamlit Cloud / Cloud Provider
├── GitHub repository
├── Docker container (optional)
├── Environment variables
├── Data files (cloud storage)
└── HTTPS endpoint
```

---

## 📊 Data Persistence

### Current Approach
```
CSV Files
├── bank_metrics.csv (main data)
├── bank_directory.csv (bank metadata)
└── collection_checklist.csv (template)
```

### Alternative: Database
```
Database
├── Tables
│   ├── bank_metrics
│   ├── banks
│   └── periods
└── Indexes (for performance)
```

---

## 🔗 Integration Points

### Data Sources
- NSE presentations (PDF)
- Manual extraction
- CSV input

### Output Channels
- Web dashboard
- CSV export
- API endpoints (future)

---

## 📋 Architecture Decisions

| Decision | Rationale |
|----------|-----------|
| Pandas | Easy data manipulation |
| Streamlit | Fast prototyping |
| CSV storage | Simple, auditable |
| Tidy tables | Standard format |
| 5 validation rules | Comprehensive QA |
| 3 analytics engines | Diverse insights |
| 4 dashboard pages | Complete view |

---

## 🎯 Design Goals

1. **Simplicity** - Easy to understand
2. **Modularity** - Independent components
3. **Scalability** - Grows with data
4. **Maintainability** - Easy to modify
5. **Testability** - Easy to verify
6. **Usability** - Simple interface
7. **Performance** - Fast response times

---

## 📚 Related Documentation

- [DATA_MODEL.md](DATA_MODEL.md) - Data structure
- [API.md](API.md) - API reference
- [USAGE.md](USAGE.md) - Usage guide

---

**Architecture documentation complete!** ✅

Last Updated: January 18, 2026
