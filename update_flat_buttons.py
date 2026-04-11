import re

with open("index.html", "r", encoding="utf-8") as f:
    text = f.read()

# Replace CSS
old_css = r"""        @layer components {
            \.btn {
                @apply inline-flex items-center justify-center gap-2 font-semibold px-\[20px\] py-\[12px\] rounded-lg transition-all duration-200 w-full sm:w-auto cursor-pointer;
            }
            \.btn-primary {
                @apply bg-whatsapp text-white hover:bg-\[#1EBE57\] hover:scale-\[1.03\] shadow-\[0_4px_14px_rgba\(37,211,102,0\.3\)\] hover:shadow-\[0_6px_20px_rgba\(37,211,102,0\.4\)\];
            }
            \.btn-secondary {
                @apply bg-white border border-gray-300 text-gray-700 hover:border-gray-400 hover:text-dark shadow-sm hover:shadow;
            }
            \.btn-ghost {
                @apply bg-transparent border-none text-gray-500 hover:text-dark hover:underline shadow-none;
            }
        }"""
        
new_css = """        @layer components {
            .btn {
                @apply inline-flex items-center justify-center transition-colors duration-200 w-full sm:w-auto outline-none cursor-pointer;
            }
            .btn-primary {
                @apply bg-[#22C55E] text-white hover:bg-[#16A34A] border-none shadow-none;
            }
            .btn-secondary {
                @apply bg-white border border-[#D1D5DB] text-[#111827] hover:border-[#9CA3AF] hover:bg-[#F9FAFB] shadow-none;
            }
            .btn-ghost {
                @apply bg-transparent border-none text-gray-500 hover:text-dark hover:underline shadow-none;
            }
        }"""
        
text = re.sub(old_css, new_css, text)

# Strict Replacements for the 7 instances:

# Nav
text = text.replace(
    '<a href="#" class="btn btn-secondary text-sm">Login</a>',
    '<a href="#" class="btn btn-secondary text-[14px] font-[500] px-[16px] py-[10px] rounded-[6px] gap-[6px]">Login <i data-lucide="arrow-right" stroke-width="1.5" class="w-3.5 h-3.5"></i></a>'
)
text = text.replace(
    '<a href="#" class="btn btn-primary text-sm">Start for FREE <i data-lucide="arrow-right" class="w-4 h-4 text-white"></i></a>',
    '<a href="#" class="btn btn-primary text-[14px] font-[600] px-[18px] py-[10px] rounded-[6px] gap-[6px]">Start for FREE <i data-lucide="arrow-right" stroke-width="1.5" class="w-3.5 h-3.5"></i></a>'
)

# Hero 
text = text.replace(
    '<button class="btn btn-primary text-lg px-8 py-4">Start 14-Day FREE Trial <i data-lucide="arrow-right" class="w-5 h-5 text-white"></i></button>',
    '<button class="btn btn-primary text-[15px] font-[600] px-[22px] py-[12px] rounded-[8px] gap-[6px]">Start 14-Day FREE Trial <i data-lucide="arrow-right" stroke-width="2" class="w-4 h-4"></i></button>'
)

# Live demo might have demo-modal-trigger or slightly different whitespace. We use Regex.
text = re.sub(
    r'<button[^>]*Join Live Demo</button>',
    '<button class="btn btn-secondary text-[15px] font-[500] px-[20px] py-[12px] rounded-[8px] gap-[6px] demo-modal-trigger cursor-pointer">Join Live Demo <i data-lucide="arrow-right" stroke-width="1.5" class="w-4 h-4"></i></button>',
    text
)

# Feature
text = text.replace(
    '<button class="btn btn-primary text-lg px-10 py-5">Start for FREE <i data-lucide="arrow-right" class="w-5 h-5 text-white"></i></button>',
    '<button class="btn btn-primary text-[15px] font-[600] px-[22px] py-[12px] rounded-[8px] gap-[6px]">Start for FREE <i data-lucide="arrow-right" stroke-width="2" class="w-4 h-4"></i></button>'
)

# Payments
text = re.sub(
    r'<button[^>]*>[\s]*<i data-lucide="credit-card"[^>]*></i> Explore Payments[\s]*</button>',
    '<button class="btn btn-secondary text-[15px] font-[500] px-[20px] py-[12px] rounded-[8px] gap-[6px]">Explore Payments <i data-lucide="arrow-right" stroke-width="1.5" class="w-4 h-4"></i></button>',
    text
)

# Final
text = text.replace(
    '<button class="btn btn-primary text-xl px-12 py-5">Start 14-Day FREE Trial <i data-lucide="arrow-right" class="w-6 h-6 text-white"></i></button>',
    '<button class="btn btn-primary text-[15px] font-[600] px-[22px] py-[12px] rounded-[8px] gap-[6px]">Start 14-Day FREE Trial <i data-lucide="arrow-right" stroke-width="2" class="w-4 h-4"></i></button>'
)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(text)

print("Button styles matched to flat UI")
