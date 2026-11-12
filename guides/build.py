"""Builds the homeowner guides (guides/<slug>.html and guides/index.html).

Edit the GUIDES list below, then run:  python3 guides/build.py
Each guide gets the site header and footer, Article + breadcrumb structured
data for Google, a short answer box at the top (what AI Overviews quote),
and a Nestory download box at the end.
"""
import html
import json
import os

SITE = "https://trynestory.com"
APP = "https://apps.apple.com/app/id6826665963"
UPDATED = "2026-11-11"
HERE = os.path.dirname(os.path.abspath(__file__))

APPLE = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M16.37 12.6c-.02-2.3 1.88-3.4 1.96-3.46-1.07-1.56-2.73-1.78-3.32-1.8-1.41-.14-2.76.83-3.48.83-.72 0-1.82-.81-3-.79-1.54.02-2.96.9-3.76 2.27-1.6 2.78-.41 6.9 1.15 9.16.76 1.1 1.67 2.34 2.86 2.3 1.15-.05 1.58-.74 2.97-.74 1.38 0 1.78.74 2.99.72 1.24-.02 2.02-1.12 2.77-2.23.87-1.28 1.23-2.52 1.25-2.58-.03-.01-2.4-.92-2.42-3.66zM14.1 5.86c.63-.77 1.06-1.83.94-2.89-.91.04-2.02.61-2.67 1.37-.58.67-1.1 1.76-.96 2.8 1.02.08 2.06-.52 2.69-1.28z"/></svg>'

