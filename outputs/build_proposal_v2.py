"""
Jones Excavating Co. × Callus Fabrication — Full-Stack Digital Proposal v2
Expanded from build_proposal.py: adds SEO, Local Search, Social Media, and updated
pricing to cover the complete digital engagement.
"""

from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    PageBreak, HRFlowable, KeepTogether, Image
)
from reportlab.lib.utils import ImageReader
import os
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT
from reportlab.lib.colors import HexColor

# ── COLORS ─────────────────────────────────────────────────────────────────────
# Jones (parent brand)
BLACK    = HexColor('#0C0E10')
CHARCOAL = HexColor('#161A1D')
ORANGE   = HexColor('#E8621A')
WHITE    = HexColor('#FFFFFF')
OFF_WHITE= HexColor('#F4F2EE')
GRAY_100 = HexColor('#F0EFEB')
GRAY_300 = HexColor('#D1CFC9')
GRAY_500 = HexColor('#8A8880')
GRAY_700 = HexColor('#4A4845')
AMBER    = HexColor('#E8A21A')

# Callus (sister brand — Hands & Fire direction)
INK      = HexColor('#1A1815')
GUNMETAL = HexColor('#2E2A26')
RUST     = HexColor('#B64A24')
RUST_DK  = HexColor('#8F3A1B')
BRASS    = HexColor('#C9A66B')
CREAM    = HexColor('#EFE7D6')
OLIVE    = HexColor('#5C5A42')

# Digital / SEO accent
TEAL     = HexColor('#2E7D8C')
TEAL_LT  = HexColor('#3D9BAD')
TEAL_BG  = HexColor('#1A3840')

W, H = letter  # 8.5 × 11 in
CONTENT_W = 6.5 * inch   # usable width (margins 0.75" each side)

OUTPUT = "/Users/tylertoone/Desktop/Claude Work/inbox/excavating-site/outputs/jones_callus_proposal_v2.pdf"

# ── LOGO PATHS ─────────────────────────────────────────────────────────────────
BASE = "/Users/tylertoone/Desktop/Claude Work/inbox/excavating-site"
JONES_LOGO   = os.path.join(BASE, "jones-assets/jones-logo-orange.png")
CALLUS_KIN   = os.path.join(BASE, "callus-logo-concepts/callus-logo-kintsugi.png")
CALLUS_SPARK = os.path.join(BASE, "callus-logo-concepts/callus-logo-spark.png")

# ── PARAGRAPH STYLES ───────────────────────────────────────────────────────────
def S(name, **kw):
    return ParagraphStyle(name, **kw)

cover_label   = S('CL',  fontName='Helvetica-Bold', fontSize=9,  textColor=ORANGE,   leading=14, spaceBefore=24)
cover_sub     = S('CS',  fontName='Helvetica',      fontSize=16, textColor=GRAY_300, leading=24, spaceAfter=6)

chapter_num   = S('CN',  fontName='Helvetica-Bold', fontSize=9,  textColor=ORANGE,   leading=14, spaceAfter=6)
chapter_title = S('CT',  fontName='Helvetica-Bold', fontSize=34, textColor=BLACK,    leading=38, spaceAfter=20)

h2  = S('H2', fontName='Helvetica-Bold', fontSize=18, textColor=BLACK,   leading=24, spaceBefore=28, spaceAfter=10)
h3  = S('H3', fontName='Helvetica-Bold', fontSize=13, textColor=ORANGE,  leading=18, spaceBefore=18, spaceAfter=6)
h3_callus = S('H3C', fontName='Helvetica-Bold', fontSize=13, textColor=RUST, leading=18, spaceBefore=18, spaceAfter=6)
h3_teal   = S('H3T', fontName='Helvetica-Bold', fontSize=13, textColor=TEAL, leading=18, spaceBefore=18, spaceAfter=6)

body = S('Bd', fontName='Helvetica', fontSize=10, textColor=GRAY_700, leading=17, spaceAfter=10)

bullet_s = S('Bu', fontName='Helvetica', fontSize=10, textColor=GRAY_700, leading=17, spaceAfter=6,  leftIndent=14)
# Sub-bullet for nested content (URLs, examples)
sub_bullet_s = S('SBu', fontName='Helvetica', fontSize=9, textColor=GRAY_500, leading=15, spaceAfter=4, leftIndent=28)
# URL / code style
url_s = S('URL', fontName='Helvetica-Oblique', fontSize=9, textColor=TEAL_LT, leading=15, spaceAfter=4, leftIndent=14)

label_s  = S('Lb', fontName='Helvetica-Bold', fontSize=8, textColor=ORANGE,  leading=12, spaceAfter=4)
label_callus = S('LbC', fontName='Helvetica-Bold', fontSize=8, textColor=RUST, leading=12, spaceAfter=4)
label_teal   = S('LbT', fontName='Helvetica-Bold', fontSize=8, textColor=TEAL, leading=12, spaceAfter=4)

toc_entry = S('TE', fontName='Helvetica',      fontSize=11, textColor=GRAY_700, leading=22)
toc_num   = S('TN', fontName='Helvetica-Bold', fontSize=11, textColor=ORANGE,   leading=22)

callout_title_s = S('CaT', fontName='Helvetica-Bold', fontSize=13, textColor=WHITE,    leading=18, spaceAfter=6)
callout_body_s  = S('CaB', fontName='Helvetica',      fontSize=10, textColor=GRAY_300, leading=16, spaceAfter=0)

tagline_s = S('TaG', fontName='Helvetica-BoldOblique', fontSize=14, textColor=WHITE, leading=20)
tagline_callus_s = S('TaGC', fontName='Helvetica-BoldOblique', fontSize=14, textColor=CREAM, leading=20)

stat_num_s = S('StN', fontName='Helvetica-Bold', fontSize=26, textColor=ORANGE,   leading=30, spaceAfter=2,  alignment=TA_CENTER)
stat_lbl_s = S('StL', fontName='Helvetica-Bold', fontSize=7,  textColor=GRAY_500, leading=11, spaceAfter=0, alignment=TA_CENTER)

# ── TABLE CELL STYLES ──────
c_hdr  = S('CH',  fontName='Helvetica-Bold',        fontSize=8,   textColor=WHITE,    leading=12, spaceAfter=0)
c_col1 = S('CC1', fontName='Helvetica-Bold',        fontSize=8.5, textColor=ORANGE,   leading=13, spaceAfter=0)
c_col1_callus = S('CC1R', fontName='Helvetica-Bold', fontSize=8.5, textColor=RUST,    leading=13, spaceAfter=0)
c_col1_teal   = S('CC1T', fontName='Helvetica-Bold', fontSize=8.5, textColor=TEAL,    leading=13, spaceAfter=0)
c_body = S('CB',  fontName='Helvetica',             fontSize=8.5, textColor=GRAY_700, leading=13, spaceAfter=0)
c_note = S('CNt', fontName='Helvetica-BoldOblique', fontSize=8.5, textColor=GRAY_500, leading=13, spaceAfter=0)
c_pri  = S('CPr', fontName='Helvetica-Bold',        fontSize=8.5, textColor=ORANGE,   leading=13, spaceAfter=0)
c_wht  = S('CWh', fontName='Helvetica',             fontSize=8.5, textColor=WHITE,    leading=13, spaceAfter=0)
c_url  = S('CUrl',fontName='Helvetica-Oblique',     fontSize=8,   textColor=TEAL_LT,  leading=12, spaceAfter=0)

# price-row
pr_item_s  = S('PRI',  fontName='Helvetica-Bold', fontSize=11, textColor=BLACK,   leading=15, spaceAfter=0)
pr_item_hl = S('PRIHL',fontName='Helvetica-Bold', fontSize=11, textColor=WHITE,   leading=15, spaceAfter=0)
pr_note_s  = S('PRN',  fontName='Helvetica',      fontSize=9,  textColor=GRAY_500,leading=13, spaceAfter=0)
pr_note_hl = S('PRNHL',fontName='Helvetica',      fontSize=9,  textColor=GRAY_300,leading=13, spaceAfter=0)
pr_price_s = S('PRP',  fontName='Helvetica-Bold', fontSize=15, textColor=ORANGE,  leading=19, spaceAfter=0, alignment=TA_RIGHT)
pr_price_hl= S('PRPHL',fontName='Helvetica-Bold', fontSize=15, textColor=WHITE,   leading=19, spaceAfter=0, alignment=TA_RIGHT)
pr_price_teal = S('PRPTeal', fontName='Helvetica-Bold', fontSize=15, textColor=TEAL_LT, leading=19, spaceAfter=0, alignment=TA_RIGHT)

closing_s  = S('CLO', fontName='Helvetica-Bold', fontSize=26, textColor=BLACK, leading=30, spaceAfter=16)

# ── HELPERS ────────────────────────────────────────────────────────────────────
def P(text, style=c_body):
    return Paragraph(str(text), style)

def spacer(h=12):
    return Spacer(1, h)

def hr(color=GRAY_300, thickness=0.5, width='100%', spaceB=8, spaceA=8):
    return HRFlowable(width=width, thickness=thickness, color=color,
                      spaceAfter=spaceA, spaceBefore=spaceB)

