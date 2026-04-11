import sys

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Make step 1 wrapper
target_start = """            <!-- Left Side (Info) -->
            <div class="bg-[#F8FAFC] w-full md:w-[45%] p-10 lg:p-12 border-r border-slate-100 flex flex-col justify-center relative overflow-hidden">"""

replace_start = """            <!-- Step 1 Wrapper -->
            <div id="demo-step-1" class="flex flex-col md:flex-row w-full transition-all duration-300">
                <!-- Left Side (Info) -->
                <div class="bg-[#F8FAFC] w-full md:w-[45%] p-10 lg:p-12 border-r border-slate-100 flex flex-col justify-center relative overflow-hidden">"""

text = text.replace(target_start, replace_start)

# End step 1 wrapper and add submit ID
target_end = """                    <button class="w-full bg-[#3B82F6] hover:bg-[#2563EB] text-white font-bold text-lg py-4 rounded-xl shadow-[0_4px_14px_rgba(59,130,246,0.3)] hover:shadow-[0_6px_20px_rgba(59,130,246,0.4)] transition-all cursor-pointer">
                        Submit
                    </button>
                </div>
            </div>

        </div>
    </div>"""

replace_end = """                    <button id="demo-step-1-submit" class="w-full bg-[#3B82F6] hover:bg-[#2563EB] text-white font-bold text-lg py-4 rounded-xl shadow-[0_4px_14px_rgba(59,130,246,0.3)] hover:shadow-[0_6px_20px_rgba(59,130,246,0.4)] transition-all cursor-pointer">
                        Submit
                    </button>
                </div>
            </div>
            </div> <!-- End Step 1 -->

            <!-- Step 2 (Calendar) -->
            <div id="demo-step-2" class="flex flex-col md:flex-row w-full hidden opacity-0 transition-opacity duration-300">
                <!-- Left Side (Info) -->
                <div class="bg-white w-full md:w-[35%] py-10 px-8 border-r border-slate-100 flex flex-col justify-start relative">
                    <div class="flex items-center gap-2 mb-8 group">
                        <div class="w-8 h-8 flex items-center justify-center bg-whatsapp rounded-lg text-white">
                            <i data-lucide="message-circle" class="w-[18px] h-[18px] fill-current"></i>
                        </div>
                        <span class="text-xl font-black tracking-tight text-dark">Platform<span class="text-whatsapp">.</span></span>
                    </div>
                    
                    <div class="mb-4">
                        <h2 class="text-[20px] font-bold text-dark mb-1">AiSensy Demo Meeting</h2>
                        <div class="flex items-center gap-2 text-slate-500 font-bold text-[14px]">
                            <i data-lucide="clock" class="w-4 h-4"></i> 1 hr
                        </div>
                    </div>
                    
                    <p class="text-grayTxt text-[14px] leading-relaxed font-medium">
                        Get a complete walkthrough of the platform. Learn how to blast messages, automate support, and trigger AI-driven campaigns natively.
                    </p>
                </div>

                <!-- Right Side (Calendar) -->
                <div class="w-full md:w-[65%] py-10 px-8 flex flex-col justify-start">
                    <h3 class="text-[20px] font-bold text-dark mb-8">Select a Date & Time</h3>
                    
                    <div class="w-full">
                        <!-- Calendar Header -->
                        <div class="flex items-center justify-between mb-6">
                            <h4 class="font-bold text-dark text-[15px]">April 2026</h4>
                            <div class="flex items-center gap-2">
                                <button class="w-9 h-9 rounded-full flex items-center justify-center hover:bg-blue-50 text-[#3B82F6] transition-colors cursor-pointer"><i data-lucide="chevron-left" class="w-5 h-5"></i></button>
                                <button class="w-9 h-9 rounded-full flex items-center justify-center hover:bg-blue-100 text-[#3B82F6] bg-blue-50 transition-colors cursor-pointer"><i data-lucide="chevron-right" class="w-5 h-5"></i></button>
                            </div>
                        </div>
                        
                        <!-- Grid Days -->
                        <div class="grid grid-cols-7 gap-y-4 gap-x-2 text-center text-[11px] font-bold text-slate-400 mb-2 mt-4">
                            <div>MON</div><div>TUE</div><div>WED</div><div>THU</div><div>FRI</div><div>SAT</div><div>SUN</div>
                        </div>
                        
                        <!-- Calendar Numbers Mockup -->
                        <div class="grid grid-cols-7 gap-y-2 gap-x-2 text-center text-[14px] font-bold text-dark mb-8">
                            <div class="py-2.5 text-slate-300">30</div>
                            <div class="py-2.5 text-slate-300">31</div>
                            <button class="w-11 h-11 rounded-full mx-auto flex items-center justify-center bg-blue-50 text-[#3B82F6] transition-colors cursor-pointer date-btn">1</button>
                            <button class="w-11 h-11 rounded-full mx-auto flex items-center justify-center hover:bg-blue-50 hover:text-[#3B82F6] transition-colors cursor-pointer date-btn">2</button>
                            <button class="w-11 h-11 rounded-full mx-auto flex items-center justify-center hover:bg-blue-50 hover:text-[#3B82F6] transition-colors cursor-pointer date-btn">3</button>
                            <button class="w-11 h-11 rounded-full mx-auto flex items-center justify-center hover:bg-blue-50 hover:text-[#3B82F6] transition-colors cursor-pointer date-btn">4</button>
                            <button class="w-11 h-11 rounded-full mx-auto flex items-center justify-center hover:bg-blue-50 hover:text-[#3B82F6] transition-colors cursor-pointer date-btn relative"><div class="absolute bottom-[3px] w-1 h-1 bg-slate-300 rounded-full"></div>5</button>
                            
                            <button class="w-11 h-11 rounded-full mx-auto flex items-center justify-center text-white bg-[#3B82F6] hover:bg-[#2563EB] shadow-sm shadow-blue-500/50 transition-colors cursor-pointer date-btn" id="selected-date">6</button>
                            
                            <button class="w-11 h-11 rounded-full mx-auto flex items-center justify-center hover:bg-blue-50 hover:text-[#3B82F6] transition-colors cursor-pointer date-btn relative"><div class="absolute bottom-[3px] w-1 h-1 bg-slate-300 rounded-full"></div>7</button>
                            <button class="w-11 h-11 rounded-full mx-auto flex items-center justify-center hover:bg-blue-50 hover:text-[#3B82F6] transition-colors cursor-pointer date-btn">8</button>
                            <button class="w-11 h-11 rounded-full mx-auto flex items-center justify-center hover:bg-blue-50 hover:text-[#3B82F6] transition-colors cursor-pointer date-btn">9</button>
                            <button class="w-11 h-11 rounded-full mx-auto flex items-center justify-center hover:bg-blue-50 hover:text-[#3B82F6] transition-colors cursor-pointer date-btn">10</button>
                            <button class="w-11 h-11 rounded-full mx-auto flex items-center justify-center hover:bg-blue-50 hover:text-[#3B82F6] transition-colors cursor-pointer date-btn">11</button>
                            <button class="w-11 h-11 rounded-full mx-auto flex items-center justify-center hover:bg-blue-50 hover:text-[#3B82F6] transition-colors cursor-pointer date-btn">12</button>
                            <button class="w-11 h-11 rounded-full mx-auto flex items-center justify-center hover:bg-blue-50 hover:text-[#3B82F6] transition-colors cursor-pointer date-btn">13</button>
                            <button class="w-11 h-11 rounded-full mx-auto flex items-center justify-center hover:bg-blue-50 hover:text-[#3B82F6] transition-colors cursor-pointer date-btn">14</button>
                            <button class="w-11 h-11 rounded-full mx-auto flex items-center justify-center hover:bg-blue-50 hover:text-[#3B82F6] transition-colors cursor-pointer date-btn">15</button>
                            <button class="w-11 h-11 rounded-full mx-auto flex items-center justify-center hover:bg-blue-50 hover:text-[#3B82F6] transition-colors cursor-pointer date-btn">16</button>
                            <button class="w-11 h-11 rounded-full mx-auto flex items-center justify-center hover:bg-blue-50 hover:text-[#3B82F6] transition-colors cursor-pointer date-btn relative"><div class="absolute bottom-[3px] w-1 h-1 bg-slate-300 rounded-full"></div>17</button>
                        </div>
                        
                        <!-- Timezone -->
                        <div class="flex items-center gap-2 mt-auto text-dark font-medium cursor-pointer hover:underline w-max pt-4 border-t border-slate-100">
                            <i data-lucide="globe" class="w-4 h-4 text-slate-500"></i>
                            <span class="text-[14px]">India Standard Time (11:00)</span>
                            <i data-lucide="chevron-down" class="w-3 h-3 text-slate-500 pt-0.5"></i>
                        </div>
                    </div>
                </div>
            </div>

        </div>
    </div>"""