GUIDES = [
    {
        "slug": "how-long-do-appliances-last",
        "title": "How Long Do Appliances Last? Typical Lifespans for Every Major Appliance",
        "short": "How long do appliances last?",
        "desc": "Typical lifespans for refrigerators, washers, dishwashers, water heaters, furnaces, AC units and more, plus signs it's time to replace and how to make them last longer.",
        "lede": "Most major appliances last 8 to 20 years. Here's what to expect from each one, the signs one is near the end, and how to plan for it before it breaks.",
        "cta": "Nestory keeps the model and serial number, warranty and repair history for every appliance, so you always know what you have and what's still covered.",
        "body": """
<div class="answer"><p><strong>Short answer:</strong> a refrigerator typically lasts 10–15 years, a washer 10–14, a dishwasher 9–12, a tank water heater 8–12, a furnace 15–20 and a central air conditioner 12–17. How you use and maintain an appliance can move those numbers by several years in either direction.</p></div>

<h2>Typical appliance lifespans</h2>
<table>
<tr><th>Appliance</th><th>Typical lifespan</th></tr>
<tr><td>Refrigerator</td><td>10–15 years</td></tr>
<tr><td>Freezer (standalone)</td><td>10–20 years</td></tr>
<tr><td>Dishwasher</td><td>9–12 years</td></tr>
<tr><td>Washing machine</td><td>10–14 years</td></tr>
<tr><td>Clothes dryer</td><td>10–13 years</td></tr>
<tr><td>Range or oven (gas)</td><td>13–15 years</td></tr>
<tr><td>Range or oven (electric)</td><td>11–13 years</td></tr>
<tr><td>Microwave</td><td>7–10 years</td></tr>
<tr><td>Garbage disposal</td><td>8–12 years</td></tr>
<tr><td>Water heater (tank)</td><td>8–12 years</td></tr>
<tr><td>Water heater (tankless)</td><td>15–20 years</td></tr>
<tr><td>Furnace (gas)</td><td>15–20 years</td></tr>
<tr><td>Central air conditioner</td><td>12–17 years</td></tr>
<tr><td>Heat pump</td><td>10–15 years</td></tr>
<tr><td>Asphalt shingle roof</td><td>20–30 years</td></tr>
</table>
<p class="note">These are typical ranges gathered from manufacturer guidance and home industry estimates. Your appliance may last more or less depending on the brand, how often it runs, your water quality and how well it's maintained.</p>

<h2>Signs an appliance is near the end</h2>
<ul>
<li><strong>Refrigerator:</strong> food spoils faster, the motor runs constantly, frost builds up, or the back gets unusually hot.</li>
<li><strong>Washer and dryer:</strong> loud banging, leaks, clothes still wet or not drying, or the drum won't spin.</li>
<li><strong>Dishwasher:</strong> dishes come out dirty, water pools in the bottom, or rust appears inside the tub.</li>
<li><strong>Water heater:</strong> rusty or cloudy hot water, rumbling noises, a leak around the base, or hot water running out quickly.</li>
<li><strong>Furnace and AC:</strong> uneven temperatures, short cycling, rising energy bills, or repairs every season.</li>
</ul>

<h2>Repair or replace?</h2>
<p>A common rule of thumb: if an appliance is past half of its expected lifespan and the repair would cost more than half the price of a new one, replacing it usually makes more sense. Before you pay for any repair, check whether the part is still under warranty. Compressors, sealed systems, heat exchangers and water heater tanks often have longer coverage than the rest of the appliance.</p>

<h2>How to make appliances last longer</h2>
<ul>
<li>Change your HVAC filter every 1–3 months.</li>
<li>Vacuum the refrigerator's condenser coils once a year.</li>
<li>Clean the dishwasher filter every month.</li>
<li>Clean the dryer lint trap after every load and the dryer vent once a year.</li>
<li>Flush the water heater once a year to clear sediment.</li>
<li>Have the furnace serviced in the fall and the AC in the spring.</li>
</ul>

<h2>The simple habit that helps most: write down install dates</h2>
<p>Most people have no idea how old their water heater or furnace is until it fails. If you record the install or purchase date of each appliance, you'll know which ones are getting close to the end and can budget for them instead of being surprised by an emergency replacement. The model and serial number usually encode the manufacture date too, so save those while you're at it.</p>
""",
    },
    {
        "slug": "home-inventory-for-insurance",
        "title": "How to Make a Home Inventory for Insurance (Step-by-Step Checklist)",
        "short": "Home inventory for insurance",
        "desc": "A step-by-step guide to documenting your home's belongings before a storm, fire or break-in, so an insurance claim is easier if something happens.",
        "lede": "If a storm, fire or break-in damages your home, your insurance company will ask what you owned. A home inventory made ahead of time makes that question easy to answer.",
        "cta": "Nestory keeps photos, brand, model and serial numbers, warranties and repairs for everything in your home, and exports it all as one PDF report you can share with your insurer.",
        "body": """
<div class="answer"><p><strong>Short answer:</strong> walk through your home room by room, take photos of everything of value, write down the brand, model, serial number and approximate purchase date and price of larger items, keep receipts where you can, and store the inventory somewhere other than your house, such as a cloud account. Update it once a year and after big purchases.</p></div>

<h2>Why a home inventory matters</h2>
<p>After a loss, most insurers ask you to list what was damaged or destroyed, often with details like brand, age and value. Doing that from memory, in a stressful moment, is hard. People commonly forget a large share of what they owned. A list made before anything happens helps you file a more complete claim, and it also helps you check whether you have enough coverage in the first place.</p>

<h2>Step-by-step: how to make your home inventory</h2>
<ol>
<li><strong>Start with the big things.</strong> Appliances, electronics, furniture, and home systems like the water heater, furnace and AC are the most expensive to replace.</li>
<li><strong>Go room by room.</strong> Kitchen, living room, bedrooms, bathrooms, garage, basement, attic and outdoor areas. Don't forget closets and storage.</li>
<li><strong>Take photos.</strong> One wide photo of each room, then close-ups of valuable items. A slow video walk-through works too.</li>
<li><strong>Photograph the labels.</strong> The sticker with the model and serial number is the fastest way to prove exactly what you had.</li>
<li><strong>Add the details.</strong> Brand, model, serial number, approximate purchase date and price. Exact numbers aren't required for everything; good estimates are far better than nothing.</li>
<li><strong>Keep receipts and warranties.</strong> A photo of the receipt is enough. Warranties also matter after smaller incidents, like an appliance that fails on its own.</li>
<li><strong>Store it off-site.</strong> A list kept only in a drawer, or only on a computer at home, can be lost in the same event. Save it to a cloud account and keep a copy you can share.</li>
<li><strong>Update it once a year.</strong> Add big purchases as you make them, and do a quick review each year, for example at the start of storm season.</li>
</ol>

<h2>What to include</h2>
<ul>
<li>Major appliances and home systems (with model and serial numbers)</li>
<li>TVs, computers, phones and other electronics</li>
<li>Furniture and rugs</li>
<li>Jewelry, art and collectibles (these may need separate coverage, so ask your insurer)</li>
<li>Tools, bikes and outdoor equipment</li>
<li>Clothing and shoes (a photo of each closet is usually enough)</li>
<li>Repair and renovation records, which show the condition and upgrades of your home</li>
</ul>

<h2>If something happens</h2>
<p>Every policy is different, so always follow your insurer's instructions. Common advice includes:</p>
<ul>
<li>Contact your insurance company as soon as you safely can.</li>
<li>Take photos and video of the damage before cleaning up, and prevent further damage if it's safe to do so.</li>
<li>Don't throw out damaged items until your insurer says it's OK.</li>
<li>Keep receipts for repairs and for any extra living costs if you can't stay in your home.</li>
<li>Share your inventory list with your adjuster.</li>
</ul>
<p class="note">This guide is general information, not insurance or legal advice. Check your policy or talk to your agent about what's covered.</p>
""",
    },
    {
        "slug": "find-model-serial-number",
        "title": "Where to Find the Model and Serial Number on Any Appliance",
        "short": "Where to find model and serial numbers",
        "desc": "Exactly where the model and serial number sticker is on refrigerators, dishwashers, washers, dryers, ovens, microwaves, water heaters, furnaces and AC units.",
        "lede": "Every repair, warranty claim and replacement part starts with the same question: what's the model number? Here's where to find it on each appliance.",
        "cta": "Snap the label once and Nestory keeps the brand, model and serial number with the appliance, so you never have to crawl behind it again.",
        "body": """
<div class="answer"><p><strong>Short answer:</strong> the model and serial number are printed on a sticker or metal plate, usually somewhere you can see with the door open: on the inside wall or ceiling of a refrigerator, the edge of a dishwasher door, the door frame of a washer or dryer, behind the storage drawer of an oven, and on the side of a water heater tank.</p></div>

<h2>Where to look, appliance by appliance</h2>
<table>
<tr><th>Appliance</th><th>Where the label usually is</th></tr>
<tr><td>Refrigerator</td><td>Inside the fresh food section on a side wall or the ceiling, near the crisper drawers, or at the bottom behind the front grille. Some are on the back.</td></tr>
<tr><td>Chest freezer</td><td>On the back or side of the outside cabinet, or under the lid.</td></tr>
<tr><td>Dishwasher</td><td>Open the door and look along the edge of the door or the side of the tub opening.</td></tr>
<tr><td>Front-load washer</td><td>Around the door opening, inside the door frame, or on the back panel.</td></tr>
<tr><td>Top-load washer</td><td>Under the lid, on the back of the control panel, or on the back of the cabinet.</td></tr>
<tr><td>Dryer</td><td>Inside the door opening on the frame, or on the back panel.</td></tr>
<tr><td>Range or oven</td><td>Behind the storage or warming drawer, on the frame behind the oven door, or on the back.</td></tr>
<tr><td>Over-the-range microwave</td><td>Inside the door frame or on the inside wall when the door is open.</td></tr>
<tr><td>Countertop microwave</td><td>On the back or the bottom.</td></tr>
<tr><td>Water heater</td><td>On the rating plate, a large label on the side of the tank.</td></tr>
<tr><td>Furnace</td><td>Inside the front access panel, on the blower compartment door or wall.</td></tr>
<tr><td>Central AC (outdoor unit)</td><td>On the data plate on the side or back of the condenser.</td></tr>
<tr><td>Garbage disposal</td><td>On the bottom of the unit, under the sink.</td></tr>
</table>
<p class="note">Locations vary by brand and model. If you can't find it, the manual or the manufacturer's website usually shows exactly where to look.</p>

<h2>Model number vs. serial number</h2>
<p><strong>The model number</strong> tells you what kind of appliance it is. You need it for manuals, replacement parts and repair quotes. <strong>The serial number</strong> identifies your specific unit. You need it for warranty claims and recalls, and many brands encode the manufacture date in it, which tells you how old the appliance is.</p>

<h2>Tips</h2>
<ul>
<li>Take a photo of every label now, while nothing is broken. It takes a few minutes for the whole house.</li>
<li>Use your phone's flashlight and zoom for labels in dark corners.</li>
<li>If a label is worn, check the original box, receipt or registration email.</li>
<li>Register new appliances with the manufacturer. It can unlock longer warranties and recall notices.</li>
</ul>
""",
    },
    {
        "slug": "new-home-warranties",
        "title": "What's Under Warranty in Your Home? A Homeowner's Guide",
        "short": "What's under warranty in your home",
        "desc": "Builder warranties, home warranties and manufacturer warranties explained, plus how long appliances, water heaters, HVAC, roofs and windows are typically covered.",
        "lede": "Many homeowners pay for repairs that a warranty would have covered. Here's what is often still under warranty in your home, and how to find out.",
        "cta": "Nestory keeps every warranty's end date in one place and reminds you before it expires, so you can get repairs done while they're still covered.",
        "body": """
<div class="answer"><p><strong>Short answer:</strong> appliances usually come with a 1-year manufacturer warranty, but key parts often last longer: refrigerator compressors frequently 5–10 years, water heater tanks often 6–12 years, and HVAC parts commonly 5–10 years when registered. Roof shingles and windows often carry 10–25+ year manufacturer warranties, and new construction homes usually have a builder warranty.</p></div>

<h2>The three kinds of warranties in a home</h2>
<h3>1. Manufacturer warranties</h3>
<p>These come with each product, from appliances to shingles to windows. They cover defects, not wear and tear or damage. Coverage often differs by part: the whole appliance might be covered for one year, while the most expensive part is covered much longer.</p>
<h3>2. Builder warranties (new construction)</h3>
<p>Many builders offer a warranty on a newly built home. A common structure is 1 year for workmanship and materials, 2 years for systems like plumbing, electrical and HVAC, and 10 years for major structural defects. Terms vary by builder and state, so read yours.</p>
<h3>3. Home warranties (service contracts)</h3>
<p>A home warranty is a separate service plan, often bought by the seller or buyer at closing, that helps pay for repairs to systems and appliances, usually for one year at a time with a service fee per visit. It's different from a manufacturer warranty, and the two can overlap.</p>

<h2>Typical coverage by item</h2>
<table>
<tr><th>Item</th><th>Typical manufacturer coverage</th></tr>
<tr><td>Most appliances</td><td>1 year parts and labor</td></tr>
<tr><td>Refrigerator compressor / sealed system</td><td>Often 5–10 years on parts</td></tr>
<tr><td>Water heater tank</td><td>Often 6–12 years, depending on the model</td></tr>
<tr><td>Furnace, AC and heat pump parts</td><td>Often 5–10 years, with the longer term usually requiring registration</td></tr>
<tr><td>Furnace heat exchanger</td><td>Often 20 years to lifetime</td></tr>
<tr><td>Roof shingles</td><td>Often 25 years to "limited lifetime" on materials. Installer workmanship is separate.</td></tr>
<tr><td>Windows</td><td>Often 10–20 years, some lifetime on the glass</td></tr>
</table>
<p class="note">These are common ranges, not guarantees. Check the warranty for your exact model.</p>

<h2>Don't miss these</h2>
<ul>
<li><strong>Registration deadlines.</strong> Some HVAC brands only give the longer parts warranty if the system is registered within a set time after installation, often about 60 days.</li>
<li><strong>Transfers.</strong> Some roof and window warranties transfer to a new owner, sometimes only if you register the transfer. If you just bought a home, ask the seller for warranty documents.</li>
<li><strong>Credit card protection.</strong> Some credit cards extend the manufacturer's warranty on items you bought with them. Benefits vary and change, so check your card's terms.</li>
<li><strong>Proof of purchase.</strong> Most claims need the purchase or install date. Keep receipts and installer invoices.</li>
</ul>

<h2>How to find what's still covered</h2>
<ol>
<li>List your appliances and systems, with model and serial numbers.</li>
<li>Look up each warranty on the manufacturer's website using the model number.</li>
<li>Write down each end date, especially for the expensive parts.</li>
<li>Set a reminder a month or two before each one expires, so you can have anything suspicious checked while it's still free.</li>
</ol>
""",
    },
    {
        "slug": "seasonal-home-maintenance-checklist",
        "title": "Seasonal Home Maintenance Checklist (Spring, Summer, Fall and Winter)",
        "short": "Seasonal home maintenance checklist",
        "desc": "A simple home maintenance checklist for every season and every month: HVAC filters, smoke detectors, gutters, water heater, dryer vent and more.",
        "lede": "A little upkeep each season prevents most of the expensive surprises. Here's what to do and when.",
        "cta": "Set each task once in Nestory and get a reminder on your phone when it's due, along with the history of everything you've done.",
        "body": """
<div class="answer"><p><strong>Short answer:</strong> every month, test smoke and CO detectors and clean the dishwasher filter. Every 1–3 months, change the HVAC filter. In spring, service the AC and clean the gutters. In summer, check outside caulk and the dryer vent. In fall, service the furnace and clean the gutters again. In winter, protect pipes and check for ice dams.</p></div>

<h2>Every month</h2>
<ul>
<li>Test smoke and carbon monoxide detectors.</li>
<li>Clean the dishwasher filter.</li>
<li>Check the HVAC filter, and change it every 1–3 months (more often with pets or allergies).</li>
<li>Test GFCI outlets in the kitchen and bathrooms.</li>
<li>Run water in unused sinks and showers so drain traps don't dry out.</li>
</ul>

<h2>Spring</h2>
<ul>
<li>Have the air conditioner serviced before the first hot days.</li>
<li>Clean gutters and downspouts, and make sure water drains away from the foundation.</li>
<li>Inspect the roof for damaged or missing shingles after winter.</li>
<li>Test the sump pump if you have one.</li>
<li>Check outdoor faucets and hoses for leaks.</li>
<li>Review your home inventory before storm season.</li>
</ul>

<h2>Summer</h2>
<ul>
<li>Clean the dryer vent all the way to the outside.</li>
<li>Check caulk and weatherstripping around windows and doors.</li>
<li>Clean the refrigerator's condenser coils.</li>
<li>Keep plants and debris at least two feet away from the outdoor AC unit.</li>
<li>Look for signs of pests around the foundation.</li>
</ul>

<h2>Fall</h2>
<ul>
<li>Have the furnace or heat pump serviced before it gets cold.</li>
<li>Clean the gutters again after the leaves fall.</li>
<li>Drain and shut off outdoor faucets, and disconnect hoses.</li>
<li>Flush the water heater to clear sediment.</li>
<li>Have the chimney inspected and cleaned if you use a fireplace.</li>
<li>Replace smoke and CO detector batteries (or once a year, whenever you remember best).</li>
</ul>

<h2>Winter</h2>
<ul>
<li>Keep the house heated enough to protect pipes, and insulate any exposed pipes.</li>
<li>Know where your main water shut-off is in case a pipe bursts.</li>
<li>Watch for ice dams and icicles along the roof edge.</li>
<li>Check the attic for leaks or condensation.</li>
<li>Reverse ceiling fans to push warm air down.</li>
</ul>

<h2>Once a year</h2>
<ul>
<li>Replace the refrigerator water filter (about every 6 months for many models).</li>
<li>Check the water heater's pressure relief valve.</li>
<li>Test the garage door's auto-reverse.</li>
<li>Update your home inventory and warranty list.</li>
</ul>
<p class="note">Always follow your manufacturer's instructions, and call a professional for gas, electrical and roof work.</p>
""",
    },
]


