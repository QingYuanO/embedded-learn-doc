#!/usr/bin/env python3
"""Generate simplified SVG schematic diagrams for electronic-components docs."""

from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "public" / "electronic-components" / "diagrams"
OUT.mkdir(parents=True, exist_ok=True)

STYLE = """
<style>
  .stroke { fill: none; stroke: var(--ec-stroke); stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; }
  .thin { stroke-width: 1.5; }
  .divider { fill: none; stroke: var(--ec-divider); stroke-width: 2; }
  .divider-thin { fill: none; stroke: var(--ec-divider); stroke-width: 1.5; }
  .fill-light { fill: var(--ec-fill-neutral); stroke: var(--ec-stroke); stroke-width: 1.5; }
  .fill-blue { fill: var(--ec-fill-blue); stroke: var(--ec-blue); stroke-width: 1.5; }
  .fill-red { fill: var(--ec-fill-red); stroke: var(--ec-red); stroke-width: 1.5; }
  .fill-green { fill: var(--ec-fill-green); stroke: var(--ec-green); stroke-width: 1.5; }
  .fill-yellow { fill: var(--ec-fill-yellow); stroke: var(--ec-yellow); stroke-width: 1.5; }
  .label { font: 14px ui-sans-serif, system-ui, sans-serif; fill: var(--ec-text); }
  .small { font-size: 12px; fill: var(--ec-muted); }
  .title { font: 600 15px ui-sans-serif, system-ui, sans-serif; fill: var(--ec-title); }
  .accent-blue { stroke: var(--ec-blue); fill: none; }
  .accent-blue-fill { fill: var(--ec-blue); stroke: none; }
  .accent-red { stroke: var(--ec-red); fill: none; }
  .accent-red-fill { fill: var(--ec-red); stroke: none; }
  .accent-green { stroke: var(--ec-green); fill: none; }
  .accent-green-fill { fill: var(--ec-green); stroke: none; }
  .text-blue { fill: var(--ec-blue); }
  .text-red { fill: var(--ec-red); }
  .seg-on { stroke: var(--ec-red); fill: none; stroke-width: 4; }
  .seg-off { stroke: var(--ec-green); fill: none; stroke-width: 4; }
  .symbol-fill { fill: var(--ec-stroke); stroke: none; }
</style>
"""

