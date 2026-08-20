# -*- coding: utf-8 -*-
"""Генерирует превью для мессенджеров (og-image.png) и иконки сайта."""
import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
FONTS = r'C:\Windows\Fonts'

BG        = (20, 20, 15)
SURFACE   = (32, 32, 26)
ACCENT    = (233, 185, 73)
INK       = (237, 234, 224)
INK_SOFT  = (176, 171, 160)
RULE      = (56, 55, 48)


def font(name, size):
    return ImageFont.truetype(os.path.join(FONTS, name), size)


def tracked(draw, xy, text, fnt, fill, spacing=0):
    """Текст с межбуквенным интервалом."""
    x, y = xy
    for ch in text:
        draw.text((x, y), ch, font=fnt, fill=fill)
        x += draw.textlength(ch, font=fnt) + spacing
    return x


def editor_mark(draw, x, y, size, scale=1.0):
    """Значок: окно редактора с курсором-кареткой."""
    r = int(14 * scale)
    draw.rounded_rectangle([x, y, x + size, y + size], radius=r,
                           fill=SURFACE, outline=ACCENT, width=max(2, int(4 * scale)))
    # полоса заголовка окна
    bar = y + int(size * 0.26)
    draw.line([x + r, bar, x + size - r, bar], fill=RULE, width=max(2, int(3 * scale)))
    dot = max(3, int(size * 0.035))
    for i in range(3):
        cx = x + int(size * 0.13) + i * dot * 3
        cy = y + int(size * 0.13)
        draw.ellipse([cx - dot, cy - dot, cx + dot, cy + dot], fill=ACCENT if i == 0 else RULE)
    # "код": две строки и мигающая каретка
    lx = x + int(size * 0.16)
    ly = bar + int(size * 0.18)
    lh = max(3, int(size * 0.055))
    draw.rounded_rectangle([lx, ly, lx + int(size * 0.42), ly + lh], radius=lh // 2, fill=INK_SOFT)
    ly2 = ly + int(size * 0.16)
    draw.rounded_rectangle([lx, ly2, lx + int(size * 0.26), ly2 + lh], radius=lh // 2, fill=RULE)
    cw = max(4, int(size * 0.055))
    draw.rectangle([lx + int(size * 0.30), ly2 - int(lh * 0.6),
                    lx + int(size * 0.30) + cw, ly2 + lh * 2], fill=ACCENT)


def build_og():
    W, H = 1200, 630
    img = Image.new('RGB', (W, H), BG)
    d = ImageDraw.Draw(img)

    # акцентная полоса слева
    d.rectangle([0, 0, 10, H], fill=ACCENT)

    pad = 76
    # метка
    tracked(d, (pad, 74), 'ПОДГОТОВИТЕЛЬНЫЙ ЭТАП', font('arialbd.ttf', 21), ACCENT, spacing=3.4)

    # заголовок
    f_h1 = font('arialbd.ttf', 82)
    d.text((pad - 4, 126), 'Стартовый набор', font=f_h1, fill=INK)
    d.text((pad - 4, 218), 'вайб-кодера', font=f_h1, fill=INK)

    # подзаголовок
    f_sub = font('arial.ttf', 32)
    d.text((pad, 336), 'Что установить на компьютер', font=f_sub, fill=INK_SOFT)
    d.text((pad, 380), 'и какой нейросетью писать код', font=f_sub, fill=INK_SOFT)

    # разделитель
    d.line([pad, 462, W - pad, 462], fill=RULE, width=2)

    # список программ
    f_chip = font('arialbd.ttf', 26)
    x = pad
    for i, name in enumerate(['Happ', 'VS Code', 'Docker', 'Python', 'superwhisper']):
        if i:
            d.text((x, 500), '·', font=f_chip, fill=ACCENT)
            x += d.textlength('·', font=f_chip) + 20
        d.text((x, 500), name, font=f_chip, fill=INK)
        x += d.textlength(name, font=f_chip) + 20

    # шаги + время — правый нижний угол
    f_meta = font('arial.ttf', 24)
    meta = '5 шагов · около 40 минут'
    d.text((W - pad - d.textlength(meta, font=f_meta), 502), meta, font=f_meta, fill=INK_SOFT)

    # значок
    editor_mark(d, W - pad - 210, 118, 210, scale=1.5)

    img.save(os.path.join(HERE, 'og-image.png'), optimize=True)
    return img.size


def build_icon(size, path):
    img = Image.new('RGB', (size, size), BG)
    d = ImageDraw.Draw(img)
    pad = int(size * 0.1)
    editor_mark(d, pad, pad, size - pad * 2, scale=size / 210)
    img.save(os.path.join(HERE, path), optimize=True)


if __name__ == '__main__':
    print('og-image.png:', build_og())
    build_icon(512, 'icon-512.png')
    build_icon(180, 'apple-touch-icon.png')
    build_icon(32, 'favicon-32.png')
    print('иконки готовы')
