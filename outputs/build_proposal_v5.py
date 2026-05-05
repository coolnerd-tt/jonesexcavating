"""
Jones Excavating Co. × Callus Fabrication — Proposal v5
v5 incorporates the first round of stakeholder edits:
- Cover: "Complete Digital Proposal" replaces "Full-Stack"
- Executive Summary: 80-year company, founded 1946, "Why Act Now"
  callout with new market-momentum framing, stat strip removed
- Global propagation of the 1946 founding / 80-year tenure
"""

import os
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    PageBreak, HRFlowable, KeepTogether, Image
)
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT
from reportlab.lib.colors import HexColor
from reportlab.lib.utils import ImageReader

# ── COLORS ─────────────────────────────────────────────────────────────────────
BLACK    = HexColor('#0C0E10')
CHARCOAL = HexColor('#161A1D')
ORANGE   = HexColor('#E8621A')
AMBER    = HexColor('#F5A623')
WHITE    = HexColor('#FFFFFF')
OFF_WHITE= HexColor('#F4F2EE')
GRAY_50  = HexColor('#FAFAF8')
GRAY_100 = HexColor('#F0EFEB')
GRAY_300 = HexColor('#D1CFC9')
GRAY_500 = HexColor('#8A8880')
GRAY_700 = HexColor('#4A4845')
GRAY_900 = HexColor('#26241F')
SPARK    = HexColor('#D93B18')
SPARK_DK = HexColor('#A82C12')
TEAL     = HexColor('#2E7D8C')
TEAL_LT  = HexColor('#3D9BAD')
TEAL_BG  = HexColor('#1A3840')

W, H = letter
CONTENT_W = 6.6 * inch  # 0.7" margins each side

BASE = "/Users/tylertoone/Desktop/Claude Work/inbox/excavating-site"
JONES_LOGO   = os.path.join(BASE, "jones-assets/jones-logo.png")
CALLUS_LOGO  = os.path.join(BASE, "callus-logo-concepts/callus-logo-hz.png")

OUTPUT = os.path.join(BASE, "outputs/jones_callus_proposal_v5.pdf")

# ── STYLES ─────────────────────────────────────────────────────────────────────
def S(name, **kw):
    return ParagraphStyle(name, **kw)

# Cover
cover_label  = S('CL', fontName='Helvetica-Bold', fontSize=8,  textColor=ORANGE,   leading=12, spaceAfter=4)
cover_title  = S('CT', fontName='Helvetica-Bold', fontSize=42, textColor=WHITE,   leading=46, spaceAfter=0)
cover_title2 = S('CT2',fontName='Helvetica-Bold', fontSize=42, textColor=ORANGE,  leading=46, spaceAfter=0)
cover_amp    = S('CA', fontName='Helvetica-BoldOblique', fontSize=24, textColor=GRAY_500, leading=28)
cover_meta   = S('CM', fontName='Helvetica',      fontSize=9,  textColor=GRAY_300, leading=14)

# Chapter
chapter_num   = S('CN', fontName='Helvetica-Bold', fontSize=8,  textColor=ORANGE, leading=11, spaceAfter=4)
chapter_title = S('CTI',fontName='Helvetica-Bold', fontSize=26, textColor=BLACK,  leading=30, spaceAfter=14)
chapter_kicker= S('CK', fontName='Helvetica-Oblique', fontSize=10, textColor=GRAY_500, leading=14, spaceAfter=14)

# Headings
h2 = S('H2',  fontName='Helvetica-Bold', fontSize=14, textColor=BLACK,  leading=18, spaceBefore=18, spaceAfter=6)
h3 = S('H3',  fontName='Helvetica-Bold', fontSize=10.5, textColor=ORANGE, leading=14, spaceBefore=12, spaceAfter=4)
h3_teal = S('H3T', fontName='Helvetica-Bold', fontSize=10.5, textColor=TEAL, leading=14, spaceBefore=12, spaceAfter=4)
h3_spark= S('H3S', fontName='Helvetica-Bold', fontSize=10.5, textColor=SPARK, leading=14, spaceBefore=12, spaceAfter=4)

# Body — denser
body  = S('Bd', fontName='Helvetica',      fontSize=9,   textColor=GRAY_700, leading=14, spaceAfter=7)
body_lead = S('BL', fontName='Helvetica', fontSize=10, textColor=BLACK, leading=15, spaceAfter=9)
bullet_s = S('Bu', fontName='Helvetica',  fontSize=9,   textColor=GRAY_700, leading=13.5, spaceAfter=4, leftIndent=12)

# Labels
label_s  = S('Lb', fontName='Helvetica-Bold', fontSize=7.5, textColor=ORANGE, leading=11, spaceAfter=3)
label_teal = S('LbT', fontName='Helvetica-Bold', fontSize=7.5, textColor=TEAL, leading=11, spaceAfter=3)
label_spark= S('LbS', fontName='Helvetica-Bold', fontSize=7.5, textColor=SPARK, leading=11, spaceAfter=3)

# TOC
toc_num   = S('TN', fontName='Helvetica-Bold', fontSize=10, textColor=ORANGE,  leading=20)
toc_entry = S('TE', fontName='Helvetica',      fontSize=10, textColor=GRAY_700,leading=20)
toc_pg    = S('TP', fontName='Helvetica',      fontSize=9,  textColor=GRAY_500,leading=20, alignment=TA_RIGHT)

# Callouts
callout_t = S('CaT', fontName='Helvetica-Bold', fontSize=11, textColor=WHITE,    leading=15, spaceAfter=4)
callout_t_big = S('CaTB', fontName='Helvetica-Bold', fontSize=18, textColor=WHITE, leading=22, spaceAfter=8)
callout_b = S('CaB', fontName='Helvetica',      fontSize=9,  textColor=GRAY_300, leading=13.5, spaceAfter=0)

# Stat
stat_num_s = S('StN', fontName='Helvetica-Bold', fontSize=24, textColor=ORANGE, leading=27, alignment=TA_CENTER)
stat_lbl_s = S('StL', fontName='Helvetica-Bold', fontSize=7,  textColor=GRAY_500, leading=10, alignment=TA_CENTER)

# Table cells — denser
c_hdr  = S('CH',  fontName='Helvetica-Bold',        fontSize=7.5, textColor=WHITE,    leading=10)
c_body = S('CB',  fontName='Helvetica',             fontSize=8,   textColor=GRAY_700, leading=11)
c_body_b = S('CBB', fontName='Helvetica-Bold',      fontSize=8,   textColor=BLACK,    leading=11)
c_pri  = S('CPr', fontName='Helvetica-Bold',        fontSize=8,   textColor=ORANGE,   leading=11)
c_num  = S('CN',  fontName='Helvetica-Bold',        fontSize=8.5, textColor=BLACK,    leading=11, alignment=TA_RIGHT)
c_num_g = S('CNg',fontName='Helvetica',             fontSize=8.5, textColor=GRAY_500, leading=11, alignment=TA_RIGHT)
c_num_orange = S('CNo', fontName='Helvetica-Bold',  fontSize=8.5, textColor=ORANGE,   leading=11, alignment=TA_RIGHT)
# Centered numeric variants
c_num_c        = S('CNc',  fontName='Helvetica-Bold', fontSize=8.5, textColor=BLACK,  leading=11, alignment=TA_CENTER)
c_num_orange_c = S('CNoc', fontName='Helvetica-Bold', fontSize=8.5, textColor=ORANGE, leading=11, alignment=TA_CENTER)
c_body_c       = S('CBc',  fontName='Helvetica',      fontSize=8,   textColor=GRAY_700, leading=11, alignment=TA_CENTER)
c_pri_c        = S('CPrc', fontName='Helvetica-Bold', fontSize=8,   textColor=ORANGE,   leading=11, alignment=TA_CENTER)

