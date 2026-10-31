import os
from PIL import Image, ImageDraw, ImageFont

assets_dir = r"c:\Users\mawakas\Downloads\landing pages ofr envato\ui8_author_portfolio\assets"

def get_font(size, bold=False):
    font_path = "C:/Windows/Fonts/segoeuib.ttf" if bold else "C:/Windows/Fonts/segoeui.ttf"
    if not os.path.exists(font_path):
        font_path = "C:/Windows/Fonts/arialbd.ttf" if bold else "C:/Windows/Fonts/arial.ttf"
    try:
        return ImageFont.truetype(font_path, size)
    except:
        return ImageFont.load_default()

def create_waqas_avatar():
    img = Image.new('RGB', (240, 240), color=(248, 250, 252))
    d = ImageDraw.Draw(img)
    # Royal violet to deep indigo gradient circle
    for r in range(110, 0, -2):
        col = (
            int(37 + (99 - 37) * (1 - r / 110)),
            int(99 + (102 - 99) * (1 - r / 110)),
            int(235 + (241 - 235) * (1 - r / 110))
        )
        d.ellipse([120 - r, 120 - r, 120 + r, 120 + r], fill=col)
    
    font = get_font(68, bold=True)
    d.text((120, 115), "MW", fill=(255, 255, 255), font=font, anchor="mm")
    img.save(os.path.join(assets_dir, "author_avatar.png"))
    print("Updated author_avatar.png for Muhammad Waqas (MW)")

create_waqas_avatar()
