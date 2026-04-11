import sys

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace inner right side of step 2 to include the flex layout
target_right_side_start = """                    <div class="w-full">
                        <!-- Calendar Header -->"""
target_right_side_end = """                        <!-- Timezone -->
                        <div class="flex items-center gap-2 mt-auto text-dark font-medium cursor-pointer hover:underline w-max pt-4 border-t border-slate-100">
                            <i data-lucide="globe" class="w-4 h-4 text-slate-500"></i>
                            <span class="text-[14px]">India Standard Time (11:00)</span>
                            <i data-lucide="chevron-down" class="w-3 h-3 text-slate-500 pt-0.5"></i>
                        </div>
                    </div>"""

# Replace the inner calendar with flex wrappers
# We actually just want to wrap the `<div class="w-full">` -> `<div class="flex items-start gap-4 lg:gap-8 w-full h-full">`
# and put the original inner contents in `<div id="calendar-container" class="flex-grow transition-all duration-300 flex flex-col w-full">`
new_inner_right = """                    <div class="flex items-start gap-6 lg:gap-8 w-full h-full relative" id="calendar-flex-wrapper">
                        <!-- Left Calendar View -->
                        <div id="calendar-container" class="transition-all duration-300 w-full flex flex-col min-w-[250px]">
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
                            
                            <!-- Calendar Numbers -->
                            <div class="grid grid-cols-7 gap-y-2 gap-x-1 sm:gap-x-2 text-center text-[14px] font-bold text-dark mb-8">
                                <div class="py-2.5 text-slate-300">30</div>
                                <div class="py-2.5 text-slate-300">31</div>
                                <button class="w-10 h-10 sm:w-11 sm:h-11 rounded-full mx-auto flex items-center justify-center bg-blue-50 text-[#3B82F6] transition-colors cursor-pointer date-btn">1</button>
                                <button class="w-10 h-10 sm:w-11 sm:h-11 rounded-full mx-auto flex items-center justify-center hover:bg-blue-50 hover:text-[#3B82F6] transition-colors cursor-pointer date-btn">2</button>
                                <button class="w-10 h-10 sm:w-11 sm:h-11 rounded-full mx-auto flex items-center justify-center hover:bg-blue-50 hover:text-[#3B82F6] transition-colors cursor-pointer date-btn">3</button>
                                <button class="w-10 h-10 sm:w-11 sm:h-11 rounded-full mx-auto flex items-center justify-center hover:bg-blue-50 hover:text-[#3B82F6] transition-colors cursor-pointer date-btn">4</button>
                                <button class="w-10 h-10 sm:w-11 sm:h-11 rounded-full mx-auto flex items-center justify-center hover:bg-blue-50 hover:text-[#3B82F6] transition-colors cursor-pointer date-btn relative"><div class="absolute bottom-[3px] w-1 h-1 bg-slate-300 rounded-full"></div>5</button>
                                
                                <button class="w-10 h-10 sm:w-11 sm:h-11 rounded-full mx-auto flex items-center justify-center hover:bg-blue-50 hover:text-[#3B82F6] transition-colors cursor-pointer date-btn relative"><div class="absolute bottom-[3px] w-1 h-1 bg-slate-300 rounded-full"></div>6</button>
                                <button class="w-10 h-10 sm:w-11 sm:h-11 rounded-full mx-auto flex items-center justify-center hover:bg-blue-50 hover:text-[#3B82F6] transition-colors cursor-pointer date-btn relative"><div class="absolute bottom-[3px] w-1 h-1 bg-slate-300 rounded-full"></div>7</button>
                                <button class="w-10 h-10 sm:w-11 sm:h-11 rounded-full mx-auto flex items-center justify-center hover:bg-blue-50 hover:text-[#3B82F6] transition-colors cursor-pointer date-btn">8</button>
                                <button class="w-10 h-10 sm:w-11 sm:h-11 rounded-full mx-auto flex items-center justify-center hover:bg-blue-50 hover:text-[#3B82F6] transition-colors cursor-pointer date-btn">9</button>
                                <button class="w-10 h-10 sm:w-11 sm:h-11 rounded-full mx-auto flex items-center justify-center hover:bg-blue-50 hover:text-[#3B82F6] transition-colors cursor-pointer date-btn">10</button>
                                <button class="w-10 h-10 sm:w-11 sm:h-11 rounded-full mx-auto flex items-center justify-center hover:bg-blue-50 hover:text-[#3B82F6] transition-colors cursor-pointer date-btn">11</button>
                                <button class="w-10 h-10 sm:w-11 sm:h-11 rounded-full mx-auto flex items-center justify-center hover:bg-blue-50 hover:text-[#3B82F6] transition-colors cursor-pointer date-btn">12</button>
                                <button class="w-10 h-10 sm:w-11 sm:h-11 rounded-full mx-auto flex items-center justify-center hover:bg-blue-50 hover:text-[#3B82F6] transition-colors cursor-pointer date-btn">13</button>
                                <button class="w-10 h-10 sm:w-11 sm:h-11 rounded-full mx-auto flex items-center justify-center hover:bg-blue-50 hover:text-[#3B82F6] transition-colors cursor-pointer date-btn">14</button>
                                <button class="w-10 h-10 sm:w-11 sm:h-11 rounded-full mx-auto flex items-center justify-center hover:bg-blue-50 hover:text-[#3B82F6] transition-colors cursor-pointer date-btn">15</button>
                                <button class="w-10 h-10 sm:w-11 sm:h-11 rounded-full mx-auto flex items-center justify-center hover:bg-blue-50 hover:text-[#3B82F6] transition-colors cursor-pointer date-btn">16</button>
                                <button class="w-10 h-10 sm:w-11 sm:h-11 rounded-full mx-auto flex items-center justify-center hover:bg-blue-50 hover:text-[#3B82F6] transition-colors cursor-pointer date-btn relative"><div class="absolute bottom-[3px] w-1 h-1 bg-slate-300 rounded-full"></div>17</button>
                            </div>
                            
                            <!-- Timezone -->
                            <div class="flex items-center gap-2 mt-auto text-dark font-medium cursor-pointer hover:underline w-max pt-4 border-t border-slate-100">
                                <i data-lucide="globe" class="w-4 h-4 text-slate-500"></i>
                                <span class="text-[14px]">India Standard Time (11:00)</span>
                                <i data-lucide="chevron-down" class="w-3 h-3 text-slate-500 pt-0.5"></i>
                            </div>
                        </div>

                        <!-- Right Time Slots View (Hidden Initially) -->
                        <div id="time-slots-container" class="w-[180px] shrink-0 hidden opacity-0 transition-opacity duration-300 flex-col h-full border-l border-slate-100 pl-4 lg:pl-6 -mt-2">
                            <h4 class="font-bold text-dark text-[14px] mb-4 mt-2" id="time-slot-day-title">Tuesday, 6 April</h4>
                            <div class="flex flex-col gap-3 overflow-y-auto max-h-[290px] pr-2 custom-scrollbar">
                                <button class="w-full border border-slate-200 bg-white text-[#3B82F6] font-[800] text-[14px] py-3.5 rounded-lg hover:border-[#3B82F6] transition-all cursor-pointer time-btn shadow-sm">10:00 AM</button>
                                <button class="w-full border border-slate-200 bg-white text-[#3B82F6] font-[800] text-[14px] py-3.5 rounded-lg hover:border-[#3B82F6] transition-all cursor-pointer time-btn shadow-sm">12:00 PM</button>
                                <button class="w-full border border-slate-200 bg-white text-[#3B82F6] font-[800] text-[14px] py-3.5 rounded-lg hover:border-[#3B82F6] transition-all cursor-pointer time-btn shadow-sm">4:00 PM</button>
                            </div>
                            <div id="confirm-booking-wrapper" class="hidden opacity-0 transition-opacity duration-300 mt-5 pt-3 border-t border-slate-100 w-full">
                                <button id="confirm-booking-btn" class="w-full bg-[#3B82F6] hover:bg-[#2563EB] text-white font-bold text-[14px] py-3.5 rounded-lg shadow-[0_4px_14px_rgba(59,130,246,0.3)] transition-colors cursor-pointer">Confirm</button>
                            </div>
                        </div>
                    </div>"""

