# 📚 NPA Analysis Dashboard - Documentation

Welcome to the complete documentation for the NPA Analysis Dashboard project.

## 📖 Documentation Index

### Quick Start
- **[QUICK_START.md](QUICK_START.md)** - Get started in 5 minutes
- **[INSTALLATION.md](INSTALLATION.md)** - Detailed installation guide

### User Guide
- **[USAGE.md](USAGE.md)** - How to use the dashboard
- **[FAQ.md](FAQ.md)** - Frequently asked questions

### Technical Documentation
- **[DATA_MODEL.md](DATA_MODEL.md)** - Data schema and structure
- **[ARCHITECTURE.md](ARCHITECTURE.md)** - System architecture overview
- **[API.md](API.md)** - API reference for all modules

### Additional Resources
- **[CONTRIBUTING.md](CONTRIBUTING.md)** - How to contribute

---

## 🎯 Quick Navigation

### For Users
1. Start with [QUICK_START.md](QUICK_START.md)
2. Read [USAGE.md](USAGE.md) for features
3. Check [FAQ.md](FAQ.md) for common questions

### For Developers
1. Read [INSTALLATION.md](INSTALLATION.md)
2. Review [DATA_MODEL.md](DATA_MODEL.md)
3. Study [ARCHITECTURE.md](ARCHITECTURE.md)
4. Check [API.md](API.md) for code reference
5. See [CONTRIBUTING.md](CONTRIBUTING.md) to contribute

---

## 📊 Project Overview

**NPA Analysis Dashboard** is an interactive web application for analyzing Non-Performing Assets (NPA) across Indian banks.

### Key Features
- 📈 Real-time NPA metrics tracking
- 🏦 12-bank peer comparison
- 📊 3-year historical analysis
- 🎯 Asset quality analytics
- 💰 Profitability metrics
- 📍 Quadrant analysis
- ✅ Data validation (5 rules)
- 📤 CSV export with audit trail

### Technology Stack
- **Frontend**: Streamlit
- **Data**: Pandas, NumPy
- **Visualization**: Plotly
- **Language**: Python 3.7+

---

## 🚀 Getting Started

### Fastest Way (5 minutes)

```bash
# 1. Clone repository
git clone https://github.com/username/npa-analysis-dashboard.git
cd npa-analysis-dashboard

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run dashboard
streamlit run src/app.py
```

Opens at: `http://localhost:8501`

### Detailed Instructions
See [INSTALLATION.md](INSTALLATION.md) for step-by-step guide.

---

## 📋 Project Structure

```
npa-analysis-dashboard/
├── src/                    # Source code
│   ├── __init__.py
│   ├── data_model.py      # Data schema
│   ├── bank_list.py       # Bank universe
│   ├── ingest.py          # Data ingestion
│   ├── validate.py        # Validation rules
│   ├── analytics.py       # Analytics engines
│   └── app.py             # Streamlit dashboard
│
├── data/                  # Data files
│   ├── raw/
│   ├── processed/
│   └── sample/
│
├── docs/                  # Documentation
│   ├── README.md
│   ├── QUICK_START.md
│   ├── INSTALLATION.md
│   ├── USAGE.md
│   ├── DATA_MODEL.md
│   ├── ARCHITECTURE.md
│   ├── API.md
│   └── FAQ.md
│
├── tests/                 # Unit tests
├── README.md
├── requirements.txt
├── LICENSE
└── .gitignore
```

---

## 💡 Key Concepts

### NPA (Non-Performing Asset)
An asset (loan) that is not generating income for the bank because the borrower is not making payments.

### GNPA (Gross NPA)
Gross Non-Performing Assets as a percentage of total advances.

### NNPA (Net NPA)
Net Non-Performing Assets after provisions.

### NIM (Net Interest Margin)
The difference between interest earned and interest paid, expressed as a percentage.

### CASA (Current Account Saving Account)
Low-cost deposits from current and savings account holders.

---

## 🎓 Learning Path

### Beginner
1. Read [QUICK_START.md](QUICK_START.md)
2. Install and run the dashboard
3. Explore the 4 dashboard pages
4. Read [USAGE.md](USAGE.md)

### Intermediate
1. Study [DATA_MODEL.md](DATA_MODEL.md)
2. Review [ARCHITECTURE.md](ARCHITECTURE.md)
3. Check [API.md](API.md)
4. Try modifying the dashboard

### Advanced
1. Study all source code
2. Read [CONTRIBUTING.md](CONTRIBUTING.md)
3. Set up development environment
4. Make contributions

---

## 📞 Support & Help

### Finding Help
1. Check [FAQ.md](FAQ.md) first
2. Review [USAGE.md](USAGE.md) for features
3. Check GitHub Issues
4. Contact maintainers

### Reporting Issues
1. Check if issue already exists
2. Provide clear description
3. Include error messages
4. Share reproducible steps

---

## 📄 Documentation Standards

All documentation follows these standards:
- Clear and concise language
- Code examples where applicable
- Links to related documents
- Regular updates
- Professional tone

---

## 🔗 External Resources

### Data Sources
- **NSE Corporate Filings**: https://www.nseindia.com/corporate/financialresults
- **RBI Publications**: https://www.rbi.org.in

### Learning Resources
- **Pandas Documentation**: https://pandas.pydata.org
- **Streamlit Documentation**: https://docs.streamlit.io
- **Plotly Documentation**: https://plotly.com/python

---

## 📝 License

This project is licensed under the MIT License - see [LICENSE](../LICENSE) for details.

---

## 👤 Author

**Prof. V. Ravichandran**
- 28+ Years Corporate Finance & Banking Experience
- 10+ Years Academic Excellence
- The Mountain Path - World of Finance

---

## 📅 Version History

See [CHANGELOG.md](../CHANGELOG.md) for version history and updates.

---

**Last Updated:** January 18, 2026  
**Status:** Active Maintenance  
**Version:** 1.0.0
