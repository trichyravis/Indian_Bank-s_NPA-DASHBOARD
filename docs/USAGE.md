# 📖 Usage Guide

Complete guide to using all features of the NPA Analysis Dashboard.

---

## 🎯 Dashboard Overview

The NPA Analysis Dashboard has **4 main pages**:

1. **📈 Overview** - System KPIs and trends
2. **🏦 Bank Deep Dive** - Individual bank analysis
3. **🏆 Peer Comparison** - Rankings and positioning
4. **📚 Data & Sources** - Raw data and attribution

---

## 📈 Page 1: Overview

### What You See

- **4 KPI Cards** at the top showing:
  - Avg GNPA % (Gross NPA)
  - Avg NNPA % (Net NPA)
  - Avg NIM % (Net Interest Margin)
  - Avg CASA % (Current Account Saving Account)

- **2 Charts** showing:
  - GNPA Rankings (lowest is best)
  - NIM Rankings (highest is best)

- **Trend Chart** showing:
  - System-wide GNPA trend
  - System-wide NIM trend

### How to Use

1. **Read KPI Cards**
   - Click on each card to see more details
   - Green ↓ means improving
   - Red ↑ means worsening

2. **Analyze Rankings**
   - See which banks have lowest NPA
   - See which banks have highest profitability

3. **Track Trends**
   - See 4-quarter trends
   - Identify patterns over time

### Example Actions

```
"I see SBI has 2.45% GNPA. Is that good?"
→ Look at ranking chart - SBI is middle of pack
→ Check trend - GNPA is decreasing (good)
→ Compare with KOTAK (1.15% GNPA) for best performer
```

---

## 🏦 Page 2: Bank Deep Dive

### What You See

1. **Bank Selector** (dropdown menu at top)
   - Select any of 12 banks
   - SBI, HDFC, ICICI, AXIS, KOTAK, etc.

2. **Latest Metrics** (4 cards)
   - Current GNPA, NNPA, NIM, CASA

3. **NPA Trends Chart** (12 quarters)
   - GNPA line (should go down = good)
   - NNPA line (should go down = good)

4. **Profitability Chart** (12 quarters)
   - NIM line (should go up = good)
   - CASA line (should go up = good)

5. **Data Table** (all quarters)
   - View exact numbers
   - Copy for analysis

### How to Use

1. **Select a Bank**
   - Click dropdown
   - Choose bank (e.g., HDFC)
   - Charts update automatically

2. **Read Latest Metrics**
   - See current GNPA, NNPA, NIM, CASA
   - Compare with average

3. **Analyze Trends**
   - GNPA trending down? Asset quality improving
   - NIM trending up? Profitability improving
   - CASA trending up? Funding cost decreasing

4. **View Details**
   - Scroll down to see data table
   - Check exact numbers for each quarter

### Example Actions

```
"How is HDFC Bank performing?"
→ Select HDFC from dropdown
→ See GNPA: 1.32% (lower than SBI 2.45%)
→ See NIM: 4.25% (higher than SBI 3.42%)
→ Look at trend chart - both metrics improving
→ Conclusion: HDFC performing better than SBI
```

### Keyboard Shortcuts
- Use arrow keys to navigate dropdown
- Press Enter to select
- Ctrl+A to select all data

---

## 🏆 Page 3: Peer Comparison

### What You See

1. **Metric Selector** (dropdown)
   - Choose: GNPA%, NIM%, or CASA%

2. **Rankings Chart** (sorted)
   - Shows all banks ranked by selected metric
   - Color gradient from best to worst

3. **Quadrant Scatter Chart**
   - X-axis: CASA%
   - Y-axis: GNPA%
   - Size of bubble: NIM%
   - Color: Bank name

4. **Full Rankings Table**
   - All metrics for all banks
   - Sortable columns

### How to Use

1. **Compare by Single Metric**
   - Select metric (GNPA%, NIM%, or CASA%)
   - See ranked list
   - Identify best and worst performers

2. **Analyze Quadrant View**
   - **BEST Quadrant** (top-left): High CASA, Low GNPA
   - **CAUTION Quadrant** (top-right): High CASA, High GNPA
   - **WATCH Quadrant** (bottom-left): Low CASA, Low GNPA
   - **WORST Quadrant** (bottom-right): Low CASA, High GNPA

3. **View Full Comparison**
   - See all metrics in table
   - Compare banks side-by-side
   - Export for further analysis

### Quadrant Explained

```
                        CASA %
                          ↑
                     CAUTION | BEST
                             |
         GNPA% (decreasing) ←-+→ GNPA% (increasing)
                             |
                     WORST   | WATCH
                          ↓
```

### Example Actions

```
"Which bank is best positioned?"
→ Go to Peer Comparison
→ Look at quadrant chart
→ Find bank in BEST quadrant (top-left)
→ KOTAK is in BEST (high CASA 42%, low GNPA 1.15%)
→ Conclusion: KOTAK is best positioned

"How does AXIS compare to ICICI?"
→ Look at table
→ AXIS: GNPA 1.89%, NIM 3.65%, CASA 40.5%
→ ICICI: GNPA 1.28%, NIM 3.18%, CASA 39.8%
→ AXIS has worse GNPA (higher is worse)
→ But AXIS has better NIM (higher is better)
```

---

## 📚 Page 4: Data & Sources

### What You See

1. **Raw Data Table** (all rows)
   - Bank names
   - All metrics
   - Period/quarter
   - Source information

2. **Download Button**
   - Downloads data as CSV
   - Timestamped filename

3. **Source Attribution** (expandable)
   - Source URL for each row
   - Document date
   - Reference notes

### How to Use

