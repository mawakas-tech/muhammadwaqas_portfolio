import os
from PIL import Image, ImageDraw, ImageFont

assets_dir = r"c:\Users\mawakas\Downloads\landing pages ofr envato\ui8_author_portfolio\assets"
os.makedirs(assets_dir, exist_ok=True)

# Helper for loading fonts
def get_font(size, bold=False):
    font_path = "C:/Windows/Fonts/segoeuib.ttf" if bold else "C:/Windows/Fonts/segoeui.ttf"
    if not os.path.exists(font_path):
        font_path = "C:/Windows/Fonts/arialbd.ttf" if bold else "C:/Windows/Fonts/arial.ttf"
    try:
        return ImageFont.truetype(font_path, size)
    except:
        return ImageFont.load_default()

# 1. Author Avatar
def create_avatar():
    img = Image.new('RGB', (240, 240), color=(248, 250, 252))
    d = ImageDraw.Draw(img)
    # Gradient-like background circle
    for r in range(110, 0, -2):
        col = (
            int(79 + (124 - 79) * (1 - r / 110)),
            int(70 + (58 - 70) * (1 - r / 110)),
            int(229 + (237 - 229) * (1 - r / 110))
        )
        d.ellipse([120 - r, 120 - r, 120 + r, 120 + r], fill=col)
    
    font = get_font(72, bold=True)
    d.text((120, 115), "JD", fill=(255, 255, 255), font=font, anchor="mm")
    img.save(os.path.join(assets_dir, "author_avatar.png"))
    print("Created author_avatar.png")

create_avatar()

# Generator for high quality Behance-style project covers (900x580 px)
def make_cover(filename, bg_col, title, subtitle, render_content_fn):
    w, h = 900, 580
    img = Image.new('RGB', (w, h), color=bg_col)
    d = ImageDraw.Draw(img)

    # Subtle grid dots or pattern
    for x in range(30, w, 40):
        for y in range(30, h, 40):
            d.rectangle([x, y, x + 2, y + 2], fill=(225, 232, 240))

    # Render specific UI mockup elements
    render_content_fn(d, w, h)

    # Top overlay badge
    d.rounded_rectangle([32, 28, 190, 62], radius=17, fill=(255, 255, 255), outline=(226, 232, 240), width=1)
    d.ellipse([46, 41, 54, 49], fill=(16, 185, 129))
    f_badge = get_font(12, bold=True)
    d.text((64, 45), subtitle.upper(), fill=(15, 23, 42), font=f_badge, anchor="lm")

    # Bottom gradient overlay for title contrast
    # (keeps it clean Behance aesthetic)
    img.save(os.path.join(assets_dir, filename), quality=95)
    print(f"Created {filename}")

