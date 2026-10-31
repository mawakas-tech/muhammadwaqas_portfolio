import os

assets_dir = r"c:\Users\mawakas\Downloads\landing pages ofr envato\ui8_author_portfolio\assets"

def write_svg(filename, content):
    path = os.path.join(assets_dir, filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content.strip())
    print(f"Generated {filename}")

# 1. AetherFlow SaaS Dashboard Preview SVG
aetherflow_svg = '''<svg width="800" height="500" viewBox="0 0 800 500" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bgGrad" x1="0" y1="0" x2="800" y2="500" gradientUnits="userSpaceOnUse">
      <stop stop-color="#F8FAFC"/>
      <stop offset="1" stop-color="#EEF2F6"/>
    </linearGradient>
    <linearGradient id="cardGrad" x1="0" y1="0" x2="1" y2="1">
      <stop stop-color="#FFFFFF"/>
      <stop offset="1" stop-color="#FBFDFE"/>
    </linearGradient>
    <linearGradient id="primaryGrad" x1="0" y1="0" x2="1" y2="0">
      <stop stop-color="#4F46E5"/>
      <stop offset="1" stop-color="#7C3AED"/>
    </linearGradient>
    <linearGradient id="chartGrad" x1="0" y1="0" x2="0" y2="1">
      <stop stop-color="#4F46E5" stop-opacity="0.3"/>
      <stop offset="1" stop-color="#4F46E5" stop-opacity="0.0"/>
    </linearGradient>
    <filter id="shadow" x="0" y="4" width="800" height="500" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB">
      <feDropShadow dx="0" dy="12" stdDeviation="16" flood-color="#0F172A" flood-opacity="0.06"/>
    </filter>
  </defs>

  <!-- Background -->
  <rect width="800" height="500" rx="16" fill="url(#bgGrad)"/>
  
  <!-- Subtle decorative grid -->
  <g opacity="0.4" stroke="#E2E8F0" stroke-width="1" stroke-dasharray="4 4">
    <line x1="40" y1="0" x2="40" y2="500" />
    <line x1="200" y1="0" x2="200" y2="500" />
    <line x1="400" y1="0" x2="400" y2="500" />
    <line x1="600" y1="0" x2="600" y2="500" />
    <line x1="0" y1="80" x2="800" y2="80" />
    <line x1="0" y1="240" x2="800" y2="240" />
    <line x1="0" y1="400" x2="800" y2="400" />
  </g>

  <!-- Window Container -->
  <g filter="url(#shadow)">
    <rect x="30" y="30" width="740" height="440" rx="12" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1"/>
    
    <!-- Window Header -->
    <rect x="30" y="30" width="740" height="42" rx="12" fill="#F8FAFC"/>
    <path d="M30 60 H770 V72 H30 Z" fill="#F8FAFC"/>
    <line x1="30" y1="72" x2="770" y2="72" stroke="#E2E8F0" stroke-width="1"/>
    
    <!-- Window controls -->
    <circle cx="54" cy="51" r="5" fill="#EF4444"/>
    <circle cx="70" cy="51" r="5" fill="#F59E0B"/>
    <circle cx="86" cy="51" r="5" fill="#10B981"/>

    <!-- Search Bar in Header -->
    <rect x="240" y="42" width="280" height="20" rx="6" fill="#FFFFFF" stroke="#E2E8F0"/>
    <circle cx="254" cy="52" r="3.5" stroke="#94A3B8" stroke-width="1.2" fill="none"/>
    <line x1="256.5" y1="54.5" x2="260" y2="58" stroke="#94A3B8" stroke-width="1.2"/>
    <text x="270" y="56" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="9" font-weight="500">Search analytics, metrics, workflows...</text>
    <rect x="492" y="45" width="22" height="14" rx="4" fill="#F1F5F9"/>
    <text x="496" y="55" fill="#64748B" font-family="system-ui, sans-serif" font-size="8" font-weight="600">⌘K</text>

    <!-- Header Actions -->
    <circle cx="710" cy="51" r="11" fill="#F1F5F9"/>
    <circle cx="740" cy="51" r="11" fill="#4F46E5"/>
    <text x="736" y="55" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="10" font-weight="700">UI</text>

    <!-- Left Sidebar -->
    <rect x="30" y="72" width="150" height="398" fill="#FAFAFB"/>
    <line x1="180" y1="72" x2="180" y2="470" stroke="#E2E8F0"/>
    
    <!-- Sidebar Menu Items -->
    <!-- Active Item -->
    <rect x="42" y="90" width="126" height="28" rx="6" fill="#EEF2FF"/>
    <rect x="52" y="99" width="10" height="10" rx="2" fill="#4F46E5"/>
    <text x="70" y="108" fill="#4F46E5" font-family="system-ui, sans-serif" font-size="10" font-weight="600">Overview</text>

    <g opacity="0.7">
      <rect x="52" y="131" width="10" height="10" rx="2" fill="#64748B"/>
      <text x="70" y="140" fill="#334155" font-family="system-ui, sans-serif" font-size="10" font-weight="500">Analytics</text>

      <rect x="52" y="163" width="10" height="10" rx="2" fill="#64748B"/>
      <text x="70" y="172" fill="#334155" font-family="system-ui, sans-serif" font-size="10" font-weight="500">Customers</text>

      <rect x="52" y="195" width="10" height="10" rx="2" fill="#64748B"/>
      <text x="70" y="204" fill="#334155" font-family="system-ui, sans-serif" font-size="10" font-weight="500">Integrations</text>

      <rect x="52" y="227" width="10" height="10" rx="2" fill="#64748B"/>
      <text x="70" y="236" fill="#334155" font-family="system-ui, sans-serif" font-size="10" font-weight="500">Settings</text>
    </g>

    <!-- Main Content Area -->
    <!-- Top Stat Row -->
    <!-- Card 1 -->
    <rect x="200" y="90" width="170" height="80" rx="8" fill="#FFFFFF" stroke="#E2E8F0"/>
    <text x="214" y="110" fill="#64748B" font-family="system-ui, sans-serif" font-size="9" font-weight="500">TOTAL REVENUE (ARR)</text>
    <text x="214" y="136" fill="#0F172A" font-family="system-ui, sans-serif" font-size="18" font-weight="700">$248,650</text>
    <rect x="214" y="146" width="46" height="16" rx="4" fill="#ECFDF5"/>
    <text x="220" y="157" fill="#059669" font-family="system-ui, sans-serif" font-size="8" font-weight="600">+18.4% ↑</text>
    <text x="266" y="157" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="8">vs last mo</text>

    <!-- Card 2 -->
    <rect x="385" y="90" width="170" height="80" rx="8" fill="#FFFFFF" stroke="#E2E8F0"/>
    <text x="399" y="110" fill="#64748B" font-family="system-ui, sans-serif" font-size="9" font-weight="500">ACTIVE WORKSPACES</text>
    <text x="399" y="136" fill="#0F172A" font-family="system-ui, sans-serif" font-size="18" font-weight="700">14,892</text>
    <rect x="399" y="146" width="46" height="16" rx="4" fill="#ECFDF5"/>
    <text x="405" y="157" fill="#059669" font-family="system-ui, sans-serif" font-size="8" font-weight="600">+24.1% ↑</text>
    <text x="451" y="157" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="8">organic</text>

    <!-- Card 3 -->
    <rect x="570" y="90" width="180" height="80" rx="8" fill="#FFFFFF" stroke="#E2E8F0"/>
    <text x="584" y="110" fill="#64748B" font-family="system-ui, sans-serif" font-size="9" font-weight="500">CONVERSION RATE</text>
    <text x="584" y="136" fill="#0F172A" font-family="system-ui, sans-serif" font-size="18" font-weight="700">4.82%</text>
    <rect x="584" y="146" width="46" height="16" rx="4" fill="#EFF6FF"/>
    <text x="590" y="157" fill="#2563EB" font-family="system-ui, sans-serif" font-size="8" font-weight="600">Top 5%</text>
    <text x="636" y="157" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="8">benchmark</text>

    <!-- Chart Panel -->
    <rect x="200" y="185" width="355" height="180" rx="8" fill="#FFFFFF" stroke="#E2E8F0"/>
    <text x="216" y="208" fill="#0F172A" font-family="system-ui, sans-serif" font-size="11" font-weight="600">Revenue Growth Velocity</text>
    <text x="216" y="222" fill="#64748B" font-family="system-ui, sans-serif" font-size="8">Real-time cohort retention & expansion</text>
    
    <!-- Mini chart -->
    <path d="M216 320 C250 310, 280 270, 310 275 C340 280, 370 240, 400 245 C430 250, 460 215, 490 220 C510 223, 530 190, 540 195 L540 335 L216 335 Z" fill="url(#chartGrad)"/>
    <path d="M216 320 C250 310, 280 270, 310 275 C340 280, 370 240, 400 245 C430 250, 460 215, 490 220 C510 223, 530 190, 540 195" stroke="#4F46E5" stroke-width="2.5" stroke-linecap="round"/>
    
    <!-- Data dots -->
    <circle cx="310" cy="275" r="3" fill="#FFFFFF" stroke="#4F46E5" stroke-width="2"/>
    <circle cx="400" cy="245" r="3" fill="#FFFFFF" stroke="#4F46E5" stroke-width="2"/>
    <circle cx="490" cy="220" r="3" fill="#FFFFFF" stroke="#4F46E5" stroke-width="2"/>
    <circle cx="540" cy="195" r="4" fill="#4F46E5"/>

    <!-- Right Side Bento Widget -->
    <rect x="570" y="185" width="180" height="180" rx="8" fill="#FFFFFF" stroke="#E2E8F0"/>
    <text x="584" y="208" fill="#0F172A" font-family="system-ui, sans-serif" font-size="11" font-weight="600">Design System Status</text>
    
    <rect x="584" y="222" width="152" height="32" rx="6" fill="#F8FAFC" stroke="#E2E8F0"/>
    <circle cx="598" cy="238" r="4" fill="#10B981"/>
    <text x="610" y="242" fill="#1E293B" font-family="system-ui, sans-serif" font-size="8" font-weight="600">Auto Layout 5.0</text>
    <text x="696" y="242" fill="#10B981" font-family="system-ui, sans-serif" font-size="7" font-weight="700">100%</text>

    <rect x="584" y="260" width="152" height="32" rx="6" fill="#F8FAFC" stroke="#E2E8F0"/>
    <circle cx="598" cy="276" r="4" fill="#3B82F6"/>
    <text x="610" y="280" fill="#1E293B" font-family="system-ui, sans-serif" font-size="8" font-weight="600">Variables & Tokens</text>
    <text x="702" y="280" fill="#3B82F6" font-family="system-ui, sans-serif" font-size="7" font-weight="700">Synced</text>

    <rect x="584" y="298" width="152" height="32" rx="6" fill="#F8FAFC" stroke="#E2E8F0"/>
    <circle cx="598" cy="314" r="4" fill="#8B5CF6"/>
    <text x="610" y="318" fill="#1E293B" font-family="system-ui, sans-serif" font-size="8" font-weight="600">Light / Dark Modes</text>
    <text x="706" y="318" fill="#8B5CF6" font-family="system-ui, sans-serif" font-size="7" font-weight="700">Ready</text>

    <rect x="584" y="336" width="152" height="20" rx="4" fill="url(#primaryGrad)"/>
    <text x="622" y="350" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="8" font-weight="700">Open In Figma →</text>

    <!-- Bottom Data Table Row -->
    <rect x="200" y="380" width="550" height="74" rx="8" fill="#FAFAFB" stroke="#E2E8F0"/>
    <line x1="200" y1="406" x2="750" y2="406" stroke="#E2E8F0"/>
    <text x="216" y="398" fill="#64748B" font-family="system-ui, sans-serif" font-size="8" font-weight="600">MODULE</text>
    <text x="360" y="398" fill="#64748B" font-family="system-ui, sans-serif" font-size="8" font-weight="600">ARTBOARDS</text>
    <text x="480" y="398" fill="#64748B" font-family="system-ui, sans-serif" font-size="8" font-weight="600">VARIANTS</text>
    <text x="630" y="398" fill="#64748B" font-family="system-ui, sans-serif" font-size="8" font-weight="600">STATUS</text>

    <text x="216" y="426" fill="#0F172A" font-family="system-ui, sans-serif" font-size="9" font-weight="600">Analytics Pro Suite</text>
    <text x="360" y="426" fill="#475569" font-family="system-ui, sans-serif" font-size="9">48 Screens</text>
    <text x="480" y="426" fill="#475569" font-family="system-ui, sans-serif" font-size="9">320 Components</text>
    <rect x="630" y="416" width="58" height="15" rx="3" fill="#ECFDF5"/>
    <text x="636" y="427" fill="#059669" font-family="system-ui, sans-serif" font-size="8" font-weight="600">UI8 Tested</text>

    <text x="216" y="446" fill="#0F172A" font-family="system-ui, sans-serif" font-size="9" font-weight="600">AI Prompt Studio</text>
    <text x="360" y="446" fill="#475569" font-family="system-ui, sans-serif" font-size="9">36 Screens</text>
    <text x="480" y="446" fill="#475569" font-family="system-ui, sans-serif" font-size="9">240 Components</text>
    <rect x="630" y="436" width="58" height="15" rx="3" fill="#ECFDF5"/>
    <text x="636" y="447" fill="#059669" font-family="system-ui, sans-serif" font-size="8" font-weight="600">UI8 Tested</text>
  </g>
</svg>'''