def wrap(name: str, vb: str, body: str, w=720, h=400) -> str:
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}" width="{w}" height="{h}" role="img">
{STYLE}
{body}
</svg>
'''

DIAGRAMS = {}

# --- Chapter 1 ---
DIAGRAMS["atom-structure"] = wrap("atom", "0 0 720 320", '''
<text class="title" x="360" y="28" text-anchor="middle">碳原子结构（简化）</text>
<circle cx="360" cy="170" r="28" class="fill-red"/>
<text class="label" x="360" y="175" text-anchor="middle">原子核</text>
<text class="small" x="360" y="192" text-anchor="middle">质子 + 中子</text>
<circle cx="360" cy="170" r="55" class="stroke thin"/>
<text class="small" x="430" y="120">第 1 层 (2e)</text>
<circle cx="360" cy="170" r="90" class="stroke thin"/>
<text class="small" x="470" y="95">第 2 层 (8e)</text>
<circle cx="310" cy="130" r="5" class="fill-blue"/>
<circle cx="410" cy="130" r="5" class="fill-blue"/>
<circle cx="360" cy="95" r="5" class="fill-blue"/>
<circle cx="280" cy="170" r="5" class="fill-blue"/>
<circle cx="440" cy="170" r="5" class="fill-blue"/>
<circle cx="360" cy="245" r="5" class="fill-blue"/>
<text class="small" x="360" y="300" text-anchor="middle">电子（负电荷）围绕原子核运动</text>
''', h=320)

DIAGRAMS["graphite-diamond"] = wrap("graphite", "0 0 720 280", '''
<text class="title" x="180" y="28" text-anchor="middle">石墨（导体）</text>
<text class="title" x="540" y="28" text-anchor="middle">金刚石（绝缘体）</text>
<line x1="360" y1="40" x2="360" y2="260" class="divider"/>
<circle cx="120" cy="100" r="16" class="fill-light"/><circle cx="180" cy="100" r="16" class="fill-light"/>
<circle cx="150" cy="150" r="16" class="fill-light"/><circle cx="210" cy="150" r="16" class="fill-light"/>
<line x1="136" y1="100" x2="164" y2="100" class="stroke thin"/>
<line x1="166" y1="108" x2="142" y2="142" class="stroke thin"/>
<line x1="180" y1="116" x2="195" y2="134" class="stroke thin"/>
<circle cx="240" cy="120" r="6" class="fill-blue"/>
<text class="small" x="180" y="210" text-anchor="middle">层间自由电子</text>
<text class="small" x="180" y="230" text-anchor="middle">可移动 → 导电</text>
<circle cx="480" cy="110" r="16" class="fill-light"/><circle cx="540" cy="90" r="16" class="fill-light"/>
<circle cx="600" cy="110" r="16" class="fill-light"/><circle cx="510" cy="170" r="16" class="fill-light"/>
<circle cx="570" cy="170" r="16" class="fill-light"/><circle cx="630" cy="150" r="16" class="fill-light"/>
<line x1="496" y1="110" x2="524" y2="98" class="stroke thin"/>
<line x1="556" y1="98" x2="584" y2="110" class="stroke thin"/>
<line x1="488" y1="122" x2="502" y2="154" class="stroke thin"/>
<line x1="524" y1="170" x2="556" y2="170" class="stroke thin"/>
<text class="small" x="540" y="210" text-anchor="middle">共价键封闭</text>
<text class="small" x="540" y="230" text-anchor="middle">无自由电子 → 绝缘</text>
''', h=280)

DIAGRAMS["current-direction"] = wrap("current", "0 0 720 220", '''
<text class="title" x="360" y="28" text-anchor="middle">电流方向 vs 电子移动方向</text>
<rect x="80" y="60" width="560" height="50" rx="8" class="fill-light"/>
<line x1="120" y1="85" x2="600" y2="85" class="stroke"/>
<polygon points="590,85 575,78 575,92" class="accent-blue-fill"/>
<text class="label text-blue" x="360" y="90" text-anchor="middle">电流方向 I（正电荷方向）</text>
<line x1="600" y1="130" x2="120" y2="130" class="accent-red"/>
<polygon points="130,130 145,123 145,137" class="accent-red-fill"/>
<circle cx="200" cy="130" r="6" class="fill-red"/>
<circle cx="280" cy="130" r="6" class="fill-red"/>
<circle cx="360" cy="130" r="6" class="fill-red"/>
<text class="label text-red" x="360" y="135" text-anchor="middle">电子 e⁻ 实际移动方向（相反）</text>
<text class="small" x="360" y="190" text-anchor="middle">约定：电流方向与电子流动方向相反</text>
''', h=220)

DIAGRAMS["field-analogy"] = wrap("field", "0 0 720 300", '''
<text class="title" x="180" y="28" text-anchor="middle">重力场类比</text>
<text class="title" x="540" y="28" text-anchor="middle">电场</text>
<line x1="360" y1="40" x2="360" y2="280" class="divider-thin"/>
<rect x="140" y="220" width="80" height="12" class="fill-light"/>
<text class="small" x="180" y="250" text-anchor="middle">地面</text>
<circle cx="180" cy="120" r="18" class="fill-green"/>
<line x1="180" y1="138" x2="180" y2="220" class="accent-green" stroke-width="2" marker-end="url(#arr)"/>
<text class="small" x="180" y="100" text-anchor="middle">质量 m</text>
<text class="small" x="180" y="180" text-anchor="middle">重力 F=mg</text>
<circle cx="540" cy="160" r="22" class="fill-red"/>
<text class="small" x="540" y="165" text-anchor="middle">+</text>
<circle cx="480" cy="220" r="10" class="fill-blue"/>
<text class="small" x="480" y="224" text-anchor="middle">+</text>
<line x1="490" y1="215" x2="520" y2="175" class="accent-blue" stroke-width="2"/>
<text class="small" x="540" y="250" text-anchor="middle">试探电荷受力</text>
<defs><marker id="arr" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto"><polygon points="0,0 8,4 0,8" class="accent-green-fill"/></marker></defs>
''', h=300)

DIAGRAMS["circuit-basic"] = wrap("circuit", "0 0 720 260", '''
<text class="title" x="360" y="28" text-anchor="middle">基本电路组成</text>
<rect x="100" y="100" width="80" height="50" rx="6" class="fill-yellow"/>
<text class="label" x="140" y="130" text-anchor="middle">电源</text>
<line x1="180" y1="125" x2="260" y2="125" class="stroke"/>
<rect x="260" y="105" width="70" height="40" class="fill-light"/>
<text class="label" x="295" y="130" text-anchor="middle">开关</text>
<line x1="330" y1="125" x2="420" y2="125" class="stroke"/>
<circle cx="470" cy="125" r="28" class="fill-light"/>
<text class="label" x="470" y="130" text-anchor="middle">负载</text>
<line x1="498" y1="125" x2="580" y2="125" class="stroke"/>
<line x1="580" y1="125" x2="580" y2="200" class="stroke"/>
<line x1="580" y1="200" x2="100" y2="200" class="stroke"/>
<line x1="100" y1="200" x2="100" y2="150" class="stroke"/>
<text class="small" x="360" y="230" text-anchor="middle">电源 → 导线 → 开关 → 用电器 → 回到电源（闭合回路）</text>
''', h=260)

DIAGRAMS["series-parallel"] = wrap("sp", "0 0 720 340", '''
<text class="title" x="180" y="28" text-anchor="middle">串联</text>
<text class="title" x="540" y="28" text-anchor="middle">并联</text>
<line x1="360" y1="40" x2="360" y2="320" class="divider-thin"/>
<rect x="60" y="80" width="50" height="30" class="fill-yellow"/><line x1="110" y1="95" x2="140" y2="95" class="stroke"/>
<rect x="140" y="85" width="40" height="20" class="fill-light"/><text class="small" x="160" y="99" text-anchor="middle">R1</text>
<line x1="180" y1="95" x2="210" y2="95" class="stroke"/>
<rect x="210" y="85" width="40" height="20" class="fill-light"/><text class="small" x="230" y="99" text-anchor="middle">R2</text>
<line x1="250" y1="95" x2="300" y2="95" class="stroke"/>
<text class="small" x="180" y="140" text-anchor="middle">I 相同，U 分配</text>
<rect x="400" y="80" width="50" height="30" class="fill-yellow"/>
<line x1="450" y1="95" x2="500" y2="95" class="stroke"/>
<line x1="500" y1="95" x2="500" y2="70" class="stroke"/>
<line x1="500" y1="70" x2="580" y2="70" class="stroke"/>
<rect x="580" y="60" width="40" height="20" class="fill-light"/><text class="small" x="600" y="74" text-anchor="middle">R1</text>
<line x1="620" y1="70" x2="660" y2="70" class="stroke"/>
<line x1="660" y1="70" x2="660" y2="95" class="stroke"/>
<line x1="500" y1="95" x2="500" y2="120" class="stroke"/>
<line x1="500" y1="120" x2="580" y2="120" class="stroke"/>
<rect x="580" y="110" width="40" height="20" class="fill-light"/><text class="small" x="600" y="124" text-anchor="middle">R2</text>
<line x1="620" y1="120" x2="660" y2="120" class="stroke"/>
<line x1="660" y1="120" x2="660" y2="95" class="stroke"/>
<text class="small" x="540" y="160" text-anchor="middle">U 相同，I 分配</text>
''', h=340)

DIAGRAMS["ac-dc"] = wrap("acdc", "0 0 720 260", '''
<text class="title" x="180" y="28" text-anchor="middle">直流 DC</text>
<text class="title" x="540" y="28" text-anchor="middle">交流 AC</text>
<line x1="360" y1="40" x2="360" y2="240" class="divider-thin"/>
<line x1="60" y1="160" x2="300" y2="160" class="stroke thin"/>
<line x1="160" y1="160" x2="260" y2="160" class="accent-blue" stroke-width="3"/>
<polygon points="260,160 248,154 248,166" class="accent-blue-fill"/>
<text class="small" x="180" y="190" text-anchor="middle">方向不变</text>
<path d="M400,160 L430,100 L460,160 L490,220 L520,160 L550,100 L580,160" class="accent-blue"/>
<line x1="400" y1="160" x2="580" y2="160" class="stroke thin"/>
<text class="small" x="490" y="190" text-anchor="middle">方向周期性变化</text>
''', h=260)

# --- Resistors ---
DIAGRAMS["resistor-symbol"] = wrap("res", "0 0 720 180", '''
<text class="title" x="360" y="28" text-anchor="middle">电阻器电路符号</text>
<line x1="120" y1="90" x2="200" y2="90" class="stroke"/>
<polyline points="200,90 220,70 260,110 300,70 340,110 380,70 420,110 440,90" class="stroke"/>
<line x1="440" y1="90" x2="520" y2="90" class="stroke"/>
<text class="label" x="320" y="140" text-anchor="middle">R — 限制电流、分压</text>
''', h=180)

DIAGRAMS["color-band"] = wrap("band", "0 0 720 220", '''
<text class="title" x="360" y="28" text-anchor="middle">四色环电阻读法（示例 150Ω ±5%）</text>
<rect x="180" y="70" width="360" height="36" rx="18" fill="#d4a574" stroke="#92400e"/>
<rect x="200" y="70" width="16" height="36" fill="#8B4513"/><rect x="240" y="70" width="16" height="36" fill="#008000"/>
<rect x="280" y="70" width="16" height="36" fill="#1a1a1a"/><rect x="320" y="70" width="16" height="36" fill="#8B4513"/>
<rect x="480" y="70" width="16" height="36" fill="#FFD700"/>
<text class="small" x="208" y="130" text-anchor="middle">1</text>
<text class="small" x="248" y="130" text-anchor="middle">5</text>
<text class="small" x="288" y="130" text-anchor="middle">×10⁰</text>
<text class="small" x="488" y="130" text-anchor="middle">±5%</text>
<text class="label" x="360" y="180" text-anchor="middle">= 15 × 10⁰ = 150Ω</text>
''', h=220)

# --- Capacitor ---
DIAGRAMS["capacitor-structure"] = wrap("cap", "0 0 720 240", '''
<text class="title" x="360" y="28" text-anchor="middle">电容器结构</text>
<line x1="280" y1="80" x2="280" y2="180" class="stroke" stroke-width="4"/>
<line x1="320" y1="80" x2="320" y2="180" class="stroke" stroke-width="4"/>
<rect x="200" y="120" width="80" height="40" rx="4" class="fill-blue" opacity="0.5"/>
<text class="small" x="240" y="145" text-anchor="middle">极板 +</text>
<rect x="320" y="120" width="80" height="40" rx="4" class="fill-red" opacity="0.5"/>
<text class="small" x="360" y="145" text-anchor="middle">极板 −</text>
<text class="small" x="300" y="210" text-anchor="middle">中间电介质（绝缘） · 充电 = 储存电荷</text>
<line x1="120" y1="130" x2="280" y2="130" class="stroke"/>
<line x1="320" y1="130" x2="480" y2="130" class="stroke"/>
''', h=240)

DIAGRAMS["cap-ac-dc"] = wrap("capacd", "0 0 720 220", '''
<text class="title" x="360" y="28" text-anchor="middle">隔直流、通交流</text>
<text class="small" x="180" y="70" text-anchor="middle">直流 → 充满后开路</text>
<line x1="80" y1="100" x2="140" y2="100" class="stroke"/>
<line x1="140" y1="85" x2="140" y2="115" class="stroke" stroke-width="3"/>
<line x1="160" y1="85" x2="160" y2="115" class="stroke" stroke-width="3"/>
<line x1="160" y1="100" x2="280" y2="100" class="stroke" stroke-dasharray="6 4"/>
<text class="small" x="540" y="70" text-anchor="middle">交流 → 反复充放电</text>
<path d="M400,100 L430,80 L460,100 L490,120 L520,100" class="accent-blue"/>
<line x1="140" y1="100" x2="400" y2="100" class="stroke" opacity="0"/>
<line x1="520" y1="100" x2="620" y2="100" class="stroke"/>
<line x1="400" y1="85" x2="400" y2="115" class="stroke" stroke-width="3"/>
<line x1="420" y1="85" x2="420" y2="115" class="stroke" stroke-width="3"/>
''', h=220)

# --- Semiconductor ---
DIAGRAMS["n-p-type"] = wrap("np", "0 0 720 300", '''
<text class="title" x="180" y="28" text-anchor="middle">N 型半导体</text>
<text class="title" x="540" y="28" text-anchor="middle">P 型半导体</text>
<line x1="360" y1="40" x2="360" y2="280" class="divider-thin"/>
<text class="small" x="180" y="60" text-anchor="middle">掺杂磷 (P) → 多出的自由电子</text>
<circle cx="120" cy="120" r="10" class="fill-light"/><circle cx="180" cy="100" r="10" class="fill-light"/>
<circle cx="240" cy="120" r="10" class="fill-light"/>
<circle cx="200" cy="160" r="6" class="fill-blue"/><text class="small" x="200" y="180" text-anchor="middle">e⁻</text>
<circle cx="150" cy="150" r="6" class="fill-blue"/>
<text class="small" x="180" y="220" text-anchor="middle">多数载流子：电子</text>
<text class="small" x="540" y="60" text-anchor="middle">掺杂硼 (B) → 产生空穴</text>
<circle cx="480" cy="120" r="10" class="fill-light"/><circle cx="540" cy="100" r="10" class="fill-light"/>
<circle cx="600" cy="120" r="10" class="fill-light"/>
<circle cx="540" cy="160" r="8" class="fill-red" opacity="0.6"/><text class="small" x="540" y="180" text-anchor="middle">空穴</text>
<text class="small" x="540" y="220" text-anchor="middle">多数载流子：空穴</text>
''', h=300)

DIAGRAMS["pn-junction"] = wrap("pn", "0 0 720 320", '''
<text class="title" x="360" y="28" text-anchor="middle">PN 结与耗尽区</text>
<rect x="80" y="80" width="220" height="160" class="fill-red" opacity="0.25"/>
<text class="label" x="190" y="110" text-anchor="middle">P 型</text>
<rect x="420" y="80" width="220" height="160" class="fill-blue" opacity="0.25"/>
<text class="label" x="530" y="110" text-anchor="middle">N 型</text>
<rect x="300" y="80" width="120" height="160" class="fill-yellow"/>
<text class="small" x="360" y="165" text-anchor="middle">耗尽区</text>
<text class="small" x="190" y="200" text-anchor="middle">空穴 ⊕</text>
<text class="small" x="530" y="200" text-anchor="middle">电子 e⁻</text>
<text class="small" x="360" y="280" text-anchor="middle">内建电场阻止进一步扩散 · 正向偏置可导通</text>
''', h=320)

DIAGRAMS["pn-bias"] = wrap("pnbias", "0 0 720 260", '''
<text class="title" x="180" y="28" text-anchor="middle">正向偏置 → 导通</text>
<text class="title" x="540" y="28" text-anchor="middle">反向偏置 → 截止</text>
<line x1="360" y1="40" x2="360" y2="240" class="divider-thin"/>
<rect x="100" y="100" width="60" height="40" class="fill-red" opacity="0.4"/>
<rect x="200" y="100" width="60" height="40" class="fill-blue" opacity="0.4"/>
<text class="small" x="130" y="125" text-anchor="middle">P</text><text class="small" x="230" y="125" text-anchor="middle">N</text>
<text class="small" x="80" y="125">+</text><text class="small" x="280" y="125">−</text>
<line x1="160" y1="120" x2="200" y2="120" class="accent-green" stroke-width="2"/>
<polygon points="195,120 185,115 185,125" class="accent-green-fill"/>
<text class="small" x="180" y="160" text-anchor="middle">电流 P→N</text>
<rect x="420" y="100" width="60" height="40" class="fill-red" opacity="0.4"/>
<rect x="520" y="100" width="60" height="40" class="fill-blue" opacity="0.4"/>
<text class="small" x="450" y="125" text-anchor="middle">P</text><text class="small" x="550" y="125" text-anchor="middle">N</text>
<text class="small" x="400" y="125">−</text><text class="small" x="600" y="125">+</text>
<text class="small" x="520" y="160" text-anchor="middle">耗尽区扩大</text>
''', h=260)

# --- Diode ---
DIAGRAMS["diode-symbol"] = wrap("diode", "0 0 720 200", '''
<text class="title" x="360" y="28" text-anchor="middle">二极管符号与单向导电</text>
<line x1="120" y1="100" x2="280" y2="100" class="stroke"/>
<polygon points="280,100 320,80 320,120" class="fill-light"/>
<line x1="320" y1="80" x2="320" y2="120" class="stroke" stroke-width="3"/>
<line x1="320" y1="100" x2="480" y2="100" class="stroke"/>
<text class="label" x="300" y="150" text-anchor="middle">P → N（允许导通）</text>
<line x1="120" y1="180" x2="480" y2="180" class="stroke" stroke-dasharray="8 6" opacity="0.5"/>
<text class="small" x="300" y="175" text-anchor="middle">反向：截止</text>
''', h=200)

DIAGRAMS["led-circuit"] = wrap("led", "0 0 720 240", '''
<text class="title" x="360" y="28" text-anchor="middle">LED 限流电阻</text>
<rect x="80" y="90" width="60" height="40" class="fill-yellow"/><text class="small" x="110" y="115" text-anchor="middle">Vcc</text>
<line x1="140" y1="110" x2="200" y2="110" class="stroke"/>
<rect x="200" y="95" width="80" height="30" class="fill-light"/><text class="small" x="240" y="115" text-anchor="middle">R</text>
<line x1="280" y1="110" x2="340" y2="110" class="stroke"/>
<polygon points="340,110 370,95 370,125" class="fill-light"/>
<line x1="370" y1="95" x2="370" y2="125" class="stroke"/>
<line x1="370" y1="110" x2="420" y2="110" class="stroke"/>
<line x1="420" y1="110" x2="420" y2="160" class="stroke"/>
<line x1="420" y1="160" x2="110" y2="160" class="stroke"/>
<line x1="110" y1="160" x2="110" y2="130" class="stroke"/>
<text class="label" x="360" y="200" text-anchor="middle">R = (Vcc − V_LED) / I_LED</text>
''', h=240)

DIAGRAMS["7segment"] = wrap("7seg", "0 0 720 280", '''
<text class="title" x="360" y="28" text-anchor="middle">七段数码管（显示数字 3）</text>
<polyline points="200,80 280,80 270,90 210,90" class="seg-on"/>
<polyline points="290,95 290,145" class="seg-on"/>
<polyline points="290,155 290,205" class="seg-off"/>
<polyline points="200,210 280,210 270,200 210,200" class="seg-on"/>
<polyline points="200,155 200,205" class="seg-off"/>
<polyline points="200,95 200,145" class="seg-off"/>
<polyline points="205,150 275,150" class="seg-on"/>
<text class="small" x="240" y="250" text-anchor="middle">点亮 a,b,c,d,g → 显示 "3"</text>
<text class="small" x="480" y="120">共阴：公共阴极接地</text>
<text class="small" x="480" y="145">共阳：公共阳极接 Vcc</text>
''', h=280)

# --- Transistor ---
DIAGRAMS["npn-structure"] = wrap("npn", "0 0 720 300", '''
<text class="title" x="360" y="28" text-anchor="middle">NPN 三极管结构与电极</text>
<rect x="280" y="70" width="160" height="50" class="fill-red" opacity="0.3"/>
<text class="label" x="360" y="100" text-anchor="middle">C 集电极</text>
<rect x="300" y="130" width="120" height="40" class="fill-yellow" opacity="0.4"/>
<text class="label" x="360" y="155" text-anchor="middle">B 基极</text>
<rect x="280" y="180" width="160" height="50" class="fill-red" opacity="0.3"/>
<text class="label" x="360" y="210" text-anchor="middle">E 发射极</text>
<text class="small" x="360" y="260" text-anchor="middle">小电流 Ib 控制大电流 Ic · 作开关或放大</text>
''', h=300)

DIAGRAMS["npn-switch"] = wrap("npnsw", "0 0 720 280", '''
<text class="title" x="360" y="28" text-anchor="middle">NPN 低端开关</text>
<rect x="80" y="80" width="50" height="30" class="fill-yellow"/><text class="small" x="105" y="100" text-anchor="middle">Vcc</text>
<line x1="130" y1="95" x2="200" y2="95" class="stroke"/>
<rect x="200" y="80" width="80" height="30" class="fill-light"/><text class="small" x="240" y="100" text-anchor="middle">负载</text>
<line x1="280" y1="95" x2="340" y2="95" class="stroke"/>
<line x1="340" y1="70" x2="340" y2="130" class="stroke"/>
<line x1="320" y1="130" x2="360" y2="130" class="stroke"/>
<line x1="340" y1="130" x2="340" y2="180" class="stroke"/>
<line x1="340" y1="180" x2="340" y2="220" class="stroke"/>
<line x1="340" y1="220" x2="120" y2="220" class="stroke"/>
<line x1="120" y1="220" x2="120" y2="110" class="stroke"/>
<text class="small" x="380" y="105">C</text><text class="small" x="380" y="135">B</text><text class="small" x="380" y="185">E</text>
<rect x="420" y="120" width="60" height="30" class="fill-green" opacity="0.4"/>
<text class="small" x="450" y="140" text-anchor="middle">GPIO</text>
<line x1="450" y1="150" x2="360" y2="130" class="stroke"/>
<text class="small" x="360" y="260" text-anchor="middle">GPIO 高 → 三极管导通 → 负载工作</text>
''', h=280)

DIAGRAMS["transistor-symbols"] = wrap("trsym", "0 0 720 220", '''
<text class="title" x="180" y="28" text-anchor="middle">NPN</text>
<text class="title" x="540" y="28" text-anchor="middle">PNP</text>
<line x1="360" y1="40" x2="360" y2="200" class="divider-thin"/>
<line x1="180" y1="120" x2="280" y2="120" class="stroke"/>
<line x1="180" y1="80" x2="180" y2="160" class="stroke"/>
<line x1="180" y1="160" x2="220" y2="160" class="stroke"/>
<polygon points="220,160 210,155 210,165" class="symbol-fill"/>
<text class="small" x="180" y="190" text-anchor="middle">箭头 P→N 在 E</text>
<line x1="540" y1="120" x2="440" y2="120" class="stroke"/>
<line x1="540" y1="80" x2="540" y2="160" class="stroke"/>
<line x1="540" y1="80" x2="500" y2="80" class="stroke"/>
<polygon points="500,80 510,75 510,85" class="symbol-fill"/>
<text class="small" x="540" y="190" text-anchor="middle">中间=B，箭头线=E</text>
''', h=220)

# --- MOSFET ---
DIAGRAMS["nmos-structure"] = wrap("nmos", "0 0 720 300", '''
<text class="title" x="360" y="28" text-anchor="middle">N 沟道增强型 MOS 管</text>
<rect x="200" y="80" width="320" height="180" class="fill-yellow" opacity="0.2"/>
<text class="small" x="360" y="100" text-anchor="middle">P 型衬底</text>
<rect x="240" y="120" width="60" height="100" class="fill-blue" opacity="0.4"/>
<text class="small" x="270" y="170" text-anchor="middle">S</text>
<rect x="420" y="120" width="60" height="100" class="fill-blue" opacity="0.4"/>
<text class="small" x="450" y="170" text-anchor="middle">D</text>
<rect x="330" y="70" width="60" height="20" class="fill-green" opacity="0.5"/>
<text class="small" x="360" y="85" text-anchor="middle">G 栅极</text>
<text class="small" x="360" y="280" text-anchor="middle">V_GS &gt; V_th → 沟道形成 → D→S 导通</text>
''', h=300)

DIAGRAMS["mosfet-symbols"] = wrap("mos", "0 0 720 260", '''
<text class="title" x="360" y="28" text-anchor="middle">MOS 管符号速记</text>
<text class="small" x="120" y="70">1. 中间 = G（栅极）</text>
<text class="small" x="120" y="95">2. 线最多 = S（源极）</text>
<text class="small" x="120" y="120">3. 箭头指向 G → N 沟道</text>
<text class="small" x="120" y="145">4. 虚线 = 增强型，实线 = 耗尽型</text>
<line x1="400" y1="80" x2="400" y2="200" class="stroke"/>
<line x1="400" y1="120" x2="480" y2="120" class="stroke"/>
<line x1="480" y1="100" x2="480" y2="180" class="stroke"/>
<line x1="480" y1="140" x2="520" y2="140" class="stroke"/>
<polygon points="520,140 512,136 512,144" class="symbol-fill"/>
<text class="small" x="440" y="115">G</text>
<text class="small" x="490" y="195">S</text>
<text class="small" x="530" y="145">D</text>
<text class="small" x="360" y="240" text-anchor="middle">体二极管需反偏 · N 增强型 V_GS &gt; V_th 导通</text>
''', h=260)

DIAGRAMS["packaging"] = wrap("pkg", "0 0 720 260", '''
<text class="title" x="180" y="28" text-anchor="middle">插件封装 THT</text>
<text class="title" x="540" y="28" text-anchor="middle">贴片封装 SMT</text>
<line x1="360" y1="40" x2="360" y2="240" class="divider-thin"/>
<rect x="140" y="100" width="80" height="40" class="fill-light"/>
<line x1="160" y1="140" x2="160" y2="180" class="stroke"/>
<line x1="200" y1="140" x2="200" y2="180" class="stroke"/>
<rect x="150" y="180" width="60" height="8" class="fill-green" opacity="0.5"/>
<text class="small" x="180" y="210" text-anchor="middle">引脚穿 PCB 孔</text>
<rect x="500" y="110" width="80" height="30" class="fill-light"/>
<rect x="490" y="145" width="20" height="8" class="fill-yellow"/>
<rect x="570" y="145" width="20" height="8" class="fill-yellow"/>
<rect x="480" y="160" width="120" height="6" class="fill-green" opacity="0.5"/>
<text class="small" x="540" y="210" text-anchor="middle">直接焊在 PCB 表面</text>
''', h=260)

DIAGRAMS["rectifier"] = wrap("rect", "0 0 720 240", '''
<text class="title" x="180" y="28" text-anchor="middle">半波整流</text>
<text class="title" x="540" y="28" text-anchor="middle">全波整流</text>
<line x1="360" y1="40" x2="360" y2="220" class="divider-thin"/>
<path d="M80,140 Q120,80 160,140 Q200,200 240,140" class="accent-blue"/>
<path d="M80,140 L240,140" class="accent-red" stroke-width="0"/>
<path d="M160,140 L240,140" class="accent-red" stroke-dasharray="4 4" opacity="0.4"/>
<text class="small" x="180" y="190" text-anchor="middle">只保留正半周</text>
<path d="M400,140 Q440,80 480,140 Q520,200 560,140 Q600,80 640,140" class="accent-blue"/>
<path d="M400,140 L640,140" class="accent-red"/>
<text class="small" x="520" y="190" text-anchor="middle">正负半周都变同一方向</text>
''', h=240)


def main():
    for name, svg in DIAGRAMS.items():
        path = OUT / f"{name}.svg"
        path.write_text(svg.strip() + "\n", encoding="utf-8")
        print(f"Wrote {path.name}")

    # Compress selected schematic-like PNGs from PDF
    try:
        from PIL import Image
        import io
        raw = Path(__file__).resolve().parent.parent / "public" / "electronic-components" / "raw"
        fig = Path(__file__).resolve().parent.parent / "public" / "electronic-components" / "figures"
        fig.mkdir(parents=True, exist_ok=True)
        picks = {
            "p15_img2.png": "circuit-symbols.png",
            "p41_img1.png": "e12-series.png",
            "p69_img1.png": "led-iv-curve.png",
        }
        for src_name, dst_name in picks.items():
            src = raw / src_name
            if not src.exists():
                continue
            im = Image.open(src).convert("RGB")
            max_w = 960
            if im.width > max_w:
                im = im.resize((max_w, int(im.height * max_w / im.width)), Image.Resampling.LANCZOS)
            im.save(fig / dst_name, optimize=True, quality=85)
            print(f"Compressed {dst_name}")
    except ImportError:
        print("PIL not available, skip PNG compression")

    print(f"Total SVG: {len(DIAGRAMS)}")


if __name__ == "__main__":
    main()
