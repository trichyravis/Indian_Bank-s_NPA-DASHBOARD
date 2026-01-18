# ❓ Frequently Asked Questions (FAQ)

Common questions and answers about the NPA Analysis Dashboard.

---

## 🚀 Getting Started

### Q1: How do I get started?
**A:** Follow these steps:
1. Install Python 3.7+
2. Clone repository
3. Install requirements: `pip install -r requirements.txt`
4. Run: `streamlit run src/app.py`
5. Open browser at http://localhost:8501

See [QUICK_START.md](QUICK_START.md) for details.

---

### Q2: Do I need to install anything else?
**A:** No, just Python and pip. All dependencies are in requirements.txt:
- streamlit (web framework)
- pandas (data analysis)
- plotly (charts)
- numpy (math)

---

### Q3: Can I use it on Windows/Mac/Linux?
**A:** Yes! It works on all operating systems that have Python 3.7+.

---

## 📊 Using the Dashboard

### Q4: What do the 4 pages do?
**A:**
- **📈 Overview** - System KPIs and trends
- **🏦 Bank Deep Dive** - Individual bank analysis
- **🏆 Peer Comparison** - Rankings and quadrants
- **📚 Data & Sources** - Raw data and attribution

---

### Q5: What do GNPA, NNPA, NIM, CASA mean?
**A:**
- **GNPA** - Gross Non-Performing Assets (bad loans %)
- **NNPA** - Net Non-Performing Assets (after provisions %)
- **NIM** - Net Interest Margin (profitability %)
- **CASA** - Current Account Saving Account (low-cost funding %)

See [DATA_MODEL.md](DATA_MODEL.md) for details.

---

### Q6: What is "better" - higher or lower values?
**A:**
- GNPA: **Lower is better** (fewer bad loans)
- NNPA: **Lower is better** (fewer bad loans after provisions)
- NIM: **Higher is better** (more profitable)
- CASA: **Higher is better** (cheaper funding)

---

### Q7: How do I download the data?
**A:**
1. Go to Page 4 (Data & Sources)
2. Click "Download CSV" button
3. File downloads as CSV
4. Open in Excel or Python

---

### Q8: How do I see where the data comes from?
**A:**
1. Go to Page 4 (Data & Sources)
2. Click expand button on each row
3. See source URL and document date
4. Click URL to see original NSE filing

---

## 📈 Data & Analysis

### Q9: Which banks are included?
**A:** 12 banks:
- **PSU**: SBI, PNB, BOB, CAN, UBI
- **Private**: HDFC, ICICI, AXIS, KOTAK, INDUSIND
- **SFB**: AU, BANDHAN

See [DATA_MODEL.md](DATA_MODEL.md) for details.

---

### Q10: How many quarters of data?
**A:** 12 quarters (3 years):
- Q3-FY26 (Oct-Dec 2025) to Q4-FY23 (Jan-Mar 2023)

---

### Q11: What does "quadrant" mean?
**A:** Banks are classified into 4 groups:
- **BEST** (top-left): High CASA, Low GNPA - Ideal
- **CAUTION** (top-right): High CASA, High GNPA - Risky
- **WATCH** (bottom-left): Low CASA, Low GNPA - Monitor
- **WORST** (bottom-right): Low CASA, High GNPA - Avoid

---

### Q12: Can I add more data?
**A:** Yes!
1. Create/update CSV file with same schema
2. Add 10 columns (bank, period, gnpa_pct, etc.)
3. Save as bank_metrics.csv
4. Restart dashboard
5. New data appears automatically

---

### Q13: Can I add more banks?
**A:** Yes!
1. Edit `src/bank_list.py`
2. Add bank to BANK_UNIVERSE dict
3. Collect data for all quarters
4. Add rows to CSV
5. Dashboard auto-scales

---

## 🛠️ Technical Questions

### Q14: What's the tech stack?
**A:**
- **Language**: Python 3.7+
- **Framework**: Streamlit (web)
- **Data**: Pandas, NumPy
- **Charts**: Plotly
- **Testing**: Pytest

---

### Q15: Is the code open source?
**A:** Yes! MIT License. You can:
- ✅ Use commercially
- ✅ Modify code
- ✅ Distribute copies
- ✅ Private use
- ❌ Hold liable

---

### Q16: How do I modify the code?
**A:** Edit files in `src/`:
- `data_model.py` - Data schema
- `bank_list.py` - Banks
- `validate.py` - Validation rules
- `analytics.py` - Calculations
- `app.py` - Dashboard

Then restart: `streamlit run src/app.py`

---

### Q17: Can I run tests?
**A:** Yes!
```bash
pytest tests/ -v
```

---

## 🌐 Deployment

### Q18: Can I deploy online?
**A:** Yes! 3 easy options:

**Option 1: Streamlit Cloud (FREE)**
1. Push to GitHub
2. Go to https://share.streamlit.io
3. Connect your repo
4. Set main file: src/app.py
5. Deploy (1 click)

**Option 2: Your Server**
1. Install Python
2. Clone repo
3. Install requirements
4. Run: `streamlit run src/app.py`
5. Keep running with supervisor/screen

**Option 3: Docker**
1. Create Dockerfile
2. Build image: `docker build -t app .`
3. Run: `docker run -p 8501:8501 app`

