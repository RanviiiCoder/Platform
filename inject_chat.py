import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

old_floating_btn_regex = r'<!-- Floating Chat Element -->.*?</a>'

new_chat_widget = """<!-- Floating AI Chat Widget -->
    <div class="fixed bottom-6 right-6 z-[100] flex flex-col items-end">
        <!-- Chat Widget Panel -->
        <div id="ai-chat-panel" class="w-[340px] bg-white rounded-[16px] shadow-[0_10px_40px_rgba(0,0,0,0.15)] border border-slate-100 mb-4 opacity-0 invisible translate-y-4 transition-all duration-300 origin-bottom-right overflow-hidden flex flex-col">
            
            <!-- Header (Green Gradient) -->
            <div class="bg-gradient-to-br from-[#1EBE57] to-[#075E54] p-6 pb-12 relative">
                <button id="close-ai-chat" class="absolute top-4 right-4 text-white/80 hover:text-white transition-colors cursor-pointer">
                    <i data-lucide="x" class="w-5 h-5"></i>
                </button>
                <div class="flex items-center gap-3 mb-2">
                    <h3 class="text-white font-bold text-[22px]">Hi there 👋</h3>
                </div>
                <p class="text-white/90 text-[13.5px] leading-snug mb-5 font-medium">Explore Docs, News or Chat with us to get started.</p>
                <!-- 3 avatars -->
                <div class="flex -space-x-3">
                    <img src="https://ui-avatars.com/api/?name=Sarah&background=random" class="w-9 h-9 rounded-full border-2 border-[#1EBE57]">
                    <img src="https://ui-avatars.com/api/?name=Alex&background=random" class="w-9 h-9 rounded-full border-2 border-[#1EBE57]">
                    <img src="https://ui-avatars.com/api/?name=AI&background=random" class="w-9 h-9 rounded-full border-2 border-[#1EBE57]">
                </div>
            </div>

            <!-- Content Area -->
            <div class="p-4 flex-grow bg-[#F8FAFC] relative">
                <!-- Floating Preview Card -->
                <div class="bg-white rounded-xl shadow-sm border border-slate-100 p-4 -mt-12 relative z-10 mb-4 cursor-pointer hover:shadow-md transition-all">
                    <div class="flex items-center gap-2 mb-2">
                        <span class="px-2 py-0.5 rounded bg-blue-100 text-blue-700 text-[10px] uppercase font-bold tracking-wider">News</span>
                        <span class="text-[11px] text-slate-400 font-medium">Just now</span>
                    </div>
                    <h4 class="text-[14px] font-bold text-dark leading-tight mb-1.5">Template Message Journey is now live 🚀</h4>
                    <p class="text-[12px] text-grayTxt leading-snug">Automate entire drip campaigns via WhatsApp API easily.</p>
                </div>

                <!-- Input area -->
                <div class="bg-white rounded-xl shadow-sm border border-slate-100 flex items-center justify-between mb-3 mt-4 overflow-hidden">
                    <input type="text" placeholder="Ask a question..." class="flex-grow bg-transparent border-none text-[13px] px-4 py-3 focus:ring-0 outline-none text-dark placeholder:text-slate-400">
                    <button class="w-[38px] h-[38px] rounded-lg bg-whatsapp/10 text-whatsapp flex items-center justify-center hover:bg-whatsapp hover:text-white transition-colors cursor-pointer shrink-0 mr-1.5">
                        <i data-lucide="send" class="w-[18px] h-[18px]"></i>
                    </button>
                </div>
                <p class="text-center text-[10.5px] text-slate-400 font-medium pb-1">AI agent team can help.</p>
            </div>

            <!-- Footer Nav -->
            <div class="bg-white border-t border-slate-100 p-1 flex justify-evenly items-center">
                <button class="flex flex-col items-center justify-center gap-1 text-whatsapp w-full py-3 cursor-pointer transition-colors">
                    <i data-lucide="home" class="w-[18px] h-[18px]"></i>
                    <span class="text-[11px] font-bold">Home</span>
                </button>
                <button class="flex flex-col items-center justify-center gap-1 text-slate-400 hover:text-dark transition-colors w-full py-3 cursor-pointer">
                    <i data-lucide="message-square" class="w-[18px] h-[18px]"></i>
                    <span class="text-[11px] font-medium">Messages</span>
                </button>
                <button class="flex flex-col items-center justify-center gap-1 text-slate-400 hover:text-dark transition-colors w-full py-3 cursor-pointer relative">
                    <div class="absolute top-[8px] right-[38px] w-[7px] h-[7px] bg-red-500 rounded-full"></div>
                    <i data-lucide="zap" class="w-[18px] h-[18px]"></i>
                    <span class="text-[11px] font-medium">News</span>
                </button>
            </div>
        </div>

        <!-- Toggle Button (Floating Bounce) -->
        <button id="ai-chat-btn" class="w-[60px] h-[60px] bg-whatsapp text-white rounded-full shadow-floating flex items-center justify-center hover:scale-105 transition-all duration-300 cursor-pointer hover:shadow-[0_10px_30px_rgba(37,211,102,0.4)] animate-[bounce_3s_infinite]">
            <span id="ai-chat-icon-open" class="flex"><i data-lucide="message-square-text" class="w-[28px] h-[28px] fill-current"></i></span>
            <span id="ai-chat-icon-close" class="hidden"><i data-lucide="chevron-down" class="w-[28px] h-[28px]"></i></span>
        </button>
    </div>"""

text = re.sub(old_floating_btn_regex, new_chat_widget, text, flags=re.DOTALL)

script_logic = """
        // Intercom-style AI Chat Widget Logic
        const aiChatBtn = document.getElementById('ai-chat-btn');
        const closeAiChatBtn = document.getElementById('close-ai-chat');
        const aiChatPanel = document.getElementById('ai-chat-panel');
        const iconOpen = document.getElementById('ai-chat-icon-open');
        const iconClose = document.getElementById('ai-chat-icon-close');

        function toggleAiChat() {
            if(!aiChatPanel) return;
            const isClosed = aiChatPanel.classList.contains('opacity-0');
            if(isClosed) {
                // Open panel
                aiChatPanel.classList.remove('opacity-0', 'invisible', 'translate-y-4');
                aiChatPanel.classList.add('opacity-100', 'visible', 'translate-y-0');
                
                // Toggle Icon
                iconOpen.classList.add('hidden');
                iconOpen.classList.remove('flex');
                iconClose.classList.add('flex');
                iconClose.classList.remove('hidden');
                
                // Stop bounce
                aiChatBtn.classList.remove('animate-[bounce_3s_infinite]');
            } else {
                // Close panel
                aiChatPanel.classList.add('opacity-0', 'invisible', 'translate-y-4');
                aiChatPanel.classList.remove('opacity-100', 'visible', 'translate-y-0');
                
                // Toggle Icon
                iconClose.classList.add('hidden');
                iconClose.classList.remove('flex');
                iconOpen.classList.add('flex');
                iconOpen.classList.remove('hidden');
            }
        }

        if(aiChatBtn) aiChatBtn.addEventListener('click', toggleAiChat);
        if(closeAiChatBtn) closeAiChatBtn.addEventListener('click', toggleAiChat);
"""

# Inject before </body>
text = text.replace("    </script>\n</body>", script_logic + "    </script>\n</body>")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Finished inject.")