text = text.replace(target_right_side_start + text[text.find(target_right_side_start)+len(target_right_side_start):text.find(target_right_side_end)+len(target_right_side_end)], new_inner_right)

# 3. Add Step 3 (Success) UI after Step 2
target_step2_end = "            </div>\n\n        </div>\n    </div>"
step3_ui = """            </div>

            <!-- Step 3 (Success) -->
            <div id="demo-step-3" class="flex flex-col w-full h-[550px] hidden opacity-0 transition-opacity duration-500 items-center justify-center px-8 text-center bg-white relative overflow-hidden">
                <!-- Confetti/Light blobs -->
                <div class="w-64 h-64 bg-green-100 rounded-full absolute -top-10 -right-20 blur-[60px] opacity-70 pointer-events-none"></div>
                <div class="w-64 h-64 bg-blue-100 rounded-full absolute -bottom-10 -left-20 blur-[60px] opacity-70 pointer-events-none"></div>
                
                <div class="relative z-10 flex flex-col items-center">
                    <div class="w-20 h-20 bg-green-50 rounded-full flex items-center justify-center text-green-500 mb-6 mx-auto shadow-sm shadow-green-100 border border-green-100">
                        <i data-lucide="check-circle-2" class="w-10 h-10"></i>
                    </div>
                    <h2 class="text-[32px] font-black text-dark mb-4 leading-tight">Your demo is booked 🎉</h2>
                    <p class="text-[16px] font-medium text-slate-500 max-w-[450px] mx-auto mb-10 leading-relaxed">
                        We've sent a calendar invitation directly to your email. Please check your inbox for the Google Meet link and details.
                    </p>
                    <button id="close-success-btn" class="bg-dark hover:bg-slate-800 text-white font-bold text-lg py-4 px-12 rounded-xl transition-all shadow-floating cursor-pointer hover:shadow-2xl hover:-translate-y-1">
                        Back to site
                    </button>
                </div>
            </div>

        </div>
    </div>"""