def inline_label(text, callus=False, teal=False):
    if teal:
        return Paragraph(text.upper(), label_teal)
    return Paragraph(text.upper(), label_callus if callus else label_s)

def bullet(text):
    return Paragraph(f'<b>\u2022</b>  {text}', bullet_s)

def sub_bullet(text):
    return Paragraph(f'\u2013  {text}', sub_bullet_s)

def url_line(text):
    return Paragraph(text, url_s)

# ── COMPONENT BUILDERS ─────────────────────────────────────────────────────────
def section_divider(num, title, accent=ORANGE):
    num_str = f'0{num}' if num < 10 else str(num)
    num_style = S(f'CN{accent.hexval()}', fontName='Helvetica-Bold', fontSize=9,
                  textColor=accent, leading=14, spaceAfter=6)
    data = [[P(num_str, num_style), P(title.upper(), chapter_title)]]
    t = Table(data, colWidths=[0.55*inch, 5.95*inch])
    t.setStyle(TableStyle([
        ('VALIGN',        (0,0),(-1,-1),'BOTTOM'),
        ('TOPPADDING',    (0,0),(-1,-1),0),
        ('BOTTOMPADDING', (0,0),(-1,-1),0),
        ('LEFTPADDING',   (0,0),(0,0),10),
        ('RIGHTPADDING',  (0,0),(-1,-1),0),
        ('LINEBEFORE',    (0,0),(0,-1),3, accent),
    ]))
    return t

def callout_box(title, body_text, bg=CHARCOAL, accent=ORANGE):
    PAD = 20
    inner_w = CONTENT_W - 4
    inner = Table([
        [P(title, callout_title_s)],
        [P(body_text, callout_body_s)],
    ], colWidths=[inner_w - PAD*2])
    inner.setStyle(TableStyle([
        ('BACKGROUND',    (0,0),(-1,-1), bg),
        ('TOPPADDING',    (0,0),(-1,-1), PAD),
        ('BOTTOMPADDING', (0,0),(-1,-1), PAD),
        ('LEFTPADDING',   (0,0),(-1,-1), PAD),
        ('RIGHTPADDING',  (0,0),(-1,-1), PAD),
    ]))
    wrapper = Table([[inner]], colWidths=[inner_w])
    wrapper.setStyle(TableStyle([
        ('LEFTPADDING',   (0,0),(-1,-1),0),
        ('RIGHTPADDING',  (0,0),(-1,-1),0),
        ('TOPPADDING',    (0,0),(-1,-1),0),
        ('BOTTOMPADDING', (0,0),(-1,-1),14),
        ('LINEBEFORE',    (0,0),(-1,-1),4, accent),
    ]))
    return wrapper

def two_col(left_items, right_items):
    col_w = (CONTENT_W - 0.3*inch) / 2

    def col_table(items):
        rows = [[item] for item in items]
        t = Table(rows, colWidths=[col_w])
        t.setStyle(TableStyle([
            ('TOPPADDING',    (0,0),(-1,-1),2),
            ('BOTTOMPADDING', (0,0),(-1,-1),2),
            ('LEFTPADDING',   (0,0),(-1,-1),0),
            ('RIGHTPADDING',  (0,0),(-1,-1),0),
        ]))
        return t

    lt = col_table(left_items)
    rt = col_table(right_items)
    outer = Table([[lt, Spacer(0.3*inch, 1), rt]],
                  colWidths=[col_w, 0.3*inch, col_w])
    outer.setStyle(TableStyle([
        ('VALIGN',        (0,0),(-1,-1),'TOP'),
        ('TOPPADDING',    (0,0),(-1,-1),0),
        ('BOTTOMPADDING', (0,0),(-1,-1),0),
        ('LEFTPADDING',   (0,0),(-1,-1),0),
        ('RIGHTPADDING',  (0,0),(-1,-1),0),
    ]))
    return outer

def brand_intro_block(name, positioning, tagline, accent=ORANGE, bg=CHARCOAL):
    """Big branded intro panel used at the top of each brand track."""
    name_s = S(f'BN{accent.hexval()}', fontName='Helvetica-Bold', fontSize=34,
               textColor=WHITE, leading=38, spaceAfter=4)
    pos_s = S(f'BP{accent.hexval()}', fontName='Helvetica', fontSize=10,
              textColor=GRAY_300, leading=16, spaceAfter=12)
    tag_s = S(f'BT{accent.hexval()}', fontName='Helvetica-BoldOblique', fontSize=18,
              textColor=accent, leading=22, spaceAfter=0)
    lbl_s = S(f'BL{accent.hexval()}', fontName='Helvetica-Bold', fontSize=8,
              textColor=accent, leading=12, spaceAfter=4)

    inner = Table([
        [P('BRAND', lbl_s)],
        [P(name, name_s)],
        [P(positioning, pos_s)],
        [P(f'"{tagline}"', tag_s)],
    ], colWidths=[CONTENT_W - 48])
    inner.setStyle(TableStyle([
        ('BACKGROUND',    (0,0),(-1,-1), bg),
        ('TOPPADDING',    (0,0),(-1,-1), 6),
        ('BOTTOMPADDING', (0,0),(-1,-1), 6),
        ('LEFTPADDING',   (0,0),(-1,-1), 24),
        ('RIGHTPADDING',  (0,0),(-1,-1), 24),
    ]))
    wrapper = Table([[inner]], colWidths=[CONTENT_W])
    wrapper.setStyle(TableStyle([
        ('BACKGROUND',    (0,0),(-1,-1), bg),
        ('LEFTPADDING',   (0,0),(-1,-1), 0),
        ('RIGHTPADDING',  (0,0),(-1,-1), 0),
        ('TOPPADDING',    (0,0),(-1,-1), 24),
        ('BOTTOMPADDING', (0,0),(-1,-1), 24),
        ('LINEBEFORE',    (0,0),(-1,-1), 6, accent),
    ]))
    return wrapper

def color_swatch(hex_color, label, name):
    """Small color swatch card for palette rows."""
    txt_on_swatch = WHITE if hex_color not in (CREAM, BRASS, AMBER, GRAY_100, OFF_WHITE, WHITE) else INK
    hx_style = S(f'HX{hex_color.hexval()}', fontName='Helvetica-Bold',
                 fontSize=7, textColor=txt_on_swatch, leading=10, alignment=TA_CENTER)
    nm_style = S(f'NM{hex_color.hexval()}', fontName='Helvetica-Bold',
                 fontSize=8, textColor=INK, leading=10, alignment=TA_CENTER)
    lb_style = S(f'LB{hex_color.hexval()}', fontName='Helvetica',
                 fontSize=7, textColor=GRAY_500, leading=9, alignment=TA_CENTER)

    swatch = Table([[P(name.upper(), hx_style)]], colWidths=[0.95*inch])
    swatch.setStyle(TableStyle([
        ('BACKGROUND',    (0,0),(-1,-1), hex_color),
        ('TOPPADDING',    (0,0),(-1,-1), 28),
        ('BOTTOMPADDING', (0,0),(-1,-1), 28),
    ]))
    combined = Table([
        [swatch],
        [P(label, nm_style)],
        [P(hex_color.hexval().upper(), lb_style)],
    ], colWidths=[0.95*inch])
    combined.setStyle(TableStyle([
        ('TOPPADDING',    (0,0),(-1,-1), 2),
        ('BOTTOMPADDING', (0,0),(-1,-1), 2),
        ('LEFTPADDING',   (0,0),(-1,-1), 0),
        ('RIGHTPADDING',  (0,0),(-1,-1), 0),
    ]))
    return combined

def palette_row(colors):
    """colors = [(hex_color, 'Name', 'role'), ...] — max 6"""
    cells = []
    for hex_c, label, name in colors:
        cells.append(color_swatch(hex_c, label, name))
        cells.append(Spacer(0.08*inch, 1))
    cells = cells[:-1]
    widths = []
    for i in range(len(cells)):
        widths.append(0.95*inch if i % 2 == 0 else 0.08*inch)
    t = Table([cells], colWidths=widths)
    t.setStyle(TableStyle([
        ('VALIGN',        (0,0),(-1,-1),'TOP'),
        ('TOPPADDING',    (0,0),(-1,-1),0),
        ('BOTTOMPADDING', (0,0),(-1,-1),0),
        ('LEFTPADDING',   (0,0),(-1,-1),0),
        ('RIGHTPADDING',  (0,0),(-1,-1),0),
    ]))
    return t