---

### Q19: What's the cost?
**A:**
- Streamlit Cloud: FREE
- Your server: Cost of server (AWS, GCP, etc.)
- Self-hosted: Free (your computer)

---

### Q20: Can I make it private?
**A:** Yes! Streamlit Cloud has authentication options.

---

## 🔧 Troubleshooting

### Q21: Dashboard won't load
**A:**
1. Check if Python is running: `python --version`
2. Check if Streamlit installed: `pip list | grep streamlit`
3. Restart: `Ctrl+C` then run again
4. Clear browser cache
5. Try different browser

---

### Q22: Charts not showing
**A:**
1. Check if Plotly installed: `pip install plotly --upgrade`
2. Refresh page: F5
3. Clear cache: `Ctrl+Shift+Delete`
4. Restart Streamlit

---

### Q23: "Module not found" error
**A:**
```bash
pip install -r requirements.txt --upgrade
```

---

### Q24: Port 8501 already in use
**A:**
```bash
streamlit run src/app.py --server.port 8502
```

---

### Q25: Slow performance
**A:**
1. Close other applications
2. Clear browser cache
3. Use Chrome (fastest)
4. Increase RAM allocation

---

## 📚 Learning

### Q26: How do I learn more about NPA?
**A:** Resources:
- [DATA_MODEL.md](DATA_MODEL.md) - Metrics explained
- [USAGE.md](USAGE.md) - Dashboard guide
- [ARCHITECTURE.md](ARCHITECTURE.md) - System design
- [API.md](API.md) - Code reference
- RBI website: https://www.rbi.org.in
- NSE website: https://www.nseindia.com

---

### Q27: How do I learn Python?
**A:** Resources:
- Official: https://www.python.org/learn
- Interactive: https://www.codecademy.com
- Tutorial: https://www.w3schools.com/python

---

### Q28: Can I modify the dashboard?
**A:** Yes! Edit `src/app.py`:
- Add new pages
- Modify charts
- Add filters
- Change colors

---

## 🤝 Contributing

### Q29: Can I contribute?
**A:** Yes! See [../CONTRIBUTING.md](../CONTRIBUTING.md)
1. Fork repository
2. Create feature branch
3. Make changes
4. Submit pull request

---

### Q30: How do I report bugs?
**A:**
1. Check existing issues
2. Create new issue on GitHub
3. Provide:
   - Error message
   - Steps to reproduce
   - Expected behavior
   - Actual behavior

---

## 💡 Advanced Questions

### Q31: Can I use a database instead of CSV?
**A:** Yes! Modify `src/data_model.py`:
```python
import sqlite3
# Load from SQLite instead of CSV
```

---

### Q32: Can I add real-time updates?
**A:** Yes! Modify `src/app.py`:
```python
import time
while True:
    # Update data
    time.sleep(3600)  # Every hour
```

---

### Q33: Can I add user authentication?
**A:** Yes! Streamlit has auth options:
```bash
streamlit deploy --with-auth
```

---

### Q34: Can I export to PDF?
**A:** Yes! Install extra dependency:
```bash
pip install streamlit-report-tool
```

---

### Q35: Can I add to my portfolio?
**A:** Yes! Perfect for:
- Data science portfolio
- Finance project
- Python showcase
- GitHub portfolio

---

## 🎓 Career Questions

### Q36: Is this useful for job interviews?
**A:** Yes! Shows:
- Python skills
- Data analysis
- Financial knowledge
- Full-stack development
- Project completion

---

### Q37: Can I use this in a job application?
**A:** Yes! It demonstrates:
- Real project
- Complete implementation
- Professional code
- Technical depth
- Communication skills

---

### Q38: Is this taught in schools?
**A:** Similar concepts taught in:
- Finance courses (NPA analysis)
- Python courses (Pandas, Streamlit)
- Data science courses
- Business intelligence courses

---

## 📞 Support

### Q39: Where can I get help?
**A:** Resources:
1. This FAQ
2. [QUICK_START.md](QUICK_START.md)
3. [USAGE.md](USAGE.md)
4. GitHub Issues
5. Contact maintainers

---

### Q40: How do I contact the author?
**A:** See [../README.md](../README.md) for contact information.

---

## 📝 General

### Q41: What's the license?
**A:** MIT License (open source, free to use)

---

### Q42: Can I use commercially?
**A:** Yes! MIT license allows commercial use.

---

### Q43: Is there support?
**A:** Community support via:
- GitHub Issues
- Documentation
- FAQ (this file)

---

### Q44: Is there a roadmap?
**A:** See [../CHANGELOG.md](../CHANGELOG.md) for planned features.

---

### Q45: Can I see the source code?
**A:** Yes! All code is public on GitHub.

---

## ✅ Quick Checklist

Before asking for help, try:
- [ ] Read [QUICK_START.md](QUICK_START.md)
- [ ] Read [USAGE.md](USAGE.md)
- [ ] Search this FAQ
- [ ] Check [INSTALLATION.md](INSTALLATION.md)
- [ ] Restart Streamlit
- [ ] Clear browser cache
- [ ] Try different browser
- [ ] Check GitHub Issues

---

**Still have questions? Create an issue on GitHub!** 🙋

Last Updated: January 18, 2026
