import sys

new_nav = """    <!-- Navbar -->
    <nav id="navbar" class="fixed w-full z-50 transition-all duration-300 top-0 border-b border-transparent bg-white/95 backdrop-blur-md h-[70px] flex items-center shadow-sm">
        <div class="w-full max-w-[1200px] mx-auto px-[20px] flex items-center justify-between h-full">
            <!-- Logo -->
            <a href="#" class="flex items-center gap-2 group shrink-0">
                <div class="w-9 h-9 border-[2px] border-whatsapp rounded-full flex items-center justify-center p-1 bg-white">
                    <i data-lucide="message-circle" class="w-[18px] h-[18px] text-whatsapp fill-whatsapp"></i>
                </div>
                <span class="text-xl font-black tracking-tight text-dark">Platform<span class="text-whatsapp">.</span></span>
            </a>

            <!-- Desktop Links -->
            <div class="hidden lg:flex items-center gap-7 h-full ml-8">
                <a href="#" class="text-[15px] font-semibold text-dark hover:text-whatsapp transition-colors h-full flex items-center cursor-pointer">Pricing</a>
                
                <!-- 1. PRODUCT DROPDOWN -->
                <div class="group/nav relative h-full flex items-center">
                    <button class="flex items-center gap-1 text-[15px] font-semibold text-dark hover:text-whatsapp transition-colors h-full cursor-pointer">
                        Product <i data-lucide="chevron-down" class="w-[14px] h-[14px] transition-transform group-hover/nav:rotate-180"></i>
                    </button>
                    <!-- Panel -->
                    <div class="absolute top-[100%] left-0 w-[300px] bg-white rounded-[16px] shadow-floating border border-slate-100 p-2.5 opacity-0 invisible group-hover/nav:opacity-100 group-hover/nav:visible transition-all duration-200 translate-y-2 group-hover/nav:translate-y-0 z-50">
                        <div class="absolute -top-6 left-0 w-full h-6"></div> <!-- Bridge -->
                        <div class="flex flex-col max-h-[70vh] overflow-y-auto">
                            <a href="#" class="flex gap-3 hover:bg-green-50 p-2.5 rounded-xl transition-colors group/item cursor-pointer">
                                <div class="w-9 h-9 rounded-lg bg-whatsapp/10 text-whatsapp flex items-center justify-center shrink-0 group-hover/item:scale-110 transition-transform"><i data-lucide="megaphone" class="w-[18px] h-[18px]"></i></div>
                                <div class="flex flex-col justify-center gap-0.5"><h4 class="font-bold text-dark text-[14px] leading-tight">WhatsApp Marketing</h4><p class="text-[12px] text-grayTxt leading-tight">Broadcast, Automate & Grow</p></div>
                            </a>
                            <a href="#" class="flex gap-3 hover:bg-green-50 p-2.5 rounded-xl transition-colors group/item cursor-pointer">
                                <div class="w-9 h-9 rounded-lg bg-whatsapp/10 text-whatsapp flex items-center justify-center shrink-0 group-hover/item:scale-110 transition-transform"><i data-lucide="mouse-pointer-click" class="w-[18px] h-[18px]"></i></div>
                                <div class="flex flex-col justify-center gap-0.5"><h4 class="font-bold text-dark text-[14px] leading-tight">AI Ads Manager</h4><p class="text-[12px] text-grayTxt leading-tight">5X your leads</p></div>
                            </a>
                            <a href="#" class="flex gap-3 hover:bg-green-50 p-2.5 rounded-xl transition-colors group/item cursor-pointer">
                                <div class="w-9 h-9 rounded-lg bg-whatsapp/10 text-whatsapp flex items-center justify-center shrink-0 group-hover/item:scale-110 transition-transform"><i data-lucide="bot" class="w-[18px] h-[18px]"></i></div>
                                <div class="flex flex-col justify-center gap-0.5"><h4 class="font-bold text-dark text-[14px] leading-tight">WhatsApp Chatbots</h4><p class="text-[12px] text-grayTxt leading-tight">Automate conversations</p></div>
                            </a>
                            <a href="#" class="flex gap-3 hover:bg-green-50 p-2.5 rounded-xl transition-colors group/item cursor-pointer">
                                <div class="w-9 h-9 rounded-lg bg-whatsapp/10 text-whatsapp flex items-center justify-center shrink-0 group-hover/item:scale-110 transition-transform"><i data-lucide="brain-circuit" class="w-[18px] h-[18px]"></i></div>
                                <div class="flex flex-col justify-center gap-0.5"><h4 class="font-bold text-dark text-[14px] leading-tight">AI WhatsApp Chatbot</h4><p class="text-[12px] text-grayTxt leading-tight">Fully AI automation</p></div>
                            </a>
                            <a href="#" class="flex gap-3 hover:bg-green-50 p-2.5 rounded-xl transition-colors group/item cursor-pointer">
                                <div class="w-9 h-9 rounded-lg bg-whatsapp/10 text-whatsapp flex items-center justify-center shrink-0 group-hover/item:scale-110 transition-transform"><i data-lucide="credit-card" class="w-[18px] h-[18px]"></i></div>
                                <div class="flex flex-col justify-center gap-0.5"><h4 class="font-bold text-dark text-[14px] leading-tight">WhatsApp Payments</h4><p class="text-[12px] text-grayTxt leading-tight">Collect payments in chat</p></div>
                            </a>
                            <a href="#" class="flex gap-3 hover:bg-green-50 p-2.5 rounded-xl transition-colors group/item cursor-pointer">
                                <div class="w-9 h-9 rounded-lg bg-whatsapp/10 text-whatsapp flex items-center justify-center shrink-0 group-hover/item:scale-110 transition-transform"><i data-lucide="form-input" class="w-[18px] h-[18px]"></i></div>
                                <div class="flex flex-col justify-center gap-0.5"><h4 class="font-bold text-dark text-[14px] leading-tight">WhatsApp Forms</h4><p class="text-[12px] text-grayTxt leading-tight">Capture leads natively</p></div>
                            </a>
                            <a href="#" class="flex gap-3 hover:bg-green-50 p-2.5 rounded-xl transition-colors group/item cursor-pointer">
                                <div class="w-9 h-9 rounded-lg bg-whatsapp/10 text-whatsapp flex items-center justify-center shrink-0 group-hover/item:scale-110 transition-transform"><i data-lucide="link" class="w-[18px] h-[18px]"></i></div>
                                <div class="flex flex-col justify-center gap-0.5"><h4 class="font-bold text-dark text-[14px] leading-tight">WhatsApp Link & QR</h4><p class="text-[12px] text-grayTxt leading-tight">Generate links & QR</p></div>
                            </a>
                            <a href="#" class="flex gap-3 hover:bg-green-50 p-2.5 rounded-xl transition-colors group/item cursor-pointer">
                                <div class="w-9 h-9 rounded-lg bg-whatsapp/10 text-whatsapp flex items-center justify-center shrink-0 group-hover/item:scale-110 transition-transform"><i data-lucide="check-badge" class="w-[18px] h-[18px]"></i></div>
                                <div class="flex flex-col justify-center gap-0.5"><h4 class="font-bold text-dark text-[14px] leading-tight">WhatsApp Blue Tick</h4><p class="text-[12px] text-grayTxt leading-tight">Get verified badge</p></div>
                            </a>
                            <a href="#" class="flex gap-3 hover:bg-green-50 p-2.5 rounded-xl transition-colors group/item cursor-pointer">
                                <div class="w-9 h-9 rounded-lg bg-whatsapp/10 text-whatsapp flex items-center justify-center shrink-0 group-hover/item:scale-110 transition-transform"><i data-lucide="store" class="w-[18px] h-[18px]"></i></div>
                                <div class="flex flex-col justify-center gap-0.5"><h4 class="font-bold text-dark text-[14px] leading-tight">Showroom Kit</h4><p class="text-[12px] text-grayTxt leading-tight">Offline QR setup</p></div>
                            </a>
                            <a href="#" class="flex gap-3 hover:bg-green-50 p-2.5 rounded-xl transition-colors group/item cursor-pointer">
                                <div class="w-9 h-9 rounded-lg bg-whatsapp/10 text-whatsapp flex items-center justify-center shrink-0 group-hover/item:scale-110 transition-transform"><i data-lucide="sparkles" class="w-[18px] h-[18px]"></i></div>
                                <div class="flex flex-col justify-center gap-0.5"><h4 class="font-bold text-dark text-[14px] leading-tight">AiPersy</h4><p class="text-[12px] text-grayTxt leading-tight">Hire AI employees</p></div>
                            </a>
                        </div>
                    </div>
                </div>

                <!-- 2. FEATURES DROPDOWN -->
                <div class="group/nav relative h-full flex items-center">
                    <button class="flex items-center gap-1 text-[15px] font-semibold text-dark hover:text-whatsapp transition-colors h-full cursor-pointer">
                        Features <i data-lucide="chevron-down" class="w-[14px] h-[14px] transition-transform group-hover/nav:rotate-180"></i>
                    </button>
                    <!-- Panel -->
                    <div class="absolute top-[100%] left-0 w-[300px] bg-white rounded-[16px] shadow-floating border border-slate-100 p-2.5 opacity-0 invisible group-hover/nav:opacity-100 group-hover/nav:visible transition-all duration-200 translate-y-2 group-hover/nav:translate-y-0 z-50">
                        <div class="absolute -top-6 left-0 w-full h-6"></div> <!-- Bridge -->
                        <div class="flex flex-col max-h-[70vh] overflow-y-auto">
                            <a href="#" class="flex gap-3 hover:bg-green-50 p-2.5 rounded-xl transition-colors group/item cursor-pointer">
                                <div class="w-9 h-9 rounded-lg bg-whatsapp/10 text-whatsapp flex items-center justify-center shrink-0 group-hover/item:scale-110 transition-transform"><i data-lucide="star" class="w-[18px] h-[18px]"></i></div>
                                <div class="flex flex-col justify-center gap-0.5"><h4 class="font-bold text-dark text-[14px] leading-tight">Features</h4><p class="text-[12px] text-grayTxt leading-tight">Explore all powerful features</p></div>
                            </a>
                            <div class="h-[1px] bg-slate-100 my-1 mx-2"></div>
                            <a href="#" class="flex gap-3 hover:bg-green-50 p-2.5 rounded-xl transition-colors group/item cursor-pointer border-t border-slate-100">
                                <div class="w-9 h-9 rounded-lg bg-whatsapp/10 text-whatsapp flex items-center justify-center shrink-0 group-hover/item:scale-110 transition-transform"><i data-lucide="send" class="w-[18px] h-[18px]"></i></div>
                                <div class="flex flex-col justify-center gap-0.5"><h4 class="font-bold text-dark text-[14px] leading-tight">WhatsApp Broadcasting</h4><p class="text-[12px] text-grayTxt leading-tight">Retargeting, CRM & more</p></div>
                            </a>
                            <a href="#" class="flex gap-3 hover:bg-green-50 p-2.5 rounded-xl transition-colors group/item cursor-pointer">
                                <div class="w-9 h-9 rounded-lg bg-whatsapp/10 text-whatsapp flex items-center justify-center shrink-0 group-hover/item:scale-110 transition-transform"><i data-lucide="brain" class="w-[18px] h-[18px]"></i></div>
                                <div class="flex flex-col justify-center gap-0.5"><h4 class="font-bold text-dark text-[14px] leading-tight">AI WhatsApp Chatbot</h4><p class="text-[12px] text-grayTxt leading-tight">Automate anything with AI</p></div>
                            </a>
                            <a href="#" class="flex gap-3 hover:bg-green-50 p-2.5 rounded-xl transition-colors group/item cursor-pointer">
                                <div class="w-9 h-9 rounded-lg bg-whatsapp/10 text-whatsapp flex items-center justify-center shrink-0 group-hover/item:scale-110 transition-transform"><i data-lucide="trending-up" class="w-[18px] h-[18px]"></i></div>
                                <div class="flex flex-col justify-center gap-0.5"><h4 class="font-bold text-dark text-[14px] leading-tight">Ads Manager</h4><p class="text-[12px] text-grayTxt leading-tight">3X your leads</p></div>
                            </a>
                            <a href="#" class="flex gap-3 hover:bg-green-50 p-2.5 rounded-xl transition-colors group/item cursor-pointer">
                                <div class="w-9 h-9 rounded-lg bg-whatsapp/10 text-whatsapp flex items-center justify-center shrink-0 group-hover/item:scale-110 transition-transform"><i data-lucide="message-square" class="w-[18px] h-[18px]"></i></div>
                                <div class="flex flex-col justify-center gap-0.5"><h4 class="font-bold text-dark text-[14px] leading-tight">WhatsApp Chatbots</h4><p class="text-[12px] text-grayTxt leading-tight">Drag & drop flow builder</p></div>
                            </a>
                            <a href="#" class="flex gap-3 hover:bg-green-50 p-2.5 rounded-xl transition-colors group/item cursor-pointer">
                                <div class="w-9 h-9 rounded-lg bg-whatsapp/10 text-whatsapp flex items-center justify-center shrink-0 group-hover/item:scale-110 transition-transform"><i data-lucide="shopping-bag" class="w-[18px] h-[18px]"></i></div>
                                <div class="flex flex-col justify-center gap-0.5"><h4 class="font-bold text-dark text-[14px] leading-tight">WhatsApp Catalog</h4><p class="text-[12px] text-grayTxt leading-tight">Sell products in chat</p></div>
                            </a>
                            <a href="#" class="flex gap-3 hover:bg-green-50 p-2.5 rounded-xl transition-colors group/item cursor-pointer">
                                <div class="w-9 h-9 rounded-lg bg-whatsapp/10 text-whatsapp flex items-center justify-center shrink-0 group-hover/item:scale-110 transition-transform"><i data-lucide="indian-rupee" class="w-[18px] h-[18px]"></i></div>
                                <div class="flex flex-col justify-center gap-0.5"><h4 class="font-bold text-dark text-[14px] leading-tight">WhatsApp Payments</h4><p class="text-[12px] text-grayTxt leading-tight">Collect via UPI & cards</p></div>
                            </a>
                            <a href="#" class="flex gap-3 hover:bg-green-50 p-2.5 rounded-xl transition-colors group/item cursor-pointer">
                                <div class="w-9 h-9 rounded-lg bg-whatsapp/10 text-whatsapp flex items-center justify-center shrink-0 group-hover/item:scale-110 transition-transform"><i data-lucide="clipboard-list" class="w-[18px] h-[18px]"></i></div>
                                <div class="flex flex-col justify-center gap-0.5"><h4 class="font-bold text-dark text-[14px] leading-tight">WhatsApp Forms</h4><p class="text-[12px] text-grayTxt leading-tight">Native data collection</p></div>
                            </a>
                            <a href="#" class="flex gap-3 hover:bg-green-50 p-2.5 rounded-xl transition-colors group/item cursor-pointer">
                                <div class="w-9 h-9 rounded-lg bg-whatsapp/10 text-whatsapp flex items-center justify-center shrink-0 group-hover/item:scale-110 transition-transform"><i data-lucide="globe" class="w-[18px] h-[18px]"></i></div>
                                <div class="flex flex-col justify-center gap-0.5"><h4 class="font-bold text-dark text-[14px] leading-tight">WhatsApp Webviews</h4><p class="text-[12px] text-grayTxt leading-tight">Web inside WhatsApp</p></div>
                            </a>
                            <a href="#" class="flex gap-3 hover:bg-green-50 p-2.5 rounded-xl transition-colors group/item cursor-pointer">
                                <div class="w-9 h-9 rounded-lg bg-whatsapp/10 text-whatsapp flex items-center justify-center shrink-0 group-hover/item:scale-110 transition-transform"><i data-lucide="crosshair" class="w-[18px] h-[18px]"></i></div>
                                <div class="flex flex-col justify-center gap-0.5"><h4 class="font-bold text-dark text-[14px] leading-tight">Click Tracking</h4><p class="text-[12px] text-grayTxt leading-tight">Import, broadcast & track</p></div>
                            </a>
                        </div>
                    </div>
                </div>

                <!-- 3. INDUSTRIES DROPDOWN -->
                <div class="group/nav relative h-full flex items-center">
                    <button class="flex items-center gap-1 text-[15px] font-semibold text-dark hover:text-whatsapp transition-colors h-full cursor-pointer">
                        Industries <i data-lucide="chevron-down" class="w-[14px] h-[14px] transition-transform group-hover/nav:rotate-180"></i>
                    </button>
                    <!-- Panel -->
                    <div class="absolute top-[100%] left-0 w-[300px] bg-white rounded-[16px] shadow-floating border border-slate-100 p-2.5 opacity-0 invisible group-hover/nav:opacity-100 group-hover/nav:visible transition-all duration-200 translate-y-2 group-hover/nav:translate-y-0 z-50">
                        <div class="absolute -top-6 left-0 w-full h-6"></div> <!-- Bridge -->
                        <div class="flex flex-col max-h-[70vh] overflow-y-auto">
                            <a href="#" class="flex gap-3 hover:bg-green-50 p-2.5 rounded-xl transition-colors group/item cursor-pointer">
                                <div class="w-9 h-9 rounded-lg bg-whatsapp/10 text-whatsapp flex items-center justify-center shrink-0 group-hover/item:scale-110 transition-transform"><i data-lucide="building-2" class="w-[18px] h-[18px]"></i></div>
                                <div class="flex flex-col justify-center gap-0.5"><h4 class="font-bold text-dark text-[14px] leading-tight">All Industries</h4><p class="text-[12px] text-grayTxt leading-tight">Industry-wise use cases</p></div>
                            </a>
                            <div class="h-[1px] bg-slate-100 my-1 mx-2"></div>
                            <a href="#" class="flex gap-3 hover:bg-green-50 p-2.5 rounded-xl transition-colors group/item cursor-pointer">
                                <div class="w-9 h-9 rounded-lg bg-whatsapp/10 text-whatsapp flex items-center justify-center shrink-0 group-hover/item:scale-110 transition-transform"><i data-lucide="graduation-cap" class="w-[18px] h-[18px]"></i></div>
                                <div class="flex flex-col justify-center gap-0.5"><h4 class="font-bold text-dark text-[14px] leading-tight">Education</h4><p class="text-[12px] text-grayTxt leading-tight">Edtech, coaches</p></div>
                            </a>
                            <a href="#" class="flex gap-3 hover:bg-green-50 p-2.5 rounded-xl transition-colors group/item cursor-pointer">
                                <div class="w-9 h-9 rounded-lg bg-whatsapp/10 text-whatsapp flex items-center justify-center shrink-0 group-hover/item:scale-110 transition-transform"><i data-lucide="shopping-cart" class="w-[18px] h-[18px]"></i></div>
                                <div class="flex flex-col justify-center gap-0.5"><h4 class="font-bold text-dark text-[14px] leading-tight">E-commerce</h4><p class="text-[12px] text-grayTxt leading-tight">D2C brands</p></div>
                            </a>
                            <a href="#" class="flex gap-3 hover:bg-green-50 p-2.5 rounded-xl transition-colors group/item cursor-pointer">
                                <div class="w-9 h-9 rounded-lg bg-whatsapp/10 text-whatsapp flex items-center justify-center shrink-0 group-hover/item:scale-110 transition-transform"><i data-lucide="landmark" class="w-[18px] h-[18px]"></i></div>
                                <div class="flex flex-col justify-center gap-0.5"><h4 class="font-bold text-dark text-[14px] leading-tight">Finance & Insurance</h4><p class="text-[12px] text-grayTxt leading-tight">Fintech & banking</p></div>
                            </a>
                            <a href="#" class="flex gap-3 hover:bg-green-50 p-2.5 rounded-xl transition-colors group/item cursor-pointer">
                                <div class="w-9 h-9 rounded-lg bg-whatsapp/10 text-whatsapp flex items-center justify-center shrink-0 group-hover/item:scale-110 transition-transform"><i data-lucide="stethoscope" class="w-[18px] h-[18px]"></i></div>
                                <div class="flex flex-col justify-center gap-0.5"><h4 class="font-bold text-dark text-[14px] leading-tight">Healthcare</h4><p class="text-[12px] text-grayTxt leading-tight">Appointment booking</p></div>
                            </a>
                            <a href="#" class="flex gap-3 hover:bg-green-50 p-2.5 rounded-xl transition-colors group/item cursor-pointer">
                                <div class="w-9 h-9 rounded-lg bg-whatsapp/10 text-whatsapp flex items-center justify-center shrink-0 group-hover/item:scale-110 transition-transform"><i data-lucide="car" class="w-[18px] h-[18px]"></i></div>
                                <div class="flex flex-col justify-center gap-0.5"><h4 class="font-bold text-dark text-[14px] leading-tight">Automobile</h4><p class="text-[12px] text-grayTxt leading-tight">Book test drives</p></div>
                            </a>
                            <a href="#" class="flex gap-3 hover:bg-green-50 p-2.5 rounded-xl transition-colors group/item cursor-pointer">
                                <div class="w-9 h-9 rounded-lg bg-whatsapp/10 text-whatsapp flex items-center justify-center shrink-0 group-hover/item:scale-110 transition-transform"><i data-lucide="home" class="w-[18px] h-[18px]"></i></div>
                                <div class="flex flex-col justify-center gap-0.5"><h4 class="font-bold text-dark text-[14px] leading-tight">Real Estate</h4><p class="text-[12px] text-grayTxt leading-tight">Brokers & developers</p></div>
                            </a>
                            <a href="#" class="flex gap-3 hover:bg-green-50 p-2.5 rounded-xl transition-colors group/item cursor-pointer">
                                <div class="w-9 h-9 rounded-lg bg-whatsapp/10 text-whatsapp flex items-center justify-center shrink-0 group-hover/item:scale-110 transition-transform"><i data-lucide="monitor" class="w-[18px] h-[18px]"></i></div>
                                <div class="flex flex-col justify-center gap-0.5"><h4 class="font-bold text-dark text-[14px] leading-tight">IT Services & Internet</h4><p class="text-[12px] text-grayTxt leading-tight">Showcase services</p></div>
                            </a>
                            <a href="#" class="flex gap-3 hover:bg-green-50 p-2.5 rounded-xl transition-colors group/item cursor-pointer">
                                <div class="w-9 h-9 rounded-lg bg-whatsapp/10 text-whatsapp flex items-center justify-center shrink-0 group-hover/item:scale-110 transition-transform"><i data-lucide="calendar" class="w-[18px] h-[18px]"></i></div>
                                <div class="flex flex-col justify-center gap-0.5"><h4 class="font-bold text-dark text-[14px] leading-tight">Events & Webinar</h4><p class="text-[12px] text-grayTxt leading-tight">Boost attendance</p></div>
                            </a>
                        </div>
                    </div>
                </div>

                <!-- 4. RESOURCES DROPDOWN -->
                <div class="group/nav relative h-full flex items-center">
                    <button class="flex items-center gap-1 text-[15px] font-semibold text-dark hover:text-whatsapp transition-colors h-full cursor-pointer">
                        Resources <i data-lucide="chevron-down" class="w-[14px] h-[14px] transition-transform group-hover/nav:rotate-180"></i>
                    </button>
                    <!-- Panel -->
                    <div class="absolute top-[100%] left-[50%] -translate-x-[50%] w-[300px] bg-white rounded-[16px] shadow-floating border border-slate-100 p-2.5 opacity-0 invisible group-hover/nav:opacity-100 group-hover/nav:visible transition-all duration-200 translate-y-2 group-hover/nav:translate-y-0 z-50">
                        <div class="absolute -top-6 left-0 w-full h-6"></div> <!-- Bridge -->
                        <div class="flex flex-col max-h-[70vh] overflow-y-auto">
                            <a href="#" class="flex gap-3 hover:bg-green-50 p-2.5 rounded-xl transition-colors group/item cursor-pointer">
                                <div class="w-9 h-9 rounded-lg bg-whatsapp/10 text-whatsapp flex items-center justify-center shrink-0 group-hover/item:scale-110 transition-transform"><i data-lucide="help-circle" class="w-[18px] h-[18px]"></i></div>
                                <div class="flex flex-col justify-center gap-0.5"><h4 class="font-bold text-dark text-[14px] leading-tight">Help Center</h4><p class="text-[12px] text-grayTxt leading-tight">FAQs & guides</p></div>
                            </a>
                            <a href="#" class="flex gap-3 hover:bg-green-50 p-2.5 rounded-xl transition-colors group/item cursor-pointer">
                                <div class="w-9 h-9 rounded-lg bg-whatsapp/10 text-whatsapp flex items-center justify-center shrink-0 group-hover/item:scale-110 transition-transform"><i data-lucide="play-circle" class="w-[18px] h-[18px]"></i></div>
                                <div class="flex flex-col justify-center gap-0.5"><h4 class="font-bold text-dark text-[14px] leading-tight">Tutorials</h4><p class="text-[12px] text-grayTxt leading-tight">Learn platform</p></div>
                            </a>
                            <a href="#" class="flex gap-3 hover:bg-green-50 p-2.5 rounded-xl transition-colors group/item cursor-pointer">
                                <div class="w-9 h-9 rounded-lg bg-whatsapp/10 text-whatsapp flex items-center justify-center shrink-0 group-hover/item:scale-110 transition-transform"><i data-lucide="youtube" class="w-[18px] h-[18px]"></i></div>
                                <div class="flex flex-col justify-center gap-0.5"><h4 class="font-bold text-dark text-[14px] leading-tight">YouTube</h4><p class="text-[12px] text-grayTxt leading-tight">Videos & podcasts</p></div>
                            </a>
                            <a href="#" class="flex gap-3 hover:bg-green-50 p-2.5 rounded-xl transition-colors group/item cursor-pointer">
                                <div class="w-9 h-9 rounded-lg bg-whatsapp/10 text-whatsapp flex items-center justify-center shrink-0 group-hover/item:scale-110 transition-transform"><i data-lucide="library" class="w-[18px] h-[18px]"></i></div>
                                <div class="flex flex-col justify-center gap-0.5"><h4 class="font-bold text-dark text-[14px] leading-tight">Template Library</h4><p class="text-[12px] text-grayTxt leading-tight">Ready templates</p></div>
                            </a>
                            <a href="#" class="flex gap-3 hover:bg-green-50 p-2.5 rounded-xl transition-colors group/item cursor-pointer">
                                <div class="w-9 h-9 rounded-lg bg-whatsapp/10 text-whatsapp flex items-center justify-center shrink-0 group-hover/item:scale-110 transition-transform"><i data-lucide="file-text" class="w-[18px] h-[18px]"></i></div>
                                <div class="flex flex-col justify-center gap-0.5"><h4 class="font-bold text-dark text-[14px] leading-tight">Blog</h4><p class="text-[12px] text-grayTxt leading-tight">Updates & stories</p></div>
                            </a>
                            <a href="#" class="flex gap-3 hover:bg-green-50 p-2.5 rounded-xl transition-colors group/item cursor-pointer">
                                <div class="w-9 h-9 rounded-lg bg-whatsapp/10 text-whatsapp flex items-center justify-center shrink-0 group-hover/item:scale-110 transition-transform"><i data-lucide="code" class="w-[18px] h-[18px]"></i></div>
                                <div class="flex flex-col justify-center gap-0.5"><h4 class="font-bold text-dark text-[14px] leading-tight">Developer APIs</h4><p class="text-[12px] text-grayTxt leading-tight">Send templates via API</p></div>
                            </a>
                            <a href="#" class="flex gap-3 hover:bg-green-50 p-2.5 rounded-xl transition-colors group/item cursor-pointer">
                                <div class="w-9 h-9 rounded-lg bg-whatsapp/10 text-whatsapp flex items-center justify-center shrink-0 group-hover/item:scale-110 transition-transform"><i data-lucide="award" class="w-[18px] h-[18px]"></i></div>
                                <div class="flex flex-col justify-center gap-0.5"><h4 class="font-bold text-dark text-[14px] leading-tight">Case Studies</h4><p class="text-[12px] text-grayTxt leading-tight">Growth stories</p></div>
                            </a>
                        </div>
                    </div>
                </div>

                <!-- 5. INTEGRATIONS DROPDOWN -->
                <div class="group/nav relative h-full flex items-center">
                    <button class="flex items-center gap-1 text-[15px] font-semibold text-dark hover:text-whatsapp transition-colors h-full cursor-pointer">
                        Integrations <i data-lucide="chevron-down" class="w-[14px] h-[14px] transition-transform group-hover/nav:rotate-180"></i>
                    </button>
                    <!-- Panel -->
                    <div class="absolute top-[100%] right-0 w-[300px] bg-white rounded-[16px] shadow-floating border border-slate-100 p-2.5 opacity-0 invisible group-hover/nav:opacity-100 group-hover/nav:visible transition-all duration-200 translate-y-2 group-hover/nav:translate-y-0 z-50">
                        <div class="absolute -top-6 left-0 w-full h-6"></div> <!-- Bridge -->
                        <div class="flex flex-col max-h-[70vh] overflow-y-auto">
                            <a href="#" class="flex gap-3 hover:bg-green-50 p-2.5 rounded-xl transition-colors group/item cursor-pointer">
                                <div class="w-9 h-9 rounded-lg bg-whatsapp/10 text-whatsapp flex items-center justify-center shrink-0 group-hover/item:scale-110 transition-transform"><i data-lucide="blocks" class="w-[18px] h-[18px]"></i></div>
                                <div class="flex flex-col justify-center gap-0.5"><h4 class="font-bold text-dark text-[14px] leading-tight">Explore all Integrations</h4><p class="text-[12px] text-grayTxt leading-tight">Automate notifications</p></div>
                            </a>
                            <div class="h-[1px] bg-slate-100 my-1 mx-2"></div>
                            <a href="#" class="flex gap-3 hover:bg-green-50 p-2.5 rounded-xl transition-colors group/item cursor-pointer">
                                <div class="w-9 h-9 rounded-lg bg-whatsapp/10 text-whatsapp flex items-center justify-center shrink-0 group-hover/item:scale-110 transition-transform"><i data-lucide="shopping-bag" class="w-[18px] h-[18px]"></i></div>
                                <div class="flex flex-col justify-center gap-0.5"><h4 class="font-bold text-dark text-[14px] leading-tight">Shopify</h4><p class="text-[12px] text-grayTxt leading-tight">Abandoned cart, orders</p></div>
                            </a>
                            <a href="#" class="flex gap-3 hover:bg-green-50 p-2.5 rounded-xl transition-colors group/item cursor-pointer">
                                <div class="w-9 h-9 rounded-lg bg-whatsapp/10 text-whatsapp flex items-center justify-center shrink-0 group-hover/item:scale-110 transition-transform"><i data-lucide="credit-card" class="w-[18px] h-[18px]"></i></div>
                                <div class="flex flex-col justify-center gap-0.5"><h4 class="font-bold text-dark text-[14px] leading-tight">Razorpay</h4><p class="text-[12px] text-grayTxt leading-tight">Payment alerts</p></div>
                            </a>
                            <a href="#" class="flex gap-3 hover:bg-green-50 p-2.5 rounded-xl transition-colors group/item cursor-pointer">
                                <div class="w-9 h-9 rounded-lg bg-whatsapp/10 text-whatsapp flex items-center justify-center shrink-0 group-hover/item:scale-110 transition-transform"><i data-lucide="shopping-cart" class="w-[18px] h-[18px]"></i></div>
                                <div class="flex flex-col justify-center gap-0.5"><h4 class="font-bold text-dark text-[14px] leading-tight">Shopify Checkouts</h4><p class="text-[12px] text-grayTxt leading-tight">Magic checkout</p></div>
                            </a>
                            <a href="#" class="flex gap-3 hover:bg-green-50 p-2.5 rounded-xl transition-colors group/item cursor-pointer">
                                <div class="w-9 h-9 rounded-lg bg-whatsapp/10 text-whatsapp flex items-center justify-center shrink-0 group-hover/item:scale-110 transition-transform"><i data-lucide="webhook" class="w-[18px] h-[18px]"></i></div>
                                <div class="flex flex-col justify-center gap-0.5"><h4 class="font-bold text-dark text-[14px] leading-tight">WebEngage</h4><p class="text-[12px] text-grayTxt leading-tight">Journey automation</p></div>
                            </a>
                            <a href="#" class="flex gap-3 hover:bg-green-50 p-2.5 rounded-xl transition-colors group/item cursor-pointer">
                                <div class="w-9 h-9 rounded-lg bg-whatsapp/10 text-whatsapp flex items-center justify-center shrink-0 group-hover/item:scale-110 transition-transform"><i data-lucide="users" class="w-[18px] h-[18px]"></i></div>
                                <div class="flex flex-col justify-center gap-0.5"><h4 class="font-bold text-dark text-[14px] leading-tight">LeadSquared</h4><p class="text-[12px] text-grayTxt leading-tight">CRM integration</p></div>
                            </a>
                            <a href="#" class="flex gap-3 hover:bg-green-50 p-2.5 rounded-xl transition-colors group/item cursor-pointer">
                                <div class="w-9 h-9 rounded-lg bg-whatsapp/10 text-whatsapp flex items-center justify-center shrink-0 group-hover/item:scale-110 transition-transform"><i data-lucide="link-2" class="w-[18px] h-[18px]"></i></div>
                                <div class="flex flex-col justify-center gap-0.5"><h4 class="font-bold text-dark text-[14px] leading-tight">Integrately</h4><p class="text-[12px] text-grayTxt leading-tight">Build automations</p></div>
                            </a>
                            <a href="#" class="flex gap-3 hover:bg-green-50 p-2.5 rounded-xl transition-colors group/item cursor-pointer">
                                <div class="w-9 h-9 rounded-lg bg-whatsapp/10 text-whatsapp flex items-center justify-center shrink-0 group-hover/item:scale-110 transition-transform"><i data-lucide="network" class="w-[18px] h-[18px]"></i></div>
                                <div class="flex flex-col justify-center gap-0.5"><h4 class="font-bold text-dark text-[14px] leading-tight">Webhook APIs</h4><p class="text-[12px] text-grayTxt leading-tight">Backend connection</p></div>
                            </a>
                        </div>
                    </div>
                </div>

                <a href="#" class="text-[15px] font-semibold text-dark hover:text-whatsapp transition-colors h-full flex items-center cursor-pointer">App</a>
                <a href="#" class="text-[15px] font-semibold text-dark hover:text-whatsapp transition-colors h-full flex items-center cursor-pointer">Partner</a>
            </div>

            <!-- Right Nav -->
            <div class="hidden lg:flex items-center gap-5 shrink-0">
                <button class="flex items-center gap-1.5 text-[15px] font-semibold text-dark hover:text-whatsapp transition-colors cursor-pointer">Eng <i data-lucide="globe" class="w-4 h-4"></i></button>
                <a href="#" class="text-[14px] font-bold text-dark bg-white border-2 border-slate-200 px-5 py-2.5 rounded-xl hover:border-dark transition-colors cursor-pointer">Login</a>
                <a href="#" class="text-[14px] font-bold bg-whatsapp text-white px-6 py-2.5 rounded-xl hover:bg-whatsappHover shadow-[0_4px_14px_rgba(37,211,102,0.4)] hover:shadow-[0_6px_20px_rgba(37,211,102,0.5)] transition-all transform hover:-translate-y-0.5 cursor-pointer">Start for FREE</a>
            </div>

            <!-- Mobile Toggle -->
            <button id="mobile-menu-btn" class="lg:hidden text-dark bg-slate-50 p-2 rounded-lg cursor-pointer">
                <i data-lucide="menu" class="w-6 h-6"></i>
            </button>
        </div>
    </nav>
"""

with open('index.html', 'r') as f:
    content = f.read()

start_idx = content.find('<nav id="navbar"')
end_idx = content.find('</nav>', start_idx) + 6

if start_idx != -1 and end_idx != -1:
    new_content = content[:start_idx] + new_nav + content[end_idx:]
    with open('index.html', 'w') as f:
        f.write(new_content)
    print("Replaced!")
else:
    print("Not found!")
