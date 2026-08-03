"""
=========================================================
Thème officiel OptiManager
=========================================================
"""

from styles.colors import *

WINDOW_STYLE = f"""
QMainWindow{{
    background:{BACKGROUND};
}}

QWidget{{
    background:{BACKGROUND};
    color:{TEXT};
    font-family:'Segoe UI';
    font-size:11pt;
}}

QTableWidget{{
    background:white;
    border:1px solid {BORDER};
}}

QLineEdit{{
    padding:6px;
    border:1px solid {BORDER};
    border-radius:6px;
}}

QComboBox{{
    padding:6px;
    border:1px solid {BORDER};
    border-radius:6px;
}}
"""