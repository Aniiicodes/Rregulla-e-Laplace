from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE


shembujt = [(10, 100), (50, 96), (200, 93)]

prs = Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)


def tekst(slide, x, y, w, h, permbajtja, madhesia=24, ngjyra=(25, 39, 82), bold=False):
    kutia = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = kutia.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = permbajtja
    p.alignment = PP_ALIGN.CENTER
    p.font.size = Pt(madhesia)
    p.font.bold = bold
    p.font.color.rgb = RGBColor(*ngjyra)
    return kutia

for i, (n, perqindja) in enumerate(shembujt, start=1):
    s = n * perqindja / 100
    if not s.is_integer():
        raise ValueError('Numri i vleresimeve pozitive duhet te jete numer i plote.')
    s = int(s)
    rezultati = (s + 1) / (n + 2) * 100
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    bg = slide.background.fill
    bg.solid()
    bg.fore_color.rgb = RGBColor(247, 250, 255)

    shirit = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, Inches(0.16))
    shirit.fill.solid()
    shirit.fill.fore_color.rgb = RGBColor(39, 95, 172)
    shirit.line.fill.background()

    tekst(slide, 1, 0.5, 11.3, 0.7, f'SHEMBULLI {i}', 30, (24, 53, 111), True)
    tekst(slide, 1, 1.35, 11.3, 0.55, f'{n} vlerësime  |  {perqindja}% pozitive', 23)
    tekst(slide, 1.2, 2.25, 10.9, 0.55, f's = {perqindja}/100 × {n} = {s} vlerësime pozitive', 23)
    tekst(slide, 1.2, 3.1, 10.9, 0.55, 'Rregulla e Laplace-it: P = (s + 1) / (n + 2)', 23)
    tekst(slide, 1.2, 3.95, 10.9, 0.65, f'P = ({s} + 1) / ({n} + 2) = {s+1} / {n+2}', 26, (24, 53, 111), True)
    tekst(slide, 1.2, 5.1, 10.9, 0.9, f'Rezultati: {rezultati:.1f}%', 36, (16, 126, 93), True)
    tekst(slide, 1.2, 6.65, 10.9, 0.3, 'Vlerësim i korrigjuar, jo garanci për cilësinë e produktit.', 14, (90, 103, 124))

emri = 'Vetem_3_Llogaritjet_Laplace.pptx'
prs.save(emri)
import os

os.startfile("Vetem_3_Llogaritjet_Laplace.pptx")
print(f'PowerPoint u krijua: {emri}')