def phase_row(phase, title, duration, tasks, is_dark=False, accent=ORANGE):
    bg = CHARCOAL if is_dark else GRAY_100
    ph_s  = S(f'ph{accent.hexval()}',  fontName='Helvetica-Bold', fontSize=9,  textColor=accent, leading=13)
    ti_s  = S(f'ti{accent.hexval()}{is_dark}', fontName='Helvetica-Bold', fontSize=12,
              textColor=WHITE if is_dark else BLACK, leading=16)
    du_s  = S(f'du{is_dark}',  fontName='Helvetica-Bold', fontSize=8,
              textColor=GRAY_300 if is_dark else GRAY_500, leading=12)
    ta_s  = S(f'ta{is_dark}',  fontName='Helvetica',      fontSize=9,
              textColor=GRAY_300 if is_dark else GRAY_700, leading=15)
    task_html = '<br/>'.join([f'\u2022 {t}' for t in tasks])
    data = [[P(phase, ph_s), P(title, ti_s), P(duration.upper(), du_s), P(task_html, ta_s)]]
    t = Table(data, colWidths=[0.5*inch, 1.7*inch, 0.95*inch, 3.35*inch])
    t.setStyle(TableStyle([
        ('BACKGROUND',    (0,0),(-1,-1), bg),
        ('TOPPADDING',    (0,0),(-1,-1),14),
        ('BOTTOMPADDING', (0,0),(-1,-1),14),
        ('LEFTPADDING',   (0,0),(-1,-1),12),
        ('RIGHTPADDING',  (0,0),(-1,-1),12),
        ('VALIGN',        (0,0),(-1,-1),'TOP'),
        ('LINEBEFORE',    (0,0),(0,-1),3, accent),
    ]))
    return t

def price_row(item, price, note='', highlight=False, accent=ORANGE, teal=False):
    if teal:
        bg = TEAL_BG
        price_style = pr_price_teal
        item_style  = S('PRIT', fontName='Helvetica-Bold', fontSize=11, textColor=TEAL_LT, leading=15, spaceAfter=0)
        note_style  = S('PRNT', fontName='Helvetica',      fontSize=9,  textColor=GRAY_500, leading=13, spaceAfter=0)
    elif highlight:
        bg = accent
        price_style = pr_price_hl
        item_style  = pr_item_hl
        note_style  = pr_note_hl
    else:
        bg = GRAY_100
        price_style = S(f'prp{accent.hexval()}', fontName='Helvetica-Bold',
                        fontSize=15, textColor=accent, leading=19, spaceAfter=0, alignment=TA_RIGHT)
        item_style  = pr_item_s
        note_style  = pr_note_s

    data = [[
        P(item,  item_style),
        P(note,  note_style),
        P(price, price_style),
    ]]
    t = Table(data, colWidths=[2.2*inch, 2.6*inch, 1.7*inch])
    t.setStyle(TableStyle([
        ('BACKGROUND',    (0,0),(-1,-1), bg),
        ('TOPPADDING',    (0,0),(-1,-1),13),
        ('BOTTOMPADDING', (0,0),(-1,-1),13),
        ('LEFTPADDING',   (0,0),(-1,-1),14),
        ('RIGHTPADDING',  (0,0),(-1,-1),14),
        ('VALIGN',        (0,0),(-1,-1),'MIDDLE'),
    ]))
    return t

def data_table_style(n_data_rows):
    return TableStyle([
        ('BACKGROUND',    (0,0),(-1,0), CHARCOAL),
        ('TOPPADDING',    (0,0),(-1,-1),10),
        ('BOTTOMPADDING', (0,0),(-1,-1),10),
        ('LEFTPADDING',   (0,0),(-1,-1),10),
        ('RIGHTPADDING',  (0,0),(-1,-1),10),
        ('VALIGN',        (0,0),(-1,-1),'TOP'),
        ('ROWBACKGROUNDS',(0,1),(-1,-1),[WHITE, GRAY_100]),
        ('LINEBELOW',     (0,0),(-1,-1),0.5, GRAY_300),
    ])

def keyword_table(jones_kws, callus_kws):
    """Two-column keyword comparison table: Jones keywords | Callus keywords."""
    col_w = (CONTENT_W - 0.2*inch) / 2
    # Header row
    rows = [
        [P('JONES EXCAVATING — KEYWORDS', c_hdr), P('CALLUS FABRICATION — KEYWORDS', c_hdr)]
    ]
    # Zip keyword lists, padding with empty if unequal length
    max_len = max(len(jones_kws), len(callus_kws))
    for i in range(max_len):
        jk = jones_kws[i] if i < len(jones_kws) else ''
        ck = callus_kws[i] if i < len(callus_kws) else ''
        rows.append([P(jk, c_url if jk else c_body), P(ck, c_url if ck else c_body)])
    t = Table(rows, colWidths=[col_w, col_w], repeatRows=1)
    ts = TableStyle([
        ('BACKGROUND',    (0,0),(-1,0), TEAL_BG),
        ('TOPPADDING',    (0,0),(-1,-1),8),
        ('BOTTOMPADDING', (0,0),(-1,-1),8),
        ('LEFTPADDING',   (0,0),(-1,-1),10),
        ('RIGHTPADDING',  (0,0),(-1,-1),10),
        ('VALIGN',        (0,0),(-1,-1),'TOP'),
        ('ROWBACKGROUNDS',(0,1),(-1,-1),[WHITE, GRAY_100]),
        ('LINEBELOW',     (0,0),(-1,-1),0.5, GRAY_300),
        ('LINEAFTER',     (0,0),(0,-1),0.5, GRAY_300),
    ])
    t.setStyle(ts)
    return t

# ── PAGE CANVAS ────────────────────────────────────────────────────────────────
class ProposalCanvas:
    def on_page(self, canvas, doc):
        page = doc.page
        canvas.saveState()
        if page == 1:
            # Cover page — dark with orange & rust dual accents
            canvas.setFillColor(BLACK)
            canvas.rect(0, 0, W, H, fill=1, stroke=0)
            # Left orange accent (Jones)
            canvas.setFillColor(ORANGE)
            canvas.rect(0, 0, 6, H, fill=1, stroke=0)
            # Right rust accent (Callus)
            canvas.setFillColor(RUST)
            canvas.rect(W-6, 0, 6, H, fill=1, stroke=0)
            # Grid
            canvas.setStrokeColor(HexColor('#1A1E22'))
            canvas.setLineWidth(0.5)
            for x in range(0, int(W)+1, 40):
                canvas.line(x, 0, x, H)
            for y in range(0, int(H)+1, 40):
                canvas.line(0, y, W, y)
            # Top: split orange/rust bar
            canvas.setFillColor(ORANGE)
            canvas.rect(0, 0, W/2, 5, fill=1, stroke=0)
            canvas.setFillColor(RUST)
            canvas.rect(W/2, 0, W/2, 5, fill=1, stroke=0)
            # Header stamp
            canvas.setFont('Helvetica-Bold', 7)
            canvas.setFillColor(GRAY_700)
            canvas.drawRightString(W-36, H-28, 'CONFIDENTIAL  |  JONES EXCAVATING × CALLUS FABRICATION')
            # Faint watermark: Jones logo on left, Callus kintsugi on right
            try:
                canvas.saveState()
                canvas.setFillAlpha(0.06)
                jw, jh = 5.2*inch, 2.2*inch
                canvas.drawImage(ImageReader(JONES_LOGO),
                                 -1.2*inch, H/2 - jh/2 + 0.4*inch,
                                 width=jw, height=jh, mask='auto',
                                 preserveAspectRatio=True)
                canvas.setFillAlpha(0.05)
                cw, ch = 3.0*inch, 3.0*inch
                canvas.drawImage(ImageReader(CALLUS_KIN),
                                 W - cw + 0.6*inch, H/2 - ch/2 - 0.2*inch,
                                 width=cw, height=ch, mask='auto',
                                 preserveAspectRatio=True)
                canvas.restoreState()
            except Exception:
                pass
        else:
            canvas.setFillColor(ORANGE)
            canvas.rect(0, H-4, W, 4, fill=1, stroke=0)
            canvas.setFillColor(CHARCOAL)
            canvas.rect(0, H-36, W, 32, fill=1, stroke=0)
            canvas.setFont('Helvetica-Bold', 8)
            canvas.setFillColor(WHITE)
            canvas.drawString(36, H-24, 'JONES × CALLUS')
            canvas.setFillColor(ORANGE)
            canvas.drawString(36+90, H-24, '|')
            canvas.setFillColor(GRAY_300)
            canvas.setFont('Helvetica', 8)
            canvas.drawString(36+100, H-24, 'Full-Stack Digital Proposal  ·  2026')
            canvas.setFont('Helvetica-Bold', 8)
            canvas.setFillColor(ORANGE)
            canvas.drawRightString(W-36, H-24, f'{page}')
            canvas.setFillColor(GRAY_100)
            canvas.rect(0, 0, W, 26, fill=1, stroke=0)
            canvas.setFont('Helvetica', 7)
            canvas.setFillColor(GRAY_500)
            canvas.drawString(36, 9, 'Confidential — prepared exclusively for Jones Excavating Co.  |  © 2026')
            canvas.drawRightString(W-36, 9, 'jonesexcavating.com  ·  callusfabrication.com')
        canvas.restoreState()

