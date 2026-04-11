import re

with open("index.html", "r", encoding="utf-8") as f:
    text = f.read()

# 1. FIX LOGO LINK (Dashboard)
# Find the exact logo link which currently has features.html and contains the SVG or image
text = re.sub(
    r'<a href="features\.html"( class="flex items-center gap-2 group shrink-0">)',
    r'<a href="index.html"\1',
    text
)

# Also fix the footer logo if it exists
text = re.sub(
    r'<a href="features\.html"( class="flex items-center gap-2 group mb-6">)',
    r'<a href="index.html"\1',
    text
)

# 2. FIX SPECIFIC EXPLORE LINKS
text = re.sub(
    r'<a href="features\.html"([^>]*>Explore AI Ads)',
    r'<a href="ai-ads.html"\1',
    text
)
text = re.sub(
    r'<a href="features\.html"([^>]*>Explore Forms)',
    r'<a href="forms.html"\1',
    text
)
text = re.sub(
    r'<a href="features\.html"([^>]*>Explore Payments)',
    r'<a href="payments.html"\1',
    text
)
# Pricing in header
text = re.sub(
    r'<a href="features\.html"([^>]*>Pricing</a>)',
    r'<a href="pricing.html"\1',
    text
)
# Footer link for pricing
text = re.sub(
    r'<a href="features\.html"([^>]*>Pricing</a>)',
    r'<a href="pricing.html"\1',
    text
)
# Mega menu features -> features.html (this is already fine but let's ensure it's not tampered with if they click "Features")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(text)


# 3. EXTRACT NAVBAR AND FOOTER FOR TEMPLATES
nav_match = re.search(r'(<nav id="navbar".*?</nav>)', text, flags=re.DOTALL)
footer_match = re.search(r'(<footer.*?</footer>)', text, flags=re.DOTALL)
header_tail = text[:nav_match.end()]
footer_head = text[footer_match.start():]

def make_page(filename, title, subtitle):
    # Strip any floating chat widgets or modals from the footer tail
    clean_footer_head = re.sub(r'<!-- Floating AI Chat Widget -->.*', '</body>\n</html>', footer_head, flags=re.DOTALL)
    
    html = f"""{header_tail}

    <!-- Spacer for fixed navbar -->
    <div class="h-[70px]"></div>

    <!-- Minimal Hero Section -->
    <section class="pt-32 pb-24 px-6 relative overflow-hidden bg-[#F8FAFC]">
        <div class="absolute top-0 right-0 w-[500px] h-[500px] bg-whatsapp/5 rounded-full blur-[80px]"></div>
        <div class="absolute bottom-0 left-0 w-[500px] h-[500px] bg-blue-500/5 rounded-full blur-[80px]"></div>
        
        <div class="max-w-[1200px] mx-auto text-center relative z-10">
            <h1 class="text-4xl md:text-5xl lg:text-[4rem] font-black text-dark tracking-tight leading-[1.1] mb-6">
                {title}<span class="text-btnPrimary">.</span>
            </h1>
            <p class="text-lg md:text-xl text-grayTxt mb-12 max-w-[600px] mx-auto font-medium">
                {subtitle}
            </p>
            <a href="index.html" class="btn btn-secondary text-[15px] font-[500] px-[20px] py-[12px] rounded-[8px] gap-[6px]">
                <i data-lucide="arrow-left" stroke-width="1.5" class="w-4 h-4"></i> Back to Dashboard
            </a>
        </div>
    </section>

{clean_footer_head}"""
    
    with open(filename, "w", encoding="utf-8") as f:
        f.write(html)

make_page("ai-ads.html", "AI Ads Automation", "Launch predictive click-to-WhatsApp ad sequences designed explicitly for modern SaaS conversions.")
make_page("forms.html", "Conversational Forms", "Deploy intelligent data-collection routines completely within the chat interface. Skip the external links.")
make_page("payments.html", "Frictionless Payments", "Native Razorpay and standard payment gateway routines running securely inside your active D2C conversations.")
make_page("pricing.html", "Transparent Pricing", "Enterprise-grade WhatsApp API bandwidth with honest, predictable billing tailored for high volume senders.")
make_page("features.html", "Platform Features", "Explore the dense suite of modules built to command your entire messaging architecture.")

print("All section mockups generated and wired up.")
