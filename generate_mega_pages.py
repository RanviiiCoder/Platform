import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Secure matching for dummy links (features.html or empty anchors) 
# Note: we ignore '#', we specifically look for features.html since that's what we seeded the megamenus with primarily
links = re.findall(r'<a href="(?:features\.html|#)"([^>]*)>(.*?)</a>', html, flags=re.DOTALL)

replacements = []
pages_to_create = {}

def slugify(text):
    text = re.sub(r'<[^>]+>', ' ', text)
    text = ' '.join(text.split())
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s-]', '', text)
    text = re.sub(r'[\s]+', '-', text).strip('-')
    return text

for attrs, inner_html in links:
    # Attempt to extract primary title if formatted as a complex block
    h4_match = re.search(r'<h4[^>]*>(.*?)</h4>', inner_html, flags=re.DOTALL|re.IGNORECASE)
    if h4_match:
        title = ' '.join(re.sub(r'<[^>]+>', ' ', h4_match.group(1)).split())
        subtitle_match = re.search(r'<p[^>]*>(.*?)</p>', inner_html, flags=re.DOTALL|re.IGNORECASE)
        subtitle = ' '.join(re.sub(r'<[^>]+>', ' ', subtitle_match.group(1)).split()) if subtitle_match else "Next-generation WhatsApp features arriving soon."
    else:
        # standard text link
        title = ' '.join(re.sub(r'<[^>]+>', ' ', inner_html).split())
        subtitle = "Platform expansion module arriving soon."
        
    if not title or len(title) < 2 or 'lucide' in title.lower(): 
        continue
    
    # Standardize explicit feature routes from earlier
    lower_title = title.lower()
    if 'ai ads' in lower_title: slug = 'ai-ads'
    elif 'forms' in lower_title: slug = 'forms'
    elif 'payments' in lower_title: slug = 'payments'
    elif 'pricing' in lower_title: slug = 'pricing'
    elif 'features' in lower_title and 'explore' not in lower_title: slug = 'features-overview'
    else: slug = slugify(title)
    
    if not slug: continue
    
    slug_file = slug + ".html"
    pages_to_create[slug_file] = {"title": title, "subtitle": subtitle}
    
    # Recreate link strings for exact replacement
    # Using specific attrs matching to ensure precise swapping without globbing
    find_link1 = f'<a href="features.html"{attrs}>{inner_html}</a>'
    find_link2 = f'<a href="#"{attrs}>{inner_html}</a>'
    
    # Avoid wiping out the login button if it sneaks back
    if 'login.html' in find_link1 or 'login.html' in find_link2 or 'Back to Website' in title:
        continue
        
    new_link_str = f'<a href="{slug_file}"{attrs}>{inner_html}</a>'
    
    # Replace in file exactly
    html = html.replace(find_link1, new_link_str)
    html = html.replace(find_link2, new_link_str)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print(f"Updated index.html core routing across {len(pages_to_create)} distinct contextual endpoints.")

# Second Pass: Extract structurally perfected Navbar and Footer headers from the written source
updated_nav_match = re.search(r'(<nav id="navbar".*?</nav>)', html, flags=re.DOTALL)
header_tail = html[:updated_nav_match.end()]
footer_head = html[re.search(r'(<footer.*?</footer>)', html, flags=re.DOTALL).start():]

def make_page(filename, title, subtitle):
    # Base layout mirroring the exact index HTML head resources seamlessly
    page_html = f"""{header_tail}

    <!-- Spacer for fixed navbar -->
    <div class="h-[70px]"></div>

    <!-- Contextual Feature Page -->
    <section class="pt-32 pb-24 px-6 relative overflow-hidden bg-[#F8FAFC] min-h-[70vh] flex flex-col items-center justify-center">
        <!-- Abstract branding blurs -->
        <div class="absolute top-0 right-0 w-[500px] h-[500px] bg-whatsapp/5 rounded-full blur-[80px] pointer-events-none"></div>
        <div class="absolute bottom-0 left-0 w-[500px] h-[500px] bg-blue-500/5 rounded-full blur-[80px] pointer-events-none"></div>
        
        <div class="max-w-[900px] mx-auto text-center relative z-10 w-full bg-white p-12 md:p-20 rounded-[20px] shadow-[0_20px_40px_rgba(0,0,0,0.04)] border border-slate-100 fade-up visible">
            <div class="w-20 h-20 bg-emerald-50 border border-emerald-100 rounded-2xl flex items-center justify-center mx-auto mb-10 text-whatsapp shadow-sm">
                <i data-lucide="blocks" stroke-width="1.5" class="w-10 h-10"></i>
            </div>
            
            <h1 class="text-3xl md:text-5xl font-black text-dark tracking-tight leading-[1.1] mb-6">
                {title}<span class="text-btnPrimary">.</span>
            </h1>
            <p class="text-[17px] text-grayTxt mb-12 max-w-[500px] mx-auto font-medium leading-relaxed">
                {subtitle}
            </p>
            
            <div class="flex items-center justify-center gap-4">
                <a href="index.html" class="btn btn-secondary text-[15px] font-[500] px-[20px] py-[12px] rounded-[8px] gap-[6px] shadow-sm hover:-translate-y-0.5 transition-transform">
                    <i data-lucide="arrow-left" stroke-width="1.5" class="w-4 h-4"></i> Return Home
                </a>
            </div>
        </div>
    </section>

{footer_head}"""
    
    with open(filename, "w", encoding="utf-8") as file:
        file.write(page_html)

for filename, spec in pages_to_create.items():
    make_page(filename, spec['title'], spec['subtitle'])
    print(f"Generated successfully: {filename}")