# ── DOCUMENT BUILD ─────────────────────────────────────────────────────────────
def build_pdf():
    doc = SimpleDocTemplate(
        OUTPUT, pagesize=letter,
        leftMargin=0.75*inch, rightMargin=0.75*inch,
        topMargin=0.75*inch,  bottomMargin=0.5*inch,
        title='Jones × Callus — Full-Stack Digital Proposal v2',
    )
    story = []
    canvas_cb = ProposalCanvas()

    # ═══ COVER ═══════════════════════════════════════════════════════
    story.append(spacer(1.1*inch))
    story.append(P('FULL-STACK DIGITAL PROPOSAL', cover_label))
    story.append(P('BRAND · WEB · SEO · DIGITAL', cover_label))
    story.append(spacer(16))
    cm = S('CTM', fontName='Helvetica-Bold', fontSize=48, textColor=WHITE,  leading=52, spaceAfter=0)
    ca = S('CTA', fontName='Helvetica-Bold', fontSize=48, textColor=ORANGE, leading=52, spaceAfter=0)
    cr = S('CTR', fontName='Helvetica-Bold', fontSize=48, textColor=RUST,   leading=52, spaceAfter=0)
    cam= S('CAM', fontName='Helvetica-BoldOblique', fontSize=28, textColor=GRAY_500, leading=32, spaceAfter=0)

    # Real logos side-by-side on the cover
    jones_img = Image(JONES_LOGO, width=2.6*inch, height=1.05*inch, kind='proportional')
    kin_img   = Image(CALLUS_KIN, width=1.3*inch, height=1.3*inch, kind='proportional')
    logo_row = Table(
        [[jones_img, '', kin_img]],
        colWidths=[3.0*inch, 0.4*inch, 1.5*inch],
    )
    logo_row.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('ALIGN',  (0,0), (0,0), 'LEFT'),
        ('ALIGN',  (2,0), (2,0), 'LEFT'),
        ('LEFTPADDING',   (0,0), (-1,-1), 0),
        ('RIGHTPADDING',  (0,0), (-1,-1), 0),
        ('TOPPADDING',    (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 0),
    ]))
    story += [logo_row, spacer(22)]

    story += [P('JONES EXCAVATING', ca), spacer(2),
              P('&amp;', cam), spacer(2),
              P('CALLUS FABRICATION', cr), spacer(28)]

    rule_l = Table([['']], colWidths=[1.5*inch])
    rule_l.setStyle(TableStyle([('LINEBELOW',(0,0),(-1,-1),2,ORANGE),('TOPPADDING',(0,0),(-1,-1),0),('BOTTOMPADDING',(0,0),(-1,-1),0)]))
    rule_r = Table([['']], colWidths=[1.5*inch])
    rule_r.setStyle(TableStyle([('LINEBELOW',(0,0),(-1,-1),2,RUST),('TOPPADDING',(0,0),(-1,-1),0),('BOTTOMPADDING',(0,0),(-1,-1),0)]))
    dual_rule = Table([[rule_l, Spacer(0.15*inch,1), rule_r]], colWidths=[1.5*inch, 0.15*inch, 1.5*inch])
    dual_rule.setStyle(TableStyle([('LEFTPADDING',(0,0),(-1,-1),0),('RIGHTPADDING',(0,0),(-1,-1),0)]))
    story += [dual_rule, spacer(28)]

    story.append(P('Paired Brand Refresh  ·  Sister-Company Identity Build  ·  Paired Marketing Sites  ·  SEO &amp; Local Search  ·  Social Media', cover_sub))
    story.append(spacer(48))
    ml = S('ml', fontName='Helvetica-Bold', fontSize=8,  textColor=GRAY_500, leading=12)
    mv = S('mv', fontName='Helvetica-Bold', fontSize=11, textColor=WHITE,    leading=16)
    meta = Table([
        [P('PREPARED FOR',ml), P('DATE',ml),         P('VERSION',ml)],
        [P('Jones Excavating Co.',mv), P('April 2026',mv), P('2.0 — Digital',mv)],
    ], colWidths=[2.5*inch, 2.2*inch, 1.8*inch])
    meta.setStyle(TableStyle([
        ('BACKGROUND',    (0,0),(-1,-1),HexColor('#1A1E22')),
        ('TOPPADDING',    (0,0),(-1,-1),14),('BOTTOMPADDING',(0,0),(-1,-1),14),
        ('LEFTPADDING',   (0,0),(-1,-1),18),('RIGHTPADDING',  (0,0),(-1,-1),18),
        ('LINEBEFORE',    (0,0),(0,-1),3,ORANGE),
        ('LINEAFTER',     (0,0),(0,-1),0.5,HexColor('#2A2E32')),
        ('LINEAFTER',     (1,0),(1,-1),0.5,HexColor('#2A2E32')),
        ('LINEAFTER',     (2,0),(2,-1),3,RUST),
        ('VALIGN',        (0,0),(-1,-1),'MIDDLE'),
    ]))
    story += [meta, PageBreak()]

    # ═══ TABLE OF CONTENTS ════════════════════════════════════════════
    story += [spacer(8), P('TABLE OF CONTENTS', label_s), spacer(4),
              hr(ORANGE, thickness=2, spaceB=0, spaceA=20)]
    toc_items = [
        ('01', 'Executive Summary',                         '03', ORANGE),
        ('02', 'Approach — Two Brands, One Project',        '04', ORANGE),
        ('03', 'Jones Excavating — Brand Refresh',          '05', ORANGE),
        ('04', 'Callus Fabrication — Brand Direction',      '07', RUST),
        ('05', 'Web Strategy',                              '09', ORANGE),
        ('06', 'SEO &amp; Local Search',                    '11', TEAL),
        ('07', 'Social Media &amp; Content',                '14', TEAL),
        ('08', 'Timeline &amp; Investment',                 '15', ORANGE),
        ('09', 'Next Steps',                                '17', ORANGE),
    ]
    pn_s = S('PN', fontName='Helvetica-Bold', fontSize=11, textColor=GRAY_500, alignment=TA_RIGHT, leading=22)
    for num, title, pg, accent in toc_items:
        dot = Table([['']], colWidths=[3.0*inch])
        dot.setStyle(TableStyle([('LINEBELOW',(0,0),(0,0),0.5,GRAY_300,0,(2,2)),('TOPPADDING',(0,0),(-1,-1),10),('BOTTOMPADDING',(0,0),(-1,-1),0)]))
        num_style = S(f'TN{accent.hexval()}', fontName='Helvetica-Bold', fontSize=11, textColor=accent, leading=22)
        row = Table([[P(num, num_style), P(title, toc_entry), dot, P(pg, pn_s)]],
                    colWidths=[0.45*inch, 2.95*inch, 2.65*inch, 0.45*inch])
        row.setStyle(TableStyle([
            ('VALIGN',        (0,0),(-1,-1),'BOTTOM'),
            ('TOPPADDING',    (0,0),(-1,-1),4),('BOTTOMPADDING',(0,0),(-1,-1),4),
            ('LEFTPADDING',   (0,0),(-1,-1),0),('RIGHTPADDING',  (0,0),(-1,-1),0),
            ('LINEBELOW',     (0,0),(-1,-1),0.5,GRAY_100),
        ]))
        story.append(row)
    story.append(PageBreak())

    # ═══ 01 EXECUTIVE SUMMARY ════════════════════════════════════════
    story += [section_divider(1,'Executive Summary'), spacer(16)]
    story.append(P(
        'Jones Excavating Co. has spent seven decades building a reputation for taking on the '
        'excavation work others won\'t touch — deep foundations, shoring, complex site drilling. '
        'Callus Fabrication, the sister company, brings the same hands-on standard to mobile welding '
        'and custom steel fabrication across the Wasatch Front. Both brands have real equity. Neither '
        'currently has a visual identity, web presence, or digital marketing strategy that reflects '
        'the quality of the work.',
        body))
    story.append(P(
        'This proposal covers the <b>full-stack digital engagement</b>: branding, web, SEO, local '
        'search, and social media — delivered as two parallel tracks, one for each company. The result '
        'is a pair of distinct brand systems, two marketing sites, a local SEO foundation for both, '
        'and a social content strategy that keeps each brand visible to the customers it actually '
        'serves.', body))
    story += [spacer(8), callout_box(
        'Two brands. Full-stack digital. One project.',
        'Jones keeps its heritage mark — sharpened and modernized. Callus gets a fresh identity of '
        'its own. Both get mobile-first websites, Google Business Profile optimization, local keyword '
        'strategy, citation building, and content direction. One coordinated engagement, built to '
        'generate real pipeline for both companies.'
    ), spacer(20), P('What This Proposal Covers', h2)]

    for ttl, desc in [
        ('Jones Brand Refresh',       'Wordmark refinement, palette system, typography, voice guide — rooted in 70-year equity.'),
        ('Callus Brand Identity',     'Full brand identity from scratch: logo, palette, typography, voice, and brand standards.'),
        ('Dual Marketing Sites',      'Two complete sites, launched together. Mobile-first, CMS-powered, PageSpeed 90+ target.'),
        ('SEO &amp; Local Search',    'Local SEO for both brands: GBP optimization, schema markup, keyword strategy, citation building, monthly reporting.'),
        ('Social Media &amp; Content','Platform strategy, content pillars, posting cadence, Google Business posts for both companies.'),
        ('Timeline &amp; Investment', 'Phased schedule with updated all-in pricing — brand, web, and digital — plus monthly SEO retainer options.'),
    ]:
        t = Table([[P(ttl, h3), P(desc, body)]], colWidths=[1.9*inch, 4.6*inch])
        t.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'TOP'),('TOPPADDING',(0,0),(-1,-1),4),('BOTTOMPADDING',(0,0),(-1,-1),4),('LEFTPADDING',(0,0),(-1,-1),0),('RIGHTPADDING',(0,0),(-1,-1),0)]))
        story.append(t)
    story.append(PageBreak())

    # ═══ 02 APPROACH ══════════════════════════════════════════════════
    story += [section_divider(2,'Approach — Two Brands, One Project'), spacer(16),
              P('The central question: <b>how separate should Jones and Callus feel?</b> We reviewed '
                'three directions — one merged brand, a parent/sibling visual system, and two '
                'independent identities. After weighing the customer overlap (low), market positioning '
                '(distinct), and future-flexibility (Callus may outgrow a sibling system), the '
                'recommendation is <b>distinct identities, coordinated project</b>. The same logic '
                'applies to SEO and social: two separate GBP listings, two distinct keyword targets, '
                'two separate social presences — but built in parallel with shared production '
                'efficiency.', body),
              spacer(10)]

    comp_rows = [
        [P('DIMENSION', c_hdr), P('JONES EXCAVATING', c_hdr), P('CALLUS FABRICATION', c_hdr)],
        [P('Market', c_col1),        P('Commercial GCs, public agencies, developers across UT/WY/ID', c_body), P('Commercial contractors on the Wasatch Front, public works', c_body)],
        [P('Trade', c_col1),         P('Excavation, deep foundations, shoring, drilling, site work', c_body), P('Mobile welding, custom fabrication, structural steel', c_body)],
        [P('History', c_col1),       P('70+ years. Known name. Heritage equity.', c_body), P('15+ years. Newer brand. Room to build identity.', c_body)],
        [P('Brand voice', c_col1),   P('Direct. Confident. Grounded.', c_body), P('Craftsman. Honest. Earned.', c_body)],
        [P('Visual feel', c_col1),   P('Industrial-modern. Dark. Orange accent.', c_body), P('Heritage-craftsman. Warm. Rust accent.', c_body)],
        [P('Typography', c_col1),    P('Barlow Condensed · Inter', c_body), P('Roboto Slab · Oswald · Inter', c_body)],
        [P('SEO focus', c_col1),     P('Local Utah/WY/ID; deep foundation, excavation terms', c_body), P('Wasatch Front; mobile welding, custom fab terms', c_body)],
        [P('Social platform', c_col1),P('Facebook primary — local GC network, community trust', c_body), P('Instagram primary — visual craft, project portfolio', c_body)],
    ]
    comp_t = Table(comp_rows, colWidths=[1.05*inch, 2.75*inch, 2.7*inch], repeatRows=1)
    comp_t.setStyle(data_table_style(8))
    story += [comp_t, spacer(18), callout_box(
        'Why not a sibling system?',
        'A shared visual language was considered and ruled out — it makes Callus feel like a Jones '
        'sub-line, which under-indexes Callus\' own customer base. Distinct brands give Callus room '
        'to grow its own reputation and its own search presence. A small shared cue — "proudly part '
        'of the Jones Excavating family" in the footer — signals the tie without subordinating the '
        'brand or competing for the same search terms.',
        bg=GUNMETAL, accent=RUST
    ), PageBreak()]

    # ═══ 03 JONES REFRESH ═════════════════════════════════════════════
    story += [section_divider(3,'Jones Excavating — Brand Refresh'), spacer(16)]
    story.append(brand_intro_block(
        'Jones Excavating Co.',
        'Commercial deep foundations and complex site work across Utah, Wyoming, and Idaho. Seven decades of heritage.',
        'Built for the Hard Jobs.',
        accent=ORANGE, bg=CHARCOAL
    ))
    story += [spacer(20), inline_label('Positioning')]
    story.append(callout_box(
        'The thesis',
        'The Jones logo has real regional equity — the blocky "JONES" wordmark, the inline stripes, '
        'the excavator-bucket J mark. We refine, not replace: tighten the geometry, preserve the '
        'inline typography, modernize the system around it. The tagline "Built for the Hard Jobs" '
        'captures what Jones already is — and gives sales, marketing, and recruiting one consistent '
        'line to rally around.',
    ))

    story += [spacer(16), inline_label('Color System'), spacer(8)]
    story.append(palette_row([
        (BLACK, 'Jet Black', 'Primary'),
        (CHARCOAL, 'Charcoal', 'Cards/UI'),
        (ORANGE, 'Signal Orange', 'Accent'),
        (AMBER, 'Amber', 'Highlight'),
        (OFF_WHITE, 'Off-White', 'Light bg'),
        (GRAY_500, 'Steel Gray', 'Body text'),
    ]))

    story += [spacer(18), inline_label('Typography')]
    story.append(two_col(
        [P('Headlines &amp; Display', h3),
         P('<b>Barlow Condensed</b> — weights 700–900.<br/>Industrial, condensed, confident. '
           'All section titles, hero copy, stats, wordmark.', body)],
        [P('Body &amp; UI', h3),
         P('<b>Inter</b> — weights 400–700.<br/>Modern, highly legible. Body copy, navigation, forms, proposals.', body)],
    ))

    story += [spacer(10), inline_label('Logo Direction')]
    for item in [
        'Preserve the excavator-bucket J mark — same geometry, cleaner edges',
        'Preserve the inline-stripe "JONES" typography — signature, recognizable, heritage',
        'Two approved concepts: <b>Monochrome refresh</b> (black/white, classic) and <b>Signal Orange</b> (orange stripes + contractor bar)',
        'Logo works at every scale: hard-hat stickers, equipment decals, signage, digital, proposal cover',
        'Delivered in SVG, PNG (multi-size), and print-ready PDF formats',
    ]:
        story.append(bullet(item))

    story += [spacer(12), inline_label('Voice')]
    voice_rows = [
        [P('TONE',c_hdr),       P('WHAT IT MEANS IN PRACTICE',c_hdr)],
        [P('Direct',c_col1),    P('No fluff. Say what you do and how well you do it. No corporate jargon.',c_body)],
        [P('Confident',c_col1), P('Speak from expertise. Don\'t hedge. "We handle the jobs others won\'t" — not "we try to..."',c_body)],
        [P('Grounded',c_col1),  P('Real language of the industry. Acknowledge the difficulty of the work — don\'t sanitize it.',c_body)],
    ]
    voice_t = Table(voice_rows, colWidths=[1.2*inch, 5.3*inch], repeatRows=1)
    voice_t.setStyle(data_table_style(3))
    story += [voice_t, spacer(14), inline_label('Website')]
    story.append(P(
        'Dark, industrial, orange-accented. Mobile-first (GC superintendents review subs on phones). '
        'Phone number in header on every page. Quote form on homepage. Real project photography with '
        'specs, stats, and ADSC recognition front and center. Target PageSpeed 90+ on mobile. '
        'A homepage prototype has been built and is available for review at '
        '<b>jonesexcavating.com</b> (staged).', body))
    story.append(PageBreak())

    # ═══ 04 CALLUS DIRECTION ══════════════════════════════════════════
    story += [section_divider(4,'Callus Fabrication — Brand Direction', accent=RUST), spacer(16)]
    story.append(brand_intro_block(
        'Callus Fabrication',
        'Mobile welding, custom fabrication, and structural steel for commercial contractors across the Wasatch Front.',
        "It's all in the name.",
        accent=RUST, bg=INK
    ))
    story += [spacer(20), inline_label('Positioning', callus=True)]
    story.append(callout_box(
        'The thesis — "Hands &amp; Fire"',
        '"Callus" is a gift of a name — hands hardened by work, the literal badge of the trade. '
        'Plus a ready-made CTA: Call us. The brand leans into both meanings. The system is warmer '
        'and more handmade than Jones: rust and gunmetal, slab serif typography, a shield mark built '
        'from a hammer and sparks. It\'s the opposite of a slick corporate rebrand — it reads as a '
        'working shop with decades of earned expertise.',
        bg=GUNMETAL, accent=RUST,
    ))

    story += [spacer(16), inline_label('Color System', callus=True), spacer(8)]
    story.append(palette_row([
        (INK, 'Ink', 'Primary'),
        (GUNMETAL, 'Gunmetal', 'Cards/UI'),
        (RUST, 'Rust', 'Accent'),
        (BRASS, 'Brass', 'Highlight'),
        (CREAM, 'Cream', 'Light bg'),
        (OLIVE, 'Olive', 'Body text'),
    ]))

    story += [spacer(18), inline_label('Typography', callus=True)]
    story.append(two_col(
        [P('Headlines &amp; Display', h3_callus),
         P('<b>Roboto Slab</b> — weights 600–700, italic for emphasis.<br/>Heritage, handmade, solid. '
           'Headlines, wordmark, shop signage.', body)],
        [P('Accents &amp; UI', h3_callus),
         P('<b>Oswald</b> (labels, captions) &amp; <b>Inter</b> (body).<br/>'
           'Oswald gives industrial signage feel; Inter keeps forms &amp; paragraphs readable.', body)],
    ))

    story += [spacer(10), inline_label('Logo Direction', callus=True)]
    for item in [
        'Shield-mark silhouette — refreshed from the current Callus mark, keeping the "trade badge" read',
        'Hammer + sparks inside the shield — visual shorthand for fabrication, hand work, heat',
        '"EST. 2009" banner across the top — plants the heritage flag immediately',
        'Wordmark in Roboto Slab with a rust period — "Callus." — and a small italic subtitle: <i>— Fabrication —</i>',
        'Tagline lockup: "It\'s all in the name."',
        'Delivered in SVG, PNG (multi-size), print-ready PDF, plus single-color versions for decals, stickers, and stamping onto steel',
    ]:
        story.append(bullet(item))

    story += [spacer(12), inline_label('Voice', callus=True)]
    voice_c_rows = [
        [P('TONE',c_hdr),       P('WHAT IT MEANS IN PRACTICE',c_hdr)],
        [P('Craftsman',c_col1_callus), P('Respect for the trade. Technical accuracy. Proud of the work — not precious about it.',c_body)],
        [P('Honest',c_col1_callus),    P('Quote straight. Tell you if a job isn\'t in our wheelhouse. Back the warranty in person.',c_body)],
        [P('Earned',c_col1_callus),    P('No boasting. Let the weld bead speak. Occasional shop humor, never corporate slick.',c_body)],
    ]
    voice_c_t = Table(voice_c_rows, colWidths=[1.2*inch, 5.3*inch], repeatRows=1)
    voice_c_t.setStyle(data_table_style(3))
    story += [voice_c_t, spacer(14), inline_label('Website', callus=True)]
    story.append(P(
        'Warm cream background, rust and brass accents, slab serif headlines. Sections: hero with '
        'shield mark, capabilities grid (Mobile Welding / Custom Fab / Structural / Public Works), '
        '"The Shop" story, recent work gallery, "4 Reasons GCs Keep Calling Back," and a big '
        '"It\'s all in the name" CTA with the phone number oversized. Footer carries a small '
        'sister-brand acknowledgment. A working mockup is available at <b>callusfabrication.com</b> (staged).',
        body))
    story.append(PageBreak())

    # ═══ 05 WEB STRATEGY ══════════════════════════════════════════════
    story += [section_divider(5,'Web Strategy'), spacer(16),
              P('Two sites, built in parallel. Each reflects its brand. Both are built on the same '
                'technical foundation — mobile-first, CMS-powered, fast, and maintainable by the '
                'client without a developer.', body), spacer(12)]

    story.append(two_col(
        [
            P('Jones Excavating Co.', h3),
            P('6–8 pages. CMS (WordPress or Webflow). Contact/quote form. Equipment/project gallery. '
              'ADSC recognition, stats, and project specs front and center. Phone number pinned in '
              'header on every page. PageSpeed 90+ target on mobile.', body),
            P('Pages', h3),
        ] + [bullet(p) for p in [
            'Home — hero, stats, services overview, trust bar',
            'Services — excavation, deep foundations, shoring, drilling',
            'Projects — photo/spec gallery with project detail pages',
            'About — history, team, ADSC, values',
            'Equipment — fleet list, capabilities',
            'Contact — quote form, phone, map',
        ]],
        [
            P('Callus Fabrication', h3_callus),
            P('5–6 pages. CMS. Services grid, work gallery, "4 Reasons" trust section. '
              'Shop story, phone number prominent. Warm brand palette applied site-wide. '
              'PageSpeed 90+ mobile target.', body),
            P('Pages', h3_callus),
        ] + [bullet(p) for p in [
            'Home — hero with shield mark, capabilities, CTA',
            'Services — mobile welding, custom fab, structural, public works',
            'Work — project gallery with detail pages',
            'Shop — about the company, team, shop story',
            'Contact — quote form, phone, map',
        ]],
    ))

    story += [spacer(16), inline_label('CMS Recommendation')]
    story.append(P(
        '<b>Webflow</b> is recommended for both sites — no-plugin security surface, visual editor, '
        'built-in hosting on a global CDN, and easy content updates for staff without developer '
        'access. WordPress is an acceptable alternative if the client has existing WP infrastructure. '
        'Either way: no page builders, no plugin bloat, hand-built templates for performance.', body))

    story += [spacer(10), inline_label('Technical Standards')]
    for item in [
        'PageSpeed / Core Web Vitals: 90+ on mobile for both sites (LCP &lt; 2.5s, CLS &lt; 0.1)',
        'HTTPS enforced; security headers configured (CSP, HSTS, X-Frame-Options)',
        'Structured data: LocalBusiness schema on contact pages, BreadcrumbList on interior pages',
        'XML sitemap submitted to Google Search Console on launch day',
        'robots.txt configured; staging environments blocked from indexing',
        'Cross-browser QA: Chrome, Safari, Firefox, Edge — desktop and mobile',
        'Accessibility: WCAG 2.1 AA compliance target — keyboard nav, alt text, contrast ratios',
        'Analytics: GA4 + Google Search Console on both sites from day one',
    ]:
        story.append(bullet(item))

    story += [spacer(10), inline_label('Hosting')]
    story.append(P(
        'Webflow hosting (Enterprise or CMS tier) covers both sites. Includes global CDN, SSL, '
        'daily backups, and 99.9% uptime SLA. If WordPress is chosen: WP Engine or Kinsta managed '
        'hosting recommended — both include staging environments, automatic backups, and CDN.', body))
    story.append(PageBreak())

    # ═══ 06 SEO & LOCAL SEARCH ════════════════════════════════════════
    story += [section_divider(6,'SEO & Local Search', accent=TEAL), spacer(16)]
    story.append(callout_box(
        'Local search is where these companies get found.',
        'Most customers for Jones and Callus start with a Google search — often from a job site on '
        'a phone. "Excavating contractor Salt Lake City." "Mobile welder West Jordan Utah." If '
        'neither company shows up in the local pack or the first organic page, they\'re invisible '
        'to that search. This chapter covers the foundation for fixing that.',
        bg=TEAL_BG, accent=TEAL
    ))

    story += [spacer(20), inline_label('Google Business Profile Optimization', teal=True)]
    story.append(P(
        'Two separate GBP listings — one for each company. GBP is the highest-leverage local SEO '
        'asset for service contractors. Both listings will be fully optimized as part of setup.', body))
    for item in [
        'Complete all fields: business name, category, service areas (county + city level), hours, phone, website',
        'Primary category: <b>Excavating Contractor</b> (Jones) | <b>Welding Supply Store</b> or <b>Metal Fabricator</b> (Callus)',
        'Add all applicable secondary categories for broader search surface',
        'Upload 20+ photos at launch: equipment, job sites, team, shop interior, finished work',
        'Enable Q&amp;A section — seed with 5–8 common customer questions and answers',
        'Set up Google Business Posts: weekly posts using project photos, before/after, seasonal content',
        'Review solicitation strategy — template responses, timing guidance for both companies',
    ]:
        story.append(bullet(item))

    story += [spacer(16), inline_label('Schema Markup', teal=True)]
    story.append(P(
        'Structured data tells search engines exactly what each page is about. Both sites will '
        'implement schema on relevant pages at launch.', body))
    schema_rows = [
        [P('SCHEMA TYPE', c_hdr), P('APPLIED TO', c_hdr), P('BENEFIT', c_hdr)],
        [P('LocalBusiness', c_col1_teal), P('Contact / homepage', c_body), P('Enables rich results: address, phone, hours in SERP', c_body)],
        [P('GeneralContractor', c_col1_teal), P('Services page (Jones)', c_body), P('Tells Google this is a licensed contractor', c_body)],
        [P('HomeAndConstructionBusiness', c_col1_teal), P('Services page (Callus)', c_body), P('Broader contractor schema for fab/welding', c_body)],
        [P('BreadcrumbList', c_col1_teal), P('All interior pages', c_body), P('Clean breadcrumb trail in SERP snippets', c_body)],
        [P('FAQPage', c_col1_teal), P('Service pages (both)', c_body), P('FAQ rich results expand SERP real estate', c_body)],
        [P('ImageObject', c_col1_teal), P('Project galleries', c_body), P('Image search visibility for project photos', c_body)],
    ]
    schema_t = Table(schema_rows, colWidths=[1.6*inch, 2.0*inch, 2.9*inch], repeatRows=1)
    schema_ts = TableStyle([
        ('BACKGROUND',    (0,0),(-1,0), TEAL_BG),
        ('TOPPADDING',    (0,0),(-1,-1),9),
        ('BOTTOMPADDING', (0,0),(-1,-1),9),
        ('LEFTPADDING',   (0,0),(-1,-1),10),
        ('RIGHTPADDING',  (0,0),(-1,-1),10),
        ('VALIGN',        (0,0),(-1,-1),'TOP'),
        ('ROWBACKGROUNDS',(0,1),(-1,-1),[WHITE, GRAY_100]),
        ('LINEBELOW',     (0,0),(-1,-1),0.5, GRAY_300),
    ])
    schema_t.setStyle(schema_ts)
    story += [schema_t, spacer(20)]

    story += [inline_label('Keyword Strategy', teal=True), spacer(6)]
    story.append(P(
        'Target keywords are grouped by intent: informational (how do I find a contractor), '
        'transactional (contractor + location), and navigational (brand name searches). Jones '
        'keywords focus on the Wasatch Front and Mountain West for heavy commercial work. '
        'Callus keywords focus on the Wasatch Front for trade and contractor audiences.', body))

    jones_kws = [
        'excavating contractor Utah',
        'excavation company Salt Lake City',
        'foundation drilling SLC',
        'deep foundation contractor Utah',
        'site excavation contractor Wasatch Front',
        'excavating company West Jordan Utah',
        'shoring contractor Salt Lake',
        'caisson drilling Utah',
        'commercial excavation Utah',
        'ADSC certified driller Utah',
        'excavation contractor Wyoming',
        'excavation contractor Idaho',
        'utility excavation contractor SLC',
        'trenching contractor Utah',
    ]
    callus_kws = [
        'mobile welding Utah',
        'mobile welder Salt Lake City',
        'custom fabrication West Jordan',
        'custom steel fabrication Utah',
        'structural steel fabrication SLC',
        'welding contractor Wasatch Front',
        'mobile welder West Jordan Utah',
        'custom metal fabrication Utah',
        'steel fabricator Salt Lake',
        'commercial welding contractor Utah',
        'on-site welding Utah',
        'portable welding service SLC',
        'fabrication shop West Jordan',
        'steel fabrication contractor Utah',
    ]
    story.append(keyword_table(jones_kws, callus_kws))
    story += [spacer(20), inline_label('Citation Building', teal=True)]
    story.append(P(
        'Citations — consistent business listings across the web — are a core local ranking factor. '
        'Both companies will have their NAP (Name, Address, Phone) submitted and verified across '
        'the major contractor and business directories.', body))
    for item in [
        '<b>General:</b> Google Business Profile, Apple Maps, Bing Places, Yelp, Yellow Pages',
        '<b>Contractor-specific:</b> Angi (formerly Angie\'s List), HomeAdvisor, Houzz, BuildZoom, Contractors.com',
        '<b>Trade associations:</b> ADSC member listing (Jones), AWS directory (Callus)',
        '<b>Local:</b> Utah Better Business Bureau, local chambers of commerce (Salt Lake, West Jordan)',
        '<b>Data aggregators:</b> Foursquare (Data Axle), Neustar Localeze — feeds hundreds of downstream directories',
        'Ongoing citation audit — fix inconsistent NAP before building new citations',
    ]:
        story.append(bullet(item))
    story.append(PageBreak())

    story += [inline_label('On-Page SEO', teal=True)]
    story.append(P(
        'Every page on both sites will be built with on-page SEO as a design constraint, not an '
        'afterthought applied after launch.', body))
    onpage_rows = [
        [P('ELEMENT', c_hdr), P('JONES EXAMPLE', c_hdr), P('CALLUS EXAMPLE', c_hdr)],
        [P('Title tag', c_col1_teal),
         P('Jones Excavating Co. | Excavation Contractor Utah', c_url),
         P('Callus Fabrication | Mobile Welding &amp; Custom Fab Utah', c_url)],
        [P('Meta description', c_col1_teal),
         P('Utah\'s most trusted excavation contractor for deep foundations, shoring &amp; site work. ADSC-certified. 70+ years.', c_body),
         P('Custom steel fabrication and mobile welding for contractors across the Wasatch Front. 15+ years. Call us.', c_body)],
        [P('H1 (homepage)', c_col1_teal),
         P('"Built for the Hard Jobs"', c_body),
         P('"It\'s All in the Name"', c_body)],
        [P('Service page H1', c_col1_teal),
         P('"Deep Foundation Drilling — Utah &amp; Mountain West"', c_body),
         P('"Mobile Welding — Wasatch Front &amp; Salt Lake Valley"', c_body)],
        [P('Image alt text', c_col1_teal),
         P('Jones excavator on deep foundation job, Salt Lake City', c_body),
         P('Callus welder on structural beam, West Jordan Utah', c_body)],
        [P('Internal linking', c_col1_teal),
         P('Services → Project gallery by trade → Contact', c_body),
         P('Services → Work gallery by service → Contact', c_body)],
    ]
    onpage_t = Table(onpage_rows, colWidths=[1.25*inch, 2.625*inch, 2.625*inch], repeatRows=1)
    onpage_ts = TableStyle([
        ('BACKGROUND',    (0,0),(-1,0), TEAL_BG),
        ('TOPPADDING',    (0,0),(-1,-1),8),
        ('BOTTOMPADDING', (0,0),(-1,-1),8),
        ('LEFTPADDING',   (0,0),(-1,-1),9),
        ('RIGHTPADDING',  (0,0),(-1,-1),9),
        ('VALIGN',        (0,0),(-1,-1),'TOP'),
        ('ROWBACKGROUNDS',(0,1),(-1,-1),[WHITE, GRAY_100]),
        ('LINEBELOW',     (0,0),(-1,-1),0.5, GRAY_300),
        ('LINEAFTER',     (0,0),(0,-1),0.5, GRAY_300),
        ('LINEAFTER',     (1,0),(1,-1),0.5, GRAY_300),
    ])
    onpage_t.setStyle(onpage_ts)
    story += [onpage_t, spacer(18), inline_label('Technical SEO', teal=True)]
    story.append(P(
        'Technical SEO is handled at build time — these are not post-launch cleanup items. '
        'Both sites launch with a full technical foundation.', body))
    for item in [
        '<b>Page speed:</b> PageSpeed 90+ mobile. Images in WebP/AVIF, lazy-loaded. Minimal JS. No render-blocking resources.',
        '<b>Core Web Vitals:</b> LCP &lt; 2.5s, FID &lt; 100ms, CLS &lt; 0.1 — measured and fixed before launch',
        '<b>Crawlability:</b> clean URL structure (/services/excavation/, not /?p=42), canonical tags, no duplicate content',
        '<b>XML sitemap:</b> auto-generated, submitted to Google Search Console and Bing Webmaster Tools on launch day',
        '<b>robots.txt:</b> staging environment blocked; production configured to allow all search engines',
        '<b>HTTPS:</b> SSL enforced site-wide, HSTS header configured, no mixed-content warnings',
        '<b>Mobile-first indexing:</b> responsive design, no separate mobile URLs, viewport meta tag on every page',
        '<b>404 handling:</b> custom 404 pages with navigation; 301 redirects for any legacy URLs',
    ]:
        story.append(bullet(item))

    story += [spacer(16), inline_label('Monthly SEO Reporting', teal=True)]
    story.append(P(
        'Monthly reports cover both companies. Delivered by the 5th of each month.', body))
    for item in [
        'Google Search Console: impressions, clicks, average position, top queries by brand',
        'GBP insights: searches, views, calls, direction requests, review count and average rating',
        'Ranking report: tracked keyword positions for all target terms (both sites)',
        'Traffic report: organic sessions, new vs. returning, top landing pages, conversion events',
        'Citation and backlink audit: new citations added, any NAP inconsistencies flagged',
        'Recommendations: one or two priority actions for the month ahead',
    ]:
        story.append(bullet(item))
    story.append(PageBreak())

    # ═══ 07 SOCIAL MEDIA & CONTENT ════════════════════════════════════
    story += [section_divider(7,'Social Media & Content', accent=TEAL), spacer(16),
              P('Neither Jones nor Callus needs a huge social media presence — but both benefit from '
                'a consistent, on-brand one. The goal is not followers; it\'s trust signals and '
                'project visibility for the GCs and developers who look up a company before calling.', body),
              spacer(12)]

    story.append(two_col(
        [
            P('Jones Excavating Co.', h3),
            P('<b>Primary platform: Facebook.</b><br/>'
              'Jones\' customers — GC project managers, public agency PMs, developers — skew toward '
              'Facebook for professional local credibility checks. A well-maintained Facebook page '
              'with project photos and reviews reads as "established, real company."', body),
            P('Content Pillars', h3),
        ] + [bullet(p) for p in [
            'Project photos — equipment in the field, job site progress',
            'Behind the scenes — crew, equipment yard, maintenance days',
            'Stats &amp; milestones — "Completed 80th deep foundation"',
            'Heritage — throwback photos, company history content',
            'Community — local events, safety, industry news',
        ]] + [
            P('Posting Cadence', h3),
            P('2–3 posts/week. No posting for the sake of posting — every post should have a photo.', body),
        ],
        [
            P('Callus Fabrication', h3_callus),
            P('<b>Primary platform: Instagram.</b><br/>'
              'Callus\' work is inherently visual — welds, fabricated pieces, finished steel. '
              'Instagram\'s visual-first format is the right home for that work. Contractors who '
              'vet subs frequently check Instagram for portfolio evidence.', body),
            P('Content Pillars', h3_callus),
        ] + [bullet(p) for p in [
            'Finished work — clean shots of completed fabrication and welds',
            'Process — in-progress shots, arc glow, fit-up photos',
            'Shop life — behind the scenes, equipment, the team',
            'Educational — quick tips on welding processes, steel types',
            'Before/after — transformation shots of custom fabrications',
        ]] + [
            P('Posting Cadence', h3_callus),
            P('3–4 posts/week. Reels (short video) 1–2x/month to boost reach.', body),
        ],
    ))

    story += [spacer(16), inline_label('Google Business Posts', teal=True)]
    story.append(P(
        'GBP posts appear directly in Google Search results and Maps — they\'re often more valuable '
        'than social posts for local service contractors because they show up when someone is '
        'already searching for you. Both listings will use weekly GBP posts as part of the SEO '
        'retainer. Post types: project photos, seasonal offers (e.g. spring site prep), team '
        'spotlights, and award/certification announcements.', body))

    story += [spacer(10), inline_label('Content Production Notes', teal=True)]
    for item in [
        'We produce the first 3 months of content — copy, captions, hashtag sets — as part of setup',
        'Client provides project photos (guidance document on what to shoot and how will be delivered)',
        'Monthly content calendar template — client or team can maintain independently after setup',
        'Optional: add ongoing social management to the monthly retainer (available as add-on)',
    ]:
        story.append(bullet(item))
    story.append(PageBreak())

    # ═══ 08 TIMELINE & INVESTMENT ═════════════════════════════════════
    story += [section_divider(8,'Timeline & Investment'), spacer(16),
              P('Five phases. Branding lands first — both companies can start using new identity inside '
                'three weeks — then web development carries through to a coordinated dual launch, '
                'followed by SEO setup and social media launch.', body),
              spacer(16)]
    for phase, title, duration, tasks, is_dark, accent in [
        ('PH.1','Discovery &amp; Strategy','Week 1–2',
         ['Stakeholder interviews with Jones and Callus leadership',
          'Customer / market positioning for both brands',
          'Finalize voice guides and brand architecture',
          'Keyword research: Jones and Callus target term sets',
          'Competitive review: peers, sister-brand playbooks, local SEO landscape'], False, ORANGE),
        ('PH.2','Brand Systems','Week 3–5',
         ['Jones logo refresh — 2 finalized concepts delivered',
          'Callus identity — logo, palette, typography, guidelines',
          'Brand standards PDFs for both companies',
          'Asset packages: SVG, PNG, PDF (print), single-color versions',
          'Client approval checkpoint — both brands locked before web starts'], True, ORANGE),
        ('PH.3','Web Design &amp; Build','Week 6–11',
         ['Jones site: 6–8 pages, CMS, forms, analytics',
          'Callus site: 5–6 pages, CMS, forms, analytics',
          'On-page SEO: title tags, meta, H-tag structure, schema markup on all pages',
          'Mobile-first design, PageSpeed 90+ target on both',
          'Cross-browser QA and accessibility checks'], False, ORANGE),
        ('PH.4','Launch &amp; SEO Setup','Week 12–13',
         ['DNS cutover, dual launch — both sites go live together',
          'GBP optimization: both listings fully built out with photos and posts',
          'Citation building: submissions to 30+ directories for each company',
          'Analytics, Search Console, and GBP Insights connected',
          'Post-launch 2-week support window'], True, TEAL),
        ('PH.5','Digital Ongoing (Monthly)','Month 2+',
         ['Monthly SEO report: rankings, traffic, GBP insights, citations',
          'Weekly GBP posts for both companies',
          'Keyword rank tracking — all target terms, both sites',
          'Citation monitoring and NAP consistency checks',
          'Quarterly SEO review call + strategy update'], False, TEAL),
    ]:
        story.append(phase_row(phase, title, duration, tasks, is_dark, accent))
        story.append(spacer(2))

    story += [spacer(20), inline_label('One-Time Investment'), spacer(8)]
    for item, note, price, teal in [
        ('Jones Brand Refresh',     'Logo refinement, color/type system, voice guide, brand PDF, asset pack',   '$3,500 – $5,500', False),
        ('Jones Website',            '6–8 pages, CMS, forms, analytics, SEO foundation, mobile-first',          '$8,000 – $12,000', False),
        ('Callus Brand Identity',    'Full identity from scratch, shield mark, palette, type, voice, asset pack','$4,500 – $6,500', False),
        ('Callus Website',           '5–6 pages, CMS, forms, analytics, SEO foundation, mobile-first',          '$6,500 – $10,000', False),
        ('SEO Setup (both sites)',   'GBP optimization, schema markup, citation building, Search Console setup, on-page SEO audit', '$2,500 – $3,500', True),
        ('Social Media Setup',       'Platform profiles, first 3 months of content, content calendar template, GBP post templates', '$1,500 – $2,500', True),
    ]:
        story.append(price_row(item, price, note, teal=teal))
        story.append(spacer(2))

    story += [spacer(6), price_row('ALL-IN PROJECT TOTAL', 'Both brands, both sites, SEO setup, social setup — bundle pricing',
                                    '$26,500 – $40,000', highlight=True),
              spacer(4)]

    story += [inline_label('Monthly Retainer (after launch)', teal=True), spacer(6)]
    for item, note, price in [
        ('Monthly SEO Retainer',   'Rankings, GBP posts, citation monitoring, monthly report — both sites', '$800 – $1,200/mo'),
    ]:
        story.append(price_row(item, price, note, teal=True))
        story.append(spacer(2))

    story += [spacer(12),
              P('<i>Bundle discount of ~10% applied to all-in engagement vs. running tracks independently. '
                'Individual tracks can be scoped separately if preferred. Monthly retainer can be added '
                'at any time after launch — recommended to start in Month 2.</i>', body),
              PageBreak()]

    # ═══ 09 NEXT STEPS ════════════════════════════════════════════════
    story += [section_divider(9,'Next Steps'), spacer(16),
              P('Two working site mockups (Jones and Callus), a brand-concepts deck, and a preview of '
                'the SEO keyword strategy are already built and viewable. From here, the path is short.', body),
              spacer(14)]
    for ttl, desc, accent in [
        ('1. Review',   'Scroll the brand concepts deck and both homepage mockups. Note what lands, what doesn\'t, what feels off. Review the keyword lists and flag any terms that need adjusting.', h3),
        ('2. Approve',  'Confirm brand direction for each company (Jones refresh path, Callus "Hands &amp; Fire" direction), and green-light scope. Sign-off on keyword strategy and SEO target cities.', h3),
        ('3. Kickoff',  'Half-day brand workshop with Jones and Callus leadership. We lock voice, positioning, keyword targets, and open questions before design begins.', h3),
        ('4. Ship',     'Brand systems delivered in three weeks. Full dual-site launch twelve weeks from kickoff. SEO and social setup complete by end of Week 13. Monthly reporting starts Month 2.', h3),
    ]:
        story.append(KeepTogether([P(ttl, accent), P(desc, body), spacer(8)]))

    story += [spacer(8), hr(ORANGE, thickness=2), spacer(16),
              P('Ready when you are.', closing_s),
              P('Links to the live mockups are in the cover email. The fastest next move is a '
                '30-minute call to walk through what you like in each direction and where you want '
                'to push back — we\'ll take that feedback straight into the workshop agenda.', body),
              spacer(20)]

    ns_s  = S('NS', fontName='Helvetica-Bold', fontSize=9,  textColor=ORANGE, leading=14, spaceAfter=10)
    nst_s = S('NST',fontName='Helvetica',      fontSize=11, textColor=WHITE,  leading=20, spaceAfter=0)
    steps = Table([
        [P('LIVE DELIVERABLES', ns_s)],
        [P('• Brand concepts deck — <b>brand_concepts.html</b><br/>'
           '• Jones homepage mockup — <b>index.html</b><br/>'
           '• Callus homepage mockup — <b>callus.html</b><br/>'
           '• Agency proposal landing page — <b>outputs/landing.html</b><br/><br/>'
           '<b>Schedule a 30-minute walkthrough</b> to react to each concept and we\'ll shape the workshop agenda around your notes.', nst_s)],
    ], colWidths=[CONTENT_W - 0.1*inch])
    steps.setStyle(TableStyle([
        ('BACKGROUND',    (0,0),(-1,-1),CHARCOAL),
        ('TOPPADDING',    (0,0),(-1,-1),20),('BOTTOMPADDING',(0,0),(-1,-1),20),
        ('LEFTPADDING',   (0,0),(-1,-1),28),('RIGHTPADDING',  (0,0),(-1,-1),28),
        ('LINEBEFORE',    (0,0),(-1,-1),5,ORANGE),
    ]))
    story.append(steps)

    # ── BUILD ──────────────────────────────────────────────────────────
    doc.build(story, onFirstPage=canvas_cb.on_page, onLaterPages=canvas_cb.on_page)
    print(f'PDF saved -> {OUTPUT}')

if __name__ == '__main__':
    build_pdf()
