import os
import glob
import re

mobile_nav_html = """
    <!-- Mobile Menu Container -->
    <div id="mobile-menu" class="fixed inset-0 bg-white z-[40] w-full h-[100dvh] overflow-y-auto transform translate-x-full transition-transform duration-300 lg:hidden flex flex-col pt-[70px]">
        <div class="px-5 py-4 border-b border-slate-100 flex flex-col gap-1">
            <a href="pricing.html" class="py-3 text-[16px] font-semibold text-dark hover:text-whatsapp transition-colors">Pricing</a>
            
            <!-- Mobile Accordion 1 -->
            <div class="mobile-accordion group">
                <button class="w-full py-3 flex items-center justify-between text-[16px] font-semibold text-dark hover:text-whatsapp transition-colors accordion-btn outline-none">
                    Product <i data-lucide="chevron-down" class="w-4 h-4 transition-transform duration-200"></i>
                </button>
                <div class="accordion-content hidden flex-col pl-4 pb-2 gap-3 mt-1 border-l-2 border-slate-100 ml-2">
                    <a href="whatsapp-marketing.html" class="text-[14px] text-grayTxt hover:text-whatsapp">WhatsApp Marketing</a>
                    <a href="ai-ads.html" class="text-[14px] text-grayTxt hover:text-whatsapp">AI Ads Manager</a>
                    <a href="whatsapp-chatbots.html" class="text-[14px] text-grayTxt hover:text-whatsapp">WhatsApp Chatbots</a>
                    <a href="ai-whatsapp-chatbot.html" class="text-[14px] text-grayTxt hover:text-whatsapp">AI WhatsApp Chatbot</a>
                    <a href="payments.html" class="text-[14px] text-grayTxt hover:text-whatsapp">WhatsApp Payments</a>
                    <a href="forms.html" class="text-[14px] text-grayTxt hover:text-whatsapp">WhatsApp Forms</a>
                    <a href="whatsapp-link-qr.html" class="text-[14px] text-grayTxt hover:text-whatsapp">WhatsApp Link & QR</a>
                    <a href="whatsapp-blue-tick.html" class="text-[14px] text-grayTxt hover:text-whatsapp">WhatsApp Blue Tick</a>
                    <a href="showroom-kit.html" class="text-[14px] text-grayTxt hover:text-whatsapp">Showroom Kit</a>
                    <a href="aipersy.html" class="text-[14px] text-grayTxt hover:text-whatsapp">AiPersy</a>
                </div>
            </div>

            <!-- Mobile Accordion 2 -->
            <div class="mobile-accordion group">
                <button class="w-full py-3 flex items-center justify-between text-[16px] font-semibold text-dark hover:text-whatsapp transition-colors accordion-btn outline-none">
                    Features <i data-lucide="chevron-down" class="w-4 h-4 transition-transform duration-200"></i>
                </button>
                <div class="accordion-content hidden flex-col pl-4 pb-2 gap-3 mt-1 border-l-2 border-slate-100 ml-2">
                    <a href="features-overview.html" class="text-[14px] text-grayTxt hover:text-whatsapp">Features Overview</a>
                    <a href="whatsapp-broadcasting.html" class="text-[14px] text-grayTxt hover:text-whatsapp">WhatsApp Broadcasting</a>
                    <a href="ads-manager.html" class="text-[14px] text-grayTxt hover:text-whatsapp">Ads Manager</a>
                    <a href="whatsapp-catalog.html" class="text-[14px] text-grayTxt hover:text-whatsapp">WhatsApp Catalog</a>
                    <a href="whatsapp-chatbots.html" class="text-[14px] text-grayTxt hover:text-whatsapp">WhatsApp Chatbots</a>
                    <a href="whatsapp-webviews.html" class="text-[14px] text-grayTxt hover:text-whatsapp">WhatsApp Webviews</a>
                    <a href="click-tracking.html" class="text-[14px] text-grayTxt hover:text-whatsapp">Click Tracking</a>
                </div>
            </div>

            <!-- Mobile Accordion 3 -->
            <div class="mobile-accordion group">
                <button class="w-full py-3 flex items-center justify-between text-[16px] font-semibold text-dark hover:text-whatsapp transition-colors accordion-btn outline-none">
                    Industries <i data-lucide="chevron-down" class="w-4 h-4 transition-transform duration-200"></i>
                </button>
                <div class="accordion-content hidden flex-col pl-4 pb-2 gap-3 mt-1 border-l-2 border-slate-100 ml-2">
                    <a href="all-industries.html" class="text-[14px] text-grayTxt hover:text-whatsapp">All Industries</a>
                    <a href="education.html" class="text-[14px] text-grayTxt hover:text-whatsapp">Education</a>
                    <a href="e-commerce.html" class="text-[14px] text-grayTxt hover:text-whatsapp">E-commerce</a>
                    <a href="finance-insurance.html" class="text-[14px] text-grayTxt hover:text-whatsapp">Finance & Insurance</a>
                    <a href="healthcare.html" class="text-[14px] text-grayTxt hover:text-whatsapp">Healthcare</a>
                    <a href="automobile.html" class="text-[14px] text-grayTxt hover:text-whatsapp">Automobile</a>
                    <a href="real-estate.html" class="text-[14px] text-grayTxt hover:text-whatsapp">Real Estate</a>
                    <a href="it-services-internet.html" class="text-[14px] text-grayTxt hover:text-whatsapp">IT Services & Internet</a>
                    <a href="events-webinar.html" class="text-[14px] text-grayTxt hover:text-whatsapp">Events & Webinar</a>
                </div>
            </div>
            
            <!-- Mobile Accordion 4 -->
            <div class="mobile-accordion group">
                <button class="w-full py-3 flex items-center justify-between text-[16px] font-semibold text-dark hover:text-whatsapp transition-colors accordion-btn outline-none">
                    Resources <i data-lucide="chevron-down" class="w-4 h-4 transition-transform duration-200"></i>
                </button>
                <div class="accordion-content hidden flex-col pl-4 pb-2 gap-3 mt-1 border-l-2 border-slate-100 ml-2">
                    <a href="help-center.html" class="text-[14px] text-grayTxt hover:text-whatsapp">Help Center</a>
                    <a href="tutorials.html" class="text-[14px] text-grayTxt hover:text-whatsapp">Tutorials</a>
                    <a href="youtube.html" class="text-[14px] text-grayTxt hover:text-whatsapp">YouTube</a>
                    <a href="template-library.html" class="text-[14px] text-grayTxt hover:text-whatsapp">Template Library</a>
                    <a href="blog.html" class="text-[14px] text-grayTxt hover:text-whatsapp">Blog</a>
                    <a href="developer-apis.html" class="text-[14px] text-grayTxt hover:text-whatsapp">Developer APIs</a>
                    <a href="case-studies.html" class="text-[14px] text-grayTxt hover:text-whatsapp">Case Studies</a>
                </div>
            </div>
            
            <!-- Mobile Accordion 5 -->
            <div class="mobile-accordion group">
                <button class="w-full py-3 flex items-center justify-between text-[16px] font-semibold text-dark hover:text-whatsapp transition-colors accordion-btn outline-none">
                    Integrations <i data-lucide="chevron-down" class="w-4 h-4 transition-transform duration-200"></i>
                </button>
                <div class="accordion-content hidden flex-col pl-4 pb-2 gap-3 mt-1 border-l-2 border-slate-100 ml-2">
                    <a href="explore-all-integrations.html" class="text-[14px] text-grayTxt hover:text-whatsapp">Explore all Integrations</a>
                    <a href="shopify.html" class="text-[14px] text-grayTxt hover:text-whatsapp">Shopify</a>
                    <a href="razorpay.html" class="text-[14px] text-grayTxt hover:text-whatsapp">Razorpay</a>
                    <a href="shopify-checkouts.html" class="text-[14px] text-grayTxt hover:text-whatsapp">Shopify Checkouts</a>
                    <a href="webengage.html" class="text-[14px] text-grayTxt hover:text-whatsapp">WebEngage</a>
                    <a href="leadsquared.html" class="text-[14px] text-grayTxt hover:text-whatsapp">LeadSquared</a>
                    <a href="integrately.html" class="text-[14px] text-grayTxt hover:text-whatsapp">Integrately</a>
                    <a href="webhook-apis.html" class="text-[14px] text-grayTxt hover:text-whatsapp">Webhook APIs</a>
                </div>
            </div>

            <a href="app.html" class="py-3 text-[16px] font-semibold text-dark hover:text-whatsapp transition-colors">App</a>
            <a href="partner.html" class="py-3 text-[16px] font-semibold text-dark hover:text-whatsapp transition-colors">Partner</a>
        </div>
        
        <div class="px-5 py-6 mb-8 mt-auto flex flex-col gap-4 bg-white shrink-0">
            <a href="login.html" class="btn btn-secondary text-[15px] font-[600] py-[12px] w-full">Login</a>
            <a href="login.html" class="btn btn-primary text-[15px] font-[600] py-[12px] w-full">Start for FREE</a>
        </div>
    </div>
"""

