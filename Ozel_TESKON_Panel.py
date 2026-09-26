import streamlit as st
import pandas as pd
import os
from datetime import datetime

# ============================================================
# 1. VIP SAYFA YAPILANDIRMASI
# ============================================================
st.set_page_config(
    page_title="TESKON | Sovereign Executive Suite",
    page_icon="👑",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# 2. BLACK EDITION & IMPERIAL TASARIM SİSTEMİ
# ============================================================
st.markdown("""
<style>
    /* Streamlit üst menü / footer / toolbar gizle — sidebar aç-kapa butonunu KORU */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    div[data-testid="stStatusWidget"] {display: none !important;}
    div[data-testid="stToolbar"] {display: none !important;}
    button[title="View app in Streamlit Community Cloud"] {display: none !important;}

    header {
        background: transparent !important;
        box-shadow: none !important;
    }
    .stAppHeader { background: transparent !important; }

    /* Kenar çubuğu aç/kapa butonu (mobil dahil) her koşulda görünür kalsın */
    button[data-testid="collapsedControl"],
    div[data-testid="collapsedControl"],
    [data-testid="stSidebarCollapsedControl"],
    [data-testid="stSidebarCollapseButton"],
    button[aria-label="Open sidebar"],
    button[aria-label="Close sidebar"] {
        visibility: visible !important;
        display: flex !important;
        opacity: 1 !important;
        pointer-events: auto !important;
        z-index: 999999 !important;
    }

    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@500;700;900&family=Cormorant+Garamond:ital,wght@0,400;0,600;1,500&family=Plus+Jakarta+Sans:wght@300;400;500;600;700&display=swap');

    /* ===== GLOBAL ===== */
    .stApp {
        background: radial-gradient(circle at 50% -20%, #1a160d 0%, #08090a 60%, #030405 100%);
        color: #e5e7eb;
        font-family: 'Plus Jakarta Sans', sans-serif;
    }

    ::-webkit-scrollbar { width: 8px; height: 8px; }
    ::-webkit-scrollbar-track { background: #05060a; }
    ::-webkit-scrollbar-thumb { background: linear-gradient(180deg, #bf953f, #d4af37); border-radius: 10px; }
    ::-webkit-scrollbar-thumb:hover { background: #fcf6ba; }

    @keyframes fadeSlideUp {
        0% { opacity: 0; transform: translateY(22px); }
        100% { opacity: 1; transform: translateY(0); }
    }
    .fade-in { animation: fadeSlideUp 0.9s cubic-bezier(0.22, 1, 0.36, 1) both; }
    .fade-in.delay-1 { animation-delay: 0.12s; }
    .fade-in.delay-2 { animation-delay: 0.24s; }
    .fade-in.delay-3 { animation-delay: 0.36s; }
    .fade-in.delay-4 { animation-delay: 0.48s; }

    section[data-testid="stSidebar"] {
        background: rgba(10, 12, 16, 0.9) !important;
        backdrop-filter: blur(20px);
        border-right: 1px solid rgba(212, 175, 55, 0.15) !important;
    }

    /* ===== ALTIN PARÇACIK ARKAPLANI ===== */
    @keyframes twinkle {
        0%, 100% { opacity: 0.15; transform: scale(0.8); }
        50% { opacity: 0.9; transform: scale(1.15); }
    }
    .sparkle-field {
        position: fixed; top: 0; left: 0; width: 100vw; height: 100vh;
        pointer-events: none; z-index: 1; overflow: hidden;
    }
    .sparkle {
        position: absolute; width: 5px; height: 5px;
        background: #ffe9ab; border-radius: 50%;
        box-shadow: 0 0 12px 3px rgba(255, 233, 171, 0.9);
        animation: twinkle 3.5s infinite ease-in-out;
    }

    /* ===== ALTIN BALONLAR (kutlama sayfası) ===== */
    @keyframes floatBalloon {
        0% { transform: translateY(100vh) rotate(0deg); opacity: 0.9; }
        100% { transform: translateY(-120vh) rotate(20deg); opacity: 0; }
    }
    .balloon-container {
        position: fixed; top: 0; left: 0; width: 100vw; height: 100vh;
        pointer-events: none; z-index: 99999; overflow: hidden;
    }
    .gold-balloon {
        position: absolute; bottom: -100px; width: 42px; height: 52px;
        background: radial-gradient(circle at 35% 35%, #fcf6ba, #bf953f 60%, #aa771c 100%);
        border-radius: 50% 50% 50% 50% / 40% 40% 60% 60%;
        animation: floatBalloon 9s infinite ease-in;
        box-shadow: inset -4px -4px 8px rgba(0,0,0,0.4), 0 8px 25px rgba(212, 175, 55, 0.4);
    }
    .gold-balloon::after {
        content: ""; position: absolute; bottom: -14px; left: 20px;
        width: 2px; height: 16px; background: rgba(212, 175, 55, 0.8);
    }
    .b1 { left: 4%; animation-duration: 8s; animation-delay: 0s; }
    .b2 { left: 18%; animation-duration: 10s; animation-delay: 2.5s; width: 50px; height: 62px; }
    .b3 { left: 78%; animation-duration: 9s; animation-delay: 1s; }
    .b4 { left: 91%; animation-duration: 11s; animation-delay: 3s; width: 46px; height: 56px; }
    .b5 { left: 48%; animation-duration: 12s; animation-delay: 4.5s; }

    /* ===== ÜST DURUM ŞERİDİ ===== */
    .status-strip {
        display: flex; justify-content: space-between; align-items: center;
        background: rgba(212, 175, 55, 0.06);
        border: 1px solid rgba(212, 175, 55, 0.18);
        border-radius: 14px; padding: 10px 22px; margin-bottom: 22px;
        letter-spacing: 1px; font-size: 11.5px; color: #d4af37;
        text-transform: uppercase; backdrop-filter: blur(12px);
    }
    .status-strip span.dim { color: #8b8f98; font-weight: 400; }
    .pulse-dot {
        display: inline-block; width: 7px; height: 7px; border-radius: 50%;
        background: #10b981; margin-right: 6px;
        box-shadow: 0 0 8px 2px rgba(16, 185, 129, 0.7);
        animation: pulseDot 1.8s infinite;
    }
    @keyframes pulseDot { 0%, 100% { opacity: 1; } 50% { opacity: 0.35; } }

    /* ===== BANNER ===== */
    .imperial-banner {
        background: linear-gradient(135deg, rgba(20, 20, 20, 0.9) 0%, rgba(35, 28, 15, 0.95) 50%, rgba(10, 10, 10, 0.9) 100%);
        border: 1px solid rgba(212, 175, 55, 0.4);
        border-radius: 24px; padding: 44px 40px; text-align: center;
        box-shadow: 0 20px 50px rgba(0, 0, 0, 0.8), 0 0 40px rgba(212, 175, 55, 0.12);
        margin-bottom: 35px; position: relative; backdrop-filter: blur(15px); overflow: hidden;
    }
    .imperial-banner::before {
        content: ""; position: absolute; inset: 0;
        background: linear-gradient(120deg, transparent 30%, rgba(212,175,55,0.08) 50%, transparent 70%);
        background-size: 200% 200%; animation: shimmerSweep 6s linear infinite; pointer-events: none;
    }
    @keyframes shimmerSweep { 0% { background-position: 200% 0; } 100% { background-position: -200% 0; } }
    .imperial-badge {
        display: inline-block; padding: 6px 20px;
        background: linear-gradient(90deg, #bf953f, #fcf6ba, #b38728, #fbf5b7);
        background-size: 300% 100%; animation: badgeShine 4s ease infinite;
        color: #000; font-family: 'Cinzel', serif; font-weight: 900; font-size: 11px;
        letter-spacing: 3px; border-radius: 50px; margin-bottom: 18px;
        text-transform: uppercase; box-shadow: 0 4px 15px rgba(212, 175, 55, 0.35);
    }
    @keyframes badgeShine { 0% { background-position: 0% 50%; } 50% { background-position: 100% 50%; } 100% { background-position: 0% 50%; } }
    .imperial-title {
        background: linear-gradient(180deg, #ffffff 0%, #dfb76c 100%);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        font-family: 'Cinzel', serif; font-size: 40px; font-weight: 900;
        letter-spacing: 2.5px; margin-bottom: 14px; text-shadow: 0 10px 20px rgba(0,0,0,0.5);
    }
    .imperial-sub {
        color: #d1d5db; font-family: 'Cormorant Garamond', serif; font-style: italic;
        font-size: 20px; font-weight: 500; max-width: 850px; margin: 0 auto;
        line-height: 1.8; letter-spacing: 0.4px;
    }
    .imperial-sub b { font-style: normal; font-family: 'Plus Jakarta Sans', sans-serif; color: #f3e3b3; font-weight: 600; letter-spacing: 0.5px; }

    .gold-divider { width: 140px; height: 2px; margin: 22px auto; background: linear-gradient(90deg, transparent, #d4af37, transparent); }

    /* ===== DIAMOND CARDS ===== */
    .diamond-card {
        background: rgba(18, 21, 28, 0.6);
        border: 1px solid rgba(212, 175, 55, 0.28);
        border-radius: 18px; padding: 28px 20px; text-align: center;
        box-shadow: 0 10px 30px rgba(0,0,0,0.5), 0 0 18px rgba(212, 175, 55, 0.08);
        backdrop-filter: blur(10px);
        transition: transform 0.35s ease, box-shadow 0.35s ease, border-color 0.35s ease;
    }
    .diamond-card:hover {
        transform: translateY(-8px);
        border-color: rgba(212, 175, 55, 0.85);
        box-shadow: 0 20px 45px rgba(0,0,0,0.65), 0 0 34px rgba(212, 175, 55, 0.3);
    }
    .diamond-icon { font-size: 22px; margin-bottom: 6px; opacity: 0.9; }
    .diamond-value {
        font-family: 'Cinzel', serif; font-size: 32px; font-weight: 700;
        background: linear-gradient(135deg, #ffffff 0%, #d4af37 100%);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    }
    .diamond-label { font-size: 11.5px; color: #9ca3af; letter-spacing: 1.5px; text-transform: uppercase; margin-top: 8px; font-weight: 600; }

    /* ===== SECTION TITLE ===== */
    .section-title {
        font-family: 'Cinzel', serif; color: #d4af37; font-size: 24px; letter-spacing: 1px;
        border-bottom: 1px solid rgba(212, 175, 55, 0.25); padding-bottom: 14px; margin-bottom: 22px;
    }
    .section-sub { color: #9ca3af; font-size: 13px; margin-top: -14px; margin-bottom: 18px; line-height: 1.7; }

    /* ===== INFO / CONTENT CARDS ===== */
    .info-card {
        background: rgba(255,255,255,0.035);
        border: 1px solid rgba(212,175,55,0.18);
        border-radius: 16px; padding: 20px 24px; margin-bottom: 16px;
    }
    .info-row {
        display: flex; justify-content: space-between; gap: 18px;
        padding: 9px 0; border-bottom: 1px solid rgba(255,255,255,0.06); font-size: 13.5px;
    }
    .info-row:last-child { border-bottom: none; }
    .info-row .k { color: #9ca3af; letter-spacing: 0.4px; }
    .info-row .v { color: #f3e3b3; font-weight: 600; text-align: right; }

    .mission-card {
        background: rgba(255,255,255,0.03);
        border-top: 2px solid rgba(212,175,55,0.5);
        border-radius: 14px; padding: 24px 20px; height: 100%;
    }
    .mission-card h4 { font-family: 'Cinzel', serif; color: #d4af37; font-size: 14.5px; letter-spacing: 1.2px; margin-bottom: 12px; line-height: 1.5; }
    .mission-card p { color: #c3c8d1; font-size: 13px; line-height: 1.75; margin: 0; }

    .chip-grid { display: flex; flex-wrap: wrap; gap: 10px; }
    .chip {
        background: rgba(212,175,55,0.07); border: 1px solid rgba(212,175,55,0.3);
        border-radius: 30px; padding: 9px 18px; font-size: 12.5px; color: #e6c869; letter-spacing: 0.4px;
        transition: all 0.25s ease;
    }
    .chip:hover { background: rgba(212,175,55,0.16); border-color: rgba(212,175,55,0.6); }

    .cert-badge {
        display: inline-block;
        background: linear-gradient(135deg, rgba(212,175,55,0.16), rgba(212,175,55,0.02));
        border: 1px solid rgba(212,175,55,0.4); border-radius: 10px;
        padding: 11px 18px; margin: 4px 8px 4px 0;
        font-family: 'Cinzel', serif; font-size: 11px; letter-spacing: 1.5px; color: #f3e3b3;
    }

    .contact-card {
        background: rgba(255,255,255,0.03); border: 1px solid rgba(212,175,55,0.25);
        border-radius: 16px; padding: 20px 24px; margin-bottom: 14px;
        display: flex; align-items: center; gap: 16px;
    }
    .contact-card .ic { font-size: 22px; }
    .contact-card .label { font-size: 10.5px; color: #9ca3af; letter-spacing: 1.5px; text-transform: uppercase; margin-bottom: 3px; }
    .contact-card .val { font-size: 14.5px; color: #f0f2f4; font-weight: 500; }

    /* ===== SIDEBAR MENU AKTIF GÖSTERGE ===== */
    div[data-testid="stSidebar"] div[role="radiogroup"] label {
        border-radius: 10px; padding: 9px 12px !important; letter-spacing: 0.3px;
        transition: background 0.25s ease, padding-left 0.25s ease, border-color 0.25s ease;
        border-left: 3px solid transparent;
    }
    div[data-testid="stSidebar"] div[role="radiogroup"] label:hover {
        background: rgba(212, 175, 55, 0.08); padding-left: 16px !important;
    }
    div[data-testid="stSidebar"] div[role="radiogroup"] label:has(input:checked) {
        background: linear-gradient(90deg, rgba(212,175,55,0.22), transparent 85%);
        border-left: 3px solid #d4af37; padding-left: 16px !important;
    }

    /* ===== INPUTLAR ===== */
    div[data-baseweb="input"], div[data-baseweb="select"] {
        border-radius: 12px !important;
        border: 1px solid rgba(212, 175, 55, 0.4) !important;
        background-color: rgba(255, 255, 255, 0.045) !important;
        color: #fff !important;
    }
    div[data-baseweb="input"]:focus-within, div[data-baseweb="select"]:focus-within {
        border: 1px solid rgba(212, 175, 55, 0.85) !important;
        box-shadow: 0 0 12px rgba(212, 175, 55, 0.25) !important;
    }

    .stButton>button, .stDownloadButton>button {
        background: linear-gradient(135deg, #bf953f, #fcf6ba 40%, #b38728 100%) !important;
        color: #000 !important; font-weight: 700 !important; letter-spacing: 0.6px;
        border: none !important; border-radius: 10px !important;
        box-shadow: 0 6px 18px rgba(212,175,55,0.25);
        transition: transform 0.25s ease, box-shadow 0.25s ease;
    }
    .stButton>button:hover, .stDownloadButton>button:hover {
        transform: translateY(-2px); box-shadow: 0 10px 26px rgba(212,175,55,0.4);
    }

    /* ===== DATAFRAME KAPSAYICI ===== */
    div[data-testid="stDataFrame"] {
        border: 1px solid rgba(212, 175, 55, 0.2);
        border-radius: 14px; overflow: hidden;
    }

    /* ===== SIDEBAR ALTINDAKI KÜÇÜK MÜHÜR ROZETI ===== */
    .sidebar-seal {
        display: flex; align-items: center; justify-content: center; gap: 9px;
        margin-top: 16px; padding-top: 14px; border-top: 1px solid rgba(212, 175, 55, 0.15);
    }
    .sidebar-seal .icon {
        width: 28px; height: 28px; border-radius: 50%;
        border: 1px solid rgba(212, 175, 55, 0.65); display: flex; align-items: center; justify-content: center;
        font-size: 13px; background: radial-gradient(circle, rgba(212,175,55,0.22), transparent 70%);
    }
    .sidebar-seal .txt { font-size: 8.5px; letter-spacing: 2px; color: #8b8f98; text-transform: uppercase; line-height: 1.4; text-align: left; }
    .sidebar-seal .txt b { color: #d4af37; }
</style>

<div class="sparkle-field">
    <div class="sparkle" style="top:12%; left:8%; animation-delay:0s;"></div>
    <div class="sparkle" style="top:22%; left:32%; animation-delay:0.6s;"></div>
    <div class="sparkle" style="top:8%; left:64%; animation-delay:1.2s;"></div>
    <div class="sparkle" style="top:35%; left:85%; animation-delay:1.8s;"></div>
    <div class="sparkle" style="top:60%; left:14%; animation-delay:2.1s;"></div>
    <div class="sparkle" style="top:75%; left:48%; animation-delay:0.9s;"></div>
    <div class="sparkle" style="top:48%; left:70%; animation-delay:1.5s;"></div>
    <div class="sparkle" style="top:85%; left:90%; animation-delay:2.4s;"></div>
    <div class="sparkle" style="top:5%; left:45%; animation-delay:0.3s;"></div>
    <div class="sparkle" style="top:65%; left:60%; animation-delay:2.7s;"></div>
</div>
""", unsafe_allow_html=True)


# ============================================================
# 3. YARDIMCI FONKSİYONLAR
# ============================================================

def style_table(dframe: pd.DataFrame, zebra_limit: int = 1500):
    working = dframe.reset_index(drop=True)
    if len(working) > zebra_limit:
        return working
    try:
        styled = working.style.hide(axis="index")
    except Exception:
        styled = working.style.hide_index()

    def zebra(row):
        if row.name % 2 == 0:
            return ['background-color: rgba(255,255,255,0.035); color:#e8eaed;'] * len(row)
        return ['background-color: rgba(0,0,0,0.28); color:#e8eaed;'] * len(row)

    return styled.apply(zebra, axis=1)


def render_info_card(rows):
    html = "<div class='info-card'>"
    for k, v in rows:
        html += f"<div class='info-row'><span class='k'>{k}</span><span class='v'>{v}</span></div>"
    html += "</div>"
    st.markdown(html, unsafe_allow_html=True)


def render_chips(items):
    html = "<div class='chip-grid'>" + "".join([f"<span class='chip'>{i}</span>" for i in items]) + "</div>"
    st.markdown(html, unsafe_allow_html=True)


# ============================================================
# 4. OTOMATİK VERİ DOSYASI BULMA (.ods / .xlsx)
# ============================================================
@st.cache_data
def load_ods_data():
    current_dir = os.path.dirname(os.path.abspath(__file__)) if '__file__' in globals() else os.getcwd()
    for file in os.listdir(current_dir):
        if file.endswith('.ods') or file.endswith('.xlsx'):
            try:
                file_path = os.path.join(current_dir, file)
                df = pd.read_excel(file_path, engine='odf' if file.endswith('.ods') else None)
                if 'Yuzolcum' in df.columns:
                    df['Yuzolcum_Sayısal'] = pd.to_numeric(
                        df['Yuzolcum'].astype(str).str.replace(',', '.'), errors='coerce'
                    )
                return df, file
            except Exception as e:
                return str(e), None
    return None, None


df, filename = load_ods_data()


# ============================================================
# 5. KURUMSAL SABİT VERİLER
# ============================================================

IS_BITIRME_KAYITLARI = [
    ("A1", "KÖPRÜ ve VİYADÜK İŞLERİ", "Yurtiçi", "₺37.365.000,00"),
    ("A1", "KÖPRÜ ve VİYADÜK İŞLERİ", "Yurtiçi", "₺93.412.500,00"),
    ("A1", "KÖPRÜ ve VİYADÜK İŞLERİ", "Yurtiçi", "₺144.750.000,00"),
    ("A3", "BORU ve İLETİM HATTI İŞLERİ", "Yurtdışı", "$22.365.000,00"),
    ("A3", "BORU ve İLETİM HATTI İŞLERİ", "Yurtiçi", "₺98.569.841,00"),
    ("A3", "BORU ve İLETİM HATTI İŞLERİ", "Yurtiçi", "₺246.424.602,50"),
    ("A3", "BORU ve İLETİM HATTI İŞLERİ", "Yurtiçi", "₺198.326.511,00"),
    ("A4", "İÇME, KULLANMA SUYU ve KANALİZASYON İŞLERİ", "Yurtdışı", "$32.648.921,00"),
    ("A4", "İÇME, KULLANMA SUYU ve KANALİZASYON İŞLERİ", "Yurtiçi", "₺79.878.745,00"),
    ("A4", "İÇME, KULLANMA SUYU ve KANALİZASYON İŞLERİ", "Yurtiçi", "₺337.987.145,00"),
    ("A4", "İÇME, KULLANMA SUYU ve KANALİZASYON İŞLERİ", "Yurtiçi", "₺199.696.862,00"),
    ("A5", "KARAYOLU İŞLERİ", "Yurtdışı", "$137.874.512,00"),
    ("A5", "KARAYOLU İŞLERİ", "Yurtiçi", "₺94.686.280,00"),
    ("A5", "KARAYOLU İŞLERİ", "Yurtiçi", "₺113.623.536,00"),
    ("A6", "DEMİRYOLU İŞLERİ", "Yurtiçi", "₺85.217.652,00"),
    ("A9", "BARAJLAR ve SU YAPILARI", "Yurtdışı", "$39.515.000,00"),
    ("A9", "BARAJLAR ve SU YAPILARI", "Yurtiçi", "₺118.545.000,00"),
    ("A10", "DENİZ YAPILARI", "Yurtiçi", "₺79.822.745,00"),
    ("A11", "ARITMA TESİSLERİ", "Yurtiçi", "₺139.874.412,00"),
    ("A11", "ARITMA TESİSLERİ", "Yurtdışı", "$49.686.030,00"),
    ("A11", "ARITMA TESİSLERİ", "Yurtiçi", "₺159.874.992,00"),
    ("A16", "ENDÜSTRİYEL TESİS İNŞAATLARI", "Yurtiçi", "₺23.987.441,00"),
    ("A16", "ENDÜSTRİYEL TESİS İNŞAATLARI", "Yurtiçi", "₺71.962.323,00"),
    ("A16", "ENDÜSTRİYEL TESİS İNŞAATLARI", "Yurtdışı", "$179.905.807,50"),
    ("A16", "ENDÜSTRİYEL TESİS İNŞAATLARI", "Yurtiçi", "₺215.886.969,00"),
    ("A18", "SAHA İŞLERİ", "Yurtiçi", "₺123.987.400,00"),
    ("B2", "BİNA İŞLERİ", "Yurtiçi", "₺29.514.400,00"),
    ("B2", "BİNA İŞLERİ", "Yurtdışı", "$73.786.000,00"),
    ("B2", "BİNA İŞLERİ", "Yurtiçi", "₺88.543.200,00"),
    ("B2", "BİNA İŞLERİ", "Yurtiçi", "₺221.358.000,00"),
    ("B2", "BİNA İŞLERİ", "Yurtiçi", "₺265.629.600,00"),
    ("C2", "ISITMA, SOĞUTMA, HAVALANDIRMA ve İKLİMLENDİRME İŞLERİ", "Yurtdışı", "$23.985.541,00"),
    ("C2", "ISITMA, SOĞUTMA, HAVALANDIRMA ve İKLİMLENDİRME İŞLERİ", "Yurtiçi", "₺59.963.852,00"),
    ("D1", "ENERJİ İLETİM İŞLERİ", "Yurtiçi", "₺111.891.557,50"),
    ("D1", "ENERJİ İLETİM İŞLERİ", "Yurtiçi", "₺71.956.623,50"),
]

ARAC_PARKI = [
    (2, "BETON POMPA ARACI", "POMPA"),
    (2, "BETON POMPALARI", "BETON POMPASI"),
    (2, "BETON SANTRALLERİ", "BETON SANTRALİ"),
    (2, "ÇİMENTO SİLOLARI", "ÇİMENTO SİLOSU"),
    (3, "TRANSMİKSERLER", "TRANSMİKSER"),
    (2, "ÇEKİCİLER", "ÇEKİCİ"),
    (4, "DAMPERLİ KAMYONLAR", "DAMPERLİ"),
    (3, "DOZER ve GREYDER", "DOZER ve GREYDER"),
    (2, "DELİCİ ve KIRICILAR", "DELİCİ ve KIRICI"),
    (7, "EKSKAVATÖRLER", "EKSKAVATÖR"),
    (4, "FİNİŞERLER", "PALETLİ FİNİŞER"),
    (3, "JENERATÖRLER", "JENERATÖR"),
    (2, "KAMYONLAR", "KAMYON"),
    (2, "KIRMA-ELEME TESİSLERİ", "KIRMA-ELEME TESİSİ"),
    (4, "ASFALT PLENTLERİ", "ASFALT PLENTİ"),
    (2, "ASFALT SİLİNDİRLERİ", "ASFALT SİLİNDİRİ"),
    (3, "LASTİKLİ ASFALT SİLİNDİRLERİ", "LASTİKLİ ASFALT SİLİNDİRİ"),
    (2, "TOPRAK SİLİNDİRLERİ", "TOPRAK SİLİNDİRİ"),
    (3, "YAMA SİLİNDİRLERİ", "YAMA SİLİNDİRİ"),
    (1, "KAZICI ve YÜKLEYİCİLER", "KAZICI ve YÜKLEYİCİ"),
    (2, "SU TANKERLERİ", "SU TANKERİ"),
    (2, "YAKIT ARAÇLARI", "YAKIT ARACI"),
    (2, "KANTARLAR", "KANTAR"),
    (2, "SERVİS ARAÇLARI", "SERVİS ARACI"),
    (4, "BİNEK ARAÇLAR", "BİNEK ARAÇ"),
]

SEKTORLER = [
    "⚗️ Petrokimya ve Rafineriler", "🛢️ Petrol ve Gaz Boru Hatları", "🌊 Barajlar ve Sulama Projeleri",
    "🏭 Demir Çelik Fabrikaları", "🚢 Gemi İnşaa ve Petrol Rafinerileri", "🧪 Kimyasal Tesis Projeleri",
    "🏗️ Çimento Fabrikaları", "🍞 Gıda Üretim Tesisleri", "📦 Kağıt, Karton ve Ambalaj Tesisleri",
    "⚡ HES ve Termik Santraller", "⚓ Tersane, Liman ve Deniz Yapıları", "🔌 Elektrik İletim ve Trafo Merkezleri",
    "💧 Atıksu Arıtma Tesisleri", "🛣️ Karayolları ve Demiryolları", "⛏️ Maden Üretim Tesisleri",
    "🌉 Tünel, Köprü ve Viyadükler", "🏢 Bina ve Üstyapı İşleri", "♻️ Atık Yakma ve Geri Dönüşüm",
]


# ============================================================
# 6. SOL NAVİGASYON
# ============================================================
with st.sidebar:
    st.markdown("<div style='text-align: center; padding: 10px 0;'><span style='font-size: 40px;'>👑</span></div>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center; font-family: Cinzel; color: #d4af37; letter-spacing: 2px; margin-top: -10px;'>TESKON</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 10px; color: #6b7280; letter-spacing: 2px; text-transform: uppercase;'>Sovereign Executive Suite</p>", unsafe_allow_html=True)
    st.divider()

    sayfa = st.radio(
        "KONTROL MERKEZİ",
        [
            "👑  Imperial Executive Suite",
            "🏛️  Kurumsal & Tarihçe",
            "💎  Zenith Data Intelligence",
            "📜  İş Bitirme Sicili",
            "🌐  Sektörler",
            "🚜  Apex Filo",
            "📞  Privé İletişim",
        ]
    )

    st.divider()
    st.markdown("""
    <div style='background: rgba(212, 175, 55, 0.05); border: 1px solid rgba(212, 175, 55, 0.2); border-radius: 12px; padding: 15px; text-align: center;'>
        <p style='font-size: 11px; color: #d4af37; font-weight: bold; margin: 0;'>SİSTEM DURUMU</p>
        <p style='font-size: 10px; color: #10b981; margin: 5px 0 0 0;'>🟢 Veri Tabanı Aktif</p>
    </div>

    <div style='text-align: center; margin-top: 22px;'>
        <p style='font-size: 8px; color: #6b7280; letter-spacing: 3px; text-transform: uppercase; margin: 0;'>ARCHITECTED & ENGINEERED BY</p>
        <p style='font-size: 12px; font-family: "Cinzel", serif; color: #d4af37; font-weight: 900; letter-spacing: 3px; margin-top: 4px; text-shadow: 0 0 10px rgba(212, 175, 55, 0.3);'>ÖNDER & ATLAS</p>
    </div>

    <div class="sidebar-seal">
        <div class="icon">👑</div>
        <div class="txt"><b>Sovereign Seal</b><br>TESKON © 2026</div>
    </div>
    """, unsafe_allow_html=True)


# ============================================================
# 7. ÜST DURUM ŞERİDİ
# ============================================================
now_str = datetime.now().strftime("%d.%m.%Y  •  %H:%M")
sayfa_temiz = sayfa.split("  ", 1)[1] if "  " in sayfa else sayfa
st.markdown(f"""
<div class="status-strip fade-in">
    <div><span class="pulse-dot"></span>{sayfa_temiz.upper()} <span class="dim">/ Black Edition v2</span></div>
    <div class="dim">{now_str}</div>
</div>
""", unsafe_allow_html=True)


# ============================================================
# 8. SAYFA 1 — IMPERIAL EXECUTIVE SUITE (KUTLAMA)
# ============================================================
if sayfa == "👑  Imperial Executive Suite":
    st.markdown("""
    <div class="balloon-container">
        <div class="gold-balloon b1"></div>
        <div class="gold-balloon b2"></div>
        <div class="gold-balloon b3"></div>
        <div class="gold-balloon b4"></div>
        <div class="gold-balloon b5"></div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="imperial-banner fade-in">
        <div style="font-size: 28px; margin-bottom: 10px;">🎆 🎇 👑 ✨ 🎇 🎆</div>
        <div class="imperial-badge">✨ Sovereign Signature Edition ✨</div>
        <div class="imperial-title">NİCE MUTLU VE SAĞLIKLI YAŞLARA, ALİ BEY</div>
        <div class="gold-divider"></div>
        <div class="imperial-sub">
            25 yıllık köklü geçmişimiz, sarsılmaz finansal gücümüz ve vizyoner liderliğinizle inşa edilen bu dev
            imparatorlukta;<br>
            <b>Yeni yaşınızın sağlık, huzur, sonsuz başarı ve yeni zirveler getirmesini dileriz.</b>
        </div>
    </div>
    """, unsafe_allow_html=True)

    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.markdown('<div class="diamond-card fade-in delay-1"><div class="diamond-icon">⏳</div><div class="diamond-value">25 YIL</div><div class="diamond-label">Köklü Miras</div></div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="diamond-card fade-in delay-2"><div class="diamond-icon">🌍</div><div class="diamond-value">18+</div><div class="diamond-label">Global Sektör</div></div>', unsafe_allow_html=True)
    with c3:
        st.markdown('<div class="diamond-card fade-in delay-3"><div class="diamond-icon">🚛</div><div class="diamond-value">55+</div><div class="diamond-label">Apex Ağır Filo</div></div>', unsafe_allow_html=True)
    with c4:
        st.markdown('<div class="diamond-card fade-in delay-4"><div class="diamond-icon">📍</div><div class="diamond-value">YENİKENT</div><div class="diamond-label">Entegre Veri Seti</div></div>', unsafe_allow_html=True)


# ============================================================
# 9. SAYFA 2 — KURUMSAL & TARİHÇE
# ============================================================
elif sayfa == "🏛️  Kurumsal & Tarihçe":
    st.markdown("<div class='section-title fade-in'>🏛️ Kurumsal & Tarihçe</div>", unsafe_allow_html=True)
    st.markdown("""
    <div class="imperial-sub" style="text-align:left; max-width:100%; margin-bottom:26px;">
        Zorlu müteahhitlik faaliyetlerinin öncü kuruluşlarından biri olan TESKON Mühendislik'in temelleri 2005 yılında
        atılmıştır. Türkiye, Ortadoğu, Kuzey Afrika, Kafkasya, Orta Asya, Doğu ve Orta Avrupa'da büyük başarılara imza
        atan <b>uluslararası bir yüklenici</b> olarak; ağır inşaat işlerinden rafineri ve petrokimya tesislerine,
        uydu kentlerden büyük endüstriyel tesislere kadar geniş bir yelpazede hizmet vermektedir.
    </div>
    """, unsafe_allow_html=True)

    s1, s2, s3, s4 = st.columns(4)
    with s1:
        st.markdown('<div class="diamond-card fade-in delay-1"><div class="diamond-icon">🌍</div><div class="diamond-value">22</div><div class="diamond-label">Ülke</div></div>', unsafe_allow_html=True)
    with s2:
        st.markdown('<div class="diamond-card fade-in delay-2"><div class="diamond-icon">👥</div><div class="diamond-value">255</div><div class="diamond-label">Personel</div></div>', unsafe_allow_html=True)
    with s3:
        st.markdown('<div class="diamond-card fade-in delay-3"><div class="diamond-icon">📁</div><div class="diamond-value">160</div><div class="diamond-label">Proje</div></div>', unsafe_allow_html=True)
    with s4:
        st.markdown('<div class="diamond-card fade-in delay-4"><div class="diamond-icon">🚛</div><div class="diamond-value">67</div><div class="diamond-label">Araç</div></div>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    m1, m2, m3 = st.columns(3)
    with m1:
        st.markdown("""<div class="mission-card"><h4>KÖKLÜ BİR TARİH</h4>
        <p>25 yıla dayanan tecrübe, sağlam finansal güç, ticari ahlak ve en önemlisi insana verdiğimiz değerler.</p></div>""", unsafe_allow_html=True)
    with m2:
        st.markdown("""<div class="mission-card"><h4>BİZE DUYULAN GÜVENLE</h4>
        <p>Yaptığımız her işte, sunduğumuz her hizmette insanlık için değer yaratmanın sorumluluğunu taşıyoruz.</p></div>""", unsafe_allow_html=True)
    with m3:
        st.markdown("""<div class="mission-card"><h4>HER GÜN AZMİMİZİN, KARARLILIĞIMIZIN ÜRÜNÜ</h4>
        <p>Eserlere milyonlarca insan tanıklık ediyor. Başarı; akıllı ve planlı bir çalışmanın sonucudur.</p></div>""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    col_a, col_b = st.columns([1.3, 1])
    with col_a:
        st.markdown("<h4 style='color:#d4af37; font-family:Cinzel; font-size:16px; letter-spacing:1px;'>FİRMA KÜNYESİ</h4>", unsafe_allow_html=True)
        render_info_card([
            ("Firma Ünvanı", "Teskon Mühendislik LTD. ŞTİ."),
            ("Kurucu", "Ali ALTIBAĞ"),
            ("Kuruluş Yılı", "2005"),
            ("Kuruluş Yeri", "İstanbul"),
            ("Vergi Dairesi", "Kozyatağı"),
            ("Vergi Numarası", "6080977255"),
            ("Web Adresi", "www.teskonproje.com.tr"),
            ("e-Posta", "teskon@teskonproje.com.tr"),
        ])
    with col_b:
        st.markdown("<h4 style='color:#d4af37; font-family:Cinzel; font-size:16px; letter-spacing:1px;'>SERTİFİKALAR</h4>", unsafe_allow_html=True)
        st.markdown("""
        <span class="cert-badge">ISO 9001:2015</span>
        <span class="cert-badge">ISO 14001:2015</span>
        <span class="cert-badge">OHSAS 18001:2007</span>
        <span class="cert-badge">ISO 27001:2013</span>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    with st.expander("🗂️ Organizasyon Yapısını Görüntüle"):
        st.markdown("""
- **Genel Müdür / General Manager**
    - Asistan / Assistant
    - **Genel Müdür Yardımcısı (Teknik)**
        - Satın Alma Yönetimi
        - Teklif Hazırlama Yönetimi
        - **Projeler Koordinatörü**
            - **Proje Şantiye Müdürü** → Asistan
                - Mühendis ve Proje → Mühendis → Tasarımcı → Tekniker
                - Hakediş Yönetimi → Mühendis → Tekniker
                - İnşaat - Çelik → Mühendis → Formen → Usta
                - Borulama → Mühendis → Formen → Usta
                - Elektrik → Mühendis → Formen → Usta
                - Enstrüman ve Otomasyon → Mühendis → Formen → Usta
        - Bilgi İşlem Yönetimi
        - İş Geliştirme Yönetimi
        """)


# ============================================================
# 10. SAYFA 3 — ZENITH DATA INTELLIGENCE (YENİKENT FİLTRELEME)
# ============================================================
elif sayfa == "💎  Zenith Data Intelligence":
    st.markdown("<div class='section-title fade-in'>💎 Zenith Yenikent Akıllı Filtreleme & Sorgulama Engine</div>", unsafe_allow_html=True)

    if isinstance(df, pd.DataFrame):
        st.success(f"🟢 **Sistem Hazır:** `{filename}` yüklendi (Toplam **{len(df):,}** kayıt)")

        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("### 🎛️ Gelişmiş VIP Arama & Filtreleme Paneli")

        f_col1, f_col2, f_col3, f_col4 = st.columns(4)
        with f_col1:
            mahalle_listesi = ["Tümü"] + sorted([str(x) for x in df['MahalleKoyAdi'].dropna().unique()]) if 'MahalleKoyAdi' in df.columns else ["Tümü"]
            sel_mahalle = st.selectbox("🏙️ Mahalle / Köy", mahalle_listesi)
        with f_col2:
            sel_ada = st.text_input("📍 Ada No", placeholder="Örn: 101")
        with f_col3:
            sel_parsel = st.text_input("📐 Parsel No", placeholder="Örn: 835")
        with f_col4:
            sel_adi = st.text_input("👤 Adı / Unvan", placeholder="Örn: MALİYE")

        f_col5, f_col6, f_col7, f_col8 = st.columns(4)
        with f_col5:
            sel_soyadi = st.text_input("👤 Soyadı", placeholder="Soyadı...")
        with f_col6:
            sel_tc = st.text_input("🆔 TC / Vergi No", placeholder="TC Kimlik No...")
        with f_col7:
            sirala_sutun = st.selectbox("📊 Sıralama Ölçütü", ["Yüzölçümü (m²)", "Ada No", "Parsel No", "ID / Kayıt Sırası"])
        with f_col8:
            sirala_yon = st.radio("🔄 Sıralama Yönü", ["Büyükten Küçüğe ⬇️", "Küçükten Büyüğe ⬆️"], horizontal=True)

        genel_arama = st.text_input("🔍 Serbest Genel Arama:", placeholder="Adres, Mevkii vb...")

        filtered_df = df.copy()

        if sel_mahalle != "Tümü":
            filtered_df = filtered_df[filtered_df['MahalleKoyAdi'].astype(str) == sel_mahalle]
        if sel_ada.strip():
            filtered_df = filtered_df[filtered_df['Ada'].astype(str).str.contains(sel_ada.strip(), case=False, na=False)]
        if sel_parsel.strip():
            filtered_df = filtered_df[filtered_df['Parsel'].astype(str).str.contains(sel_parsel.strip(), case=False, na=False)]
        if sel_adi.strip():
            filtered_df = filtered_df[filtered_df['Adi'].astype(str).str.contains(sel_adi.strip(), case=False, na=False)]
        if sel_soyadi.strip():
            filtered_df = filtered_df[filtered_df['Soyadi'].astype(str).str.contains(sel_soyadi.strip(), case=False, na=False)]
        if sel_tc.strip():
            filtered_df = filtered_df[filtered_df['TCKimlikNo'].astype(str).str.contains(sel_tc.strip(), case=False, na=False)]
        if genel_arama.strip():
            mask = filtered_df.astype(str).apply(lambda row: row.str.contains(genel_arama.strip(), case=False, na=False)).any(axis=1)
            filtered_df = filtered_df[mask]

        ascending = True if "Küçükten Büyüğe" in sirala_yon else False
        if sirala_sutun == "Yüzölçümü (m²)" and 'Yuzolcum_Sayısal' in filtered_df.columns:
            filtered_df = filtered_df.sort_values(by='Yuzolcum_Sayısal', ascending=ascending)
        elif sirala_sutun == "Ada No" and 'Ada' in filtered_df.columns:
            filtered_df = filtered_df.sort_values(by='Ada', ascending=ascending)
        elif sirala_sutun == "Parsel No" and 'Parsel' in filtered_df.columns:
            filtered_df = filtered_df.sort_values(by='Parsel', ascending=ascending)
        elif sirala_sutun == "ID / Kayıt Sırası" and 'ID' in filtered_df.columns:
            filtered_df = filtered_df.sort_values(by='ID', ascending=ascending)

        display_cols = [c for c in filtered_df.columns if not c.endswith('_Sayısal')]

        st.divider()
        st.markdown(f"<h4 style='color: #10b981;'>🎯 Bulunan Kayıt Sayısı: {len(filtered_df):,} / {len(df):,}</h4>", unsafe_allow_html=True)
        st.dataframe(filtered_df[display_cols], use_container_width=True, height=550)

        csv_data = filtered_df[display_cols].to_csv(index=False, encoding='utf-8-sig').encode('utf-8-sig')
        st.download_button("📥 Sonuçları İndir (Excel/CSV)", csv_data, "Yenikent_Filtreli.csv", "text/csv")
    else:
        st.error("⚠️ Klasörde ODS veya XLSX formatında veri dosyası bulunamadı! Lütfen verinizi klasöre yükleyin.")
        if filename is None and df is not None:
            st.caption(f"Teknik hata detayı: {df}")


# ============================================================
# 11. SAYFA 4 — İŞ BİTİRME SİCİLİ
# ============================================================
elif sayfa == "📜  İş Bitirme Sicili":
    st.markdown("<div class='section-title fade-in'>📜 İş Bitirme Belgeleri Sicili</div>", unsafe_allow_html=True)
    st.markdown("<div class='section-sub'>25 yıllık faaliyet süresince tamamlanan işlere ait iş bitirme belgesi kayıtları.</div>", unsafe_allow_html=True)

    is_df = pd.DataFrame(IS_BITIRME_KAYITLARI, columns=["Grup Kodu", "İş Grubu", "Yurtiçi / Yurtdışı", "Tutar"])

    g_col1, g_col2 = st.columns([1, 1])
    with g_col1:
        grup_listesi = ["Tümü"] + sorted(is_df["İş Grubu"].unique().tolist())
        sel_grup = st.selectbox("🏗️ İş Grubuna Göre Filtrele", grup_listesi)
    with g_col2:
        yer_listesi = ["Tümü"] + sorted(is_df["Yurtiçi / Yurtdışı"].unique().tolist())
        sel_yer = st.selectbox("🌍 Yurtiçi / Yurtdışı", yer_listesi)

    filtered_is_df = is_df.copy()
    if sel_grup != "Tümü":
        filtered_is_df = filtered_is_df[filtered_is_df["İş Grubu"] == sel_grup]
    if sel_yer != "Tümü":
        filtered_is_df = filtered_is_df[filtered_is_df["Yurtiçi / Yurtdışı"] == sel_yer]

    st.markdown(f"<h4 style='color:#10b981;'>Toplam {len(filtered_is_df)} kayıt gösteriliyor</h4>", unsafe_allow_html=True)
    st.dataframe(filtered_is_df, use_container_width=True, height=560, hide_index=True)


# ============================================================
# 12. SAYFA 5 — SEKTÖRLER
# ============================================================
elif sayfa == "🌐  Sektörler":
    st.markdown("<div class='section-title fade-in'>🌐 Faaliyet Gösterdiğimiz Sektörler</div>", unsafe_allow_html=True)
    st.markdown("<div class='section-sub'>Ağır sanayiden enerjiye, alt yapıdan çevre tesislerine kadar geniş bir hizmet yelpazesi.</div>", unsafe_allow_html=True)
    render_chips(SEKTORLER)


# ============================================================
# 13. SAYFA 6 — APEX FİLO
# ============================================================
elif sayfa == "🚜  Apex Filo":
    st.markdown("<div class='section-title fade-in'>🚜 Apex Ağır Ekipman & Araç Filosu</div>", unsafe_allow_html=True)

    filo_df = pd.DataFrame(ARAC_PARKI, columns=["Adet", "Ekipman Grubu", "Ekipman Tipi"])
    toplam_adet = filo_df["Adet"].sum()

    fc1, fc2 = st.columns(2)
    with fc1:
        st.markdown(f'<div class="diamond-card fade-in delay-1"><div class="diamond-icon">🚛</div><div class="diamond-value">{toplam_adet}</div><div class="diamond-label">Toplam Ekipman</div></div>', unsafe_allow_html=True)
    with fc2:
        st.markdown(f'<div class="diamond-card fade-in delay-2"><div class="diamond-icon">🗂️</div><div class="diamond-value">{len(filo_df)}</div><div class="diamond-label">Ekipman Kategorisi</div></div>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.dataframe(filo_df, use_container_width=True, height=650, hide_index=True)


# ============================================================
# 14. SAYFA 7 — PRİVÉ İLETİŞİM
# ============================================================
elif sayfa == "📞  Privé İletişim":
    st.markdown("<div class='section-title fade-in'>📞 Privé İletişim</div>", unsafe_allow_html=True)

    st.markdown("""
    <div class="contact-card"><span class="ic">🏢</span>
        <div><div class="label">Merkez Ofis</div>
        <div class="val">Varyap Meridian Grand Tower, A Blok, Kat: 11, Daire: 112 Ataşehir / İstanbul</div></div>
    </div>
    <div class="contact-card"><span class="ic">🌐</span>
        <div><div class="label">Web Adresi</div><div class="val">www.teskonproje.com.tr</div></div>
    </div>
    <div class="contact-card"><span class="ic">✉️</span>
        <div><div class="label">e-Posta</div><div class="val">teskon@teskonproje.com.tr</div></div>
    </div>
    """, unsafe_allow_html=True)


# ============================================================
# 15. ORTAK FOOTER
# ============================================================
st.markdown("<br><hr style='border: 0; height: 1px; background: rgba(212,175,55,0.3);'><br>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 11px; color: #6b7280;'>© 2026 TESKON Mühendislik • Architected & Developed by ÖNDER & ATLAS</p>", unsafe_allow_html=True)