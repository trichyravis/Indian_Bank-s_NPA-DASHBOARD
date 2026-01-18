# 🚀 Quick Start Guide - 5 Minutes

Get the NPA Analysis Dashboard running in 5 minutes.

---

## ✅ Prerequisites

- Python 3.7 or higher
- pip (Python package manager)
- 50 MB disk space
- Web browser (Chrome, Firefox, Safari, Edge)

---

## 🎯 Step 1: Clone Repository (1 min)

```bash
git clone https://github.com/YOUR-USERNAME/npa-analysis-dashboard.git
cd npa-analysis-dashboard
```

Or download ZIP and extract:
```bash
unzip npa-analysis-dashboard.zip
cd npa-analysis-dashboard
```

---

## 📦 Step 2: Install Dependencies (2 min)

```bash
pip install -r requirements.txt
```

**What gets installed:**
- streamlit (web framework)
- pandas (data analysis)
- plotly (charts)
- numpy (numerical computing)

---

## ▶️ Step 3: Run Dashboard (1 min)

```bash
streamlit run src/app.py
```

**Expected output:**
```
  You can now view your Streamlit app in your browser.

  URL: http://localhost:8501
```

---

## 🌐 Step 4: Open in Browser (1 min)

Click the link or open in your browser:
```
http://localhost:8501
```

---

## 🎉 Done! Dashboard is Running

You should see:
- 📊 Dashboard title at the top
- 🎯 Sidebar with navigation menu
- 📈 Overview page with KPIs
- 📊 Charts and data visualizations

---

## 🔍 Explore the Dashboard

### Page 1: Overview
- System KPIs (GNPA%, NNPA%, NIM%, CASA%)
- Bank rankings
- System trends

### Page 2: Bank Deep Dive
- Select individual bank
- 12-quarter trends
- Detailed metrics

### Page 3: Peer Comparison
- Rankings by metric
- Quadrant analysis
- Competitive positioning

### Page 4: Data & Sources
- View all data
- Download CSV
- Source attribution

---

## 🎮 Try These Actions

1. **View Rankings**: Go to Peer Comparison page
2. **Select Bank**: Go to Bank Deep Dive, pick a bank
3. **Download Data**: Go to Data & Sources, click download button
4. **Change Metric**: On Peer Comparison, select different metrics

---

## ⚙️ Stop the Dashboard

Press `Ctrl + C` in terminal to stop:
```
^CKeyboardInterrupt: Shutting down...
```

---

## 🔄 Run Again

To run again:
```bash
streamlit run src/app.py
```

---

## ❓ Troubleshooting

### Port Already in Use
```bash
streamlit run src/app.py --server.port 8502
```

### Module Not Found
```bash
pip install --upgrade -r requirements.txt
```

### Dashboard Won't Load
- Clear browser cache (Ctrl+Shift+Delete)
- Try different browser
- Restart Python: `Ctrl+C` then run again

---

## 📚 Next Steps

1. ✅ Dashboard running? Great!
2. 📖 Read [USAGE.md](USAGE.md) for detailed features
3. 📊 Check [DATA_MODEL.md](DATA_MODEL.md) to understand data
4. 🏗️ Read [ARCHITECTURE.md](ARCHITECTURE.md) for system design

---

## 🤔 Common Questions

**Q: Can I modify the dashboard?**
A: Yes! See [CONTRIBUTING.md](../CONTRIBUTING.md)

**Q: How do I add more data?**
A: See [DATA_MODEL.md](DATA_MODEL.md) and [USAGE.md](USAGE.md)

**Q: Can I deploy online?**
A: Yes! See [INSTALLATION.md](INSTALLATION.md) for deployment options

**Q: What if I get errors?**
A: Check [FAQ.md](FAQ.md) for solutions

---

## ✨ Tips & Tricks

### Reload Dashboard
- Press `R` to rerun script
- Or press `C` to clear cache

### Full Screen
- Press `F` for full screen charts
- Press `X` to exit

### Share Link
- After deployment, share URL with others
- They can view dashboard without installing anything

---

## 🎯 What's Next?

**Beginner Path:**
1. Explore all 4 dashboard pages
2. Download data and view in Excel
3. Read [FAQ.md](FAQ.md)

**Intermediate Path:**
1. Study [DATA_MODEL.md](DATA_MODEL.md)
2. Understand data validation
3. Learn analytics logic

**Advanced Path:**
1. Modify dashboard code
2. Add new features
3. Deploy to production

---

## 📞 Need Help?

1. Check [FAQ.md](FAQ.md)
2. Read [USAGE.md](USAGE.md)
3. Review [INSTALLATION.md](INSTALLATION.md)
4. Check GitHub Issues
5. Contact maintainers

---

## ✅ Success Checklist

- [x] Python 3.7+ installed
- [x] Repository cloned/extracted
- [x] Dependencies installed
- [x] Dashboard running
- [x] Browser shows dashboard
- [x] Can navigate between pages

**If all checked: You're all set! 🎉**

---

**Enjoy exploring the NPA Analysis Dashboard!**

Last Updated: January 18, 2026