# --- 1. AetherFlow SaaS ---
def render_aetherflow(d, w, h):
    # Main browser window
    bx, by, bw, bh = 50, 75, 800, 470
    d.rounded_rectangle([bx, by, bx + bw, by + bh], radius=16, fill=(255, 255, 255), outline=(226, 232, 240), width=2)
    # Header
    d.rounded_rectangle([bx, by, bx + bw, by + 46], radius=16, fill=(248, 250, 252))
    d.rectangle([bx, by + 30, bx + bw, by + 46], fill=(248, 250, 252))
    d.line([bx, by + 46, bx + bw, by + 46], fill=(226, 232, 240), width=1)
    # Window dots
    d.ellipse([bx + 20, by + 18, bx + 30, by + 28], fill=(239, 68, 68))
    d.ellipse([bx + 38, by + 18, bx + 48, by + 28], fill=(245, 158, 11))
    d.ellipse([bx + 56, by + 18, bx + 66, by + 28], fill=(16, 185, 129))

    # Sidebar
    d.rectangle([bx, by + 46, bx + 160, by + bh], fill=(250, 250, 251))
    d.line([bx + 160, by + 46, bx + 160, by + bh], fill=(226, 232, 240), width=1)
    # Menu items
    d.rounded_rectangle([bx + 14, by + 65, bx + 146, by + 98], radius=8, fill=(238, 242, 255))
    f_sm = get_font(13, bold=True)
    d.text((bx + 30, by + 81), "Overview", fill=(79, 70, 229), font=f_sm, anchor="lm")
    f_reg = get_font(13, bold=False)
    d.text((bx + 30, by + 120), "Analytics", fill=(100, 116, 139), font=f_reg, anchor="lm")
    d.text((bx + 30, by + 155), "AI Studio", fill=(100, 116, 139), font=f_reg, anchor="lm")
    d.text((bx + 30, by + 190), "Customers", fill=(100, 116, 139), font=f_reg, anchor="lm")

    # Content - Stat cards
    card_w = 180
    for i, (metric, val, diff) in enumerate([("REVENUE (ARR)", "$342,850", "+24.8%"), ("WORKSPACES", "18,420", "+18.2%"), ("CONVERSION", "5.42%", "+3.6%")]):
        cx = bx + 180 + i * (card_w + 16)
        d.rounded_rectangle([cx, by + 65, cx + card_w, by + 160], radius=10, fill=(255, 255, 255), outline=(226, 232, 240), width=1)
        d.text((cx + 14, by + 85), metric, fill=(100, 116, 139), font=get_font(11, bold=True), anchor="lm")
        d.text((cx + 14, by + 115), val, fill=(15, 23, 42), font=get_font(22, bold=True), anchor="lm")
        d.rounded_rectangle([cx + 14, by + 132, cx + 75, by + 150], radius=4, fill=(236, 253, 245))
        d.text((cx + 20, by + 141), diff, fill=(5, 150, 105), font=get_font(11, bold=True), anchor="lm")

    # Chart box
    d.rounded_rectangle([bx + 180, by + 175, bx + 560, by + 370], radius=12, fill=(255, 255, 255), outline=(226, 232, 240), width=1)
    d.text((bx + 200, by + 200), "Growth & Retention Cohorts", fill=(15, 23, 42), font=get_font(15, bold=True), anchor="lm")
    # Wave chart line
    points = [(bx + 200, by + 320), (bx + 260, by + 300), (bx + 320, by + 270), (bx + 380, by + 280), (bx + 440, by + 230), (bx + 500, by + 240), (bx + 540, by + 210)]
    for i in range(len(points) - 1):
        d.line([points[i], points[i+1]], fill=(79, 70, 229), width=3)
        d.ellipse([points[i][0] - 4, points[i][1] - 4, points[i][0] + 4, points[i][1] + 4], fill=(255, 255, 255), outline=(79, 70, 229), width=2)
    d.ellipse([points[-1][0] - 5, points[-1][1] - 5, points[-1][0] + 5, points[-1][1] + 5], fill=(79, 70, 229))

    # Right side bento card
    d.rounded_rectangle([bx + 580, by + 175, bx + 775, by + 370], radius=12, fill=(248, 250, 252), outline=(226, 232, 240), width=1)
    d.text((bx + 600, by + 200), "AI Assistant Status", fill=(15, 23, 42), font=get_font(14, bold=True), anchor="lm")
    d.rounded_rectangle([bx + 600, by + 225, bx + 755, by + 275], radius=8, fill=(255, 255, 255), outline=(226, 232, 240), width=1)
    d.text((bx + 612, by + 245), "Prompt Generator", fill=(30, 41, 59), font=get_font(12, bold=True), anchor="lm")
    d.text((bx + 612, by + 262), "99.4% Latency: 48ms", fill=(100, 116, 139), font=get_font(11, bold=False), anchor="lm")

    # Table preview on bottom
    d.rounded_rectangle([bx + 180, by + 385, bx + 775, by + 450], radius=8, fill=(255, 255, 255), outline=(226, 232, 240), width=1)
    d.text((bx + 200, by + 418), "Enterprise Plan • Acme Global Corp", fill=(15, 23, 42), font=get_font(12, bold=True), anchor="lm")
    d.text((bx + 520, by + 418), "$48,000 / yr", fill=(5, 150, 105), font=get_font(13, bold=True), anchor="lm")
    d.rounded_rectangle([bx + 680, by + 406, bx + 755, by + 430], radius=4, fill=(238, 242, 255))
    d.text((bx + 692, by + 418), "Active", fill=(79, 70, 229), font=get_font(11, bold=True), anchor="lm")

make_cover("aetherflow_cover.png", (244, 247, 251), "AetherFlow", "UI/UX & Web Apps", render_aetherflow)

