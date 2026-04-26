"""
One-page executive summary — leave-behind for Jen.
Designed to email or hand over before the full v4 proposal.
"""
import os
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image, HRFlowable
)
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT
from reportlab.lib.colors import HexColor
from reportlab.lib.utils import ImageReader

BLACK    = HexColor('#0C0E10')
CHARCOAL = HexColor('#161A1D')
ORANGE   = HexColor('#E8621A')
AMBER    = HexColor('#F5A623')
WHITE    = HexColor('#FFFFFF')
GRAY_50  = HexColor('#FAFAF8')
GRAY_300 = HexColor('#D1CFC9')
GRAY_500 = HexColor('#8A8880')
GRAY_700 = HexColor('#4A4845')

W, H = letter
BASE = "/Users/tylertoone/Desktop/Claude Work/inbox/excavating-site"
JONES_LOGO  = os.path.join(BASE, "jones-assets/jones-logo-orange.png")
CALLUS_LOGO = os.path.join(BASE, "callus-logo-concepts/callus-logo-spark.png")
OUTPUT      = os.path.join(BASE, "outputs/jones_callus_one_pager.pdf")

def S(n, **kw): return ParagraphStyle(n, **kw)

eyebrow = S('eb', fontName='Helvetica-Bold', fontSize=8, textColor=ORANGE,
            leading=11, spaceAfter=6, alignment=TA_LEFT)
title   = S('ti', fontName='Helvetica-Bold', fontSize=24, textColor=BLACK,
            leading=27, spaceAfter=4)
subtitle= S('st', fontName='Helvetica-Oblique', fontSize=11, textColor=GRAY_500,
            leading=14, spaceAfter=12)
h2      = S('h2', fontName='Helvetica-Bold', fontSize=11, textColor=ORANGE,
            leading=14, spaceBefore=10, spaceAfter=4)
body    = S('bd', fontName='Helvetica', fontSize=9, textColor=GRAY_700,
            leading=12.5, spaceAfter=5)
body_b  = S('bdb',fontName='Helvetica-Bold', fontSize=9, textColor=BLACK,
            leading=12.5, spaceAfter=5)
small   = S('sm', fontName='Helvetica', fontSize=7.5, textColor=GRAY_500,
            leading=10)
white_h = S('wh', fontName='Helvetica-Bold', fontSize=10, textColor=WHITE, leading=13)
white_b = S('wb', fontName='Helvetica',     fontSize=9,  textColor=WHITE, leading=12.5)
price_n = S('pn', fontName='Helvetica-Bold', fontSize=18, textColor=ORANGE,
            leading=22, alignment=TA_CENTER)
price_l = S('pl', fontName='Helvetica-Bold', fontSize=7,  textColor=GRAY_500,
            leading=10, alignment=TA_CENTER)

def bullet(t):
    return Paragraph(f'<font color="#E8621A"><b>\u25AA</b></font>  {t}',
                     S('bu', fontName='Helvetica', fontSize=9, textColor=GRAY_700,
                       leading=12.5, leftIndent=10, spaceAfter=3))

def stat_card(num, label):
    t = Table([[Paragraph(num, price_n)], [Paragraph(label, price_l)]],
              colWidths=[1.4*inch])
    t.setStyle(TableStyle([
        ('BACKGROUND',(0,0),(-1,-1), GRAY_50),
        ('TOPPADDING',(0,0),(-1,-1), 8),
        ('BOTTOMPADDING',(0,0),(-1,-1), 10),
        ('LINEBEFORE',(0,0),(0,-1), 2.5, ORANGE),
    ]))
    return t

