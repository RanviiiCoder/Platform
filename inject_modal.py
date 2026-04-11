import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Add class 'demo-modal-trigger' to any button containing "Join Live Demo"
text = re.sub(
    r'(<button class="btn btn-secondary text-lg px-8 py-4">)(<i data-lucide="play-circle" class="w-5 h-5"></i> Join Live Demo</button>)',
    r'\1 \2'.replace('btn-secondary', 'btn-secondary demo-modal-trigger'),
    text,
    flags=re.IGNORECASE|re.MULTILINE
)
# Ensure we got it by just replacing globally where the text shows up if the strict regex misfires
text = text.replace(
    '<button class="btn btn-secondary text-lg px-8 py-4"><i data-lucide="play-circle" class="w-5 h-5"></i> Join Live Demo</button>',
    '<button class="btn btn-secondary text-lg px-8 py-4 demo-modal-trigger"><i data-lucide="play-circle" class="w-5 h-5"></i> Join Live Demo</button>'
)

# 2. Append Modal HTML before Floating AI Chat Widget
modal_html = """
    <!-- Live Demo Modal Backdrop -->
    <div id="demo-modal-backdrop" class="fixed inset-0 bg-black/50 backdrop-blur-sm z-[200] opacity-0 invisible transition-all duration-300 flex items-center justify-center p-4">
        <!-- Modal Box -->
        <div id="demo-modal-box" class="bg-white rounded-[16px] w-full max-w-[850px] shadow-2xl flex flex-col md:flex-row overflow-hidden scale-95 opacity-0 transition-all duration-300 origin-center relative">
            
            <!-- Close Button -->
            <button id="close-demo-modal" class="absolute top-4 right-4 text-slate-400 hover:text-dark z-30 transition-colors bg-white/50 rounded-full p-1 backdrop-blur-md cursor-pointer">
                <i data-lucide="x" class="w-6 h-6"></i>
            </button>

            <!-- Left Side (Info) -->
            <div class="bg-[#F8FAFC] w-full md:w-[45%] p-10 lg:p-12 border-r border-slate-100 flex flex-col justify-center relative overflow-hidden">
                <!-- Abstract blob -->
                <div class="absolute -top-10 -left-10 w-40 h-40 bg-blue-100 blur-[50px] rounded-full z-0"></div>
                <div class="absolute -bottom-10 -right-10 w-40 h-40 bg-whatsapp/10 blur-[50px] rounded-full z-0"></div>

                <div class="relative z-10">
                    <div class="flex items-center gap-2 mb-8 group">
                        <div class="w-8 h-8 flex items-center justify-center bg-whatsapp rounded-lg text-white">
                            <i data-lucide="message-circle" class="w-[18px] h-[18px] fill-current"></i>
                        </div>
                        <span class="text-xl font-black tracking-tight text-dark">Platform<span class="text-whatsapp">.</span></span>
                    </div>

                    <h2 class="text-[26px] font-bold text-dark mb-4 leading-tight">Live Demo Call</h2>
                    <p class="text-grayTxt text-[15px] leading-relaxed font-medium mb-8">
                        Get a complete walkthrough of the platform. Learn how to blast messages, automate support, and trigger AI-driven campaigns natively.
                    </p>
                    <div class="bg-white p-5 rounded-xl border border-slate-200 shadow-sm">
                        <p class="text-[14px] font-bold text-dark flex items-center gap-2"><i data-lucide="languages" class="w-4 h-4 text-whatsapp"></i> हिंदी में डेमो के लिए</p>
                        <p class="text-[13px] text-grayTxt font-medium mt-1.5 leading-snug">हमारे विशेषज्ञ आपको आपके व्यवसाय को बढ़ाने के तरीके हिंदी में समझाएंगे।</p>
                    </div>
                </div>
            </div>

            <!-- Right Side (Action) -->
            <div class="w-full md:w-[55%] p-10 lg:p-12 flex flex-col justify-center">
                <h3 class="text-[22px] font-bold text-dark mb-8">Select preferred language</h3>
                
                <!-- Custom Dropdown Wrapper -->
                <div class="relative mb-8" id="language-dropdown-wrapper">
                    <button id="language-dropdown-btn" class="w-full bg-white border-2 border-slate-200 rounded-xl px-5 py-4 flex items-center justify-between text-left hover:border-whatsapp transition-colors focus:outline-none focus:border-whatsapp cursor-pointer">
                        <div>
                            <div class="font-bold text-dark text-[16px] mb-0.5" id="selected-lang-title">English</div>
                            <div class="text-[13px] text-grayTxt font-medium" id="selected-lang-time">(Mon-Sat, 4 PM IST)</div>
                        </div>
                        <i data-lucide="chevron-down" class="text-slate-400 transition-transform duration-300" id="lang-dropdown-icon"></i>
                    </button>

                    <!-- Dropdown List -->
                    <div id="language-options" class="absolute top-full left-0 w-full bg-white border border-slate-100 rounded-xl shadow-floating mt-2 py-2 opacity-0 invisible translate-y-2 transition-all duration-200 z-20">
                        <div class="pt-1 pb-1">
                            <button class="w-full text-left px-5 py-3 hover:bg-slate-50 transition-colors lang-option cursor-pointer" data-title="English" data-time="(Mon-Sat, 4 PM IST)">
                                <div class="font-bold text-dark text-[15px] mb-0.5">English</div>
                                <div class="text-[12px] text-grayTxt font-medium opacity-80">(Mon-Sat, 4 PM IST)</div>
                            </button>
                            <button class="w-full text-left px-5 py-3 hover:bg-slate-50 transition-colors lang-option cursor-pointer" data-title="Hindi" data-time="(Mon-Sat, 12 PM IST)">
                                <div class="font-bold text-dark text-[15px] mb-0.5">Hindi</div>
                                <div class="text-[12px] text-grayTxt font-medium opacity-80">(Mon-Sat, 12 PM IST)</div>
                            </button>
                        </div>
                    </div>
                </div>

                <div class="mt-auto">
                    <button class="w-full bg-[#3B82F6] hover:bg-[#2563EB] text-white font-bold text-lg py-4 rounded-xl shadow-[0_4px_14px_rgba(59,130,246,0.3)] hover:shadow-[0_6px_20px_rgba(59,130,246,0.4)] transition-all cursor-pointer">
                        Submit
                    </button>
                </div>
            </div>

        </div>
    </div>
"""

