import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Add CSS base components immediately before @layer utilities {
css_addition = """
        @layer components {
            .btn {
                @apply inline-flex items-center justify-center gap-2 font-semibold px-[20px] py-[12px] rounded-lg transition-all duration-200 w-full sm:w-auto cursor-pointer;
            }
            .btn-primary {
                @apply bg-whatsapp text-white hover:bg-[#1EBE57] hover:scale-[1.03] shadow-[0_4px_14px_rgba(37,211,102,0.3)] hover:shadow-[0_6px_20px_rgba(37,211,102,0.4)];
            }
            .btn-secondary {
                @apply bg-white border border-gray-300 text-gray-700 hover:border-gray-400 hover:text-dark shadow-sm hover:shadow;
            }
            .btn-ghost {
                @apply bg-transparent border-none text-gray-500 hover:text-dark hover:underline shadow-none;
            }
        }
"""
if "@layer components" not in text:
    text = text.replace("@layer utilities {", css_addition + "\n        @layer utilities {")

# 2. Update Nav buttons
text = text.replace(
    '<a href="#" class="text-[14px] font-bold text-dark bg-white border-2 border-slate-200 px-5 py-2.5 rounded-xl hover:border-dark transition-colors cursor-pointer">Login</a>',
    '<a href="#" class="btn btn-secondary text-sm">Login</a>'
)
text = text.replace(
    '<a href="#" class="text-[14px] font-bold bg-whatsapp text-white px-6 py-2.5 rounded-xl hover:bg-whatsappHover shadow-[0_4px_14px_rgba(37,211,102,0.4)] hover:shadow-[0_6px_20px_rgba(37,211,102,0.5)] transition-all transform hover:-translate-y-0.5 cursor-pointer">Start for FREE</a>',
    '<a href="#" class="btn btn-primary text-sm">Start for FREE <i data-lucide="arrow-right" class="w-4 h-4 text-white"></i></a>'
)

# 3. Hero buttons
text = re.sub(
    r'<button[^>]*>[\s]*<span[^>]*>Start Free Trial</span>[\s]*<div[^>]*></div>[\s]*</button>',
    '<button class="btn btn-primary text-lg px-8 py-4">Start 14-Day FREE Trial <i data-lucide="arrow-right" class="w-5 h-5 text-white"></i></button>',
    text,
    flags=re.IGNORECASE|re.MULTILINE
)
text = re.sub(
    r'<button[^>]*>[\s]*<i data-lucide="play-circle"[^>]*></i> Join Live Demo[\s]*</button>',
    '<button class="btn btn-secondary text-lg px-8 py-4"><i data-lucide="play-circle" class="w-5 h-5"></i> Join Live Demo</button>',
    text,
    flags=re.IGNORECASE|re.MULTILINE
)

# 4. Marketing Broadcast Button
text = re.sub(
    r'<button[^>]*>Start for FREE</button>',
    '<button class="btn btn-primary text-lg px-10 py-5">Start for FREE <i data-lucide="arrow-right" class="w-5 h-5 text-white"></i></button>',
    text,
    flags=re.IGNORECASE|re.MULTILINE
)

# 5. Explore AI Ads / Forms
text = re.sub(
    r'<a[^>]*>Explore AI Ads <i data-lucide="arrow-right"[^>]*></i></a>',
    '<a href="#" class="btn btn-ghost text-blue-600 hover:text-blue-700 px-0">Explore AI Ads <i data-lucide="arrow-right" class="w-5 h-5"></i></a>',
    text,
    flags=re.IGNORECASE|re.MULTILINE
)
text = re.sub(
    r'<a[^>]*>Explore Forms <i data-lucide="arrow-right"[^>]*></i></a>',
    '<a href="#" class="btn btn-ghost text-purple-600 hover:text-purple-700 px-0">Explore Forms <i data-lucide="arrow-right" class="w-5 h-5"></i></a>',
    text,
    flags=re.IGNORECASE|re.MULTILINE
)

# 6. Payments Explorer
text = re.sub(
    r'<button[^>]*>Explore Payments</button>',
    '<button class="btn btn-secondary text-lg px-8 py-3.5"><i data-lucide="credit-card" class="w-5 h-5"></i> Explore Payments</button>',
    text,
    flags=re.IGNORECASE|re.MULTILINE
)

# 7. Trust API button
text = re.sub(
    r'<button[^>]*>Start Now for FREE</button>',
    '<button class="btn btn-primary text-lg px-10 py-5">Start for FREE <i data-lucide="arrow-right" class="w-5 h-5 text-white"></i></button>',
    text,
    flags=re.IGNORECASE|re.MULTILINE
)

# 8. Final CTA Strip
text = re.sub(
    r'<button[^>]*>[\s]*Start Free Try[\s]*</button>',
    '<button class="btn btn-primary text-xl px-12 py-5">Start 14-Day FREE Trial <i data-lucide="arrow-right" class="w-6 h-6 text-white"></i></button>',
    text,
    flags=re.IGNORECASE|re.MULTILINE
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Buttons updated.")
