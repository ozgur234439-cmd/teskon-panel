import streamlit as st
import pandas as pd
import os
from datetime import datetime

# ============================================================
# 1. VIP SAYFA YAPILANDIRMASI  (Sidebar YOK!)
# ============================================================
st.set_page_config(
    page_title="TESKON | Sovereign Executive Suite",
    page_icon="👑",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ============================================================
# 2. BLACK EDITION & IMPERIAL TASARIM SİSTEMİ
# ============================================================
st.markdown("""
<style>
    /* Streamlit chrome (menü, footer, toolbar) tamamen gizle */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    div[data-testid="stStatusWidget"] {display: none !important;}
    div[data-testid="stToolbar"] {display: none !important;}
    button[title="View app in Streamlit Community Cloud"] {display: none !important;}
    div[data-testid="stDecoration"] {display: none !important;}

    /* Header tamamen gizle - sidebar olmadığı için gerek yok */
    header[data-testid="stHeader"] {
        background: transparent !important;
        box-shadow: none !important;
        height: 0 !important;
        min-height: 0 !important;
        display: none !important;
    }
    .stAppHeader { display: none !important; }

    /* Sidebar'ı tamamen kaldır */
    section[data-testid="stSidebar"] { display: none !important; }
    button[data-testid="collapsedControl"] { display: none !important; }
    [data-testid="stSidebarCollapsedControl"] { display: none !important; }

    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@500;700;900&family=Cormorant+Garamond:ital,wght@0,400;0,600;1,500&family=Plus+Jakarta+Sans:wght@300;400;500;600;700&display=swap');

    /* ===== GLOBAL ===== */
    .stApp {
        background: radial-gradient(circle at 50% -20%, #1a160d 0%, #08090a 60%, #030405 100%);
        color: #e5e7eb;
        font-family: 'Plus Jakarta Sans', sans-serif;
    }
    .main .block-container {
        padding-top: 2rem !important;
        padding-bottom: 2rem !important;
        max-width: 1400px !important;
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

    /* ===== BALONLAR ===== */
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

    /* ===== HERO HEADER (Sayfa Ortası) ===== */
    .hero-header {
        text-align: center;
        padding: 30px 20px 10px 20px;
        margin-bottom: 10px;
        position: relative;
        z-index: 10;
    }
    .hero-crown {
        font-size: 52px;
        margin-bottom: 8px;
        filter: drop-shadow(0 0 20px rgba(212, 175, 55, 0.6));
        animation: crownFloat 4s ease-in-out infinite;
    }
    @keyframes crownFloat {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-6px); }
    }
    .hero-title {
        font-family: 'Cinzel', serif;
        font-size: 42px;
        font-weight: 900;
        letter-spacing: 8px;
        background: linear-gradient(180deg, #ffffff 0%, #dfb76c 60%, #d4af37 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-shadow: 0 8px 24px rgba(212, 175, 55, 0.3);
        margin-bottom: 6px;
    }
    .hero-sub {
        font-family: 'Cormorant Garamond', serif;
        font-style: italic;
        font-size: 16px;
        color: #9ca3af;
        letter-spacing: 4px;
        text-transform: uppercase;
        margin-bottom: 18px;
    }
    .hero-nav-label {
        display: inline-block;
        font-family: 'Cinzel', serif;
        font-size: 11px;
        letter-spacing: 6px;
        color: #d4af37;
        text-transform: uppercase;
        padding: 8px 24px;
        border-top: 1px solid rgba(212, 175, 55, 0.4);
        border-bottom: 1px solid rgba(212, 175, 55, 0.4);
        margin-bottom: 20px;
    }

    /* ===== YATAY NAVİGASYON (RADIO) ===== */
    div[data-testid="stRadio"] > label { display: none !important; }
    div[data-testid="stRadio"] div[role="radiogroup"] {
        display: flex !important;
        flex-wrap: wrap !important;
        justify-content: center !important;
        gap: 10px !important;
        margin-bottom: 20px !important;
    }
    div[data-testid="stRadio"] div[role="radiogroup"] label {
        background: rgba(18, 21, 28, 0.7) !important;
        border: 1px solid rgba(212, 175, 55, 0.3) !important;
        border-radius: 12px !important;
        padding: 10px 20px !important;
        margin: 0 !important;
        cursor: pointer !important;
        transition: all 0.3s ease !important;
        font-family: 'Plus Jakarta Sans', sans-serif !important;
        font-size: 13px !important;
        color: #d1d5db !important;
        letter-spacing: 0.3px !important;
    }
    div[data-testid="stRadio"] div[role="radiogroup"] label:hover {
        border-color: rgba(212, 175, 55, 0.85) !important;
        background: rgba(212, 175, 55, 0.1) !important;
        transform: translateY(-2px);
        box-shadow: 0 8px 20px rgba(212, 175, 55, 0.2);
    }
    div[data-testid="stRadio"] div[role="radiogroup"] label:has(input:checked) {
        background: linear-gradient(135deg, #bf953f 0%, #fcf6ba 40%, #b38728 100%) !important;
        border-color: #fcf6ba !important;
        color: #000 !important;
        box-shadow: 0 8px 24px rgba(212, 175, 55, 0.45);
        transform: translateY(-2px);
    }
    div[data-testid="stRadio"] div[role="radiogroup"] label:has(input:checked) p,
    div[data-testid="stRadio"] div[role="radiogroup"] label:has(input:checked) div {
        color: #000 !important;
        font-weight: 700 !important;
    }
    /* Radio içindeki yuvarlak daireyi gizle */
    div[data-testid="stRadio"] div[role="radiogroup"] label > div:first-child {
        display: none !important;
    }
    div[data-testid="stRadio"] div[role="radiogroup"] input[type="radio"] {
        display: none !important;
    }
    /* Radio label içindeki metin paragraph */
    div[data-testid="stRadio"] div[role="radiogroup"] label p {
        color: #d1d5db !important;
        font-size: 13px !important;
        margin: 0 !important;
        white-space: nowrap !important;
    }

    /* ===== STATUS STRIP (Ortada) ===== */
    .status-strip {
        display: flex; justify-content: center; align-items: center; gap: 22px;
        background: rgba(212, 175, 55, 0.06);
        border: 1px solid rgba(212, 175, 55, 0.18);
        border-radius: 14px; padding: 12px 26px;
        margin: 0 auto 26px auto;
        letter-spacing: 1.5px; font-size: 11.5px; color: #d4af37;
        text-transform: uppercase; backdrop-filter: blur(12px);
        max-width: 700px;
        font-family: 'Plus Jakarta Sans', sans-serif;
    }
    .status-strip .dim { color: #8b8f98; }
    .pulse-dot {
        display: inline-block; width: 7px; height: 7px; border-radius: 50%;
        background: #10b981; margin-right: 8px;
        box-shadow: 0 0 8px 2px rgba(16, 185, 129, 0.7);
        animation: pulseDot 1.8s infinite;
        vertical-align: middle;
    }
    @keyframes pulseDot { 0%, 100% { opacity: 1; } 50% { opacity: 0.35; } }
    .status-sep { color: rgba(212, 175, 55, 0.4); }

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
        text-align: center;
    }
    .section-sub { color: #9ca3af; font-size: 13px; margin-top: -14px; margin-bottom: 18px; line-height: 1.7; text-align: center; }

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

    .chip-grid { display: flex; flex-wrap: wrap; gap: 10px; justify-content: center; }
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
    .contact-card .val { font-size: 14.5px; color: #f0f2f4; font-weight: 500; line-height: 1.55; }

    .slogan-card {
        background: linear-gradient(135deg, rgba(212,175,55,0.09), rgba(212,175,55,0.02));
        border: 1px solid rgba(212,175,55,0.3);
        border-radius: 16px; padding: 22px 20px; text-align: center; height: 100%;
        transition: transform 0.3s ease, border-color 0.3s ease;
    }
    .slogan-card:hover { transform: translateY(-5px); border-color: rgba(212,175,55,0.7); }
    .slogan-icon { font-size: 26px; margin-bottom: 10px; }
    .slogan-title {
        font-family: 'Cinzel', serif; color: #f3e3b3; font-size: 13.5px;
        font-weight: 700; letter-spacing: 2px; text-transform: uppercase; margin-bottom: 10px;
    }
    .slogan-text {
        font-family: 'Cormorant Garamond', serif; font-style: italic;
        color: #c3c8d1; font-size: 14.5px; line-height: 1.7;
    }

    .country-grid { display: flex; flex-wrap: wrap; gap: 8px; margin-top: 6px; justify-content: center; }
    .country-chip {
        background: rgba(212,175,55,0.05);
        border: 1px solid rgba(212,175,55,0.25);
        border-radius: 8px; padding: 7px 14px; font-size: 12px; color: #d1d5db;
        letter-spacing: 0.5px;
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

    div[data-testid="stDataFrame"] {
        border: 1px solid rgba(212, 175, 55, 0.2);
        border-radius: 14px; overflow: hidden;
    }

    /* ===== SOVEREIGN FOOTER SEAL ===== */
    .sovereign-footer {
        max-width: 560px;
        margin: 30px auto 0 auto;
        padding: 30px 28px 24px 28px;
        text-align: center;
        border-radius: 20px;
        background: linear-gradient(160deg, rgba(35, 28, 15, 0.55) 0%, rgba(10, 10, 10, 0.6) 100%);
        border: 1px solid rgba(212, 175, 55, 0.35);
        box-shadow: 0 0 45px rgba(212, 175, 55, 0.12), 0 15px 40px rgba(0,0,0,0.5);
    }
    .sovereign-seal {
        width: 70px; height: 70px;
        margin: 0 auto 14px auto;
        border-radius: 50%;
        border: 2px solid rgba(212, 175, 55, 0.75);
        display: flex; align-items: center; justify-content: center;
        font-size: 30px;
        background: radial-gradient(circle, rgba(212,175,55,0.22), transparent 70%);
        box-shadow: 0 0 30px rgba(212, 175, 55, 0.4), inset 0 0 15px rgba(212,175,55,0.15);
        animation: sealGlow 3.2s ease-in-out infinite;
    }
    @keyframes sealGlow {
        0%, 100% { box-shadow: 0 0 30px rgba(212, 175, 55, 0.4), inset 0 0 15px rgba(212,175,55,0.15); }
        50% { box-shadow: 0 0 48px rgba(212, 175, 55, 0.65), inset 0 0 20px rgba(212,175,55,0.25); }
    }
    .sovereign-footer-badge {
        font-family: 'Cinzel', serif;
        font-size: 12px;
        font-weight: 900;
        letter-spacing: 4px;
        text-transform: uppercase;
        background: linear-gradient(90deg, #bf953f, #fcf6ba, #b38728, #fbf5b7);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 10px;
    }
    .sovereign-footer-text {
        font-size: 12px;
        color: #cbd0d6;
        letter-spacing: 0.6px;
        line-height: 1.7;
    }
    .sovereign-footer-text b {
        color: #f3e3b3;
        font-family: 'Cinzel', serif;
        letter-spacing: 1.5px;
    }
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
# 4. VERİ YÜKLEYİCİ
# ============================================================
@st.cache_data
def load_ods_data():
    current_dir = os.path.dirname(os.path.abspath(__file__)) if '__file__' in globals() else os.getcwd()
    for file in os.listdir(current_dir):
        if file.endswith('.ods') or file.endswith('.xlsx'):
            try:
                file_path = os.path.join(current_dir, file)
                df = pd.read_excel(file_path, engine='odf' if file.endswith('.ods') else None)

                # TÜM OBJECT SÜTUNLARI STRING'E ÇEVİR
                for col in df.columns:
                    if df[col].dtype == 'object':
                        df[col] = df[col].fillna("").astype(str)
                        df[col] = df[col].replace({"nan": "", "None": "", "NaN": ""})

                if 'Yuzolcum' in df.columns:
                    df['Yuzolcum_Sayısal'] = pd.to_numeric(
                        df['Yuzolcum'].astype(str).str.replace(',', '.'),
                        errors='coerce'
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

CALISILAN_ULKELER = [
    "🇩🇪 Almanya", "🇪🇸 İspanya", "🇸🇪 İsveç", "🇳🇴 Norveç", "🇷🇺 Rusya",
    "🇰🇿 Kazakistan", "🇺🇿 Özbekistan", "🇹🇯 Tacikistan", "🇶🇦 Katar", "🇰🇼 Kuveyt",
    "🇱🇾 Libya", "🇮🇶 Irak", "🇦🇫 Afganistan", "🇬🇪 Gürcistan", "🇧🇬 Bulgaristan",
    "🇲🇦 Fas", "🇩🇿 Cezayir", "🇫🇮 Finlandiya", "🇬🇷 Yunanistan", "🌍 Diğer Ülkeler",
]

PERSONEL_DETAY = [
    ("Proje Müdürü", 10),
    ("Mühendis", 22),
    ("Tasarım Uzmanı", 21),
    ("İş Güvenliği Uzmanı", 7),
    ("Formen", 24),
    ("Kaynakçı & Usta", 49),
]

FAALIYET_ALANLARI = [
    "📐 Proje ve Tasarım",
    "⚙️ Mühendislik ve İmalat",
    "🏗️ Yapım ve Bakım",
    "🔑 Anahtar Teslim Projeler",
    "👷 Personel Temini",
    "🛠️ İşgücü Temini",
]

SLOGANLAR = [
    ("🏛️", "Köklü Bir Tarih", "25 yıla dayanan tecrübe, sağlam finansal güç, ticari ahlak ve insana verilen değer."),
    ("🤝", "Bize Duyulan Güvenle", "Yaptığımız her işte insanlık için değer yaratmanın sorumluluğunu taşıyoruz."),
    ("⚡", "Her Gün Azmimizin Ürünü", "Eserlere milyonlarca insan tanıklık ediyor. Başarı; akıllı ve planlı çalışmanın sonucudur."),
    ("🎯", "Başarı Asla Tesadüf Değildir", "Planlı çalışma, disiplinli yönetim ve vizyoner liderlikle inşa edilir."),
    ("✨", "Mükemmeli Sunmak", "Her projede en yüksek kaliteyi ve mühendislik standartlarını hedefliyoruz."),
]


# ============================================================
# 6. HERO HEADER + YATAY NAVİGASYON (Sayfa Ortası)
# ============================================================
st.markdown("""
<div class="hero-header fade-in">
    <div class="hero-crown">👑</div>
    <div class="hero-title">TESKON</div>
    <div class="hero-sub">Sovereign Executive Suite</div>
    <div class="hero-nav-label">✦ KONTROL MERKEZİ ✦</div>
</div>
""", unsafe_allow_html=True)

sayfa = st.radio(
    "nav",
    [
        "👑  Imperial Executive Suite",
        "🏛️  Kurumsal & Tarihçe",
        "💎  Zenith Data Intelligence",
        "📜  İş Bitirme Sicili",
        "🌐  Sektörler",
        "🚜  Apex Filo",
        "📞  Privé İletişim",
    ],
    horizontal=True,
    label_visibility="collapsed",
    key="main_nav"
)

# ============================================================
# 7. ORTA DURUM ŞERİDİ
# ============================================================
now_str = datetime.now().strftime("%d.%m.%Y  •  %H:%M")
st.markdown(f"""
<div class="status-strip fade-in">
    <div><span class="pulse-dot"></span>SİSTEM AKTİF</div>
    <div class="status-sep">•</div>
    <div class="dim">{now_str}</div>
    <div class="status-sep">•</div>
    <div class="dim">Black Edition v3</div>
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
        st.markdown('<div class="diamond-card fade-in delay-2"><div class="diamond-icon">🌍</div><div class="diamond-value">22</div><div class="diamond-label">Ülkede Faaliyet</div></div>', unsafe_allow_html=True)
    with c3:
        st.markdown('<div class="diamond-card fade-in delay-3"><div class="diamond-icon">🚛</div><div class="diamond-value">67</div><div class="diamond-label">Araç / İş Makinesi</div></div>', unsafe_allow_html=True)
    with c4:
        st.markdown('<div class="diamond-card fade-in delay-4"><div class="diamond-icon">📁</div><div class="diamond-value">160+</div><div class="diamond-label">Tamamlanan Proje</div></div>', unsafe_allow_html=True)

    st.markdown("<br><h3 style='font-family: Cinzel; color: #d4af37; letter-spacing: 1px; font-size: 20px; text-align:center;'>KURUMSAL DEĞERLERİMİZ</h3>", unsafe_allow_html=True)
    slog_cols = st.columns(5)
    for i, (icon, title, text) in enumerate(SLOGANLAR):
        with slog_cols[i % 5]:
            st.markdown(f"""
            <div class="slogan-card fade-in delay-{i+1}">
                <div class="slogan-icon">{icon}</div>
                <div class="slogan-title">{title}</div>
                <div class="slogan-text">{text}</div>
            </div>
            """, unsafe_allow_html=True)


# ============================================================
# 9. SAYFA 2 — KURUMSAL & TARİHÇE
# ============================================================
elif sayfa == "🏛️  Kurumsal & Tarihçe":
    st.markdown("<div class='section-title fade-in'>🏛️ Kurumsal & Tarihçe</div>", unsafe_allow_html=True)
    st.markdown("""
    <div class="imperial-sub" style="text-align:center; max-width:900px; margin:0 auto 26px auto;">
        Zorlu müteahhitlik faaliyetlerinin öncü kuruluşlarından biri olan TESKON Mühendislik'in temelleri 2005 yılında
        <b>Ali ALTIBAĞ</b> tarafından atılmıştır. Türkiye, Ortadoğu, Kuzey Afrika, Kafkasya, Orta Asya, Doğu ve Orta
        Avrupa'da büyük başarılara imza atan <b>uluslararası bir yüklenici</b> olarak; ağır inşaat işlerinden rafineri
        ve petrokimya tesislerine, uydu kentlerden büyük endüstriyel tesislere kadar geniş bir yelpazede hizmet vermektedir.
    </div>
    """, unsafe_allow_html=True)

    s1, s2, s3, s4 = st.columns(4)
    with s1:
        st.markdown('<div class="diamond-card fade-in delay-1"><div class="diamond-icon">🌍</div><div class="diamond-value">22</div><div class="diamond-label">Ülke</div></div>', unsafe_allow_html=True)
    with s2:
        st.markdown('<div class="diamond-card fade-in delay-2"><div class="diamond-icon">👥</div><div class="diamond-value">255</div><div class="diamond-label">Personel</div></div>', unsafe_allow_html=True)
    with s3:
        st.markdown('<div class="diamond-card fade-in delay-3"><div class="diamond-icon">📁</div><div class="diamond-value">160+</div><div class="diamond-label">Proje</div></div>', unsafe_allow_html=True)
    with s4:
        st.markdown('<div class="diamond-card fade-in delay-4"><div class="diamond-icon">🚛</div><div class="diamond-value">67</div><div class="diamond-label">Araç</div></div>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<h4 style='color:#d4af37; font-family:Cinzel; font-size:16px; letter-spacing:1px; text-align:center;'>ANA FAALİYET ALANLARI</h4>", unsafe_allow_html=True)
    render_chips(FAALIYET_ALANLARI)

    st.markdown("<br>", unsafe_allow_html=True)
    m1, m2, m3 = st.columns(3)
    with m1:
        st.markdown("""<div class="mission-card"><h4>KÖKLÜ BİR TARİH</h4>
        <p>25 yıla dayanan tecrübe, sağlam finansal güç, ticari ahlak ve en önemlisi insana verdiğimiz değerler.</p></div>""", unsafe_allow_html=True)
    with m2:
        st.markdown("""<div class="mission-card"><h4>BİZE DUYULAN GÜVENLE</h4>
        <p>Yaptığımız her işte, sunduğumuz her hizmette insanlık için değer yaratmanın sorumluluğunu taşıyoruz.</p></div>""", unsafe_allow_html=True)
    with m3:
        st.markdown("""<div class="mission-card"><h4>BAŞARI ASLA TESADÜF DEĞİLDİR</h4>
        <p>Eserlere milyonlarca insan tanıklık ediyor. Başarı; akıllı ve planlı bir çalışmanın sonucudur.</p></div>""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    col_a, col_b = st.columns([1.3, 1])
    with col_a:
        st.markdown("<h4 style='color:#d4af37; font-family:Cinzel; font-size:16px; letter-spacing:1px;'>FİRMA KÜNYESİ</h4>", unsafe_allow_html=True)
        render_info_card([
            ("Firma Ünvanı", "TESKON Mühendislik Ltd. Şti."),
            ("Kurucu", "Ali ALTIBAĞ"),
            ("Genel Müdür", "Ali ALTIBAĞ"),
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
    st.markdown("<h4 style='color:#d4af37; font-family:Cinzel; font-size:16px; letter-spacing:1px; text-align:center;'>İNSAN KAYNAĞI — ÖNE ÇIKAN TEKNİK KADRO</h4>", unsafe_allow_html=True)
    p_cols = st.columns(len(PERSONEL_DETAY))
    for i, (rol, adet) in enumerate(PERSONEL_DETAY):
        with p_cols[i]:
            st.markdown(f"""
            <div class="diamond-card fade-in delay-{i+1}" style="padding: 20px 12px;">
                <div class="diamond-value" style="font-size: 26px;">{adet}</div>
                <div class="diamond-label" style="font-size: 10px; line-height:1.4;">{rol}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<h4 style='color:#d4af37; font-family:Cinzel; font-size:16px; letter-spacing:1px; text-align:center;'>FAALİYET GÖSTERDİĞİMİZ ÜLKELER</h4>", unsafe_allow_html=True)
    st.markdown(
        "<div class='country-grid'>" +
        "".join([f"<span class='country-chip'>{u}</span>" for u in CALISILAN_ULKELER]) +
        "</div>",
        unsafe_allow_html=True
    )

    st.markdown("<br>", unsafe_allow_html=True)
    with st.expander("🗂️ Organizasyon Yapısını Görüntüle"):
        st.markdown("""
- **Genel Müdür / General Manager — Ali ALTIBAĞ**
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
# 10. SAYFA 3 — ZENITH DATA INTELLIGENCE
# ============================================================
elif sayfa == "💎  Zenith Data Intelligence":
    st.markdown("<div class='section-title fade-in'>💎 Zenith Akıllı Filtreleme & Sorgulama Engine</div>", unsafe_allow_html=True)

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
        st.markdown(f"<h4 style='color: #10b981; text-align:center;'>🎯 Bulunan Kayıt Sayısı: {len(filtered_df):,} / {len(df):,}</h4>", unsafe_allow_html=True)
        st.dataframe(filtered_df[display_cols], width='stretch', height=550)

        csv_data = filtered_df[display_cols].to_csv(index=False, encoding='utf-8-sig').encode('utf-8-sig')
        st.download_button("📥 Sonuçları İndir (Excel/CSV)", csv_data, "Filtreli_Sonuclar.csv", "text/csv")
    else:
        st.error("⚠️ Klasörde ODS veya XLSX dosyası bulunamadı! Lütfen verinizi klasöre atın.")


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

    st.markdown(f"<h4 style='color:#10b981; text-align:center;'>Toplam {len(filtered_is_df)} kayıt gösteriliyor</h4>", unsafe_allow_html=True)
    st.dataframe(filtered_is_df, width='stretch', height=560, hide_index=True)


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
    st.dataframe(filo_df, width='stretch', height=650, hide_index=True)


# ============================================================
# 14. SAYFA 7 — PRİVÉ İLETİŞİM
# ============================================================
elif sayfa == "📞  Privé İletişim":
    st.markdown("<div class='section-title fade-in'>📞 Privé İletişim</div>", unsafe_allow_html=True)

    st.markdown("""
    <div class="contact-card"><span class="ic">🏢</span>
        <div><div class="label">İstanbul Merkez Ofis</div>
        <div class="val">Barbaros Mahallesi, Al Zambak Sokak, Varyap Meridian Grand Tower<br>
        A Blok, Kat: 11, Daire: 112 — Ataşehir / İstanbul / Türkiye</div></div>
    </div>

    <div class="contact-card"><span class="ic">🏛️</span>
        <div><div class="label">Ankara Ofis</div>
        <div class="val">Cadde, Kat: 7, No: 25 — Çukurambar<br>
        Çankaya / Ankara / Türkiye</div></div>
    </div>

    <div class="contact-card"><span class="ic">📞</span>
        <div><div class="label">İstanbul Telefon</div>
        <div class="val">+90 216 629 49 53</div></div>
    </div>

    <div class="contact-card"><span class="ic">📱</span>
        <div><div class="label">Mobil</div>
        <div class="val">+90 534 790 08 26</div></div>
    </div>

    <div class="contact-card"><span class="ic">☎️</span>
        <div><div class="label">Ankara Telefon</div>
        <div class="val">+90 312 284 34 84</div></div>
    </div>

    <div class="contact-card"><span class="ic">🌐</span>
        <div><div class="label">Web Adresi</div><div class="val">www.teskonproje.com.tr</div></div>
    </div>

    <div class="contact-card"><span class="ic">✉️</span>
        <div><div class="label">e-Posta</div><div class="val">teskon@teskonproje.com.tr</div></div>
    </div>
    """, unsafe_allow_html=True)


# ============================================================
# 15. SOVEREIGN FOOTER SEAL (Ortada)
# ============================================================
st.markdown("""
<div class="sovereign-footer">
    <div class="sovereign-seal">👑</div>
    <div class="sovereign-footer-badge">Sovereign Seal of TESKON</div>
    <div class="sovereign-footer-text">
        ARCHITECTED &amp; ENGINEERED BY<br>
        <b>ÖNDER &amp; ATLAS</b><br>
        <span style="font-size: 10px; color: #6b7280; margin-top: 8px; display: inline-block;">
            © 2026 TESKON Mühendislik Ltd. Şti.
        </span>
    </div>
</div>
""", unsafe_allow_html=True)