write_svg("aetherflow_preview.svg", aetherflow_svg)

# 2. NovaPay FinTech Mobile Suite Preview SVG
novapay_svg = '''<svg width="800" height="500" viewBox="0 0 800 500" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="mBg" x1="0" y1="0" x2="800" y2="500">
      <stop stop-color="#F1F5F9"/>
      <stop offset="1" stop-color="#E2E8F0"/>
    </linearGradient>
    <linearGradient id="cardGrad1" x1="0" y1="0" x2="1" y2="1">
      <stop stop-color="#1E1B4B"/>
      <stop offset="1" stop-color="#4338CA"/>
    </linearGradient>
    <linearGradient id="cardGrad2" x1="0" y1="0" x2="1" y2="1">
      <stop stop-color="#0284C7"/>
      <stop offset="1" stop-color="#06B6D4"/>
    </linearGradient>
    <filter id="phoneShadow" x="0" y="10" width="800" height="500" filterUnits="userSpaceOnUse">
      <feDropShadow dx="0" dy="16" stdDeviation="20" flood-color="#0F172A" flood-opacity="0.12"/>
    </filter>
  </defs>

  <!-- Background -->
  <rect width="800" height="500" rx="16" fill="url(#mBg)"/>

  <!-- Phone 1 (Left Angled) -->
  <g transform="translate(130, 40)" filter="url(#phoneShadow)">
    <rect width="240" height="420" rx="36" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="4"/>
    <!-- Screen content -->
    <rect x="8" y="8" width="224" height="404" rx="28" fill="#FAFAFB"/>
    <!-- Dynamic Island -->
    <rect x="75" y="16" width="90" height="20" rx="10" fill="#0F172A"/>
    <circle cx="150" cy="26" r="3.5" fill="#1E293B"/>

    <!-- App Header -->
    <circle cx="36" cy="62" r="14" fill="#E2E8F0"/>
    <text x="32" y="66" fill="#475569" font-family="system-ui" font-size="10" font-weight="700">JD</text>
    <text x="58" y="58" fill="#64748B" font-family="system-ui" font-size="8">Good morning,</text>
    <text x="58" y="70" fill="#0F172A" font-family="system-ui" font-size="10" font-weight="700">Jamie Davis</text>
    <rect x="194" y="52" width="20" height="20" rx="6" fill="#F1F5F9"/>

    <!-- FinTech Balance Card -->
    <rect x="22" y="88" width="196" height="115" rx="16" fill="url(#cardGrad1)"/>
    <text x="38" y="112" fill="#A5B4FC" font-family="system-ui" font-size="8" font-weight="600">BLACK TITANIUM CARD</text>
    <text x="38" y="140" fill="#FFFFFF" font-family="system-ui" font-size="20" font-weight="800">$64,820.50</text>
    <text x="38" y="160" fill="#C7D2FE" font-family="system-ui" font-size="8">•••• 9402</text>
    <text x="160" y="160" fill="#FFFFFF" font-family="system-ui" font-size="8" font-weight="700">VISA</text>

    <!-- Quick Action Pills -->
    <g transform="translate(22, 218)">
      <rect x="0" y="0" width="44" height="44" rx="12" fill="#EEF2FF"/>
      <text x="16" y="26" fill="#4F46E5" font-family="system-ui" font-size="14" font-weight="700">↑</text>
      <text x="10" y="54" fill="#475569" font-family="system-ui" font-size="7" font-weight="600">Send</text>

      <rect x="50" y="0" width="44" height="44" rx="12" fill="#ECFDF5"/>
      <text x="66" y="26" fill="#059669" font-family="system-ui" font-size="14" font-weight="700">↓</text>
      <text x="56" y="54" fill="#475569" font-family="system-ui" font-size="7" font-weight="600">Receive</text>

      <rect x="100" y="0" width="44" height="44" rx="12" fill="#FEF3C7"/>
      <text x="115" y="26" fill="#D97706" font-family="system-ui" font-size="14" font-weight="700">⇆</text>
      <text x="108" y="54" fill="#475569" font-family="system-ui" font-size="7" font-weight="600">Swap</text>

      <rect x="150" y="0" width="44" height="44" rx="12" fill="#F1F5F9"/>
      <text x="166" y="26" fill="#475569" font-family="system-ui" font-size="14" font-weight="700">⋯</text>
      <text x="160" y="54" fill="#475569" font-family="system-ui" font-size="7" font-weight="600">More</text>
    </g>

    <!-- Recent Transactions -->
    <text x="24" y="295" fill="#0F172A" font-family="system-ui" font-size="10" font-weight="700">Recent Transfers</text>
    
    <rect x="22" y="306" width="196" height="38" rx="8" fill="#FFFFFF" stroke="#E2E8F0"/>
    <circle cx="40" cy="325" r="10" fill="#0F172A"/>
    <text x="36" y="328" fill="#FFFFFF" font-family="system-ui" font-size="9"></text>
    <text x="58" y="322" fill="#0F172A" font-family="system-ui" font-size="8" font-weight="600">Apple Store</text>
    <text x="58" y="332" fill="#94A3B8" font-family="system-ui" font-size="7">Hardware purchase</text>
    <text x="172" y="326" fill="#0F172A" font-family="system-ui" font-size="8" font-weight="700">-$1,299</text>

    <rect x="22" y="350" width="196" height="38" rx="8" fill="#FFFFFF" stroke="#E2E8F0"/>
    <circle cx="40" cy="369" r="10" fill="#22C55E"/>
    <text x="36" y="372" fill="#FFFFFF" font-family="system-ui" font-size="9">✓</text>
    <text x="58" y="366" fill="#0F172A" font-family="system-ui" font-size="8" font-weight="600">Stripe Payout</text>
    <text x="58" y="376" fill="#94A3B8" font-family="system-ui" font-size="7">UI8 Marketplace</text>
    <text x="170" y="370" fill="#16A34A" font-family="system-ui" font-size="8" font-weight="700">+$8,450</text>
  </g>

  <!-- Phone 2 (Center Right) -->
  <g transform="translate(430, 40)" filter="url(#phoneShadow)">
    <rect width="240" height="420" rx="36" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="4"/>
    <rect x="8" y="8" width="224" height="404" rx="28" fill="#FFFFFF"/>
    <!-- Dynamic Island -->
    <rect x="75" y="16" width="90" height="20" rx="10" fill="#0F172A"/>

    <!-- Screen 2: Investment Portfolio Flow -->
    <text x="24" y="65" fill="#0F172A" font-family="system-ui" font-size="12" font-weight="700">Portfolio Growth</text>
    <text x="24" y="88" fill="#059669" font-family="system-ui" font-size="18" font-weight="800">+$14,240.80</text>
    <text x="140" y="88" fill="#10B981" font-family="system-ui" font-size="9" font-weight="600">▲ +32.4%</text>

    <!-- Mini Chart Curve -->
    <path d="M24 150 C60 145, 90 120, 120 125 C150 130, 180 95, 216 100" stroke="#10B981" stroke-width="3" stroke-linecap="round" fill="none"/>
    <circle cx="216" cy="100" r="4" fill="#10B981"/>

    <!-- Asset Breakdown -->
    <rect x="22" y="170" width="196" height="54" rx="10" fill="#F8FAFC" stroke="#E2E8F0"/>
    <text x="36" y="190" fill="#0F172A" font-family="system-ui" font-size="9" font-weight="700">Global Tech Index</text>
    <text x="36" y="206" fill="#64748B" font-family="system-ui" font-size="8">54.2% allocation</text>
    <text x="160" y="195" fill="#0F172A" font-family="system-ui" font-size="9" font-weight="700">$38,200</text>

    <rect x="22" y="232" width="196" height="54" rx="10" fill="#F8FAFC" stroke="#E2E8F0"/>
    <text x="36" y="252" fill="#0F172A" font-family="system-ui" font-size="9" font-weight="700">High-Yield Treasury</text>
    <text x="36" y="268" fill="#64748B" font-family="system-ui" font-size="8">28.0% allocation</text>
    <text x="160" y="257" fill="#0F172A" font-family="system-ui" font-size="9" font-weight="700">$19,750</text>

    <!-- CTA Card -->
    <rect x="22" y="300" width="196" height="70" rx="12" fill="url(#cardGrad2)"/>
    <text x="36" y="324" fill="#FFFFFF" font-family="system-ui" font-size="10" font-weight="700">Apple Pay Instant Sync</text>
    <text x="36" y="340" fill="#E0F2FE" font-family="system-ui" font-size="8">Instant tokenization for all wallets</text>
    <rect x="36" y="348" width="80" height="16" rx="4" fill="#FFFFFF"/>
    <text x="46" y="359" fill="#0284C7" font-family="system-ui" font-size="8" font-weight="700">Activate Now</text>
  </g>
</svg>'''