1. **View All Data**
   - See all banks, all quarters
   - Check for data completeness
   - Verify metrics

2. **Download CSV**
   - Click "Download CSV"
   - File saved as: npa_metrics_YYYYMMDD_HHMMSS.csv
   - Open in Excel or Python

3. **Check Sources**
   - Click expand button for each row
   - See where data came from
   - Verify data authenticity

### Example Actions

```
"I need to analyze this data in Excel"
→ Go to Data & Sources page
→ Click "Download CSV"
→ File downloads to computer
→ Open in Excel
→ Analyze further

"Which source did this GNPA value come from?"
→ Look at table
→ Find the row
→ Click expand button
→ See source URL, date, and notes
→ Click link to see original PDF
```

---

## 🎮 Interactive Features

### 1. Hover Over Charts
```
→ Hover mouse on chart
→ See exact values in tooltip
→ See bank name and metrics
```

### 2. Zoom Charts
```
→ Scroll wheel on chart
→ Zoom in/out
→ Double-click to reset
```

### 3. Pan Charts
```
→ Click and drag on chart
→ Move around zoomed chart
→ Release to stop
```

### 4. Toggle Traces
```
→ Click legend item on chart
→ Hide/show that data series
→ Useful for comparing specific items
```

### 5. Download Chart as Image
```
→ Hover over chart
→ See camera icon at top-right
→ Click to download as PNG
```

---

## 📊 Metrics Explained

### GNPA (Gross NPA %)
- **What it is**: Percentage of bad loans
- **Good range**: 0-2%
- **Trend**: Should be decreasing (lower is better)
- **Example**: SBI 2.45% means 2.45 out of 100 loans are bad

### NNPA (Net NPA %)
- **What it is**: Bad loans after accounting for provisions
- **Good range**: 0-0.5%
- **Trend**: Should be decreasing (lower is better)
- **Example**: GNPA - Provisions = NNPA

### NIM (Net Interest Margin %)
- **What it is**: Profitability from lending
- **Good range**: 3-4%
- **Trend**: Should be stable or increasing
- **Example**: Bank earns 3.42% on each rupee of loans

### CASA (Current Account Saving Account %)
- **What it is**: Percentage of low-cost deposits
- **Good range**: 35-45%
- **Trend**: Should be increasing (higher is better)
- **Example**: 44.2% means 44.2 out of 100 rupees in deposits are CASA

---

## 🔍 Analysis Tips

### Tip 1: Compare Trends Over Time
- Select a bank → Look at 12-quarter chart
- Identify patterns and trends
- GNPA going up? Problem with asset quality
- NIM going down? Profitability declining

### Tip 2: Use Quadrant Analysis
- BEST: Strong performer (invest/follow)
- CAUTION: Good CASA but high GNPA (risky)
- WATCH: Low CASA but good GNPA (monitor)
- WORST: Avoid (problem bank)

### Tip 3: Compare Peer Performance
- Use rankings to see how bank ranks
- Compare multiple metrics, not just one
- Context matters: market conditions, business model

### Tip 4: Track Changes
- Download data at different times
- Compare trends to identify changes
- Look for improvements or deterioration

### Tip 4: Check Data Source
- Always verify data source
- See when data was published
- Ensure using latest information

---

## ⌨️ Keyboard Shortcuts

| Action | Shortcut |
|--------|----------|
| Full screen chart | `F` (in Plotly charts) |
| Exit full screen | `Esc` |
| Reload dashboard | `R` |
| Clear cache | `C` |
| Focus chart | Click on chart |
| Select from dropdown | Arrow keys + Enter |

---

## 🎨 Dashboard Customization

### Change Colors
- Edit `src/app.py`
- Look for `color_continuous_scale` parameters
- Change to 'Viridis', 'Blues', 'Reds', etc.

### Add New Banks
- Edit `src/bank_list.py`
- Add bank to `BANK_UNIVERSE` dict
- Restart dashboard

### Modify Metrics
- Edit `src/data_model.py`
- Add/remove columns in schema
- Update validation rules in `src/validate.py`

---

## 🐛 Troubleshooting

### Dashboard Won't Load
```
→ Check if Streamlit is running (see terminal)
→ Try: Ctrl+C then rerun
→ Clear browser cache
→ Try different browser
```

### Data Not Showing
```
→ Check if data files exist
→ Verify CSV file format
→ Check data_model.py for schema
→ Run validation: python src/validate.py
```

### Charts Not Interactive
```
→ Check if Plotly is installed
→ Try: pip install plotly --upgrade
→ Clear browser cache
→ Try different browser
```

### Dropdown Not Working
```
→ Refresh page (F5)
→ Clear browser cache
→ Restart Streamlit
```

---

## 📚 Further Resources

- [DATA_MODEL.md](DATA_MODEL.md) - Data structure details
- [API.md](API.md) - API reference
- [FAQ.md](FAQ.md) - Common questions

---

## 🎓 Learning Exercises

### Exercise 1: Compare Two Banks
1. Go to Bank Deep Dive
2. Select Bank A (e.g., SBI)
3. Note down GNPA, NNPA, NIM, CASA
4. Select Bank B (e.g., HDFC)
5. Compare metrics
6. Identify which is performing better

### Exercise 2: Analyze Trends
1. Go to Bank Deep Dive
2. Select a bank
3. Look at 12-quarter trend
4. Identify 3-5 key observations
5. Write summary of performance

### Exercise 3: Quadrant Analysis
1. Go to Peer Comparison
2. Look at quadrant chart
3. Identify banks in each quadrant
4. Explain why they're in that quadrant
5. Determine investment implications

---

**Now you're ready to use the dashboard!** 🎉

Last Updated: January 18, 2026