class Cover:
    def on_page(self, c, doc):
        c.saveState()
        c.setFillColor(BLACK)
        c.rect(0, H-50, W, 50, fill=1, stroke=0)
        # Jones logo
        try:
            img = ImageReader(JONES_LOGO)
            iw, ih = img.getSize()
            ratio = ih / iw
            disp_w = 90
            disp_h = disp_w * ratio
            c.drawImage(img, 36, H - 28 - disp_h/2,
                        width=disp_w, height=disp_h, mask='auto')
        except Exception:
            pass
        c.setFillColor(WHITE)
        c.setFont('Helvetica-Bold', 8)
        c.drawRightString(W-36, H-30, 'EXECUTIVE SUMMARY  ·  APRIL 2026')
        # Footer
        c.setFillColor(GRAY_500)
        c.setFont('Helvetica', 7)
        c.drawString(36, 24,
            'Full v4 proposal: coolnerd-tt.github.io/jonesexcavating/outputs/jones_callus_proposal_v4.pdf')
        c.drawRightString(W-36, 24, 'Page 1 of 1')
        c.restoreState()

def build():
    doc = SimpleDocTemplate(OUTPUT, pagesize=letter,
                            leftMargin=0.5*inch, rightMargin=0.5*inch,
                            topMargin=0.85*inch, bottomMargin=0.55*inch,
                            title='Jones x Callus - Executive Summary')
    s = []
    s.append(Paragraph('PROPOSAL AT A GLANCE', eyebrow))
    s.append(Paragraph('Jones &amp; Callus &mdash; 2026 Digital Engagement', title))
    s.append(Paragraph('Two brands, two websites, one Marketing OS the team owns at the end.', subtitle))
    s.append(HRFlowable(width='100%', thickness=0.5, color=GRAY_300, spaceAfter=10))

    # The opportunity (compressed)
    s.append(Paragraph('The opportunity', h2))
    s.append(Paragraph(
        'Jones is a 79-year Utah heavy-civil contractor with no digital presence to match the work. '
        'Callus is the welding/fab arm with no presence at all. Every direct competitor in the comp set '
        '(W.W. Clyde, Geneva Rock, Staker Parson, Sunroc) has 4,000\u20137,000+ LinkedIn followers and '
        'an active Google Business Profile. One additional bid won per year pays for this engagement '
        '10\u2013100\u00D7 over.', body))

    # Two-column: what we build / what they own
    left = [
        Paragraph('What we build (90 days)', h2),
        bullet('<b>Two brand systems</b> &mdash; Jones refresh + Callus identity build (Spark direction).'),
        bullet('<b>Two production websites</b> &mdash; jonesexcavating.com + callusfabrication.com.'),
        bullet('<b>SEO foundation</b> &mdash; GBP overhaul, schema, citations, target service-area pages.'),
        bullet('<b>Content engine</b> &mdash; jobsite shoot + 90-day post library, both brands.'),
        bullet('<b>Marketing OS</b> &mdash; 5 AI agents, approval queue, Jones brand-voice config.'),
    ]
    right = [
        Paragraph('What you own at handoff', h2),
        bullet('Working code for the Marketing OS &mdash; agents, prompts, integrations.'),
        bullet('Tenant config: brand voice, services, target keywords, all editable YAML.'),
        bullet('90 days of approved content as training data for ongoing tuning.'),
        bullet('All API keys, accounts, and admin access.'),
        bullet('SOPs and a 15-min/day office-manager runbook.'),
    ]
    cols = Table([[left, right]], colWidths=[3.7*inch, 3.7*inch])
    cols.setStyle(TableStyle([
        ('VALIGN',(0,0),(-1,-1),'TOP'),
        ('LEFTPADDING',(0,0),(-1,-1),0),
        ('RIGHTPADDING',(0,0),(-1,-1),12),
        ('TOPPADDING',(0,0),(-1,-1),0),
        ('BOTTOMPADDING',(0,0),(-1,-1),0),
    ]))
    s.append(cols)
    s.append(Spacer(1, 6))

    # Marketing OS quick description
    s.append(Paragraph('The Marketing OS &mdash; new in v4', h2))
    s.append(Paragraph(
        'Foreman texts in 3 photos and 2 sentences from a jobsite. Five agents (Field-to-Content, '
        'Reputation, SEO, Lead Triage, Orchestrator) draft brand-voice posts, replies, pages, and '
        'lead alerts. Office manager taps approve in a single inbox. Nothing publishes without a click. '
        'Replaces a $50\u201370K/yr coordinator with a 15-minute-per-day routine and roughly $200/mo in API + hosting.',
        body))

    # Sample-output callout
    cs = Table([[Paragraph(
        '<b>See it working: </b>'
        'coolnerd-tt.github.io/jonesexcavating/outputs/marketing-os-sample.html '
        '\u2014 real generated drafts, in Jones voice, from one foreman text-in.', white_b)]],
        colWidths=[7.4*inch])
    cs.setStyle(TableStyle([
        ('BACKGROUND',(0,0),(-1,-1), CHARCOAL),
        ('LEFTPADDING',(0,0),(-1,-1),14),
        ('RIGHTPADDING',(0,0),(-1,-1),14),
        ('TOPPADDING',(0,0),(-1,-1),10),
        ('BOTTOMPADDING',(0,0),(-1,-1),10),
        ('LINEBEFORE',(0,0),(0,-1), 3, ORANGE),
    ]))
    s.append(cs)

    # Pricing strip
    s.append(Paragraph('Investment', h2))
    pricing = Table([[
        stat_card('$42K', 'BUILD &mdash; ONE TIME'),
        stat_card('$1,900', 'CONCIERGE &mdash; MO 1\u20133'),
        stat_card('$850', 'CO-PILOT &mdash; MO 4\u20136'),
        stat_card('$350', 'SELF-SERVE &mdash; MO 7+'),
        stat_card('~$200', 'INFRA &mdash; AT COST'),
    ]], colWidths=[1.5*inch]*5)
    pricing.setStyle(TableStyle([
        ('VALIGN',(0,0),(-1,-1),'TOP'),
        ('LEFTPADDING',(0,0),(-1,-1),0),
        ('RIGHTPADDING',(0,0),(-1,-1),5),
    ]))
    s.append(pricing)
    s.append(Spacer(1, 6))
    s.append(Paragraph(
        'Tier-down with 30 days\u2019 notice after month 3. The system keeps running either way.',
        small))

    # 90-day timeline strip
    s.append(Paragraph('90 days, three phases', h2))
    tl = Table([[
        Paragraph('<b>WEEKS 1\u20133</b><br/>Discovery + Brand', body),
        Paragraph('<b>WEEKS 4\u20139</b><br/>Design + Build + OS', body),
        Paragraph('<b>WEEKS 10\u201312</b><br/>Launch + Activate', body),
    ]], colWidths=[2.5*inch]*3)
    tl.setStyle(TableStyle([
        ('BACKGROUND',(0,0),(-1,-1), GRAY_50),
        ('LEFTPADDING',(0,0),(-1,-1),12),
        ('RIGHTPADDING',(0,0),(-1,-1),12),
        ('TOPPADDING',(0,0),(-1,-1),10),
        ('BOTTOMPADDING',(0,0),(-1,-1),10),
        ('LINEBEFORE',(0,0),(0,-1), 2.5, ORANGE),
        ('LINEBEFORE',(1,0),(1,-1), 2.5, AMBER),
        ('LINEBEFORE',(2,0),(2,-1), 2.5, HexColor('#6FB65A')),
    ]))
    s.append(tl)

    # Next step
    s.append(Spacer(1, 8))
    s.append(Paragraph('Next step', h2))
    s.append(Paragraph(
        'A 60-minute kickoff with leadership from both companies. On signature, the 90-day clock starts '
        'and the first jobsite shoot is scheduled inside week 2.', body_b))

    cb = Cover()
    doc.build(s, onFirstPage=cb.on_page, onLaterPages=cb.on_page)
    print(f'PDF -> {OUTPUT}')

if __name__ == '__main__':
    build()