write_svg("novapay_preview.svg", novapay_svg)

# 3. OmniDesign Tokens & System Preview SVG
omnidesign_svg = '''<svg width="800" height="500" viewBox="0 0 800 500" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="tokenBg" x1="0" y1="0" x2="800" y2="500">
      <stop stop-color="#FAFAFB"/>
      <stop offset="1" stop-color="#F1F5F9"/>
    </linearGradient>
    <filter id="boxShadow" x="0" y="2" width="800" height="500" filterUnits="userSpaceOnUse">
      <feDropShadow dx="0" dy="8" stdDeviation="12" flood-color="#0F172A" flood-opacity="0.05"/>
    </filter>
  </defs>

  <rect width="800" height="500" rx="16" fill="url(#tokenBg)"/>

  <!-- Left: Color Variables & Tokens Grid -->
  <g transform="translate(40, 40)" filter="url(#boxShadow)">
    <rect width="340" height="420" rx="12" fill="#FFFFFF" stroke="#E2E8F0"/>
    <text x="24" y="34" fill="#0F172A" font-family="system-ui" font-size="12" font-weight="700">Figma Variables • Semantic Tokens</text>
    <text x="24" y="50" fill="#64748B" font-family="system-ui" font-size="9">Structured across Primary, Secondary, Surface, Neutral</text>

    <!-- Color chips -->
    <!-- Primary row -->
    <text x="24" y="80" fill="#334155" font-family="system-ui" font-size="9" font-weight="600">Color / Brand Indigo</text>
    <g transform="translate(24, 90)">
      <rect x="0" y="0" width="48" height="40" rx="6" fill="#EEF2FF"/>
      <rect x="56" y="0" width="48" height="40" rx="6" fill="#818CF8"/>
      <rect x="112" y="0" width="48" height="40" rx="6" fill="#4F46E5"/>
      <rect x="168" y="0" width="48" height="40" rx="6" fill="#3730A3"/>
      <rect x="224" y="0" width="48" height="40" rx="6" fill="#1E1B4B"/>
    </g>

    <!-- Success row -->
    <text x="24" y="160" fill="#334155" font-family="system-ui" font-size="9" font-weight="600">Color / Emerald Mint</text>
    <g transform="translate(24, 170)">
      <rect x="0" y="0" width="48" height="40" rx="6" fill="#ECFDF5"/>
      <rect x="56" y="0" width="48" height="40" rx="6" fill="#34D399"/>
      <rect x="112" y="0" width="48" height="40" rx="6" fill="#10B981"/>
      <rect x="168" y="0" width="48" height="40" rx="6" fill="#047857"/>
      <rect x="224" y="0" width="48" height="40" rx="6" fill="#064E3B"/>
    </g>

    <!-- Typography Scale Preview -->
    <text x="24" y="240" fill="#334155" font-family="system-ui" font-size="9" font-weight="600">Typography Scale / Inter + Plus Jakarta</text>
    <g transform="translate(24, 255)">
      <text x="0" y="18" fill="#0F172A" font-family="system-ui" font-size="16" font-weight="800">Heading 1 / 32px Bold</text>
      <text x="0" y="42" fill="#1E293B" font-family="system-ui" font-size="13" font-weight="700">Heading 2 / 24px Semibold</text>
      <text x="0" y="66" fill="#334155" font-family="system-ui" font-size="11" font-weight="600">Heading 3 / 18px Medium</text>
      <text x="0" y="86" fill="#64748B" font-family="system-ui" font-size="9" font-weight="400">Body Large / 14px Regular • Line height 1.6</text>
      <text x="0" y="104" fill="#94A3B8" font-family="system-ui" font-size="8" font-weight="400">Caption & Footnote / 11px Monospace Spec</text>
    </g>

    <!-- Badges count -->
    <rect x="24" y="380" width="292" height="24" rx="4" fill="#F8FAFC" stroke="#E2E8F0"/>
    <text x="36" y="396" fill="#4F46E5" font-family="system-ui" font-size="8" font-weight="700">✓ 1,280+ Atomic Components • 100% WCAG AA Passed</text>
  </g>

  <!-- Right: Atomic Components Matrix -->
  <g transform="translate(420, 40)" filter="url(#boxShadow)">
    <rect width="340" height="420" rx="12" fill="#FFFFFF" stroke="#E2E8F0"/>
    <text x="24" y="34" fill="#0F172A" font-family="system-ui" font-size="12" font-weight="700">Atomic Component Variants</text>
    <text x="24" y="50" fill="#64748B" font-family="system-ui" font-size="9">Buttons, Inputs, Toggles, Tags, Modals</text>

    <!-- Buttons row -->
    <text x="24" y="80" fill="#334155" font-family="system-ui" font-size="9" font-weight="600">Button Variants (Primary, Outline, Ghost)</text>
    <g transform="translate(24, 90)">
      <rect x="0" y="0" width="85" height="32" rx="6" fill="#4F46E5"/>
      <text x="18" y="20" fill="#FFFFFF" font-family="system-ui" font-size="9" font-weight="600">Get Started</text>

      <rect x="95" y="0" width="85" height="32" rx="6" fill="#FFFFFF" stroke="#4F46E5" stroke-width="1.5"/>
      <text x="114" y="20" fill="#4F46E5" font-family="system-ui" font-size="9" font-weight="600">Preview</text>

      <rect x="190" y="0" width="85" height="32" rx="6" fill="#F1F5F9"/>
      <text x="214" y="20" fill="#475569" font-family="system-ui" font-size="9" font-weight="600">Ghost</text>
    </g>

    <!-- Form Inputs row -->
    <text x="24" y="150" fill="#334155" font-family="system-ui" font-size="9" font-weight="600">Form Inputs & States</text>
    <g transform="translate(24, 160)">
      <rect x="0" y="0" width="135" height="32" rx="6" fill="#FFFFFF" stroke="#4F46E5" stroke-width="1.5"/>
      <text x="12" y="20" fill="#0F172A" font-family="system-ui" font-size="9">jamie@ui8.net|</text>

      <rect x="145" y="0" width="135" height="32" rx="6" fill="#F8FAFC" stroke="#E2E8F0"/>
      <text x="157" y="20" fill="#94A3B8" font-family="system-ui" font-size="9">Placeholder state...</text>
    </g>

    <!-- Toggles and Badges -->
    <text x="24" y="220" fill="#334155" font-family="system-ui" font-size="9" font-weight="600">Interactive Toggles & Status Pills</text>
    <g transform="translate(24, 230)">
      <!-- Toggle ON -->
      <rect x="0" y="4" width="40" height="22" rx="11" fill="#4F46E5"/>
      <circle cx="27" cy="15" r="8" fill="#FFFFFF"/>

      <!-- Toggle OFF -->
      <rect x="52" y="4" width="40" height="22" rx="11" fill="#E2E8F0"/>
      <circle cx="63" cy="15" r="8" fill="#FFFFFF"/>

      <!-- Badges -->
      <rect x="108" y="5" width="55" height="20" rx="10" fill="#EEF2FF"/>
      <text x="116" y="18" fill="#4F46E5" font-family="system-ui" font-size="8" font-weight="600">Active</text>

      <rect x="170" y="5" width="55" height="20" rx="10" fill="#ECFDF5"/>
      <text x="178" y="18" fill="#059669" font-family="system-ui" font-size="8" font-weight="600">Verified</text>

      <rect x="232" y="5" width="55" height="20" rx="10" fill="#FEF3C7"/>
      <text x="240" y="18" fill="#D97706" font-family="system-ui" font-size="8" font-weight="600">Review</text>
    </g>

    <!-- Card Sample Organism -->
    <text x="24" y="285" fill="#334155" font-family="system-ui" font-size="9" font-weight="600">Composite Organism (Feed Card)</text>
    <g transform="translate(24, 298)">
      <rect x="0" y="0" width="292" height="90" rx="8" fill="#F8FAFC" stroke="#E2E8F0"/>
      <circle cx="28" cy="28" r="14" fill="#4F46E5"/>
      <text x="23" y="32" fill="#FFFFFF" font-family="system-ui" font-size="10" font-weight="700">UI</text>
      <text x="50" y="24" fill="#0F172A" font-family="system-ui" font-size="9" font-weight="700">UI8 Featured Author Submission</text>
      <text x="50" y="36" fill="#64748B" font-family="system-ui" font-size="8">Full support for light, dark, and high-contrast themes</text>
      
      <rect x="50" y="52" width="70" height="22" rx="4" fill="#4F46E5"/>
      <text x="60" y="66" fill="#FFFFFF" font-family="system-ui" font-size="8" font-weight="600">Inspect Spec</text>
      
      <rect x="128" y="52" width="70" height="22" rx="4" fill="#FFFFFF" stroke="#CBD5E1"/>
      <text x="138" y="66" fill="#334155" font-family="system-ui" font-size="8" font-weight="600">Copy SVG</text>
    </g>
  </g>
</svg>'''