# Pricing
pr_item   = S('PI',  fontName='Helvetica-Bold', fontSize=10, textColor=BLACK,   leading=13)
pr_item_h = S('PIh', fontName='Helvetica-Bold', fontSize=10, textColor=WHITE,   leading=13)
pr_note   = S('PN',  fontName='Helvetica',      fontSize=8.5,textColor=GRAY_500,leading=12)
pr_note_h = S('PNh', fontName='Helvetica',      fontSize=8.5,textColor=GRAY_300,leading=12)
pr_price  = S('PP',  fontName='Helvetica-Bold', fontSize=14, textColor=ORANGE,  leading=18, alignment=TA_RIGHT)
pr_price_h= S('PPh', fontName='Helvetica-Bold', fontSize=14, textColor=WHITE,   leading=18, alignment=TA_RIGHT)

# ── HELPERS ────────────────────────────────────────────────────────────────────
def P(text, style=body): return Paragraph(str(text), style)
def sp(h=10): return Spacer(1, h)
def hr(color=GRAY_300, t=0.5, sb=6, sa=6):
    return HRFlowable(width='100%', thickness=t, color=color, spaceAfter=sa, spaceBefore=sb)

def bullet(text):  return Paragraph(f'<font color="#E8621A"><b>\u25AA</b></font>  {text}', bullet_s)

def section_header(num, title, kicker=None, accent=ORANGE):
    n = f'0{num}' if num < 10 else str(num)
    n_style = S(f'cn{accent.hexval()}', fontName='Helvetica-Bold', fontSize=8,
                textColor=accent, leading=11, spaceAfter=4)
    rows = [[P(f'CHAPTER  {n}', n_style)],
            [P(title, chapter_title)]]
    if kicker:
        rows.append([P(kicker, chapter_kicker)])
    t = Table(rows, colWidths=[CONTENT_W])
    t.setStyle(TableStyle([
        ('LEFTPADDING',(0,0),(-1,-1),12),
        ('RIGHTPADDING',(0,0),(-1,-1),0),
        ('TOPPADDING',(0,0),(-1,-1),0),
        ('BOTTOMPADDING',(0,0),(-1,-1),0),
        ('LINEBEFORE',(0,0),(0,-1), 3, accent),
    ]))
    return t

def callout(title, body_text, bg=CHARCOAL, accent=ORANGE, big_title=False):
    pad = 16
    title_style = callout_t_big if big_title else callout_t
    inner = Table([
        [P(title, title_style)],
        [P(body_text, callout_b)],
    ], colWidths=[CONTENT_W - pad*2 - 4])
    inner.setStyle(TableStyle([
        ('BACKGROUND',(0,0),(-1,-1), bg),
        ('TOPPADDING',(0,0),(-1,-1), pad),
        ('BOTTOMPADDING',(0,0),(-1,-1), pad),
        ('LEFTPADDING',(0,0),(-1,-1), pad),
        ('RIGHTPADDING',(0,0),(-1,-1), pad),
    ]))
    wrap = Table([[inner]], colWidths=[CONTENT_W])
    wrap.setStyle(TableStyle([
        ('LEFTPADDING',(0,0),(-1,-1),0),
        ('RIGHTPADDING',(0,0),(-1,-1),0),
        ('TOPPADDING',(0,0),(-1,-1),0),
        ('BOTTOMPADDING',(0,0),(-1,-1),10),
        ('LINEBEFORE',(0,0),(-1,-1),3, accent),
    ]))
    return wrap

def two_col(left, right, gap=0.25*inch):
    cw = (CONTENT_W - gap) / 2
    def col(items):
        rows = [[i] for i in items]
        t = Table(rows, colWidths=[cw])
        t.setStyle(TableStyle([
            ('TOPPADDING',(0,0),(-1,-1),1),
            ('BOTTOMPADDING',(0,0),(-1,-1),1),
            ('LEFTPADDING',(0,0),(-1,-1),0),
            ('RIGHTPADDING',(0,0),(-1,-1),0),
        ]))
        return t
    out = Table([[col(left), Spacer(gap,1), col(right)]],
                colWidths=[cw, gap, cw])
    out.setStyle(TableStyle([
        ('VALIGN',(0,0),(-1,-1),'TOP'),
        ('TOPPADDING',(0,0),(-1,-1),0),
        ('BOTTOMPADDING',(0,0),(-1,-1),0),
        ('LEFTPADDING',(0,0),(-1,-1),0),
        ('RIGHTPADDING',(0,0),(-1,-1),0),
    ]))
    return out

def stat_strip(items):
    """items: [(num, label), ...]"""
    cells = []
    for num, lbl in items:
        cell = Table([[P(num, stat_num_s)], [P(lbl, stat_lbl_s)]],
                     colWidths=[CONTENT_W/len(items)])
        cell.setStyle(TableStyle([
            ('TOPPADDING',(0,0),(-1,-1),2),
            ('BOTTOMPADDING',(0,0),(-1,-1),2),
        ]))
        cells.append(cell)
    t = Table([cells], colWidths=[CONTENT_W/len(items)]*len(items))
    t.setStyle(TableStyle([
        ('BACKGROUND',(0,0),(-1,-1), GRAY_50),
        ('VALIGN',(0,0),(-1,-1),'MIDDLE'),
        ('TOPPADDING',(0,0),(-1,-1),16),
        ('BOTTOMPADDING',(0,0),(-1,-1),16),
        ('LEFTPADDING',(0,0),(-1,-1),0),
        ('RIGHTPADDING',(0,0),(-1,-1),0),
        ('LINEABOVE',(0,0),(-1,0),2, ORANGE),
        ('LINEBELOW',(0,-1),(-1,-1),0.5, GRAY_300),
    ]))
    return t

def phase_card_basic(num, title, weeks, items, bg=GRAY_50, accent=ORANGE):
    """Module-level phase card so it's usable across chapters."""
    ph_s = S('ps2', fontName='Helvetica-Bold', fontSize=8, textColor=accent, leading=11)
    ti_s = S('pt2', fontName='Helvetica-Bold', fontSize=11, textColor=BLACK, leading=14)
    wk_s = S('pw2', fontName='Helvetica-Bold', fontSize=7.5, textColor=GRAY_500, leading=10)
    it_s = S('pi2', fontName='Helvetica',     fontSize=8.5, textColor=GRAY_700, leading=12)
    items_html = '<br/>'.join([f'\u2022 {x}' for x in items])
    data = [[P(num, ph_s), P(title, ti_s), P(weeks.upper(), wk_s), P(items_html, it_s)]]
    t = Table(data, colWidths=[0.6*inch, 1.4*inch, 0.9*inch, 3.7*inch])
    t.setStyle(TableStyle([
        ('BACKGROUND',(0,0),(-1,-1), bg),
        ('TOPPADDING',(0,0),(-1,-1),12),
        ('BOTTOMPADDING',(0,0),(-1,-1),12),
        ('LEFTPADDING',(0,0),(-1,-1),12),
        ('RIGHTPADDING',(0,0),(-1,-1),12),
        ('VALIGN',(0,0),(-1,-1),'TOP'),
        ('LINEBEFORE',(0,0),(0,-1),3, accent),
    ]))
    return t


def price_row(item, price, note='', highlight=False):
    if highlight:
        bg, ist, nst, pst = ORANGE, pr_item_h, pr_note_h, pr_price_h
    else:
        bg, ist, nst, pst = GRAY_50, pr_item, pr_note, pr_price
    data = [[P(item, ist), P(note, nst), P(price, pst)]]
    t = Table(data, colWidths=[2.0*inch, 2.8*inch, 1.8*inch])
    t.setStyle(TableStyle([
        ('BACKGROUND',(0,0),(-1,-1), bg),
        ('TOPPADDING',(0,0),(-1,-1),11),
        ('BOTTOMPADDING',(0,0),(-1,-1),11),
        ('LEFTPADDING',(0,0),(-1,-1),12),
        ('RIGHTPADDING',(0,0),(-1,-1),12),
        ('VALIGN',(0,0),(-1,-1),'MIDDLE'),
        ('LINEBELOW',(0,0),(-1,-1),0.5, WHITE),
    ]))
    return t