text = text.replace(target_step2_end, step3_ui)

# Add Step 3 JS Logic
js_step3 = """
        // Step 2 > Step 3 Calendly Interactive Logic
        const dateBtns = document.querySelectorAll('.date-btn');
        const timeSlotsContainer = document.getElementById('time-slots-container');
        const timeSlotDayTitle = document.getElementById('time-slot-day-title');
        const timeBtns = document.querySelectorAll('.time-btn');
        const confirmBookingWrapper = document.getElementById('confirm-booking-wrapper');
        const confirmBookingBtn = document.getElementById('confirm-booking-btn');
        const demoStep3 = document.getElementById('demo-step-3');
        const closeSuccessBtn = document.getElementById('close-success-btn');
        const calendarContainer = document.getElementById('calendar-container');

        // Date Select
        dateBtns.forEach(btn => {
            btn.addEventListener('click', (e) => {
                // Clear active
                dateBtns.forEach(b => {
                    b.classList.remove('text-white', 'bg-[#3B82F6]', 'hover:bg-[#2563EB]', 'shadow-sm', 'shadow-blue-500/50');
                    b.classList.add('hover:bg-blue-50', 'hover:text-[#3B82F6]');
                });
                // Set active
                btn.classList.add('text-white', 'bg-[#3B82F6]', 'hover:bg-[#2563EB]', 'shadow-sm', 'shadow-blue-500/50');
                btn.classList.remove('hover:bg-blue-50', 'hover:text-[#3B82F6]');
                
                // Show Times
                timeSlotsContainer.classList.remove('hidden');
                setTimeout(() => timeSlotsContainer.classList.remove('opacity-0'), 50);
                
                // Update Date Text
                const selectedDay = btn.textContent.replace(/[^0-9]/g, '');
                timeSlotDayTitle.textContent = "April " + selectedDay + ", 2026";
                
                // Reset times + confirm btn
                timeBtns.forEach(t => {
                    t.classList.remove('bg-[#3B82F6]', 'text-white', 'border-[#3B82F6]');
                    t.classList.add('bg-white', 'text-[#3B82F6]', 'border-slate-200');
                });
                confirmBookingWrapper.classList.add('opacity-0');
                setTimeout(() => confirmBookingWrapper.classList.add('hidden'), 300);
            });
        });

        // Time Select
        timeBtns.forEach(btn => {
            btn.addEventListener('click', () => {
                // Clear active time
                timeBtns.forEach(t => {
                    t.classList.remove('bg-[#3B82F6]', 'text-white', 'border-[#3B82F6]');
                    t.classList.add('bg-white', 'text-[#3B82F6]', 'border-slate-200');
                });
                
                // Set active
                btn.classList.remove('bg-white', 'text-[#3B82F6]', 'border-slate-200');
                btn.classList.add('bg-[#3B82F6]', 'text-white', 'border-[#3B82F6]');
                
                // Show Confirm Button
                confirmBookingWrapper.classList.remove('hidden');
                setTimeout(() => confirmBookingWrapper.classList.remove('opacity-0'), 50);
            });
        });

        // Confirm
        if(confirmBookingBtn) {
            confirmBookingBtn.addEventListener('click', () => {
                // Fade out step 2
                step2.classList.add('opacity-0');
                setTimeout(() => {
                    step2.classList.add('hidden');
                    demoStep3.classList.remove('hidden');
                    
                    setTimeout(() => {
                        demoStep3.classList.remove('opacity-0');
                        lucide.createIcons();
                    }, 50);
                }, 300);
            });
        }
        
        // Close from Success
        if(closeSuccessBtn) {
            closeSuccessBtn.addEventListener('click', () => {
                closeDemoModalFunc();
            });
        }
        
        // Add to main reset logic
        if(closeDemoModal) {
            closeDemoModal.addEventListener('click', () => {
                setTimeout(() => {
                    if(demoStep3 && !demoStep3.classList.contains('hidden')) {
                        demoStep3.classList.add('hidden', 'opacity-0');
                    }
                    if(timeSlotsContainer && !timeSlotsContainer.classList.contains('hidden')) {
                        timeSlotsContainer.classList.add('hidden', 'opacity-0');
                    }
                }, 400); 
            });
        }
"""

text = text.replace("    </script>\n</body>", js_step3 + "\n    </script>\n</body>")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Step 3 UI + logic injected")