js_old = """
        // Mobile Menu Toggle
        const btn = document.getElementById('mobile-menu-btn');
        // Simple alert for mockup purposes since dropdown wasn't fully mocked for mobile
        if (btn) {
            btn.addEventListener('click', () => {
                alert('Mobile menu toggled');
            });
        }
"""

js_new = """
        // Mobile Menu Toggle logic
        const mobileBtn = document.getElementById('mobile-menu-btn');
        const mobileMenu = document.getElementById('mobile-menu');
        const mobileIcon = mobileBtn ? mobileBtn.querySelector('i') : null;
        
        if (mobileBtn && mobileMenu) {
            mobileBtn.addEventListener('click', () => {
                const isClosed = mobileMenu.classList.contains('translate-x-full');
                if (isClosed) {
                    mobileMenu.classList.remove('translate-x-full');
                    mobileMenu.classList.add('translate-x-0');
                    if (mobileIcon) {
                        mobileIcon.setAttribute('data-lucide', 'x');
                        lucide.createIcons();
                    }
                    document.body.style.overflow = 'hidden'; // prevent bg scroll
                } else {
                    mobileMenu.classList.add('translate-x-full');
                    mobileMenu.classList.remove('translate-x-0');
                    if (mobileIcon) {
                        mobileIcon.setAttribute('data-lucide', 'menu');
                        lucide.createIcons();
                    }
                    document.body.style.overflow = 'auto'; // restore scroll
                }
            });
        }

        // Mobile Accordion Logic
        const accordionBtns = document.querySelectorAll('.accordion-btn');
        accordionBtns.forEach(btn => {
            btn.addEventListener('click', () => {
                const content = btn.nextElementSibling;
                const icon = btn.querySelector('i');
                const isOpen = !content.classList.contains('hidden');
                
                // Close all others first
                document.querySelectorAll('.accordion-content').forEach(c => c.classList.add('hidden'));
                document.querySelectorAll('.accordion-content').forEach(c => c.classList.remove('flex'));
                document.querySelectorAll('.accordion-btn i').forEach(i => i.style.transform = 'rotate(0deg)');
                
                if (!isOpen) {
                    content.classList.remove('hidden');
                    content.classList.add('flex');
                    if(icon) icon.style.transform = 'rotate(180deg)';
                } else {
                    content.classList.add('hidden');
                    content.classList.remove('flex');
                    if(icon) icon.style.transform = 'rotate(0deg)';
                }
            });
        });
"""

files = glob.glob('*.html')
for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Inject the mobile nav HTML right after the closing tag of nav
    if 'id="mobile-menu"' not in content:
        content = content.replace('</nav>', '</nav>\n' + mobile_nav_html)

    # 2. Replace the old alert mobile logic with the new one
    # To handle potential whitespace differences, we use regex block replacement
    # Or just replace the specific string
    
    # We can use regex to find the Mobile Menu Toggle section safely
    pattern = re.compile(r"// Mobile Menu Toggle\s+const btn = document\.getElementById\('mobile-menu-btn'\);\s+// Simple alert.*?\s+if \(btn\) \{\s+btn\.addEventListener\('click', \(\) => \{\s+alert\('Mobile menu toggled'\);\s+\}\);\s+\}", re.DOTALL)
    
    if pattern.search(content):
        content = pattern.sub(js_new.strip(), content)
        
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Mobile navigation updated!")