def comp_table(rows, center=False):
    """rows: header + data rows, each a list of strings.
       First column = company name (bold), numeric columns right-aligned
       by default. Pass center=True to center-align all non-name columns
       (used for the GBP benchmark table where columns are paired
       categorical values, not magnitudes)."""
    table_rows = []
    # Header — center alignment of header cells matches body when center=True
    if center:
        c_hdr_style = S('CHc', fontName='Helvetica-Bold', fontSize=7.5, textColor=WHITE, leading=10, alignment=TA_CENTER)
    else:
        c_hdr_style = c_hdr
    hdr = [P(rows[0][0], c_hdr)] + [P(c, c_hdr_style) for c in rows[0][1:]]
    table_rows.append(hdr)
    for r in rows[1:]:
        is_jones = 'Jones' in r[0]
        name_style = c_pri if is_jones else c_body_b
        out = [P(r[0], name_style)]
        for v in r[1:]:
            if center:
                # All non-name columns centered, regardless of digit content
                if any(ch.isdigit() for ch in v) and not v.endswith(')'):
                    style = c_num_orange_c if is_jones else c_num_c
                else:
                    style = c_pri_c if is_jones else c_body_c
                out.append(P(v, style))
            else:
                # Default: right-align numbers, left-align text
                if any(ch.isdigit() for ch in v) and not v.endswith(')'):
                    style = c_num_orange if is_jones else c_num
                    out.append(P(v, style))
                else:
                    out.append(P(v, c_body if not is_jones else c_pri))
        table_rows.append(out)
    n_cols = len(rows[0])
    col_w = CONTENT_W / n_cols
    widths = [col_w * 1.4] + [(CONTENT_W - col_w*1.4) / (n_cols-1)] * (n_cols-1)
    t = Table(table_rows, colWidths=widths, repeatRows=1)
    t.setStyle(TableStyle([
        ('BACKGROUND',(0,0),(-1,0), CHARCOAL),
        ('TOPPADDING',(0,0),(-1,-1),8),
        ('BOTTOMPADDING',(0,0),(-1,-1),8),
        ('LEFTPADDING',(0,0),(-1,-1),9),
        ('RIGHTPADDING',(0,0),(-1,-1),9),
        ('VALIGN',(0,0),(-1,-1),'MIDDLE'),
        ('ROWBACKGROUNDS',(0,1),(-1,-1),[WHITE, GRAY_50]),
        ('LINEBELOW',(0,0),(-1,-1),0.4, GRAY_300),
    ]))
    return t

# ── PAGE CANVAS ────────────────────────────────────────────────────────────────
class Canv:
    def on_page(self, c, doc):
        page = doc.page
        c.saveState()
        if page == 1:
            # Cover background
            c.setFillColor(BLACK); c.rect(0,0,W,H,fill=1,stroke=0)
            # Side accents
            c.setFillColor(ORANGE);   c.rect(0,0,5,H,fill=1,stroke=0)
            c.setFillColor(SPARK);    c.rect(W-5,0,5,H,fill=1,stroke=0)
            # Bottom split bar
            c.setFillColor(ORANGE);   c.rect(0,0,W/2,4,fill=1,stroke=0)
            c.setFillColor(SPARK);    c.rect(W/2,0,W/2,4,fill=1,stroke=0)
            # Subtle grid
            c.setStrokeColor(HexColor('#15181B')); c.setLineWidth(0.4)
            for x in range(0,int(W)+1,40): c.line(x,0,x,H)
            for y in range(0,int(H)+1,40): c.line(0,y,W,y)
            # Watermark logos
            try:
                c.saveState()
                c.setFillAlpha(0.07)
                c.drawImage(ImageReader(JONES_LOGO),
                            -1.0*inch, H/2 - 1.0*inch + 0.5*inch,
                            width=4.6*inch, height=2.0*inch,
                            mask='auto', preserveAspectRatio=True)
                c.setFillAlpha(0.05)
                c.drawImage(ImageReader(CALLUS_LOGO),
                            W - 4.2*inch, H/2 - 0.8*inch,
                            width=4.0*inch, height=2.0*inch,
                            mask='auto', preserveAspectRatio=True)
                c.restoreState()
            except Exception:
                pass
            c.setFont('Helvetica-Bold', 7)
            c.setFillColor(GRAY_700)
            c.drawRightString(W-30, H-26, 'CONFIDENTIAL  |  PROPOSAL v5  |  APRIL 2026')
        else:
            # Top header bar
            c.setFillColor(ORANGE); c.rect(0,H-3,W,3,fill=1,stroke=0)
            c.setFillColor(CHARCOAL); c.rect(0,H-32,W,29,fill=1,stroke=0)
            c.setFont('Helvetica-Bold', 7.5); c.setFillColor(WHITE)
            c.drawString(30, H-21, 'JONES \u00D7 CALLUS')
            c.setFillColor(ORANGE); c.drawString(30+82, H-21, '|')
            c.setFillColor(GRAY_300); c.setFont('Helvetica', 7.5)
            c.drawString(30+90, H-21, 'Digital Proposal  \u00B7  v5  \u00B7  2026')
            c.setFont('Helvetica-Bold', 7.5); c.setFillColor(ORANGE)
            c.drawRightString(W-30, H-21, f'{page}')
            # Footer bar
            c.setFillColor(GRAY_100); c.rect(0,0,W,22,fill=1,stroke=0)
            c.setFont('Helvetica', 6.5); c.setFillColor(GRAY_500)
            c.drawString(30, 8, 'CONFIDENTIAL \u2014 prepared for Jones Excavating Co. \u00B7 \u00A9 2026')
            c.drawRightString(W-30, 8, 'jonesexcavating.com  \u00B7  callusfabrication.com')
        c.restoreState()