write_svg("omnidesign_preview.svg", omnidesign_svg)

# 4. Vivid3D Asset Pack Preview SVG
vivid3d_svg = '''<svg width="800" height="500" viewBox="0 0 800 500" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bg3d" x1="0" y1="0" x2="800" y2="500">
      <stop stop-color="#FAF5FF"/>
      <stop offset="1" stop-color="#F3E8FF"/>
    </linearGradient>
    <radialGradient id="sphere1" cx="35%" cy="35%" r="65%">
      <stop stop-color="#C084FC"/>
      <stop offset="0.6" stop-color="#7E22CE"/>
      <stop offset="1" stop-color="#3B0764"/>
    </radialGradient>
    <radialGradient id="sphere2" cx="30%" cy="30%" r="70%">
      <stop stop-color="#67E8F9"/>
      <stop offset="0.5" stop-color="#0284C7"/>
      <stop offset="1" stop-color="#082F49"/>
    </radialGradient>
    <radialGradient id="sphere3" cx="30%" cy="30%" r="70%">
      <stop stop-color="#FDE047"/>
      <stop offset="0.5" stop-color="#F59E0B"/>
      <stop offset="1" stop-color="#78350F"/>
    </radialGradient>
    <radialGradient id="glassSphere" cx="35%" cy="30%" r="65%">
      <stop stop-color="#FFFFFF" stop-opacity="0.8"/>
      <stop offset="0.3" stop-color="#E0E7FF" stop-opacity="0.4"/>
      <stop offset="0.8" stop-color="#818CF8" stop-opacity="0.3"/>
      <stop offset="1" stop-color="#4F46E5" stop-opacity="0.6"/>
    </radialGradient>
    <filter id="glow3d" x="0" y="0" width="800" height="500" filterUnits="userSpaceOnUse">
      <feGaussianBlur stdDeviation="25" result="blur"/>
    </filter>
  </defs>

  <rect width="800" height="500" rx="16" fill="url(#bg3d)"/>

  <!-- Ambient Light Orbs -->
  <circle cx="200" cy="180" r="140" fill="#DDD6FE" opacity="0.6" filter="url(#glow3d)"/>
  <circle cx="620" cy="300" r="160" fill="#BAE6FD" opacity="0.5" filter="url(#glow3d)"/>

  <!-- Header Banner -->
  <rect x="40" y="30" width="720" height="50" rx="10" fill="#FFFFFF" stroke="#E9D5FF"/>
  <text x="60" y="58" fill="#581C87" font-family="system-ui" font-size="12" font-weight="700">Vivid 3D & Claymorphic Asset Library</text>
  <text x="60" y="70" fill="#7E22CE" font-family="system-ui" font-size="9">80+ High-Resolution 4K Blender Renders • Transparent PNGs + GLTF + Figma Plugin</text>

  <!-- 3D Scene Composition -->
  <!-- Sphere 1 (Large Purple) -->
  <g transform="translate(160, 260)">
    <circle cx="0" cy="0" r="95" fill="url(#sphere1)"/>
    <!-- Specular highlight -->
    <ellipse cx="-35" cy="-40" rx="30" ry="18" fill="#FFFFFF" opacity="0.45" transform="rotate(-30 -35 -40)"/>
  </g>

  <!-- Torus / Donut (Center Right) -->
  <g transform="translate(420, 240)">
    <ellipse cx="0" cy="0" rx="110" ry="75" fill="#4F46E5"/>
    <ellipse cx="0" cy="0" rx="105" ry="70" fill="url(#sphere2)"/>
    <ellipse cx="0" cy="0" rx="45" ry="30" fill="url(#bg3d)"/>
    <!-- Highlight -->
    <ellipse cx="-40" cy="-35" rx="35" ry="12" fill="#FFFFFF" opacity="0.4" transform="rotate(-15 -40 -35)"/>
  </g>

  <!-- Sphere 2 (Glass Floating Sphere) -->
  <g transform="translate(630, 220)">
    <circle cx="0" cy="0" r="80" fill="url(#glassSphere)" stroke="#FFFFFF" stroke-width="2"/>
    <ellipse cx="-25" cy="-30" rx="28" ry="16" fill="#FFFFFF" opacity="0.75" transform="rotate(-25 -25 -30)"/>
    <!-- Internal refractive bubbles -->
    <circle cx="15" cy="20" r="16" fill="#FFFFFF" opacity="0.25"/>
  </g>

  <!-- Smaller accent 3D shapes -->
  <circle cx="280" cy="140" r="36" fill="url(#sphere3)"/>
  <ellipse cx="270" cy="130" rx="12" ry="7" fill="#FFFFFF" opacity="0.6"/>

  <circle cx="530" cy="350" r="42" fill="url(#sphere1)"/>
  
  <!-- UI Tags on bottom -->
  <g transform="translate(40, 420)">
    <rect x="0" y="0" width="160" height="40" rx="8" fill="#FFFFFF" stroke="#E9D5FF"/>
    <text x="16" y="24" fill="#6B21A8" font-family="system-ui" font-size="10" font-weight="700">🎨 Clay & Glass Variants</text>

    <rect x="180" y="0" width="160" height="40" rx="8" fill="#FFFFFF" stroke="#E9D5FF"/>
    <text x="196" y="24" fill="#6B21A8" font-family="system-ui" font-size="10" font-weight="700">💎 4000 × 4000 px 4K</text>

    <rect x="360" y="0" width="160" height="40" rx="8" fill="#FFFFFF" stroke="#E9D5FF"/>
    <text x="376" y="24" fill="#6B21A8" font-family="system-ui" font-size="10" font-weight="700">⚡ Blender .BLEND Included</text>

    <rect x="540" y="0" width="180" height="40" rx="8" fill="#FFFFFF" stroke="#E9D5FF"/>
    <text x="556" y="24" fill="#6B21A8" font-family="system-ui" font-size="10" font-weight="700">🛒 UI8 Commercial Approved</text>
  </g>
</svg>'''