def page(title, desc, url, body, schema, crumbs_html, h1, lede, meta_line=""):
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<link rel="canonical" href="{url}">
<meta name="apple-itunes-app" content="app-id=6826665963">
<meta property="og:site_name" content="Nestory">
<meta property="og:type" content="article">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:image" content="{SITE}/img/og.jpg">
<meta property="og:url" content="{url}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/favicon.png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/guides/guide.css">
<script type="application/ld+json">
{json.dumps(schema, indent=2, ensure_ascii=False)}
</script>
</head>
<body>
<header><div class="wrap">
  <a class="brand" href="/"><img src="/img/icon.png" alt="">Nestory</a>
  <nav>
    <a class="link" href="/#features">Features</a>
    <a class="link" href="/guides/">Guides</a>
    <a class="btn" href="{APP}">{APPLE}Download</a>
  </nav>
</div></header>
<div class="hero"><div class="wrap">
  <div class="crumbs">{crumbs_html}</div>
  <h1>{html.escape(h1)}</h1>
  <p class="lede">{html.escape(lede)}</p>
  {meta_line}
</div></div>
{body}
<footer><div class="wrap">
  <span>© 2026 Nestory</span>
  <nav>
    <a href="/">Home</a>
    <a href="/guides/">Guides</a>
    <a href="/support.html">Support</a>
    <a href="/privacy.html">Privacy</a>
    <a href="mailto:hello.nestory.app@gmail.com">Contact</a>
  </nav>