# --- 2. NovaPay Mobile FinTech ---
def render_novapay(d, w, h):
    # 2 iPhones side by side
    for offset, is_dark in [(180, True), (470, False)]:
        px, py, pw, ph = offset, 70, 250, 470
        d.rounded_rectangle([px, py, px + pw, py + ph], radius=38, fill=(255, 255, 255), outline=(203, 213, 225), width=5)
        # Screen
        bg_screen = (15, 23, 42) if is_dark else (250, 250, 251)
        d.rounded_rectangle([px + 10, py + 10, px + pw - 10, py + ph - 10], radius=30, fill=bg_screen)
        # Dynamic island
        d.rounded_rectangle([px + 80, py + 18, px + pw - 80, py + 38], radius=10, fill=(0, 0, 0))

        if is_dark:
            # Dark card screen
            d.text((px + 28, py + 65), "Good Morning,", fill=(148, 163, 184), font=get_font(11), anchor="lm")
            d.text((px + 28, py + 85), "Jamie Davis", fill=(255, 255, 255), font=get_font(16, bold=True), anchor="lm")
            # Titanium card
            d.rounded_rectangle([px + 24, py + 110, px + pw - 24, py + 235], radius=16, fill=(30, 27, 75))
            d.text((px + 40, py + 135), "BLACK TITANIUM", fill=(165, 180, 252), font=get_font(10, bold=True), anchor="lm")
            d.text((px + 40, py + 175), "$84,240.50", fill=(255, 255, 255), font=get_font(24, bold=True), anchor="lm")
            d.text((px + 40, py + 210), "•••• 9420", fill=(199, 210, 254), font=get_font(12), anchor="lm")
            d.text((px + pw - 60, py + 210), "VISA", fill=(255, 255, 255), font=get_font(14, bold=True), anchor="lm")
            # Action buttons
            for bi, lbl in enumerate(["Send", "Receive", "Swap", "Cards"]):
                bx = px + 28 + bi * 50
                d.rounded_rectangle([bx, py + 255, bx + 42, py + 297], radius=10, fill=(30, 41, 59))
                d.text((bx + 21, py + 312), lbl, fill=(203, 213, 225), font=get_font(9, bold=True), anchor="mm")
            # Transactions
            d.text((px + 28, py + 345), "Recent Activity", fill=(255, 255, 255), font=get_font(13, bold=True), anchor="lm")
            d.rounded_rectangle([px + 24, py + 360, px + pw - 24, py + 410], radius=10, fill=(30, 41, 59))
            d.text((px + 40, py + 385), "Apple Store", fill=(255, 255, 255), font=get_font(12, bold=True), anchor="lm")
            d.text((px + pw - 40, py + 385), "-$1,299", fill=(255, 255, 255), font=get_font(12, bold=True), anchor="rm")
        else:
            # Light invest screen
            d.text((px + 28, py + 65), "Investment Portfolio", fill=(100, 116, 139), font=get_font(11), anchor="lm")
            d.text((px + 28, py + 90), "+$18,450.20", fill=(5, 150, 105), font=get_font(20, bold=True), anchor="lm")
            # Graph
            d.line([(px + 28, py + 160), (px + 70, py + 150), (px + 120, py + 130), (px + 160, py + 140), (px + pw - 28, py + 110)], fill=(16, 185, 129), width=3)
            # Cards
            d.rounded_rectangle([px + 24, py + 185, px + pw - 24, py + 260], radius=12, fill=(255, 255, 255), outline=(226, 232, 240), width=1)
            d.text((px + 38, py + 210), "Tech Index Fund", fill=(15, 23, 42), font=get_font(12, bold=True), anchor="lm")
            d.text((px + 38, py + 232), "+34.8% Year to date", fill=(5, 150, 105), font=get_font(11, bold=True), anchor="lm")
            d.text((px + pw - 40, py + 220), "$42,500", fill=(15, 23, 42), font=get_font(13, bold=True), anchor="rm")

            d.rounded_rectangle([px + 24, py + 275, px + pw - 24, py + 350], radius=12, fill=(255, 255, 255), outline=(226, 232, 240), width=1)
            d.text((px + 38, py + 300), "High-Yield Savings", fill=(15, 23, 42), font=get_font(12, bold=True), anchor="lm")
            d.text((px + 38, py + 322), "5.2% APY Compounded", fill=(79, 70, 229), font=get_font(11, bold=True), anchor="lm")
            d.text((px + pw - 40, py + 310), "$28,120", fill=(15, 23, 42), font=get_font(13, bold=True), anchor="rm")

            # Apple pay button
            d.rounded_rectangle([px + 24, py + 380, px + pw - 24, py + 425], radius=10, fill=(15, 23, 42))
            d.text((px + pw // 2, py + 402), "Pay with Apple Pay", fill=(255, 255, 255), font=get_font(12, bold=True), anchor="mm")

make_cover("novapay_cover.png", (241, 245, 249), "NovaPay", "Mobile Apps", render_novapay)

# --- 3. Solaris 3D Icons (Special Category!) ---
def render_solaris(d, w, h):
    # Showcase grid of 3D icons (simulated with rich gradients & shading)
    icons = [
        ("Cloud Sync", (14, 165, 233), (56, 189, 248)),
        ("Rocket Ship", (239, 68, 68), (244, 63, 94)),
        ("Security Lock", (16, 185, 129), (52, 211, 153)),
        ("Wallet Pay", (79, 70, 229), (129, 140, 248)),
        ("Analytics Chart", (245, 158, 11), (251, 191, 36)),
        ("Notification Bell", (168, 85, 247), (192, 132, 252)),
        ("Diamond Reward", (236, 72, 153), (244, 114, 182)),
        ("Target Goal", (6, 182, 212), (34, 211, 238)),
    ]
    grid_start_x, grid_start_y = 100, 95
    box_w, box_h = 160, 190
    gap_x, gap_y = 20, 24

    for idx, (label, col_dark, col_light) in enumerate(icons):
        row = idx // 4
        col = idx % 4
        bx = grid_start_x + col * (box_w + gap_x)
        by = grid_start_y + row * (box_h + gap_y)

        # Card container
        d.rounded_rectangle([bx, by, bx + box_w, by + box_h], radius=16, fill=(255, 255, 255), outline=(226, 232, 240), width=1)
        # 3D spherical icon rendering
        cx, cy = bx + box_w // 2, by + 75
        # Soft shadow
        d.ellipse([cx - 36, cy + 30, cx + 36, cy + 46], fill=(226, 232, 240))
        # Concentric gradient shading for 3D sphere look
        for r in range(40, 0, -2):
            factor = r / 40.0
            cur_col = (
                int(col_light[0] + (col_dark[0] - col_light[0]) * (1 - factor)),
                int(col_light[1] + (col_dark[1] - col_light[1]) * (1 - factor)),
                int(col_light[2] + (col_dark[2] - col_light[2]) * (1 - factor))
            )
            d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=cur_col)
        # Specular 3D highlight
        d.ellipse([cx - 16, cy - 22, cx + 4, cy - 8], fill=(255, 255, 255, 180))

        # Icon Label
        d.text((cx, by + 140), label, fill=(15, 23, 42), font=get_font(13, bold=True), anchor="mm")
        d.text((cx, by + 160), "4K 3D Blender", fill=(100, 116, 139), font=get_font(10, bold=False), anchor="mm")

make_cover("solaris_icons_cover.png", (250, 245, 255), "Solaris", "Icon Sets", render_solaris)

# --- 4. Linear Pro Minimalist 640+ Icons (Special Category!) ---
def render_linear_icons(d, w, h):
    # Big showcase sheet with precision grid lines
    sheet_x, sheet_y, sheet_w, sheet_h = 70, 75, 760, 465
    d.rounded_rectangle([sheet_x, sheet_y, sheet_x + sheet_w, sheet_y + sheet_h], radius=14, fill=(255, 255, 255), outline=(226, 232, 240), width=2)
    
    # Header bar inside
    d.text((sheet_x + 30, sheet_y + 35), "Linear Pro • 24px Precision Vector System", fill=(15, 23, 42), font=get_font(16, bold=True), anchor="lm")
    d.rounded_rectangle([sheet_x + sheet_w - 180, sheet_y + 20, sheet_x + sheet_w - 30, sheet_y + 48], radius=6, fill=(241, 245, 249))
    d.text((sheet_x + sheet_w - 105, sheet_y + 34), "640+ SVGs Ready", fill=(71, 85, 105), font=get_font(11, bold=True), anchor="mm")

    # Grid of icon cells
    cols = 8
    rows = 4
    cell_w = 84
    cell_h = 86
    start_gx = sheet_x + 44
    start_gy = sheet_y + 70

    for r in range(rows):
        for c in range(cols):
            cx = start_gx + c * (cell_w + 4)
            cy = start_gy + r * (cell_h + 4)
            # Subtle cell border
            d.rounded_rectangle([cx, cy, cx + cell_w, cy + cell_h], radius=8, fill=(248, 250, 252), outline=(235, 240, 245), width=1)
            # Center of icon
            icx, icy = cx + cell_w // 2, cy + cell_h // 2 - 8
            # Draw various geometric monoline icon symbols
            pattern = (r * cols + c) % 8
            if pattern == 0: # Home
                d.polygon([(icx, icy - 14), (icx + 14, icy), (icx + 10, icy), (icx + 10, icy + 14), (icx - 10, icy + 14), (icx - 10, icy), (icx - 14, icy)], outline=(15, 23, 42), fill=None)
            elif pattern == 1: # User
                d.ellipse([icx - 8, icy - 14, icx + 8, icy + 2], outline=(15, 23, 42), width=2)
                d.arc([icx - 14, icy + 4, icx + 14, icy + 24], 180, 0, fill=(15, 23, 42), width=2)
            elif pattern == 2: # Settings
                d.ellipse([icx - 6, icy - 6, icx + 6, icy + 6], outline=(15, 23, 42), width=2)
                for a in range(0, 360, 45):
                    d.line([(icx, icy - 12), (icx, icy - 8)], fill=(15, 23, 42), width=2)
            elif pattern == 3: # Bell
                d.arc([icx - 10, icy - 12, icx + 10, icy + 8], 180, 0, fill=(15, 23, 42), width=2)
                d.line([(icx - 12, icy + 6), (icx + 12, icy + 6)], fill=(15, 23, 42), width=2)
                d.line([(icx - 3, icy + 10), (icx + 3, icy + 10)], fill=(15, 23, 42), width=2)
            elif pattern == 4: # Search
                d.ellipse([icx - 12, icy - 12, icx + 4, icy + 4], outline=(15, 23, 42), width=2)
                d.line([(icx + 2, icy + 2), (icx + 12, icy + 12)], fill=(15, 23, 42), width=2)
            elif pattern == 5: # Folder
                d.rectangle([icx - 12, icy - 6, icx + 12, icy + 10], outline=(15, 23, 42), width=2)
                d.line([(icx - 12, icy - 6), (icx - 6, icy - 11), (icx, icy - 11), (icx + 4, icy - 6)], fill=(15, 23, 42), width=2)
            elif pattern == 6: # Mail
                d.rectangle([icx - 12, icy - 8, icx + 12, icy + 8], outline=(15, 23, 42), width=2)
                d.line([(icx - 12, icy - 8), (icx, icy), (icx + 12, icy - 8)], fill=(15, 23, 42), width=2)
            else: # Chart
                d.line([(icx - 10, icy + 10), (icx + 10, icy + 10)], fill=(15, 23, 42), width=2)
                d.rectangle([icx - 8, icy, icx - 4, icy + 10], fill=(79, 70, 229))
                d.rectangle([icx - 2, icy - 6, icx + 2, icy + 10], fill=(79, 70, 229))
                d.rectangle([icx + 4, icy - 12, icx + 8, icy + 10], fill=(79, 70, 229))

            d.text((cx + cell_w // 2, cy + cell_h - 14), f"ic_{r*cols+c:02d}", fill=(148, 163, 184), font=get_font(9), anchor="mm")

make_cover("linear_icons_cover.png", (248, 250, 252), "Linear Pro", "Icon Sets", render_linear_icons)

# --- 5. OmniDesign Tokens & System ---
def render_omnidesign(d, w, h):
    d.rounded_rectangle([60, 75, 450, 520], radius=14, fill=(255, 255, 255), outline=(226, 232, 240), width=1)
    d.text((84, 105), "Figma Variables & Token Taxonomy", fill=(15, 23, 42), font=get_font(15, bold=True), anchor="lm")
    # Color swatches
    for ri, (cname, shades) in enumerate([("Brand Primary", [(238, 242, 255), (129, 140, 248), (79, 70, 229), (55, 48, 163)]),
                                          ("Emerald Mint", [(236, 253, 245), (52, 211, 153), (16, 185, 129), (4, 120, 87)]),
                                          ("Slate Neutrals", [(241, 245, 249), (203, 213, 225), (71, 85, 105), (15, 23, 42)])]):
        y = 145 + ri * 75
        d.text((84, y), cname, fill=(71, 85, 105), font=get_font(12, bold=True), anchor="lm")
        for si, sc in enumerate(shades):
            d.rounded_rectangle([84 + si * 75, y + 14, 84 + si * 75 + 65, y + 54], radius=6, fill=sc)

    # Right: Atomic components
    d.rounded_rectangle([470, 75, 840, 520], radius=14, fill=(255, 255, 255), outline=(226, 232, 240), width=1)
    d.text((495, 105), "Atomic Component Variants", fill=(15, 23, 42), font=get_font(15, bold=True), anchor="lm")
    # Buttons
    d.rounded_rectangle([495, 145, 600, 185], radius=8, fill=(79, 70, 229))
    d.text((547, 165), "Primary Button", fill=(255, 255, 255), font=get_font(11, bold=True), anchor="mm")
    d.rounded_rectangle([615, 145, 715, 185], radius=8, fill=(255, 255, 255), outline=(79, 70, 229), width=2)
    d.text((665, 165), "Outline Button", fill=(79, 70, 229), font=get_font(11, bold=True), anchor="mm")
    d.rounded_rectangle([730, 145, 815, 185], radius=8, fill=(241, 245, 249))
    d.text((772, 165), "Ghost", fill=(71, 85, 105), font=get_font(11, bold=True), anchor="mm")

    # Inputs
    d.rounded_rectangle([495, 210, 815, 250], radius=8, fill=(255, 255, 255), outline=(79, 70, 229), width=2)
    d.text((515, 230), "jamie.davis@design.studio|", fill=(15, 23, 42), font=get_font(12), anchor="lm")
    # Badges
    d.rounded_rectangle([495, 275, 560, 305], radius=15, fill=(238, 242, 255))
    d.text((527, 290), "Active", fill=(79, 70, 229), font=get_font(11, bold=True), anchor="mm")
    d.rounded_rectangle([570, 275, 635, 305], radius=15, fill=(236, 253, 245))
    d.text((602, 290), "Verified", fill=(5, 150, 105), font=get_font(11, bold=True), anchor="mm")

make_cover("omnidesign_cover.png", (244, 247, 251), "OmniDesign", "Design Systems", render_omnidesign)

# --- 6. Vivid3D Abstract Spatial ---
def render_vivid3d(d, w, h):
    # Iridescent spheres and torus
    d.ellipse([140, 140, 360, 360], fill=(126, 34, 206))
    d.ellipse([170, 170, 310, 310], fill=(168, 85, 247))
    d.ellipse([210, 190, 260, 240], fill=(240, 171, 252))

    # Center floating torus
    d.ellipse([450, 150, 750, 410], fill=(67, 56, 202))
    d.ellipse([470, 170, 730, 390], fill=(99, 102, 241))
    d.ellipse([540, 230, 660, 330], fill=(253, 244, 255))

    # Accent glass ball
    d.ellipse([340, 300, 460, 420], fill=(14, 165, 233))
    d.ellipse([360, 320, 420, 380], fill=(255, 255, 255))

make_cover("vivid3d_cover.png", (253, 244, 255), "Vivid3D", "3D & Illustrations", render_vivid3d)

# --- 7. PulseTrack Health ---
def render_pulsetrack(d, w, h):
    # Watch and companion screen
    wx, wy = 160, 120
    d.rounded_rectangle([wx, wy - 40, wx + 120, wy + 260], radius=10, fill=(51, 65, 85))
    d.rounded_rectangle([wx - 20, wy, wx + 140, wy + 220], radius=44, fill=(15, 23, 42), outline=(71, 85, 105), width=6)
    d.text((wx + 60, wy + 40), "HEART RATE", fill=(239, 68, 68), font=get_font(10, bold=True), anchor="mm")
    d.text((wx + 60, wy + 80), "128", fill=(255, 255, 255), font=get_font(34, bold=True), anchor="mm")
    d.text((wx + 60, wy + 110), "BPM", fill=(148, 163, 184), font=get_font(12), anchor="mm")
    # ECG line
    d.line([(wx + 10, wy + 150), (wx + 40, wy + 150), (wx + 50, wy + 130), (wx + 60, wy + 170), (wx + 70, wy + 140), (wx + 110, wy + 140)], fill=(239, 68, 68), width=3)

    # Phone mockup
    mx, my, mw, mh = 420, 70, 280, 460
    d.rounded_rectangle([mx, my, mx + mw, my + mh], radius=34, fill=(255, 255, 255), outline=(203, 213, 225), width=4)
    d.text((mx + 30, my + 45), "Today's Activity", fill=(15, 23, 42), font=get_font(18, bold=True), anchor="lm")
    # Activity rings
    rcx, rcy = mx + mw // 2, my + 170
    d.ellipse([rcx - 60, rcy - 60, rcx + 60, rcy + 60], outline=(254, 202, 202), width=12)
    d.arc([rcx - 60, rcy - 60, rcx + 60, rcy + 60], 0, 280, fill=(239, 68, 68), width=12)
    d.ellipse([rcx - 42, rcy - 42, rcx + 42, rcy + 42], outline=(187, 247, 208), width=10)
    d.arc([rcx - 42, rcy - 42, rcx + 42, rcy + 42], 0, 220, fill=(34, 197, 94), width=10)
    d.ellipse([rcx - 26, rcy - 26, rcx + 26, rcy + 26], outline=(186, 230, 253), width=8)
    d.arc([rcx - 26, rcy - 26, rcx + 26, rcy + 26], 0, 310, fill=(14, 165, 233), width=8)

    # Stat cards
    d.rounded_rectangle([mx + 24, my + 270, mx + mw - 24, my + 340], radius=12, fill=(248, 250, 252), outline=(226, 232, 240), width=1)
    d.text((mx + 40, my + 295), "Sleep Analysis Score", fill=(15, 23, 42), font=get_font(12, bold=True), anchor="lm")
    d.text((mx + 40, my + 320), "94% Optimal (8h 12m)", fill=(79, 70, 229), font=get_font(13, bold=True), anchor="lm")

make_cover("pulsetrack_cover.png", (240, 253, 244), "PulseTrack", "Mobile Apps", render_pulsetrack)

# --- 8. Lumina Editorial Luxury ---
def render_lumina(d, w, h):
    d.rounded_rectangle([70, 75, 830, 500], radius=16, fill=(255, 255, 255), outline=(226, 232, 240), width=1)
    d.text((110, 130), "L U M I N A", fill=(15, 23, 42), font=get_font(26, bold=True), anchor="lm")
    d.text((110, 190), "Timeless Digital Elegance", fill=(15, 23, 42), font=get_font(34, bold=True), anchor="lm")
    d.text((110, 235), "Award-winning Framer Template engineered for creative studios & luxury brands.", fill=(100, 116, 139), font=get_font(14), anchor="lm")
    # Bento cards inside
    d.rounded_rectangle([110, 275, 460, 460], radius=12, fill=(241, 245, 249))
    d.rounded_rectangle([130, 295, 440, 390], radius=8, fill=(203, 213, 225))
    d.text((130, 425), "Autumn Lookbook 2026", fill=(15, 23, 42), font=get_font(14, bold=True), anchor="lm")

    d.rounded_rectangle([485, 275, 790, 360], radius=12, fill=(254, 243, 199))
    d.text((510, 318), "Fluid Parallax Motion & CMS", fill=(146, 64, 14), font=get_font(15, bold=True), anchor="lm")

    d.rounded_rectangle([485, 380, 790, 460], radius=12, fill=(238, 242, 255))
    d.text((510, 420), "14 Responsive Breakpoints", fill=(55, 48, 163), font=get_font(15, bold=True), anchor="lm")

make_cover("lumina_cover.png", (255, 251, 235), "Lumina", "Framer & Web Templates", render_lumina)

# --- 9. ApexCRM B2B Sales ---
def render_apexcrm(d, w, h):
    d.rounded_rectangle([60, 75, 840, 500], radius=16, fill=(255, 255, 255), outline=(226, 232, 240), width=1)
    d.text((90, 115), "Sales Pipeline & Deal Flow Board", fill=(15, 23, 42), font=get_font(18, bold=True), anchor="lm")
    # 3 Kanban columns
    col_w = 230
    for ci, (cname, count) in enumerate([("Qualified Leads", "14"), ("Proposal Sent", "8"), ("Closed Won", "26")]):
        cx = 90 + ci * (col_w + 20)
        d.rounded_rectangle([cx, 145, cx + col_w, 470], radius=12, fill=(248, 250, 252), outline=(226, 232, 240), width=1)
        d.text((cx + 18, 175), cname, fill=(15, 23, 42), font=get_font(13, bold=True), anchor="lm")
        d.rounded_rectangle([cx + col_w - 45, 162, cx + col_w - 18, 188], radius=6, fill=(226, 232, 240))
        d.text((cx + col_w - 32, 175), count, fill=(71, 85, 105), font=get_font(11, bold=True), anchor="mm")

        # Deal cards inside column
        for di, (dtitle, dval) in enumerate([("Stripe Enterprise", "$84,000"), ("Shopify Expansion", "$42,500")]):
            dy = 205 + di * 105
            d.rounded_rectangle([cx + 12, dy, cx + col_w - 12, dy + 90], radius=8, fill=(255, 255, 255), outline=(226, 232, 240), width=1)
            d.text((cx + 24, dy + 25), dtitle, fill=(15, 23, 42), font=get_font(12, bold=True), anchor="lm")
            d.text((cx + 24, dy + 55), dval, fill=(5, 150, 105), font=get_font(14, bold=True), anchor="lm")

make_cover("apexcrm_cover.png", (241, 245, 249), "ApexCRM", "UI/UX & Web Apps", render_apexcrm)

# --- 10. AuraCraft Brand Identity ---
def render_auracraft(d, w, h):
    # Editorial stationery
    d.rounded_rectangle([100, 110, 480, 480], radius=12, fill=(255, 255, 255), outline=(226, 232, 240), width=1)
    d.text((140, 180), "A U R A C R A F T", fill=(15, 23, 42), font=get_font(24, bold=True), anchor="lm")
    d.text((140, 230), "Corporate Brand System & Stationery", fill=(100, 116, 139), font=get_font(13), anchor="lm")
    d.line([(140, 280), (440, 280)], fill=(226, 232, 240), width=2)
    # Business card mockup
    d.rounded_rectangle([440, 200, 800, 420], radius=16, fill=(15, 23, 42))
    d.text((490, 280), "Jamie Davis", fill=(255, 255, 255), font=get_font(20, bold=True), anchor="lm")
    d.text((490, 315), "Principal Design Director", fill=(148, 163, 184), font=get_font(12), anchor="lm")

make_cover("auracraft_cover.png", (250, 250, 252), "AuraCraft", "Brand Identity & Templates", render_auracraft)

# --- 11. CyberGlance Crypto Wallet ---
def render_cyberglance(d, w, h):
    mx, my, mw, mh = 310, 65, 280, 480
    d.rounded_rectangle([mx, my, mx + mw, my + mh], radius=38, fill=(15, 23, 42), outline=(51, 65, 85), width=4)
    d.text((mx + 30, my + 55), "Web3 Multi-Chain", fill=(148, 163, 184), font=get_font(11), anchor="lm")
    d.text((mx + 30, my + 90), "$114,820.40", fill=(255, 255, 255), font=get_font(22, bold=True), anchor="lm")
    # Token rows
    for ti, (tname, amt, tval) in enumerate([("Ethereum (ETH)", "32.4 ETH", "$86,400"), ("Solana (SOL)", "180.2 SOL", "$24,500")]):
        ty = my + 140 + ti * 80
        d.rounded_rectangle([mx + 20, ty, mx + mw - 20, ty + 68], radius=12, fill=(30, 41, 59))
        d.text((mx + 36, ty + 24), tname, fill=(255, 255, 255), font=get_font(12, bold=True), anchor="lm")
        d.text((mx + 36, ty + 46), amt, fill=(148, 163, 184), font=get_font(11), anchor="lm")
        d.text((mx + mw - 36, ty + 34), tval, fill=(52, 211, 153), font=get_font(13, bold=True), anchor="rm")

make_cover("cyberglance_cover.png", (241, 245, 249), "CyberGlance", "Mobile Apps", render_cyberglance)

# --- 12. GlyphMatrix Developer Monoline Icons (Special Category!) ---
def render_glyphmatrix(d, w, h):
    # Terminal style window preview
    tw_x, tw_y, tw_w, tw_h = 70, 75, 760, 465
    d.rounded_rectangle([tw_x, tw_y, tw_x + tw_w, tw_y + tw_h], radius=14, fill=(15, 23, 42), outline=(51, 65, 85), width=2)
    # Header
    d.rounded_rectangle([tw_x, tw_y, tw_x + tw_w, tw_y + 44], radius=14, fill=(30, 41, 59))
    d.rectangle([tw_x, tw_y + 30, tw_x + tw_w, tw_y + 44], fill=(30, 41, 59))
    d.ellipse([tw_x + 20, tw_y + 16, tw_x + 30, tw_y + 26], fill=(239, 68, 68))
    d.ellipse([tw_x + 38, tw_y + 16, tw_x + 48, tw_y + 26], fill=(245, 158, 11))
    d.ellipse([tw_x + 56, tw_y + 16, tw_x + 66, tw_y + 26], fill=(16, 185, 129))
    d.text((tw_x + tw_w // 2, tw_y + 22), "GlyphMatrix // 480+ DevOps & Developer Monoline Icons", fill=(203, 213, 225), font=get_font(12, bold=True), anchor="mm")

    # Developer Icon Grid
    cols, rows = 6, 3
    cw, ch = 110, 115
    for r in range(rows):
        for c in range(cols):
            ix = tw_x + 40 + c * (cw + 8)
            iy = tw_y + 65 + r * (ch + 10)
            d.rounded_rectangle([ix, iy, ix + cw, iy + ch], radius=8, fill=(30, 41, 59), outline=(51, 65, 85), width=1)
            icx, icy = ix + cw // 2, iy + 45
            # Draw monoline code icon symbols
            pattern = (r * cols + c) % 6
            if pattern == 0: # Terminal prompt
                d.line([(icx - 12, icy - 8), (icx - 4, icy), (icx - 12, icy + 8)], fill=(129, 140, 248), width=2)
                d.line([(icx, icy + 8), (icx + 12, icy + 8)], fill=(129, 140, 248), width=2)
            elif pattern == 1: # Database cylinder
                d.ellipse([icx - 12, icy - 10, icx + 12, icy - 2], outline=(52, 211, 153), width=2)
                d.line([(icx - 12, icy - 6), (icx - 12, icy + 8)], fill=(52, 211, 153), width=2)
                d.line([(icx + 12, icy - 6), (icx + 12, icy + 8)], fill=(52, 211, 153), width=2)
                d.arc([icx - 12, icy + 2, icx + 12, icy + 12], 0, 180, fill=(52, 211, 153), width=2)
            elif pattern == 2: # Git Branch
                d.ellipse([icx - 8, icy - 10, icx - 2, icy - 4], fill=(251, 191, 36))
                d.ellipse([icx - 8, icy + 6, icx - 2, icy + 12], fill=(251, 191, 36))
                d.ellipse([icx + 4, icy - 2, icx + 10, icy + 4], fill=(251, 191, 36))
                d.line([(icx - 5, icy - 4), (icx - 5, icy + 6)], fill=(251, 191, 36), width=2)
                d.arc([icx - 5, icy - 4, icx + 7, icy + 4], 90, 270, fill=(251, 191, 36), width=2)
            elif pattern == 3: # Server Stack
                for sy in [icy - 10, icy - 2, icy + 6]:
                    d.rounded_rectangle([icx - 14, sy, icx + 14, sy + 6], radius=2, outline=(56, 189, 248), width=2)
            elif pattern == 4: # Cloud API
                d.ellipse([icx - 10, icy - 6, icx + 2, icy + 6], outline=(244, 114, 182), width=2)
                d.ellipse([icx - 2, icy - 10, icx + 12, icy + 2], outline=(244, 114, 182), width=2)
            else: # Shield Security
                d.polygon([(icx, icy - 12), (icx + 12, icy - 6), (icx + 12, icy + 4), (icx, icy + 12), (icx - 12, icy + 4), (icx - 12, icy - 6)], outline=(167, 139, 250), fill=None)

            d.text((ix + cw // 2, iy + ch - 16), f"dev_{r*cols+c:02d}", fill=(148, 163, 184), font=get_font(9), anchor="mm")

make_cover("glyphmatrix_cover.png", (248, 250, 252), "GlyphMatrix", "Icon Sets", render_glyphmatrix)

print("All 12 Behance covers generated with 100% precision.")