write_svg("vivid3d_preview.svg", vivid3d_svg)

# 5. PulseTrack Health Mobile SVG
pulsetrack_svg = '''<svg width="800" height="500" viewBox="0 0 800 500" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="pBg" x1="0" y1="0" x2="800" y2="500">
      <stop stop-color="#F0FDF4"/>
      <stop offset="1" stop-color="#DCFCE7"/>
    </linearGradient>
    <linearGradient id="vitalGrad" x1="0" y1="0" x2="1" y2="0">
      <stop stop-color="#EF4444"/>
      <stop offset="1" stop-color="#F43F5E"/>
    </linearGradient>
  </defs>

  <rect width="800" height="500" rx="16" fill="url(#pBg)"/>

  <!-- Left Watch Mockup -->
  <g transform="translate(140, 100)">
    <!-- Watch Straps -->
    <rect x="55" y="-50" width="90" height="60" rx="8" fill="#334155"/>
    <rect x="55" y="290" width="90" height="60" rx="8" fill="#334155"/>

    <!-- Watch Body -->
    <rect x="20" y="0" width="160" height="200" rx="42" fill="#0F172A" stroke="#475569" stroke-width="6"/>
    <!-- Watch Screen -->
    <rect x="30" y="10" width="140" height="180" rx="34" fill="#000000"/>
    
    <text x="50" y="45" fill="#EF4444" font-family="system-ui" font-size="9" font-weight="700">HEART RATE</text>
    <text x="50" y="78" fill="#FFFFFF" font-family="system-ui" font-size="28" font-weight="800">128</text>
    <text x="105" y="78" fill="#94A3B8" font-family="system-ui" font-size="10">BPM</text>

    <!-- ECG wave on watch -->
    <path d="M40 120 L70 120 L80 95 L90 145 L100 110 L110 125 L160 125" stroke="#EF4444" stroke-width="2.5" fill="none"/>

    <circle cx="65" cy="160" r="14" fill="#16A34A" opacity="0.3"/>
    <circle cx="65" cy="160" r="8" fill="#22C55E"/>
    <text x="88" y="164" fill="#FFFFFF" font-family="system-ui" font-size="9" font-weight="600">8.4 km run</text>
  </g>

  <!-- Right: Mobile Companion App -->
  <g transform="translate(420, 40)">
    <rect width="260" height="420" rx="32" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="4"/>
    <rect x="10" y="10" width="240" height="400" rx="24" fill="#FAFAFB"/>
    
    <!-- Notch -->
    <rect x="85" y="18" width="90" height="18" rx="9" fill="#0F172A"/>

    <text x="28" y="65" fill="#0F172A" font-family="system-ui" font-size="13" font-weight="800">Daily Health Metric</text>
    <text x="28" y="78" fill="#64748B" font-family="system-ui" font-size="8">Synchronized with Apple HealthKit</text>

    <!-- Activity Rings Widget -->
    <rect x="24" y="95" width="212" height="110" rx="12" fill="#FFFFFF" stroke="#E2E8F0"/>
    
    <!-- Concentric rings -->
    <circle cx="75" cy="150" r="38" stroke="#FEE2E2" stroke-width="9" fill="none"/>
    <circle cx="75" cy="150" r="38" stroke="#EF4444" stroke-width="9" stroke-dasharray="190 240" fill="none"/>

    <circle cx="75" cy="150" r="26" stroke="#DCFCE7" stroke-width="7" fill="none"/>
    <circle cx="75" cy="150" r="26" stroke="#22C55E" stroke-width="7" stroke-dasharray="130 170" fill="none"/>

    <circle cx="75" cy="150" r="16" stroke="#E0F2FE" stroke-width="6" fill="none"/>
    <circle cx="75" cy="150" r="16" stroke="#0284C7" stroke-width="6" stroke-dasharray="80 110" fill="none"/>

    <text x="130" y="132" fill="#EF4444" font-family="system-ui" font-size="9" font-weight="700">620 / 750 Cal</text>
    <text x="130" y="152" fill="#22C55E" font-family="system-ui" font-size="9" font-weight="700">48 / 60 Min</text>
    <text x="130" y="172" fill="#0284C7" font-family="system-ui" font-size="9" font-weight="700">11 / 12 Stand</text>

    <!-- Sleep Quality Card -->
    <rect x="24" y="215" width="212" height="85" rx="12" fill="#FFFFFF" stroke="#E2E8F0"/>
    <text x="36" y="235" fill="#0F172A" font-family="system-ui" font-size="10" font-weight="700">Sleep Analysis Score</text>
    <text x="36" y="260" fill="#6366F1" font-family="system-ui" font-size="18" font-weight="800">92% Optimal</text>
    <text x="36" y="282" fill="#64748B" font-family="system-ui" font-size="8">7 hrs 48 mins • Deep sleep 2h 15m</text>

    <!-- Workout plan card -->
    <rect x="24" y="310" width="212" height="80" rx="12" fill="#15803D"/>
    <text x="36" y="334" fill="#FFFFFF" font-family="system-ui" font-size="10" font-weight="700">HIIT Cardio Session</text>
    <text x="36" y="350" fill="#DCFCE7" font-family="system-ui" font-size="8">Coach AI Recommended • 35 mins</text>
    <rect x="36" y="360" width="70" height="18" rx="4" fill="#FFFFFF"/>
    <text x="46" y="372" fill="#15803D" font-family="system-ui" font-size="8" font-weight="700">Start Session</text>
  </g>
</svg>'''