text = text.replace(target_end, replace_end)

# Add Step 2 JS Logic and Reset Logic
js_step2 = """
        // Step 2 Transition Logic
        const step1 = document.getElementById('demo-step-1');
        const step2 = document.getElementById('demo-step-2');
        const submitToStep2 = document.getElementById('demo-step-1-submit');

        if(submitToStep2) {
            submitToStep2.addEventListener('click', () => {
                // Fade out Step 1
                step1.classList.add('opacity-0');
                setTimeout(() => {
                    step1.classList.add('hidden');
                    step2.classList.remove('hidden');
                    
                    setTimeout(() => {
                        step2.classList.remove('opacity-0');
                        lucide.createIcons(); // refresh rendering of step 2 icons
                    }, 50);
                }, 300);
            });
        }
        
        // Add reset event listener after Modal close
        if(closeDemoModal) {
            closeDemoModal.addEventListener('click', () => {
                setTimeout(() => {
                    if(step2 && !step2.classList.contains('hidden')) {
                         step2.classList.add('hidden', 'opacity-0');
                         step1.classList.remove('hidden');
                         // small delay so opacity transition works without flash
                         setTimeout(() => step1.classList.remove('opacity-0'), 10);
                    }
                }, 400); // Trigger after modal fully closes
            });
        }
"""

text = text.replace("    </script>\n</body>", js_step2 + "\n    </script>\n</body>")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Step 2 calendly UI injected")