# ── DOCUMENT ───────────────────────────────────────────────────────────────────
def build():
    doc = SimpleDocTemplate(
        OUTPUT, pagesize=letter,
        leftMargin=0.7*inch, rightMargin=0.7*inch,
        topMargin=0.7*inch,  bottomMargin=0.45*inch,
        title='Jones \u00D7 Callus \u2014 Proposal v5',
    )
    s = []
    cb = Canv()

    # ═══ COVER ═══════════════════════════════════════════════════════════════
    s.append(sp(0.9*inch))
    s.append(P('DIGITAL PROPOSAL', cover_label))
    s.append(P('BRAND  \u00B7  WEB  \u00B7  SEO  \u00B7  SOCIAL', cover_label))
    s.append(sp(14))

    # Real logo lockup
    j_img = Image(JONES_LOGO,  width=2.4*inch, height=0.95*inch, kind='proportional')
    c_img = Image(CALLUS_LOGO, width=2.0*inch, height=1.25*inch, kind='proportional')
    logo_row = Table([[j_img, '', c_img]],
                     colWidths=[2.7*inch, 0.3*inch, 2.3*inch])
    logo_row.setStyle(TableStyle([
        ('VALIGN',(0,0),(-1,-1),'MIDDLE'),
        ('ALIGN',(0,0),(0,0),'LEFT'),
        ('ALIGN',(2,0),(2,0),'LEFT'),
        ('LEFTPADDING',(0,0),(-1,-1),0),
        ('RIGHTPADDING',(0,0),(-1,-1),0),
        ('TOPPADDING',(0,0),(-1,-1),0),
        ('BOTTOMPADDING',(0,0),(-1,-1),0),
    ]))
    s.append(logo_row)
    s.append(sp(20))

    # Big title
    s.append(P('JONES EXCAVATING', cover_title2))
    s.append(P('&amp;', cover_amp))
    s.append(P('CALLUS FABRICATION', cover_title))
    s.append(sp(24))

    # Dual rule
    rl = Table([['']], colWidths=[1.4*inch])
    rl.setStyle(TableStyle([('LINEBELOW',(0,0),(-1,-1),2,ORANGE),
                            ('TOPPADDING',(0,0),(-1,-1),0),
                            ('BOTTOMPADDING',(0,0),(-1,-1),0)]))
    rr = Table([['']], colWidths=[1.4*inch])
    rr.setStyle(TableStyle([('LINEBELOW',(0,0),(-1,-1),2,SPARK),
                            ('TOPPADDING',(0,0),(-1,-1),0),
                            ('BOTTOMPADDING',(0,0),(-1,-1),0)]))
    drule = Table([[rl, Spacer(0.15*inch,1), rr]],
                  colWidths=[1.4*inch, 0.15*inch, 1.4*inch])
    drule.setStyle(TableStyle([('LEFTPADDING',(0,0),(-1,-1),0),
                                ('RIGHTPADDING',(0,0),(-1,-1),0)]))
    s.append(drule)
    s.append(sp(24))

    s.append(P('A two-brand digital engagement covering brand, web,', cover_meta))
    s.append(P('search visibility, and social for two Utah contractors.', cover_meta))
    s.append(sp(40))

    meta_row = Table([
        [P('PREPARED FOR', cover_label), P('PROPOSAL VERSION', cover_label), P('STATUS', cover_label)],
        [P('Jones Excavating Co.<br/>Callus Fabrication', cover_meta),
         P('v5  \u00B7  May 2026', cover_meta),
         P('For Review', cover_meta)],
    ], colWidths=[2.4*inch, 2.2*inch, 1.7*inch])
    meta_row.setStyle(TableStyle([
        ('VALIGN',(0,0),(-1,-1),'TOP'),
        ('TOPPADDING',(0,0),(-1,-1),0),
        ('BOTTOMPADDING',(0,0),(-1,-1),0),
        ('LEFTPADDING',(0,0),(-1,-1),0),
        ('RIGHTPADDING',(0,0),(-1,-1),0),
    ]))
    s.append(meta_row)

    # Confidentiality line at bottom of cover
    s.append(sp(28))
    confid_style = S('confid', fontName='Helvetica-Oblique', fontSize=7.5,
                     textColor=GRAY_500, leading=10, alignment=TA_LEFT)
    s.append(P(
        'This proposal contains proprietary methodology and pricing, shared in confidence with '
        'Jones Excavating Co. leadership. Not for external distribution.',
        confid_style))

    s.append(PageBreak())

    # ═══ TOC ═════════════════════════════════════════════════════════════════
    s.append(section_header(0, 'Contents'))
    s.append(sp(8))
    toc_rows = [
        ('01', 'Executive Summary',           '03'),
        ('02', 'The Opportunity',             '04'),
        ('03', 'Brand &amp; Web Strategy',    '07'),
        ('04', 'SEO &amp; Local Search',      '10'),
        ('05', 'Social &amp; Content',        '12'),
        ('06', 'The Marketing Operating System',            '14'),
        ('07', 'Investment &amp; Timeline',   '17'),
        ('08', 'Next Steps',                  '19'),
    ]
    rows = [[P(n, toc_num), P(t, toc_entry), P(p, toc_pg)] for n,t,p in toc_rows]
    toc = Table(rows, colWidths=[0.55*inch, 5.55*inch, 0.5*inch])
    toc.setStyle(TableStyle([
        ('VALIGN',(0,0),(-1,-1),'MIDDLE'),
        ('TOPPADDING',(0,0),(-1,-1),5),
        ('BOTTOMPADDING',(0,0),(-1,-1),5),
        ('LINEBELOW',(0,0),(-1,-1),0.4, GRAY_300),
    ]))
    s.append(toc)
    s.append(PageBreak())

    # ═══ 01 EXECUTIVE SUMMARY ════════════════════════════════════════════════
    s.append(section_header(1, 'Executive Summary',
        kicker='What we are building, who it is for, and why it pays for itself.'))
    s.append(P(
        'Jones Excavating Co. is an 80-year Utah heavy-civil contractor specializing in '
        'excavation and utilities, founded in 1946. Callus Fabrication is its welding and '
        'custom-fabrication arm. Both companies do excellent work. Neither has a digital '
        'presence that reflects it.',
        body_lead))
    s.append(P(
        'This proposal lays out a coordinated plan for two distinct brands, two new '
        'websites, and a 90-day rollout to make both companies easier to find, easier to '
        'vet, and easier to hire than any regional competitor in their category.',
        body))

    s.append(P('What you get', h2))
    s.append(bullet('<b>One coordinated brand system</b> covering both companies \u2014 distinct identities that '
                    'still read as a family.'))
    s.append(bullet('<b>Two production websites</b>: a refreshed jonesexcavating.com and a new callusfabrication.com.'))
    s.append(bullet('<b>Local SEO + Google Business Profile (GBP) overhaul</b> to reposition both brands in the '
                    'highest-leverage channel for this category.'))
    s.append(bullet('<b>Social media content engine</b> \u2014 LinkedIn-led, sustainable post-launch.'))
    s.append(bullet('<b>90-day fixed-price build</b>, with monthly retainer options for ongoing support and '
                    'maintenance.'))

    s.append(sp(8))
    s.append(callout(
        'Why Act Now',
        'Construction investment is at a decade high \u2014 putting a spotlight on exactly the '
        'specialized work Jones delivers. Now is the time to turn that market momentum into '
        'wins. A polished, modern digital presence positions Jones as the clear, credible '
        'choice for owners, GCs, and engineers, elevates you in search results, and helps you '
        'recruit the field and office talent needed to scale. Just one additional mid-size '
        'deep-foundation or shoring award can range from $500K\u2013$5M+; if improved '
        'visibility and trust help Jones win even one new bid per year, this investment can '
        'pay back 10\u00D7\u2013100\u00D7.',
        bg=CHARCOAL, accent=ORANGE, big_title=True))

    s.append(PageBreak())

    # ═══ 02 THE OPPORTUNITY (MARKET DATA) ════════════════════════════════════
    s.append(section_header(2, 'The Opportunity',
        kicker='Where Jones stands against competitors.'))

    s.append(P(
        'Before designing anything, we conducted market research. Two takeaways drive this proposal: '
        '<b>(1) LinkedIn is where Utah heavy-civil B2B happens</b>, and <b>(2) Google Business Profile '
        'is critical to building local awareness of your business.</b> Both are areas of opportunity for Jones.',
        body_lead))

    s.append(P('LinkedIn Competitive Landscape', h2))
    s.append(P(
        'LinkedIn is where commercial GCs, owners\u2019 reps, developers, and project managers '
        'vet contractors before short-listing. Jones can become a player within this space within '
        '12 months.',
        body))

    s.append(comp_table([
        ['Company',                     'LinkedIn',  'Founded',  'Notes'],
        ['BHI',                         '~19k',      '~2000',    'Excavation + construction'],
        ['W.W. Clyde &amp; Co.',        '~14k',      '1926',     'Clyde Companies'],
        ['Staker Parson',               '~6,100',    '1952',     'Materials + civil'],
        ['Geneva Rock Products',        '~6,000',    '1954',     'Clyde Companies'],
        ['Sunroc / Suncore',            '~6,000',    '1937',     'Materials + civil'],
        ['Hadco',                       '~1,300',    '1989',     'Excavation'],
        ['Jones Excavating Co.',        '331',       '1946',     ''],
    ]))
    s.append(sp(4))
    s.append(P(
        'LinkedIn followings as of May 2026, rounded. Sources: company LinkedIn pages, '
        'agc-utah.org member directory.',
        ParagraphStyle('cap', fontName='Helvetica-Oblique', fontSize=7.5,
                       textColor=GRAY_500, leading=10)))

    s.append(P('Why this gap matters', h3))
    s.append(bullet('LinkedIn delivers <b>80% of B2B social leads</b> across all sectors and converts '
                    '<b>2.74%</b> visitor-to-lead \u2014 277% higher than Facebook or X.'))
    s.append(bullet('<b>89% of B2B marketers</b> use LinkedIn for lead gen and <b>40%</b> rate it their '
                    'most effective channel.'))
    s.append(bullet('In Utah heavy-civil specifically, LinkedIn following runs roughly <b>33% higher</b> '
                    'than Facebook for the same companies.'))

    s.append(P('Google Business Profile: Win the Map Pack', h2))
    s.append(P(
        'Google Maps is where most buyers build the short list. A search for &quot;excavating contractor '
        'Utah&quot; or &quot;deep foundation Salt Lake City&quot; returns the Map Pack first — star ratings, '
        'reviews, photos, and a one-tap path to call. Miss that real estate and Jones is invisible '
        'at the moment buyer intent is highest. A strong Google Business Profile and an active review '
        'program build instant trust, drive inbound calls, and route qualified traffic straight to the '
        'new website.',
        body))

    s.append(comp_table([
        ['Benchmark',                                           'Strong',    'Typical',   'Gap'],
        ['Google review count (regional civil contractor)',     '100+',      '20\u201380','&lt;10'],
        ['Star rating (realistic ceiling, jobsite category)',   '4.5\u20134.7','4.0\u20134.4','&lt;3.8'],
        ['GBP photos (recent, geo-tagged)',                     '40+',       '10\u201320','&lt;5'],
        ['Owner replies to reviews',                            '100%',      '~50%',      '0%'],
        ['Service area pages (linked from GBP)',                '8\u201312', '3\u20136',  '0\u20132'],
    ], center=True))
    s.append(sp(4))
    s.append(P(
        'Each additional Google review correlates with <b>+80 website visits, +63 direction requests, '
        'and +16 calls</b> per year for the average local business (BrightLocal, 2025). For a contractor '
        'whose average ticket is six figures, the unit economics are obvious.',
        body))

    s.append(PageBreak())

    # ═══ 03 BRAND & WEB STRATEGY ═════════════════════════════════════════════
    s.append(section_header(3, 'Brand &amp; Web Strategy',
        kicker='Two brands, two sites, one coordinated team.'))

    s.append(P(
        'Jones and Callus are different businesses serving different buyers. They should look '
        'related \u2014 same family, same standards \u2014 without sharing a brand.',
        body_lead))

    s.append(P('Jones Excavating Co. \u2014 Brand refresh', h3))
    s.append(P(
        'Jones already has equity. The orange J-mark is the most recognizable element you have, '
        'and 80 years of excavation and utilities work back it up. The refresh sharpens the typography, '
        'modernizes the palette, and tightens the visual system while keeping core elements people know.',
        body))
    s.append(bullet('Logo: keep the orange mark; clean up the lockup and add a horizontal version for '
                    'web/social.'))
    s.append(bullet('Palette: anchor on charcoal + Jones orange; add an amber accent for highlights '
                    'and a clean off-white for type-heavy panels.'))
    s.append(bullet('Typography: bold condensed display + readable Inter body. Industrial feel, '
                    'web-safe, performant.'))
    s.append(bullet('Photography: replace stock with on-site photos from active jobs (we run a half-day '
                    'shoot in week 2).'))

    s.append(P('Callus Fabrication \u2014 Brand build (Spark direction)', h3_spark))
    s.append(P(
        'Callus is new enough to be designed deliberately. The Spark direction \u2014 industrial '
        'badge, dark steel, glove-and-spark mark, cropped-iron typography \u2014 lands the brand '
        'where its buyers already are: GCs, plant managers, foremen who hire welders by the hour '
        'or by the project.',
        body))
    s.append(bullet('Logo: glove + spark mark, finalized, with horizontal lockup and stacked variant.'))
    s.append(bullet('Palette: black + spark red + amber, with charcoal and metal grays for depth.'))
    s.append(bullet('Voice: short sentences. Trade language. No corporate filler. "Built tough. Welded right."'))
    s.append(bullet('Family link: Callus carries a "backed by Jones Excavating Co." line in the banner, '
                    'about, and footer \u2014 borrowing trust without diluting the new brand.'))

    s.append(P('Web build \u2014 both sites', h2))
    s.append(P(
        'Both sites ship on the same modern stack so they are fast, easy to update, and search-friendly. '
        'Each site is built for the company\u2019s needs.',
        body))

    s.append(P('Architecture', h3))
    s.append(bullet('Static-first build (HTML/CSS/JS) with a content management system for blog and project '
                    'entries, so updates take minutes, not engineering tickets.'))
    s.append(bullet('Designed for mobile first \u2014 too many websites get built for desktop and feel broken on '
                    'a phone. Most contractor staff and customers browse from the jobsite or the truck.'))
    s.append(bullet('Maximize search outputs by using schema.org on every page (LocalBusiness, Service, '
                    'Project) so search engines can read the site cleanly.'))

    s.append(P('Page set', h3))
    s.append(two_col([
        P('<b>jonesexcavating.com</b>', body),
        bullet('Home (banner, services, projects, callout)'),
        bullet('Services (with sub-pages: excavation, shoring, deep foundation, trucking)'),
        bullet('Projects (case studies, filterable)'),
        bullet('About (history, leadership, equipment yard)'),
        bullet('Careers'),
        bullet('Service areas'),
        bullet('Contact / Get a quote'),
    ], [
        P('<b>callusfabrication.com</b>', body),
        bullet('Home (split banner, services, shop, projects)'),
        bullet('Services (mobile welding, MIG/TIG/Stick, line boring, OFC-A)'),
        bullet('Shop (capabilities, equipment, certifications)'),
        bullet('Projects (gallery)'),
        bullet('About / family of companies'),
        bullet('Service areas'),
        bullet('Contact / 24-hour line'),
    ]))
    s.append(PageBreak())

    # ═══ 04 SEO & LOCAL ═════════════════════════════════════════════════════
    s.append(section_header(4, 'SEO &amp; Local Search',
        kicker='The highest-leverage channel for both brands.', accent=TEAL))

    s.append(P(
        'For excavating and fabrication, the search journey is local-first: someone types a '
        'job-site need into Google, sees a map of local providers, and calls one of the top '
        'three. The website matters \u2014 but only after they have already found you on the map.',
        body_lead))

    s.append(P('Google Business Profile (GBP) \u2014 day-one work', h3_teal))
    s.append(bullet('Claim and verify both GBPs (Jones is partially claimed; Callus needs to be added).'))
    s.append(bullet('Categorize precisely \u2014 primary plus all relevant secondaries (Excavating Contractor, '
                    'Earthworks, General Contractor, Construction Services for Jones; Welder, Welding Supply, '
                    'Custom Fabricator for Callus).'))
    s.append(bullet('Service areas: every Utah county you actually work in, with named locality pages on '
                    'the website to back them up.'))
    s.append(bullet('Hours, contacts, attributes, accessibility, payment methods, languages \u2014 consistent '
                    'across the web.'))
    s.append(bullet('Add 30+ recent geo-tagged jobsite photos in batch, then continue adding 4\u20136 per month '
                    'consistently.'))
    s.append(bullet('Review program: a text template to send to clients after every completed job, with a '
                    'direct GBP link.'))
    s.append(bullet('Owner replies (target within 48 hours) on every review, positive or negative.'))

    s.append(P('Technical SEO foundation', h3_teal))
    s.append(bullet('Add structured data tags to every relevant page (business, services, projects, FAQs) '
                    'so search engines can read your site cleanly.'))
    s.append(bullet('Tune every page for fast load times \u2014 optimized images, lazy loading, and modern fonts '
                    'so the site feels instant on a phone or laptop.'))
    s.append(bullet('Smart internal linking: service pages connect to relevant project case studies, helping '
                    'visitors and search engines find the right work.'))
    s.append(bullet('Submit sitemaps and connect to the major search engines (Google, Bing) on day one so '
                    'pages get indexed quickly.'))
    s.append(bullet('Consistent business listings \u2014 name, address, and phone match across 30+ directories '
                    '(BBB, AGC of Utah, Yelp, BuildZoom, Procore, and others).'))

    s.append(P('Target keywords \u2014 first wave', h3_teal))
    s.append(two_col([
        P('<b>Jones Excavating</b>', body),
        bullet('excavating contractor utah'),
        bullet('deep foundation salt lake city'),
        bullet('shoring contractor utah'),
        bullet('site work contractor west jordan'),
        bullet('drilling contractor wasatch front'),
        bullet('utility excavation utah county'),
        bullet('commercial excavation salt lake'),
    ], [
        P('<b>Callus Fabrication</b>', body),
        bullet('mobile welder west jordan'),
        bullet('welding contractor utah'),
        bullet('custom fabrication salt lake'),
        bullet('mig welding wasatch front'),
        bullet('line boring utah'),
        bullet('industrial welding salt lake'),
        bullet('emergency welding utah'),
    ]))

    s.append(PageBreak())

    # ═══ 05 SOCIAL & CONTENT ═════════════════════════════════════════════════
    s.append(section_header(5, 'Social &amp; Content',
        kicker='Where the comp set already lives \u2014 and where Jones can catch up fastest.'))

    s.append(P(
        'Two channels matter: <b>LinkedIn</b> (B2B vetting, PM-to-PM trust) and <b>Instagram</b> '
        '(jobsite proof points, recruiting, owner-to-owner credibility). Facebook is maintenance only. '
        'TikTok is not part of this plan.',
        body_lead))

    s.append(P('LinkedIn \u2014 the priority channel', h3))
    s.append(bullet('Two channels: <b>linkedin.com/company/jones-excavating-co</b> already exists; '
                    'we will refresh the page, banner, about copy, and post cadence. A new Callus '
                    'company page launches with the website.'))
    s.append(bullet('Posting cadence: <b>3 posts/week per brand</b> mixing project milestones, behind-the-scenes '
                    'shop/yard content, hiring posts, and short ownership notes.'))
    s.append(bullet('Employee advocacy: foremen, PMs, and ownership reshare from personal accounts to boost '
                    'social engagement and amplify reach.'))
    s.append(bullet('Targeted connection campaign: 50\u2013100 thoughtful outbound connections per month '
                    '(Utah GCs, owners\u2019 reps, developers, public works PMs).'))

    s.append(P('Content pillars', h3))
    s.append(two_col([
        P('<b>Jones</b>', body),
        bullet('Jobsite milestones (with permission)'),
        bullet('Equipment in action (drone, B-roll)'),
        bullet('Crew spotlights / safety wins'),
        bullet('Project case studies (50/50 LinkedIn + site)'),
        bullet('Industry commentary from leadership'),
    ], [
        P('<b>Callus</b>', body),
        bullet('Welding before/after (mobile + shop)'),
        bullet('Time-lapse fab work (CNC, plasma, line bore)'),
        bullet('Same-day service moments'),
        bullet('Crew skill spotlights'),
        bullet('Quick how-it-was-done write-ups'),
    ]))

    s.append(P('Instagram + Facebook', h3))
    s.append(bullet('Instagram leads on jobsite imagery and short-form video. Cross-posted to Facebook '
                    'automatically (we will not run two separate content tracks).'))
    s.append(bullet('Reels: monthly time-lapse or build-progression video for each brand. Cheap to produce, '
                    'high recruiting and credibility lift.'))
    s.append(bullet('Geo-tagging every post (site city + Utah) for local discovery.'))

    s.append(P('Content engine', h3))
    s.append(bullet('<b>Professional photography &amp; videography</b> \u2014 drone, jobsite, and shop coverage. '
                    'Quarterly half-day shoots at active jobsites and the Callus shop, captured by our '
                    'team and edited in-house. One shoot feeds 8\u201310 weeks of posts across both brands.'))
    s.append(bullet('Shared content library (Dropbox or similar) so PMs and foremen can drop in raw '
                    'photos and we do the editing.'))
    s.append(bullet('Monthly performance review: top posts, follower growth, engagement, lead-source '
                    'attribution where possible.'))

    s.append(callout(
        'Realistic 12-month targets',
        '<b>Jones</b> \u2014 LinkedIn 331 \u2192 2,500+, Instagram 0 \u2192 800+, Facebook 0 \u2192 500+. &nbsp; '
        '<b>Callus</b> \u2014 LinkedIn 0 \u2192 1,000+, Instagram 0 \u2192 1,000+, Facebook 0 \u2192 500+. &nbsp; '
        'Combined cross-platform reach: 5\u201310\u00d7 current. Direct attributable inbound: '
        '4\u20138 qualified leads per month per brand by month 9.',
        bg=CHARCOAL, accent=ORANGE))
    s.append(PageBreak())

    # ═══ 06 THE MARKETING OS ═════════════════════════════════════════════════
    s.append(section_header(6, 'The Marketing Operating System',
        kicker='An AI-driven marketing system you own, not an agency you rent.'))

    s.append(P(
        'Most marketing engagements end one of two ways: the agency keeps billing forever, or '
        'the client tries to take it in-house and the work quietly stops. Neither outcome is good '
        'for Jones or Callus. This chapter describes the third option.',
        body_lead))

    s.append(P(
        'The Marketing Operating System is a custom-built, AI-agent-driven system that automates 80% of the '
        'ongoing marketing work \u2014 social posts, review responses, SEO content, lead triage \u2014 '
        'while keeping a human (you) in the approval seat for every published artifact. We build it, '
        'we train it on your voice, and we hand it over. After 90 days you own a working system, not '
        'an agency dependency.',
        body))

    s.append(P('Why this is possible now', h2))
    s.append(bullet('AI models are now good enough to draft brand-voice content from a 2-sentence note + '
                    '3 photos sent by a foreman from a jobsite.'))
    s.append(bullet('Modern workflow tools can route those drafts into approval queues, post on '
                    'schedule, and track performance without custom engineering.'))
    s.append(bullet('Google, Meta, and LinkedIn APIs are stable and accessible \u2014 we are no longer '
                    'screen-scraping or fighting tooling.'))
    s.append(bullet('The result: marketing work that used to require a part-time hire can run on a '
                    '15-minute-per-day approval routine for an office manager.'))

    s.append(P('The five agents', h2))
    s.append(P(
        'Five specialized AI agents handle distinct jobs. Each one drafts; a human approves. '
        'Nothing publishes without a click.',
        body))

    s.append(P('Field-to-Content Agent', h3))
    s.append(P(
        'A foreman or PM texts a number with photos and a short note ("Finished the Lehi sewer '
        'tie-in, biggest pour of the year, 14 hours"). The agent generates a LinkedIn post, '
        'Google Business Profile post, Instagram caption, blog snippet, and internal newsletter '
        'blurb \u2014 all in Jones or Callus voice. Office manager taps approve.',
        body))

    s.append(P('Reputation Agent', h3))
    s.append(P(
        'Watches Google reviews and Facebook recommendations across both brands. Drafts a brand-voice '
        'reply within hours, calibrated to the rating (gracious for 5\u2605, measured with a private '
        'resolution offer for 1\u20132\u2605). Office manager approves; reply posts.',
        body))

    s.append(P('SEO Content Agent', h3))
    s.append(P(
        'Each month: pulls keyword movement, identifies 1\u20132 service-area pages or blog posts that '
        'would close ranking gaps with competitors, drafts the full page, and queues it for review. '
        'Closes the gap between you and your competitors over 12 months without a copywriter.',
        body))

    s.append(P('Lead Triage Agent', h3))
    s.append(P(
        'Sits behind the website contact form and (optionally) a site chat widget. Classifies inbound '
        'inquiries (excavation / fabrication / spam / general), extracts contact info and project '
        'signals, drafts an internal message alert and a 3-line auto-reply. Routes hot leads '
        'directly to estimating in under a minute.',
        body))

    s.append(P('Orchestrator + Approval Queue', h3))
    s.append(P(
        'A central scheduler routes events to the right agent and lands all drafts in a single '
        'approval queue \u2014 one screen, one inbox, every brand. Approved items publish on the '
        'right cadence. Rejected items improve the AI prompts inside each agent.',
        body))

    s.append(callout(
        'What this replaces',
        'A part-time marketing coordinator at $50,000\u2013$70,000/yr fully loaded, or an agency '
        'retainer at $1,500\u20133,000/mo. The Marketing Operating System does the same job with a 15-minute '
        'approval routine and roughly $200/mo in infrastructure.',
        bg=CHARCOAL, accent=ORANGE))

    s.append(PageBreak())

    s.append(P('System architecture', h2))
    s.append(P(
        'The pipeline is intentionally simple. Each box is replaceable; nothing is locked in.',
        body))

    # Inline architecture diagram as a table-of-cards
    arch_lbl  = S('AL', fontName='Helvetica-Bold', fontSize=7, textColor=ORANGE, leading=10, alignment=TA_CENTER)
    arch_box  = S('AB', fontName='Helvetica-Bold', fontSize=8.5, textColor=BLACK, leading=11, alignment=TA_CENTER)
    arch_note = S('AN', fontName='Helvetica', fontSize=7, textColor=GRAY_500, leading=9.5, alignment=TA_CENTER)
    arch_arrow= S('AA', fontName='Helvetica-Bold', fontSize=14, textColor=ORANGE, leading=16, alignment=TA_CENTER)

    def abox(label, title, note, bg=GRAY_50, accent=ORANGE):
        inner = Table([
            [P(label.upper(), arch_lbl)],
            [P(title, arch_box)],
            [P(note, arch_note)],
        ], colWidths=[1.95*inch])
        inner.setStyle(TableStyle([
            ('BACKGROUND',(0,0),(-1,-1), bg),
            ('TOPPADDING',(0,0),(-1,-1), 6),
            ('BOTTOMPADDING',(0,0),(-1,-1), 6),
            ('LEFTPADDING',(0,0),(-1,-1), 8),
            ('RIGHTPADDING',(0,0),(-1,-1), 8),
            ('LINEBEFORE',(0,0),(0,-1), 2.5, accent),
        ]))
        return inner

    arr = P('\u2192', arch_arrow)

    # Row 1: Inputs
    row1 = Table([[
        abox('INPUT', 'Foreman text-in', 'Photos + 2-sentence note via SMS'),
        arr,
        abox('AGENT', 'Field-to-Content', 'Drafts 5 outputs in brand voice'),
        arr,
        abox('HUMAN', 'Approval queue', 'Office manager: 15 min/day'),
    ]], colWidths=[1.95*inch, 0.3*inch, 1.95*inch, 0.3*inch, 1.95*inch])
    row1.setStyle(TableStyle([
        ('VALIGN',(0,0),(-1,-1),'MIDDLE'),
        ('TOPPADDING',(0,0),(-1,-1),4),
        ('BOTTOMPADDING',(0,0),(-1,-1),4),
        ('LEFTPADDING',(0,0),(-1,-1),0),
        ('RIGHTPADDING',(0,0),(-1,-1),0),
    ]))
    s.append(row1)
    s.append(sp(8))

    row2 = Table([[
        abox('INPUT', 'Google review', 'New review on either brand', accent=TEAL),
        arr,
        abox('AGENT', 'Reputation', 'Drafts reply tuned to rating', accent=TEAL),
        arr,
        abox('HUMAN', 'Approval queue', 'Same single inbox', accent=TEAL),
    ]], colWidths=[1.95*inch, 0.3*inch, 1.95*inch, 0.3*inch, 1.95*inch])
    row2.setStyle(TableStyle([
        ('VALIGN',(0,0),(-1,-1),'MIDDLE'),
        ('TOPPADDING',(0,0),(-1,-1),4),
        ('BOTTOMPADDING',(0,0),(-1,-1),4),
        ('LEFTPADDING',(0,0),(-1,-1),0),
        ('RIGHTPADDING',(0,0),(-1,-1),0),
    ]))
    s.append(row2)
    s.append(sp(8))

    row3 = Table([[
        abox('INPUT', 'Monthly schedule', 'Keyword + ranking data', accent=SPARK),
        arr,
        abox('AGENT', 'SEO Content', 'Drafts service-area page', accent=SPARK),
        arr,
        abox('HUMAN', 'Approval queue', 'Edit + publish to site', accent=SPARK),
    ]], colWidths=[1.95*inch, 0.3*inch, 1.95*inch, 0.3*inch, 1.95*inch])
    row3.setStyle(TableStyle([
        ('VALIGN',(0,0),(-1,-1),'MIDDLE'),
        ('TOPPADDING',(0,0),(-1,-1),4),
        ('BOTTOMPADDING',(0,0),(-1,-1),4),
        ('LEFTPADDING',(0,0),(-1,-1),0),
        ('RIGHTPADDING',(0,0),(-1,-1),0),
    ]))
    s.append(row3)
    s.append(sp(8))

    row4 = Table([[
        abox('INPUT', 'Site contact form', 'Free-form inquiry text'),
        arr,
        abox('AGENT', 'Lead Triage', 'Classifies + drafts alert'),
        arr,
        abox('OUTPUT', 'Estimating + auto-reply', 'Hot lead routed in &lt;1 min'),
    ]], colWidths=[1.95*inch, 0.3*inch, 1.95*inch, 0.3*inch, 1.95*inch])
    row4.setStyle(TableStyle([
        ('VALIGN',(0,0),(-1,-1),'MIDDLE'),
        ('TOPPADDING',(0,0),(-1,-1),4),
        ('BOTTOMPADDING',(0,0),(-1,-1),4),
        ('LEFTPADDING',(0,0),(-1,-1),0),
        ('RIGHTPADDING',(0,0),(-1,-1),0),
    ]))
    s.append(row4)

    s.append(sp(14))
    s.append(P(
        'Built on modern orchestration tools and platform APIs (LinkedIn, Google Business Profile, '
        'Meta). Self-hosted; no monthly SaaS lock-in.',
        body))

    s.append(P('Three-phase ownership transfer', h2))
    s.append(P(
        'You do not buy this and figure it out. We run it with you, then alongside you, then behind '
        'you. By month 7 your office manager is running the system in 15 minutes a day and we are on '
        'a maintenance retainer.',
        body))

    s.append(phase_card_basic('Phase 1', 'Concierge', 'Months 1\u20133',
        ['We run the OS day-to-day while training it on your voice',
         '90 days of approved content captured as training data',
         'Office manager observes; we document the standard operating procedures (everything on how to run the system)']))
    s.append(sp(6))
    s.append(phase_card_basic('Phase 2', 'Co-pilot', 'Months 4\u20136',
        ['Office manager runs the approval queue; we maintain the system',
         'Weekly check-ins; we handle prompt tuning + integrations',
         'Performance review at month 6 to right-size phase 3']))
    s.append(sp(6))
    s.append(phase_card_basic('Phase 3', 'Self-serve', 'Month 7+',
        ['You run it. We are on retainer for system maintenance only',
         'Quarterly strategy review + prompt updates as Google/AI shift',
         'Cancel anytime; the system keeps running either way']))

    s.append(sp(10))
    s.append(callout(
        'What you own at the end',
        'You own all your data, content, brand voice configuration, and historical drafts. The '
        'underlying Marketing Operating System — the agents, prompts, and orchestration code — stays our IP, with '
        'a perpetual license to operate it as long as you are on a retainer tier (including the '
        '$350/mo Self-serve tier). Move on whenever you want; your data, content, and configuration '
        'come with you.',
        bg=CHARCOAL, accent=ORANGE))
    s.append(PageBreak())

    # ═══ 07 INVESTMENT & TIMELINE ════════════════════════════════════════════
    s.append(section_header(7, 'Investment &amp; Timeline',
        kicker='Fixed-price build, three-tier ongoing model.'))

    s.append(P('Build phase \u2014 fixed price', h2))

    s.append(price_row('Brand system \u2014 Jones',
                       '$3,500',
                       'Logo refresh, palette, typography, usage guide.'))
    s.append(price_row('Brand system \u2014 Callus',
                       '$4,500',
                       'New brand identity from the ground up — logo system, palette, tone of voice, and brand guidelines.'))
    s.append(price_row('Website \u2014 jonesexcavating.com',
                       '$8,500',
                       '7 templated pages + service-area pages.'))
    s.append(price_row('Website \u2014 callusfabrication.com',
                       '$7,500',
                       '7 templated pages + shop section.'))
    s.append(price_row('SEO foundation (both)',
                       '$3,500',
                       'Google Business Profile setup, schema, citations, technical audit, on-page.'))
    s.append(price_row('Content shoot + initial library',
                       '$2,500',
                       'Half-day jobsite + shop photo/video; 90-day post library.'))
    s.append(price_row('Marketing Operating System build',
                       '$12,000',
                       '5 agents, orchestrator, approval queue, brand-voice training, integrations.'))
    s.append(price_row('Build phase total',
                       '$42,000',
                       'One-time. 40% on signature, 30% at design approval, 30% at launch.',
                       highlight=True))

    s.append(P('Ongoing \u2014 three tiers', h2))
    s.append(P(
        'Pick the tier that matches how hands-on you want to be. You can step down a tier any time '
        'after month 3 with 30 days\u2019 notice.',
        body))

    s.append(price_row('Concierge \u2014 we run it',
                       '$1,900 / mo',
                       'Months 1\u20133 default. We operate the OS, you receive a monthly report.',
                       highlight=False))
    s.append(price_row('Co-pilot \u2014 you run it, we maintain',
                       '$850 / mo',
                       'Recommended for months 4\u20136. Office manager runs queue; we tune system.'))
    s.append(price_row('Self-serve \u2014 system maintenance',
                       '$350 / mo',
                       'Month 7+. Quarterly strategy review, prompt updates, integration patches.'))
    s.append(sp(6))
    s.append(P(
        '<b>Plus infrastructure:</b> ~$200/mo in API + hosting costs (AI provider, hosting, '
        'scheduler, email), billed at cost or paid directly to providers \u2014 your choice.',
        body))

    s.append(P('Timeline \u2014 90 days to launch', h2))

    def phase_card(num, title, weeks, items, bg=GRAY_50, accent=ORANGE):
        ph_s = S('ps', fontName='Helvetica-Bold', fontSize=8, textColor=accent, leading=11)
        ti_s = S('pt', fontName='Helvetica-Bold', fontSize=11, textColor=BLACK, leading=14)
        wk_s = S('pw', fontName='Helvetica-Bold', fontSize=7.5, textColor=GRAY_500, leading=10)
        it_s = S('pi', fontName='Helvetica',     fontSize=8.5, textColor=GRAY_700, leading=12)
        items_html = '<br/>'.join([f'\u2022 {x}' for x in items])
        data = [[P(num, ph_s), P(title, ti_s), P(weeks.upper(), wk_s), P(items_html, it_s)]]
        t = Table(data, colWidths=[0.5*inch, 1.7*inch, 0.9*inch, 3.5*inch])
        t.setStyle(TableStyle([
            ('BACKGROUND',(0,0),(-1,-1), bg),
            ('TOPPADDING',(0,0),(-1,-1),12),
            ('BOTTOMPADDING',(0,0),(-1,-1),12),
            ('LEFTPADDING',(0,0),(-1,-1),12),
            ('RIGHTPADDING',(0,0),(-1,-1),12),
            ('VALIGN',(0,0),(-1,-1),'TOP'),
            ('LINEBEFORE',(0,0),(0,-1),3, accent),
        ]))
        return t

    s.append(phase_card('01', 'Discovery + Brand', 'Weeks 1\u20133',
        ['Stakeholder interviews; site audit',
         'Jones brand refresh; Callus brand build',
         'Photography day at active jobsites + shop',
         'Brand approval gate']))
    s.append(sp(6))
    s.append(phase_card('02', 'Design + Build', 'Weeks 4\u20139',
        ['Both sites designed and built page by page',
         'Content drafted with leadership input',
         'GBP optimization + citation pass',
         'Design and content approval gates']))
    s.append(sp(6))
    s.append(phase_card('03', 'Launch + Activate', 'Weeks 10\u201312',
        ['Soft launch \u2192 final QA \u2192 hard launch',
         'LinkedIn relaunch with refreshed pages and content',
         'Review ask program activated for both brands',
         'Retainer phase begins']))
    s.append(PageBreak())

    # ═══ 08 NEXT STEPS ═══════════════════════════════════════════════════════
    s.append(section_header(8, 'Next Steps',
        kicker='What we need to start, and when we can start.'))

    s.append(P('Approvals required', h3))
    s.append(bullet('Sign-off on this proposal (this PDF + a brief MSA).'))
    s.append(bullet('Decision on Callus direction \u2014 the Spark direction is the recommended path '
                    'and what the website concept reflects today.'))
    s.append(bullet('Designated point of contact at each company for weekly check-ins.'))

    s.append(P('What we need from you', h3))
    s.append(bullet('GBP and social account access (or the green light to claim/create).'))
    s.append(bullet('Domain access for both jonesexcavating.com and callusfabrication.com.'))
    s.append(bullet('Two upcoming jobsites we can shoot in weeks 2\u20133.'))
    s.append(bullet('A list of 3\u20135 case-study-worthy projects from the last 5 years.'))

    s.append(P('Kickoff', h3))
    s.append(P(
        'On signature we hold a 60-minute kickoff with leadership from both companies, agree on the '
        'first jobsite shoot date, and start the brand work the same week. The 90-day clock starts '
        'on signature.',
        body))

    s.append(sp(20))
    s.append(callout(
        'A note on the work',
        'Jones has built something real over four generations. Callus is a chance to build '
        'something new on top of that foundation. The deliverables in this proposal exist to '
        'serve that, not the other way around. If anything in here does not fit how you want '
        'to be in the world, tell us and we will adjust before we start. We work for you.',
        bg=CHARCOAL, accent=ORANGE))

    s.append(sp(28))

    # Sign-off block
    sign_lbl = S('SL', fontName='Helvetica-Bold', fontSize=8, textColor=ORANGE, leading=11)
    sign_body= S('SB', fontName='Helvetica',      fontSize=9, textColor=GRAY_700, leading=13)
    sign_line= S('SLn',fontName='Helvetica-Bold', fontSize=10, textColor=BLACK, leading=14)

    sign_data = [
        [P('PREPARED BY', sign_lbl), '', P('APPROVED BY', sign_lbl)],
        [P('Project Lead', sign_body), '', P('Jones Excavating Co. \u2014 Authorized Signer', sign_body)],
        [P('_________________________', sign_line), '', P('_________________________', sign_line)],
        [P('Date', sign_body), '', P('Date', sign_body)],
    ]
    sign = Table(sign_data, colWidths=[2.7*inch, 0.5*inch, 3.4*inch])
    sign.setStyle(TableStyle([
        ('VALIGN',(0,0),(-1,-1),'TOP'),
        ('TOPPADDING',(0,0),(-1,-1),3),
        ('BOTTOMPADDING',(0,0),(-1,-1),3),
        ('LEFTPADDING',(0,0),(-1,-1),0),
        ('RIGHTPADDING',(0,0),(-1,-1),0),
    ]))
    s.append(sign)

    # Build
    doc.build(s, onFirstPage=cb.on_page, onLaterPages=cb.on_page)
    print(f'PDF saved -> {OUTPUT}')

if __name__ == '__main__':
    build()