write_svg("pulsetrack_preview.svg", pulsetrack_svg)

# 6. Lumina Studio Framer Template SVG
lumina_svg = '''<svg width="800" height="500" viewBox="0 0 800 500" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="lBg" x1="0" y1="0" x2="800" y2="500">
      <stop stop-color="#FFFBEB"/>
      <stop offset="1" stop-color="#FEF3C7"/>
    </linearGradient>
    <filter id="lShadow" x="0" y="4" width="800" height="500" filterUnits="userSpaceOnUse">
      <feDropShadow dx="0" dy="10" stdDeviation="16" flood-color="#78350F" flood-opacity="0.08"/>
    </filter>
  </defs>

  <rect width="800" height="500" rx="16" fill="url(#lBg)"/>

  <!-- Browser container -->
  <g transform="translate(40, 30)" filter="url(#lShadow)">
    <rect width="720" height="440" rx="12" fill="#FFFFFF" stroke="#E2E8F0"/>
    
    <!-- Browser Nav -->
    <rect width="720" height="40" rx="12" fill="#FAFAFB"/>
    <path d="M0 30 H720 V40 H0 Z" fill="#FAFAFB"/>
    <line x1="0" y1="40" x2="720" y2="40" stroke="#E2E8F0"/>

    <circle cx="24" cy="20" r="5" fill="#EF4444"/>
    <circle cx="40" cy="20" r="5" fill="#F59E0B"/>
    <circle cx="56" cy="20" r="5" fill="#10B981"/>

    <rect x="180" y="10" width="360" height="20" rx="6" fill="#FFFFFF" stroke="#E2E8F0"/>
    <text x="240" y="24" fill="#64748B" font-family="system-ui" font-size="9">https://lumina-studio.framer.website</text>

    <!-- Luxury Editorial Hero -->
    <!-- Nav inside site -->
    <text x="36" y="70" fill="#0F172A" font-family="serif" font-size="14" font-weight="700">L U M I N A</text>
    <text x="440" y="68" fill="#475569" font-family="system-ui" font-size="9" font-weight="500">Works</text>
    <text x="500" y="68" fill="#475569" font-family="system-ui" font-size="9" font-weight="500">Editorial</text>
    <text x="570" y="68" fill="#475569" font-family="system-ui" font-size="9" font-weight="500">About</text>
    <rect x="630" y="55" width="60" height="22" rx="11" fill="#0F172A"/>
    <text x="643" y="69" fill="#FFFFFF" font-family="system-ui" font-size="8" font-weight="600">Contact</text>

    <!-- Hero Title -->
    <text x="36" y="125" fill="#0F172A" font-family="serif" font-size="34" font-weight="400">Timeless Digital Elegance</text>
    <text x="36" y="155" fill="#64748B" font-family="system-ui" font-size="11" font-weight="400">Award-winning Framer Template for luxury fashion, high-end brands & creative agencies.</text>

    <!-- Bento Grid Showcase -->
    <!-- Large Card -->
    <rect x="36" y="180" width="340" height="220" rx="12" fill="#F1F5F9" stroke="#E2E8F0"/>
    <rect x="52" y="200" width="308" height="140" rx="8" fill="#E2E8F0"/>
    <circle cx="206" cy="270" r="35" fill="#CBD5E1"/>
    <text x="52" y="365" fill="#0F172A" font-family="serif" font-size="13" font-weight="700">Autumn Campaign 2026</text>
    <text x="52" y="382" fill="#64748B" font-family="system-ui" font-size="9">Interactive 3D Lookbook with CMS</text>

    <!-- Small Card Top -->
    <rect x="396" y="180" width="294" height="100" rx="12" fill="#F8FAFC" stroke="#E2E8F0"/>
    <text x="414" y="210" fill="#0F172A" font-family="serif" font-size="12" font-weight="700">Motion Architecture</text>
    <text x="414" y="228" fill="#64748B" font-family="system-ui" font-size="9">Smooth scrolling, parallax layers & fluid canvas transitions.</text>
    <rect x="414" y="244" width="70" height="20" rx="4" fill="#0F172A"/>
    <text x="426" y="257" fill="#FFFFFF" font-family="system-ui" font-size="8" font-weight="600">Live Demo</text>

    <!-- Small Card Bottom -->
    <rect x="396" y="295" width="294" height="105" rx="12" fill="#FEF3C7" stroke="#FDE68A"/>
    <text x="414" y="325" fill="#78350F" font-family="system-ui" font-size="12" font-weight="700">UI8 Best Seller Candidate</text>
    <text x="414" y="344" fill="#92400E" font-family="system-ui" font-size="9">Includes 12 page variations, responsive mobile layout, custom cursor.</text>
    <rect x="414" y="360" width="85" height="22" rx="4" fill="#B45309"/>
    <text x="424" y="374" fill="#FFFFFF" font-family="system-ui" font-size="8" font-weight="700">Framer Remix →</text>
  </g>
</svg>'''