text = text.replace('<!-- Floating AI Chat Widget -->', modal_html + '\n    <!-- Floating AI Chat Widget -->')

js_logic = """
        // Live Demo Modal Logic
        const demoTriggers = document.querySelectorAll('.demo-modal-trigger');
        const demoBackdrop = document.getElementById('demo-modal-backdrop');
        const demoModalBox = document.getElementById('demo-modal-box');
        const closeDemoModal = document.getElementById('close-demo-modal');

        function openDemoModal() {
            demoBackdrop.classList.remove('opacity-0', 'invisible');
            demoBackdrop.classList.add('opacity-100', 'visible');
            
            setTimeout(() => {
                demoModalBox.classList.remove('scale-95', 'opacity-0');
                demoModalBox.classList.add('scale-100', 'opacity-100');
            }, 50);
        }

        function closeDemoModalFunc() {
            demoModalBox.classList.remove('scale-100', 'opacity-100');
            demoModalBox.classList.add('scale-95', 'opacity-0');
            
            setTimeout(() => {
                demoBackdrop.classList.remove('opacity-100', 'visible');
                demoBackdrop.classList.add('opacity-0', 'invisible');
            }, 200);
        }

        demoTriggers.forEach(btn => {
            btn.addEventListener('click', (e) => {
                e.preventDefault();
                openDemoModal();
            });
        });

        if(closeDemoModal) closeDemoModal.addEventListener('click', closeDemoModalFunc);
        if(demoBackdrop) {
            demoBackdrop.addEventListener('click', (e) => {
                if(e.target === demoBackdrop) {
                    closeDemoModalFunc();
                }
            });
        }

        // Dropdown Logic inside Modal
        const langDropdownBtn = document.getElementById('language-dropdown-btn');
        const langOptions = document.getElementById('language-options');
        const langIcon = document.getElementById('lang-dropdown-icon');
        const selectedLangTitle = document.getElementById('selected-lang-title');
        const selectedLangTime = document.getElementById('selected-lang-time');
        const langOptionBtns = document.querySelectorAll('.lang-option');

        if(langDropdownBtn) {
            langDropdownBtn.addEventListener('click', (e) => {
                e.stopPropagation();
                const isClosed = langOptions.classList.contains('opacity-0');
                if(isClosed) {
                    langOptions.classList.remove('opacity-0', 'invisible', 'translate-y-2');
                    langIcon.style.transform = 'rotate(180deg)';
                } else {
                    langOptions.classList.add('opacity-0', 'invisible', 'translate-y-2');
                    langIcon.style.transform = 'rotate(0deg)';
                }
            });
        }

        langOptionBtns.forEach(opt => {
            opt.addEventListener('click', (e) => {
                e.stopPropagation();
                selectedLangTitle.textContent = opt.getAttribute('data-title');
                selectedLangTime.textContent = opt.getAttribute('data-time');
                langOptions.classList.add('opacity-0', 'invisible', 'translate-y-2');
                langIcon.style.transform = 'rotate(0deg)';
            });
        });
        
        // Close dropdown when typing outside
        document.addEventListener('click', (e) => {
            if(langDropdownBtn && langOptions) {
                if(!langDropdownBtn.contains(e.target) && !langOptions.contains(e.target)) {
                    langOptions.classList.add('opacity-0', 'invisible', 'translate-y-2');
                    langIcon.style.transform = 'rotate(0deg)';
                }
            }
        });
"""

text = text.replace("    </script>\n</body>", js_logic + "    </script>\n</body>")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Modal Injected Successfully")
