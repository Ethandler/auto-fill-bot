
# Auto-Fill Bot 🧠💻

This Python-based automation tool fills out web forms using data from a CSV file. It uses PyAutoGUI and pyperclip to simulate human input and can handle:

- Standard text fields
- Dropdown menus (via image recognition)
- Checkbox selections
- Real-time clipboard pasting

## 🚀 How to Use

1. Run `main.py`
2. Hover your mouse over the first form input
3. Let the bot complete the form!

## 💾 Data Input Format

`form_data.csv` must include these columns:
- Full Name
- Business / Company Name
- Email
- Phone
- Type of Work Needed *(must match dropdown)*
- Priority Level *(must match dropdown)*
- Preferred Contact Methods *(comma-separated)*
- Work Description

## 🖼 Required Screenshots

Save these images in the same directory:
- `selectservice.png` — unopened service dropdown
- `selectpriority.png` — unopened priority dropdown

## 🧰 Requirements
- Python 3.x
- `pyautogui`, `pyperclip`, `pandas`

## 🔐 Security
No data is stored or transmitted. This bot only works locally in your browser.

---

© 2025 Ethan Blankenship — Built for automation nerds by automation nerds.