write_svg("lumina_preview.svg", lumina_svg)

# 7. Author Avatar Brand Icon SVG
avatar_svg = '''<svg width="200" height="200" viewBox="0 0 200 200" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="avatarGrad" x1="0" y1="0" x2="200" y2="200" gradientUnits="userSpaceOnUse">
      <stop stop-color="#4F46E5"/>
      <stop offset="0.5" stop-color="#7C3AED"/>
      <stop offset="1" stop-color="#06B6D4"/>
    </linearGradient>
    <filter id="avGlow" x="-20" y="-20" width="240" height="240" filterUnits="userSpaceOnUse">
      <feDropShadow dx="0" dy="8" stdDeviation="16" flood-color="#4F46E5" flood-opacity="0.35"/>
    </filter>
  </defs>
  
  <rect width="200" height="200" rx="50" fill="url(#avatarGrad)" filter="url(#avGlow)"/>
  
  <!-- Subtle inner geometric grid -->
  <circle cx="100" cy="100" r="70" stroke="#FFFFFF" stroke-opacity="0.2" stroke-width="2"/>
  <circle cx="100" cy="100" r="45" stroke="#FFFFFF" stroke-opacity="0.3" stroke-width="2" stroke-dasharray="6 6"/>

  <!-- Stylized Monogram / Digital Craft Emblem -->
  <path d="M70 65 L100 120 L130 65" stroke="#FFFFFF" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/>
  <circle cx="100" cy="138" r="7" fill="#FFFFFF"/>
</svg>'''

write_svg("author_brand.svg", avatar_svg)

print("All asset previews created successfully.")
