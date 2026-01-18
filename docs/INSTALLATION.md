# 📥 Installation Guide

Complete step-by-step installation instructions for NPA Analysis Dashboard.

---

## 📋 System Requirements

### Minimum
- Python 3.7 or higher
- pip (Python package manager)
- 100 MB disk space
- 2 GB RAM

### Recommended
- Python 3.9+
- 500 MB disk space
- 4 GB RAM
- Modern web browser (Chrome, Firefox, Safari, Edge)

### Operating Systems
- ✅ Windows 10/11
- ✅ macOS 10.14+
- ✅ Ubuntu 18.04+
- ✅ Any Linux with Python 3.7+

---

## ✅ Check Python Installation

### Check if Python is installed
```bash
python --version
```

**Expected output:**
```
Python 3.9.x
```

### Check if pip is installed
```bash
pip --version
```

**Expected output:**
```
pip 23.x.x from /path/to/python/site-packages/pip
```

---

## 🔧 Installation Steps

### Step 1: Get the Code (Choose One)

#### Option A: Clone with Git
```bash
git clone https://github.com/YOUR-USERNAME/npa-analysis-dashboard.git
cd npa-analysis-dashboard
```

#### Option B: Download ZIP
1. Go to GitHub repository
2. Click "Code" → "Download ZIP"
3. Extract ZIP file
4. Open terminal in extracted folder

### Step 2: Create Virtual Environment (Recommended)

**Why virtual environment?**
- Isolates project dependencies
- Prevents version conflicts
- Keeps system Python clean

#### On Windows
```bash
python -m venv venv
venv\Scripts\activate
```

#### On macOS/Linux
```bash
python3 -m venv venv
source venv/bin/activate
```

**Expected output:**
```
(venv) $
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

**What gets installed:**
```
Collecting streamlit==1.28.1
Collecting pandas==2.0.3
Collecting plotly==5.17.0
Collecting numpy==1.24.3
Collecting pytest==7.4.0
...
Successfully installed streamlit pandas plotly numpy pytest
```

### Step 4: Verify Installation

```bash
python -c "import streamlit; import pandas; import plotly; print('✅ All imports successful!')"
```

**Expected output:**
```
✅ All imports successful!
```

---

## 🚀 Run Dashboard

### Local Development

```bash
streamlit run src/app.py
```

**Expected output:**
```
  You can now view your Streamlit app in your browser.

  URL: http://localhost:8501

  Press CTRL+C to quit.
```

### Open in Browser
- Automatically opens at: http://localhost:8501
- Or manually open that URL in your browser

---

## 🌐 Deployment Options

### Option 1: Streamlit Cloud (FREE - Easiest)

1. **Push to GitHub**
```bash
git add .
git commit -m "Initial commit"
git push origin main
```

2. **Go to Streamlit Cloud**
   - https://share.streamlit.io/

3. **Connect your repository**
   - Select your GitHub repo
   - Select branch: main
   - Set main file: src/app.py
   - Click Deploy

4. **Access your app**
   - Your app is live at: https://your-app-name.streamlit.app

### Option 2: Heroku (PAID)

1. **Create Heroku account**
   - https://www.heroku.com

2. **Install Heroku CLI**
```bash
# Windows/Mac/Linux
brew tap heroku/brew && brew install heroku
```

3. **Deploy**
```bash
heroku login
heroku create your-app-name
git push heroku main
```

### Option 3: AWS/Google Cloud (PAID - More Control)

1. **Create account on cloud provider**
2. **Set up VM/compute instance**
3. **Clone repository**
4. **Install dependencies**
5. **Run with process manager**
   - Use `gunicorn` or `supervisor`
   - Keep app running 24/7

### Option 4: Your Own Server (PAID)

1. **Set up Linux server**
2. **Install Python 3.7+**
3. **Clone repository**
4. **Install dependencies**
5. **Configure web server (nginx/Apache)**
6. **Run with process manager**

---

## 🔍 Troubleshooting

### Problem 1: Python Not Found
```
'python' is not recognized as an internal or external command
```

**Solution:**
- Install Python: https://www.python.org/downloads/
- Restart terminal/computer
- Or use `python3` instead of `python`

### Problem 2: pip Not Found
```
'pip' is not recognized
```

**Solution:**
```bash
python -m pip install --upgrade pip
```

### Problem 3: Permission Denied
```
Permission denied: /usr/local/lib/python3.9/site-packages
```

**Solution:**
- Use virtual environment (recommended)
- Or use: `pip install --user`

### Problem 4: Module Not Found
```
ModuleNotFoundError: No module named 'streamlit'
```

**Solution:**
```bash
pip install -r requirements.txt --upgrade
```

### Problem 5: Port Already in Use
```
ERROR: Address already in use
```

**Solution:**
```bash
streamlit run src/app.py --server.port 8502
```

### Problem 6: Version Conflicts
```
ERROR: pip's dependency resolver does not currently...
```

**Solution:**
```bash
pip install --upgrade pip
pip install -r requirements.txt --force-reinstall
```

---

## 📦 Dependency Details

### streamlit (1.28.1)
- Web app framework
- Interactive UI components
- Real-time updates

### pandas (2.0.3)
- Data manipulation
- CSV reading/writing
- Data analysis

### plotly (5.17.0)
- Interactive charts
- 3D visualizations
- Export to HTML/PNG

### numpy (1.24.3)
- Numerical operations
- Statistical calculations
- Array operations

### pytest (7.4.0)
- Unit testing
- Test discovery
- Test reporting

---

## 🎯 Post-Installation

### 1. Verify All Components
```bash
python -m pytest tests/ -v
```

### 2. Check Data Files
```bash
ls -la data/sample/
```

### 3. Test Dashboard
```bash
streamlit run src/app.py
```

### 4. Explore Code
```bash
cd src
ls -la
```

---

## ✅ Verification Checklist

- [ ] Python 3.7+ installed
- [ ] pip working
- [ ] Virtual environment created (optional but recommended)
- [ ] requirements.txt installed
- [ ] All imports successful
- [ ] Dashboard runs without errors
- [ ] Browser shows dashboard
- [ ] All 4 pages accessible

---

## 🔄 Updating Installation

### Update all packages
```bash
pip install -r requirements.txt --upgrade
```

### Update specific package
```bash
pip install streamlit --upgrade
```

### Check outdated packages
```bash
pip list --outdated
```

---

## 🧹 Clean Installation

### Remove virtual environment
```bash
# Windows
rmdir venv /s /q

# macOS/Linux
rm -rf venv
```

### Remove Python packages
```bash
pip uninstall -r requirements.txt -y
```

### Start fresh
```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

---

## 📚 Next Steps

1. ✅ Installation complete
2. 📖 Read [QUICK_START.md](QUICK_START.md)
3. 🎮 Run the dashboard
4. 📊 Explore all features
5. 📚 Read [USAGE.md](USAGE.md)

---

## 💡 Tips

1. **Always use virtual environment** - Keeps project isolated
2. **Keep requirements.txt updated** - Track dependencies
3. **Test after installation** - Verify everything works
4. **Use the latest Python** - Better performance
5. **Document any issues** - Help others troubleshoot

---

## 🆘 Still Having Issues?

1. Check [FAQ.md](FAQ.md)
2. Review [QUICK_START.md](QUICK_START.md)
3. Check GitHub Issues
4. Contact maintainers
5. Provide full error message

---

**Installation Guide Complete! Ready to use the dashboard.** ✅

Last Updated: January 18, 2026
