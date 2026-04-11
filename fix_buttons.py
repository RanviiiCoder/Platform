import re

with open("index.html", "r", encoding="utf-8") as f:
    text = f.read()

# 1. Update tailwind.config
tailwind_colors = """                    colors: {
                        whatsapp: '#25D366',
                        whatsappHover: '#1EBE57',
                        whatsappDark: '#075E54',
                        dark: '#0F172A',
                        grayTxt: '#64748B',
                        lightBg: '#F8FAFC',
                        btnPrimary: '#22C55E',
                        btnPrimaryHov: '#16A34A',
                        btnSecBorder: '#D1D5DB',
                        btnSecHovBorder: '#9CA3AF',
                        btnSecHovBg: '#F9FAFB',
                        btnSecTxt: '#111827'
                    },"""

text = re.sub(
    r'colors:\s*\{[^}]*lightBg:\s*\'#F8FAFC\'\s*\},?', 
    tailwind_colors, 
    text, 
    flags=re.DOTALL
)

# 2. Update the @apply classes to use standard named colors
old_css = """            .btn-primary {
                @apply bg-[#22C55E] text-white hover:bg-[#16A34A] border-none shadow-none;
            }
            .btn-secondary {
                @apply bg-white border border-[#D1D5DB] text-[#111827] hover:border-[#9CA3AF] hover:bg-[#F9FAFB] shadow-none;
            }"""
new_css = """            .btn-primary {
                @apply bg-btnPrimary text-white hover:bg-btnPrimaryHov border-none shadow-none;
            }
            .btn-secondary {
                @apply bg-white border border-btnSecBorder text-btnSecTxt hover:border-btnSecHovBorder hover:bg-btnSecHovBg shadow-none;
            }"""
text = text.replace(old_css, new_css)

# Update transition duration to 150ms per prompt "very subtle transition (0.15s)"
text = text.replace('transition-colors duration-200', 'transition-colors duration-150')

# 3. Fix "Join Live Demo" button that was missed by previous script
# Find exactly the line outputted by my grep: <button class="btn btn-secondary text-lg px-8 py-4"> <i data-lucide="play-circle" class="w-5 h-5"></i> Join Live Demo</button>
# Also need to make sure the class demo-modal-trigger is there so it WORKS.
broken_demo_btn = '<button class="btn btn-secondary text-lg px-8 py-4"> <i data-lucide="play-circle" class="w-5 h-5"></i> Join Live Demo</button>'
fixed_demo_btn = '<button class="btn btn-secondary text-[15px] font-[500] px-[20px] py-[12px] rounded-[8px] gap-[6px] demo-modal-trigger">Join Live Demo <i data-lucide="arrow-right" stroke-width="1.5" class="w-4 h-4"></i></button>'

if broken_demo_btn in text:
    text = text.replace(broken_demo_btn, fixed_demo_btn)

# Make sure all other demo buttons if any are correct
text = text.replace(
    '<button class="btn btn-secondary text-[15px] font-[500] px-[20px] py-[12px] rounded-[8px] gap-[6px]">Join Live Demo',
    '<button class="btn btn-secondary text-[15px] font-[500] px-[20px] py-[12px] rounded-[8px] gap-[6px] demo-modal-trigger">Join Live Demo'
)

# 4. Check for double spacing or any missing arrow-right from the last replace
# The final CTA has text size classes but let's make sure it's fully uniform
# Just standardizing all Hero / CTA buttons to the exact user params:
old_hero_primary = '<button class="btn btn-primary text-[15px] font-[600] px-[22px] py-[12px] rounded-[8px] gap-[6px]">Start 14-Day FREE Trial <i data-lucide="arrow-right" stroke-width="2" class="w-4 h-4"></i></button>'
new_hero_primary = '<button class="btn btn-primary text-[15px] font-[600] px-[22px] py-[12px] rounded-[8px] gap-[6px]">Start 14-Day FREE Trial <i data-lucide="arrow-right" stroke-width="1.5" class="w-[18px] h-[18px] text-white"></i></button>'
text = text.replace(old_hero_primary, new_hero_primary)

# Update nav primary button to match thin arrow correctly
old_nav_primary = '<a href="#" class="btn btn-primary text-[14px] font-[600] px-[18px] py-[10px] rounded-[6px] gap-[6px]">Start for FREE <i data-lucide="arrow-right" stroke-width="1.5" class="w-3.5 h-3.5"></i></a>'
new_nav_primary = '<a href="#" class="btn btn-primary text-[14px] font-[600] px-[18px] py-[10px] rounded-[6px] gap-[6px]">Start for FREE <i data-lucide="arrow-right" stroke-width="1.5" class="w-[14px] h-[14px]"></i></a>'
text = text.replace(old_nav_primary, new_nav_primary)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(text)

print("Button issues resolved")