</div></footer>
</body>
</html>
"""


def cta(text):
    return f"""<div class="cta"><img class="icon" src="/img/icon.png" alt="Nestory app icon"><div>
<h3>Keep track of it all with Nestory</h3>
<p>{html.escape(text)} Free on iPhone.</p>
<a class="badge" href="{APP}" aria-label="Download Nestory on the App Store">{APPLE}<span><small>Download on the</small>App Store</span></a>
</div></div>"""


def breadcrumb(items):
    return {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": n, "item": u} for i, (n, u) in enumerate(items)]}


def build():
    for g in GUIDES:
        url = f"{SITE}/guides/{g['slug']}.html"
        others = [o for o in GUIDES if o is not g]
        more = "".join(f'<a href="/guides/{o["slug"]}.html">{html.escape(o["short"])}<span>{html.escape(o["desc"][:90].rsplit(" ", 1)[0])}…</span></a>' for o in others)
        body = f'<article>{g["body"]}{cta(g["cta"])}</article>\n<section class="more"><h2>More homeowner guides</h2><div class="cards">{more}</div></section>'
        schema = {"@context": "https://schema.org", "@graph": [
            {"@type": "Article", "headline": g["title"], "description": g["desc"], "url": url,
             "image": f"{SITE}/img/og.jpg", "datePublished": UPDATED, "dateModified": UPDATED,
             "author": {"@type": "Organization", "name": "Nestory", "url": SITE + "/"},
             "publisher": {"@type": "Organization", "name": "Nestory", "logo": {"@type": "ImageObject", "url": f"{SITE}/img/icon.png"}},
             "mainEntityOfPage": url},
            breadcrumb([("Home", SITE + "/"), ("Guides", SITE + "/guides/"), (g["short"], url)]),
        ]}
        crumbs = f'<a href="/">Home</a> › <a href="/guides/">Guides</a> › {html.escape(g["short"])}'
        out = page(g["title"] + " | Nestory", g["desc"], url, body, schema, crumbs, g["title"], g["lede"],
                   f'<div class="meta">Updated November 2026 · By the Nestory team</div>')
        open(os.path.join(HERE, g["slug"] + ".html"), "w").write(out)

    url = f"{SITE}/guides/"
    cards = "".join(f'<a href="/guides/{g["slug"]}.html">{html.escape(g["short"])}<span>{html.escape(g["desc"])}</span></a>' for g in GUIDES)
    body = f'<section class="more" style="padding-top:48px"><div class="cards">{cards}</div>{cta("Nestory keeps every appliance, warranty, manual and repair for your home in one place, with reminders before warranties expire.")}</section>'
    schema = {"@context": "https://schema.org", "@graph": [
        {"@type": "CollectionPage", "name": "Homeowner guides", "url": url, "description": "Practical guides for homeowners from Nestory."},
        breadcrumb([("Home", SITE + "/"), ("Guides", url)]),
    ]}
    out = page("Homeowner Guides: Appliances, Warranties and Home Inventory | Nestory",
               "Practical guides for homeowners: appliance lifespans, home inventory for insurance, model and serial numbers, warranties and seasonal maintenance.",
               url, body, schema, '<a href="/">Home</a> › Guides', "Homeowner guides",
               "Practical answers for looking after your home: appliances, warranties, insurance and upkeep.")
    open(os.path.join(HERE, "index.html"), "w").write(out)
    print("built", len(GUIDES), "guides + index")


if __name__ == "__main__":
    build()
