import os
import re

base_dir = r'e:\azzle\azzle-main\azzle'

# ---- index.html specific changes ----
def update_index():
    filepath = os.path.join(base_dir, 'index.html')
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Title and meta
    content = content.replace(
        '<title>Azzle - AI Technology &amp; Startup HTML Template</title>',
        '<title>Nextology Innovation | Digital Solutions Partner</title>'
    )
    content = content.replace(
        '<meta name="description" content="AIMass Tailwind based SASS Template" />',
        '<meta name="description" content="Nextology Innovation delivers enterprise cloud solutions, AI development, mobile apps, and digital transformation services in Chennai. Your trusted partner for cutting-edge technology." />'
    )
    
    # Hero heading
    content = content.replace(
        'Simplify your SaaS solution with AI',
        'Your Technology-Driven Partner for Digital Success'
    )
    
    # Hero subtext
    content = content.replace(
        'Our AI SAAS tool is a cloud-based software delivery model. It\n                                helps businesses forecast demand for products and services and\n                                optimize inventory management and supply chain operations.',
        'We build secure, scalable cloud platforms and automation solutions to accelerate business growth and digital transformation.'
    )
    
    # Hero buttons
    content = content.replace('Get\n                                    started for free', 'Get in Touch')
    content = content.replace('Learn\n                                    more', 'Our Services')
    content = content.replace('<a href="#"\n                                    class="button rounded-[50px] border-2 border-black bg-black py-4 text-white after:bg-colorOrangyRed hover:border-colorOrangyRed hover:text-white">Get\n                                    started for free</a>', 
                               '<a href="contact.html"\n                                    class="button rounded-[50px] border-2 border-black bg-black py-4 text-white after:bg-colorOrangyRed hover:border-colorOrangyRed hover:text-white">Get in Touch</a>')
    content = content.replace('<a href="#"\n                                    class="button rounded-[50px] border-2 border-black bg-transparent py-4 text-black after:bg-colorOrangyRed hover:border-colorOrangyRed hover:text-white">Learn\n                                    more</a>',
                               '<a href="services.html"\n                                    class="button rounded-[50px] border-2 border-black bg-transparent py-4 text-black after:bg-colorOrangyRed hover:border-colorOrangyRed hover:text-white">Our Services</a>')
    
    # Brand slider section text
    content = content.replace(
        'Companies of all sizes trust us to find AI SaaS critical to\n                                their growth and innovation',
        'Trusted by great companies that lead their industries'
    )
    
    # Services section heading
    content = content.replace(
        '<h2>Core features that make it valuable</h2>',
        '<h2>What We Do Best</h2>'
    )
    
    # Service items - replace all 4 with Nextology's 8 services
    old_services = '''                        <!-- Service List -->
                        <ul
                            class="jos grid grid-cols-1 gap-[2px] overflow-hidden rounded-[10px] border-2 border-black bg-black sm:grid-cols-2 lg:grid-cols-4">
                            <!-- Service Item -->
                            <li class="group bg-white p-[30px] transition-all duration-300 ease-in-out hover:bg-black">
                                <div class="relative mb-9 h-[70px] w-[70px]">
                                    <img src="assets/img/th-1/service-icon-black-1.svg" alt="" width="70" height="70" />
                                    <img src="assets/img/th-1/service-icon-orange-1.svg" alt="service-icon-orange-1"
                                        width="70" height="70"
                                        class="absolute left-0 top-0 h-full w-full opacity-0 transition-all duration-300 ease-linear group-hover:opacity-100" />
                                </div>
                                <h3
                                    class="mb-4 block text-xl leading-tight -tracking-[0.5px] group-hover:text-white xl:text-2xl xxl:text-[28px]">
                                    <a href="services.html" class="hover:text-colorOrangyRed">
                                        Resource Flexibility
                                    </a>
                                </h3>

                                <p class="mb-12 duration-300 group-hover:text-white">
                                    This is an excellent option for people & small businesses
                                    who are starting out.
                                </p>

                                <a href="services.html"
                                    class="relative inline-block h-[30px] w-[30px] duration-300">
                                    <img src="assets/img/th-1/arrow-right-black.svg" alt="arrow-right-black" width="30"
                                        height="30" />
                                    <img src="assets/img/th-1/arrow-right-orange.svg" alt="arrow-right-black" width="30"
                                        height="30"
                                        class="absolute left-0 top-0 h-full w-full opacity-0 transition-all duration-300 ease-linear group-hover:opacity-100" />
                                </a>
                            </li>
                            <!-- Service Item -->
                            <!-- Service Item -->
                            <li class="group bg-white p-[30px] transition-all duration-300 ease-in-out hover:bg-black">
                                <div class="relative mb-9 h-[70px] w-[70px]">
                                    <img src="assets/img/th-1/service-icon-black-2.svg" alt="service-icon-black-2"
                                        width="70" height="70" />
                                    <img src="assets/img/th-1/service-icon-orange-2.svg" alt="service-icon-orange-1"
                                        width="70" height="70"
                                        class="absolute left-0 top-0 h-full w-full opacity-0 transition-all duration-300 ease-linear group-hover:opacity-100" />
                                </div>

                                <h3
                                    class="mb-4 block text-xl leading-tight -tracking-[0.5px] group-hover:text-white xl:text-2xl xxl:text-[28px]">
                                    <a href="services.html" class="hover:text-colorOrangyRed">
                                        Managed Services
                                    </a>
                                </h3>

                                <p class="mb-12 duration-300 group-hover:text-white">
                                    This is an excellent option for people & small businesses
                                    who are starting out.
                                </p>

                                <a href="services.html"
                                    class="relative inline-block h-[30px] w-[30px] duration-300">
                                    <img src="assets/img/th-1/arrow-right-black.svg" alt="arrow-right-black" width="30"
                                        height="30" />
                                    <img src="assets/img/th-1/arrow-right-orange.svg" alt="arrow-right-black" width="30"
                                        height="30"
                                        class="absolute left-0 top-0 h-full w-full opacity-0 transition-all duration-300 ease-linear group-hover:opacity-100" />
                                </a>
                                <!-- Features Item -->
                                <!-- Features Item -->
                            </li>
                            <!-- Service Item -->
                            <!-- Service Item -->
                            <li class="group bg-white p-[30px] transition-all duration-300 ease-in-out hover:bg-black">
                                <div class="relative mb-9 h-[70px] w-[70px]">
                                    <img src="assets/img/th-1/service-icon-black-3.svg" alt="service-icon-black-3"
                                        width="70" height="70" />
                                    <img src="assets/img/th-1/service-icon-orange-3.svg" alt="service-icon-orange-3"
                                        width="70" height="70"
                                        class="absolute left-0 top-0 h-full w-full opacity-0 transition-all duration-300 ease-linear group-hover:opacity-100" />
                                </div>
                                <h3
                                    class="mb-4 block text-xl leading-tight -tracking-[0.5px] group-hover:text-white xl:text-2xl xxl:text-[28px]">
                                    <a href="services.html" class="hover:text-colorOrangyRed">
                                        Web-Based Access
                                    </a>
                                </h3>

                                <p class="mb-12 duration-300 group-hover:text-white">
                                    This is an excellent option for people & small businesses
                                    who are starting out.
                                </p>

                                <a href="services.html"
                                    class="relative inline-block h-[30px] w-[30px] duration-300">
                                    <img src="assets/img/th-1/arrow-right-black.svg" alt="arrow-right-black" width="30"
                                        height="30" />
                                    <img src="assets/img/th-1/arrow-right-orange.svg" alt="arrow-right-black" width="30"
                                        height="30"
                                        class="absolute left-0 top-0 h-full w-full opacity-0 transition-all duration-300 ease-linear group-hover:opacity-100" />
                                </a>
                            </li>
                            <!-- Service Item -->
                            <!-- Service Item -->
                            <li class="group bg-white p-[30px] transition-all duration-300 ease-in-out hover:bg-black">
                                <div class="relative mb-9 h-[70px] w-[70px]">
                                    <img src="assets/img/th-1/service-icon-black-4.svg" alt="service-icon-black-4"
                                        width="70" height="70" />
                                    <img src="assets/img/th-1/service-icon-orange-4.svg" alt="service-icon-orange-4"
                                        width="70" height="70"
                                        class="absolute left-0 top-0 h-full w-full opacity-0 transition-all duration-300 ease-linear group-hover:opacity-100" />
                                </div>
                                <h3
                                    class="mb-4 block text-xl leading-tight -tracking-[0.5px] group-hover:text-white xl:text-2xl xxl:text-[28px]">
                                    <a href="services.html" class="hover:text-colorOrangyRed">
                                        Resource Flexibility
                                    </a>
                                </h3>

                                <p class="mb-12 duration-300 group-hover:text-white">
                                    This is an excellent option for people & small businesses
                                    who are starting out.
                                </p>

                                <a href="services.html"
                                    class="relative inline-block h-[30px] w-[30px] duration-300">
                                    <img src="assets/img/th-1/arrow-right-black.svg" alt="arrow-right-black" width="30"
                                        height="30" />
                                    <img src="assets/img/th-1/arrow-right-orange.svg" alt="arrow-right-black" width="30"
                                        height="30"
                                        class="absolute left-0 top-0 h-full w-full opacity-0 transition-all duration-300 ease-linear group-hover:opacity-100" />
                                </a>
                            </li>
                            <!-- Service Item -->
                        </ul>
                        <!-- Service List -->'''
    
    services_data = [
        ('service-icon-black-1.svg', 'service-icon-orange-1.svg', 'Mobile App Development', 'Build powerful mobile apps with stunning design and performance for iOS and Android.'),
        ('service-icon-black-2.svg', 'service-icon-orange-2.svg', 'Web Development', 'Create fast, responsive websites that engage and convert users effectively.'),
        ('service-icon-black-3.svg', 'service-icon-orange-3.svg', 'Digital Marketing', 'Boost online reach through SEO, ads, and data-driven content strategy.'),
        ('service-icon-black-4.svg', 'service-icon-orange-4.svg', 'Social Media Marketing', 'Grow your audience with creative, data-driven social media campaigns.'),
        ('service-icon-black-5.svg', 'service-icon-orange-5.svg', 'Product Development', 'Turn bold ideas into scalable, high-impact digital products that deliver.'),
        ('service-icon-black-6.svg', 'service-icon-orange-6.svg', 'Cloud & DevOps Solutions', 'Move to the cloud with seamless, secure infrastructure and DevOps automation.'),
        ('service-icon-black-1.svg', 'service-icon-orange-1.svg', 'AR/VR Solutions', 'Deliver immersive augmented and virtual reality experiences for your audience.'),
        ('service-icon-black-2.svg', 'service-icon-orange-2.svg', 'AI & Chatbot Development', 'Automate support and engagement using intelligent AI-powered chatbots.'),
    ]
    
    items_html = ''
    for (icon_b, icon_o, title, desc) in services_data:
        items_html += f'''                            <!-- Service Item -->
                            <li class="group bg-white p-[30px] transition-all duration-300 ease-in-out hover:bg-black">
                                <div class="relative mb-9 h-[70px] w-[70px]">
                                    <img src="assets/img/th-1/{icon_b}" alt="{title}" width="70" height="70" />
                                    <img src="assets/img/th-1/{icon_o}" alt="{title}" width="70" height="70"
                                        class="absolute left-0 top-0 h-full w-full opacity-0 transition-all duration-300 ease-linear group-hover:opacity-100" />
                                </div>
                                <h3 class="mb-4 block text-xl leading-tight -tracking-[0.5px] group-hover:text-white xl:text-2xl xxl:text-[28px]">
                                    <a href="services.html" class="hover:text-colorOrangyRed">{title}</a>
                                </h3>
                                <p class="mb-12 duration-300 group-hover:text-white">{desc}</p>
                                <a href="services.html" class="relative inline-block h-[30px] w-[30px] duration-300">
                                    <img src="assets/img/th-1/arrow-right-black.svg" alt="arrow-right-black" width="30" height="30" />
                                    <img src="assets/img/th-1/arrow-right-orange.svg" alt="arrow-right-black" width="30" height="30"
                                        class="absolute left-0 top-0 h-full w-full opacity-0 transition-all duration-300 ease-linear group-hover:opacity-100" />
                                </a>
                            </li>
'''
    
    new_services = f'''                        <!-- Service List -->
                        <ul class="jos grid grid-cols-1 gap-[2px] overflow-hidden rounded-[10px] border-2 border-black bg-black sm:grid-cols-2 lg:grid-cols-4">
{items_html}                        </ul>
                        <!-- Service List -->'''
    
    content = content.replace(old_services, new_services)
    
    # Content section 1 - about
    content = content.replace(
        '<h2>Accessible to a wider audience</h2>',
        '<h2>Your Digital Foundation Partner</h2>'
    )
    content = content.replace(
        'Advanced AI capabilities accessible to a broader audience,\n                                        including small &amp; medium-sized businesses and individuals\n                                        who may not have the resources or expertise to develop.\n                                    </p>\n                                    <p class="mb-7 last:mb-0">\n                                        Advanced AI capabilities accessible to a broader audience,\n                                        including small &amp; medium-sized businesses and individuals\n                                        who may not have the resources or expertise to develop.',
        'At Nextology Innovation, we pioneer the future of cloud computing by delivering enterprise-grade solutions that empower businesses to thrive in the digital age.\n                                    </p>\n                                    <p class="mb-7 last:mb-0">\n                                        From startups to Fortune 500 companies, we\'ve helped organizations across industries unlock the full potential of cloud technology. With proven methodologies, cutting-edge tools, and dedicated support, we\'re your trusted partner in digital transformation.'
    )
    
    # Content section 2 - quick deploy
    content = content.replace(
        '<h2>Providing quick deploy solutions</h2>',
        '<h2>Building Solutions That Endure</h2>'
    )
    content = content.replace(
        'Our AI SaaS solutions can be quickly deployed, enabling\n                                        users to start benefiting from AI capabilities without\n                                        lengthy setup and development times in fast-paced\n                                        industries.',
        'We design scalable, secure cloud solutions tailored to your business, blending agility with reliability.'
    )
    content = content.replace('Ready-to-use AI capabilities system', 'Enterprise-grade cloud infrastructure')
    content = content.replace('Users can quickly integrate AI features', 'Seamless DevOps & CI/CD automation')
    content = content.replace('Time savings translate to cost savings', '24/7 monitoring and dedicated support')
    
    # Funfact section
    content = content.replace(
        '<h2 class="text-white">AI-powered that streamline tasks</h2>',
        '<h2 class="text-white">12+ Years of Digital Excellence</h2>'
    )
    content = content.replace(
        'As your business grows or your AI SaaS needs change, you can\n                                    easily adjust your subscription level to match those needs.\n                                    This flexibility ensures that AI remains an asset.',
        'We build secure, scalable cloud platforms and automation solutions to accelerate your business growth and digital transformation journey.'
    )
    # Counters
    content = content.replace('data-countup-number="92">92</span>%', 'data-countup-number="98">98</span>%')
    content = content.replace('Customer service inquiries', 'Client Satisfaction & Retention')
    content = content.replace('data-countup-number="75">75</span>%', 'data-countup-number="225">225</span>+')
    content = content.replace('Using financial institutions', 'Successfully Completed Projects')
    
    # FAQ section
    content = content.replace(
        '<h2>Freely ask us for more information</h2>',
        '<h2>Frequently Asked Questions</h2>'
    )
    content = content.replace(
        'Our AI SaaS solutions can be quickly deployed, enabling\n                                        users to start benefiting from AI capabilities without\n                                        lengthy setup and development times in fast-paced\n                                        industries.\n                                    </p>\n                                    <a href="faq.html"',
        'Have questions about our services? We\'re here to help you find the right technology solutions for your business needs.\n                                    </p>\n                                    <a href="contact.html"'
    )
    content = content.replace('>Ask\n                                        you questions</a>', '>Contact Us</a>')
    content = content.replace(
        '<p>How do I start AI SaaS?</p>',
        '<p>What services does Nextology Innovation offer?</p>'
    )
    content = content.replace(
        '<p>Can I customize AI SaaS solutions?</p>',
        '<p>How long does a typical project take?</p>'
    )
    content = content.replace(
        '<p>How can AI benefit my business?</p>',
        '<p>Do you provide support after project delivery?</p>'
    )
    content = re.sub(
        r'Go to the our official website and require users to\s+create an account\. You\'ll need to provide some basic\s+information and agree to our terms and conditions\.',
        'We offer Mobile App Development, Web Development, Cloud & DevOps Solutions, AI & Chatbot Development, Digital Marketing, Social Media Marketing, Product Development, and AR/VR Solutions.',
        content,
        count=1
    )
    content = re.sub(
        r'Go to the our official website and require users to\s+create an account\. You\'ll need to provide some basic\s+information and agree to our terms and conditions\.',
        'Project timelines vary based on complexity. Simple websites take 2-4 weeks, while complex enterprise applications may take 3-6 months. We provide detailed timelines during initial consultation.',
        content,
        count=1
    )
    content = re.sub(
        r'Go to the our official website and require users to\s+create an account\. You\'ll need to provide some basic\s+information and agree to our terms and conditions\.',
        'Yes! We provide comprehensive post-delivery support including maintenance, updates, and 24/7 technical assistance to ensure your solution continues to perform optimally.',
        content,
        count=1
    )
    
    # Testimonials section heading
    content = content.replace(
        '<h2 class="text-white">Positive feedback from our users</h2>',
        '<h2 class="text-white">What Our Clients Say</h2>'
    )
    # Testimonial content
    content = content.replace(
        '"This AI SaaS tool has revolutionized the way we process and\n                                    analyze data. This is a game-changer for our business."',
        '"Working with this team was like finding the missing piece to our brand puzzle. They took our vague ideas and transformed them into a visual identity that feels unmistakably us. The website they built doesn\'t just look stunning — it converts."'
    )
    content = content.replace(
        '>Max Weber\n                                        </span>\n                                        <span class="block text-sm font-light leading-[1.4]">\n                                            HR Manager',
        '>Jessica Doe\n                                        </span>\n                                        <span class="block text-sm font-light leading-[1.4]">\n                                            Business Owner'
    )
    content = content.replace(
        '"It answers immediately, and we\'ve seen a significant\n                                    reduction in response time. Our customers love it and so do\n                                    we!"',
        '"Most agencies talk about innovation — these folks actually deliver it. They challenged our assumptions, pushed us out of our comfort zone, and designed a campaign that made our competitors look outdated."'
    )
    content = content.replace(
        '>Douglas Smith\n                                        </span>\n                                        <span class="block text-sm font-light leading-[1.4]">\n                                            Businessman',
        '>John Doe\n                                        </span>\n                                        <span class="block text-sm font-light leading-[1.4]">\n                                            Entrepreneur'
    )
    content = content.replace(
        '"It is accurate, fast and supports multiple languages\n                                    support. It is a must for any international business\n                                    success."',
        '"We\'ve hired four agencies over the years. This is the first time we\'ve walked away thinking, \'Damn, that was worth every penny.\' From branding to web design, their attention to detail is obsessive in the best way."'
    )
    content = content.replace(
        '>Abraham Maslo\n                                        </span>\n                                        <span class="block text-sm font-light leading-[1.4]">\n                                            Founder @ Marketing Company',
        '>Eric Smith\n                                        </span>\n                                        <span class="block text-sm font-light leading-[1.4]">\n                                            CEO @ Tech Firm'
    )
    content = content.replace(
        '"Security is a top concern for us, and AI SaaS takes it\n                                    seriously. It\'s a reassuring layer of protection for our\n                                    organization."',
        '"Nextology Innovation transformed our digital presence completely. Their Cloud & DevOps expertise helped us cut deployment times by 70%. Absolutely phenomenal team!"'
    )
    content = content.replace(
        '>Jack Fayol\n                                        </span>\n                                        <span class="block text-sm font-light leading-[1.4]">\n                                            HR Manager',
        '>Priya Sharma\n                                        </span>\n                                        <span class="block text-sm font-light leading-[1.4]">\n                                            CTO @ Startup'
    )
    content = content.replace(
        '"We were concerned about integrating their APIs were well\n                                    documented, and their support team was super cool."',
        '"Their mobile app development team created a stunning app for our business. The UX is flawless and user engagement has tripled since launch. Highly recommend!"'
    )
    content = content.replace(
        '>Karen Lynn\n                                        </span>\n                                        <span class="block text-sm font-light leading-[1.4]">\n                                            Software Engineer',
        '>Rajesh Kumar\n                                        </span>\n                                        <span class="block text-sm font-light leading-[1.4]">\n                                            Product Manager'
    )
    content = content.replace(
        '"The return on investment has exceeded our expectations.\n                                    it\'s an investment in the future of our business."',
        '"The AI chatbot they built for our customer service team handles 80% of queries automatically. ROI was evident within the first month. World-class quality!"'
    )
    content = content.replace(
        '>Henry Ochi\n                                        </span>\n                                        <span class="block text-sm font-light leading-[1.4]">\n                                            Bank Manager',
        '>Anitha Rajan\n                                        </span>\n                                        <span class="block text-sm font-light leading-[1.4]">\n                                            Operations Head'
    )
    
    # Footer slider text
    content = content.replace('Start building software', "Let's Build Something Remarkable")
    
    # Footer mission text
    content = content.replace(
        'Our mission is to harness the power of AI to solve complex\n                            business challenges &amp; decision-makers with data-driven insights,\n                            and enhance user experiences across digital platforms.',
        'Nextology Innovation pioneers the future of cloud computing and digital transformation, delivering enterprise-grade solutions that empower businesses to thrive in the digital age.'
    )
    content = content.replace(
        'Website: <a href="https://www.example.com">www.example.com</a>',
        'Email: <a href="mailto:contact@nextologyinnovations.com">contact@nextologyinnovations.com</a><br>Phone: <a href="tel:+918925017127">+91 89250 17127</a>'
    )
    
    # Footer copyright
    content = content.replace(
        '&copy; Copyright 2023, All Rights Reserved by Mthemeus',
        '&copy; Copyright 2025, All Rights Reserved by Nextology Innovation'
    )
    
    # Header login/signup buttons -> Book a Call / Contact
    content = content.replace(
        '<a href="login.html"\n                            class="button hidden rounded-[50px] border-[#7F8995] bg-transparent text-black after:bg-colorOrangyRed hover:border-colorOrangyRed hover:text-white lg:inline-block">Login</a>',
        '<a href="contact.html"\n                            class="button hidden rounded-[50px] border-[#7F8995] bg-transparent text-black after:bg-colorOrangyRed hover:border-colorOrangyRed hover:text-white lg:inline-block">Book a Call</a>'
    )
    content = content.replace(
        '<a href="signup.html"\n                            class="button hidden rounded-[50px] border-black bg-black text-white after:bg-colorOrangyRed hover:border-colorOrangyRed hover:text-white lg:inline-block">Sign\n                            up free</a>',
        '<a href="contact.html"\n                            class="button hidden rounded-[50px] border-black bg-black text-white after:bg-colorOrangyRed hover:border-colorOrangyRed hover:text-white lg:inline-block">Get Started</a>'
    )
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Updated index.html")

# ---- Common changes for ALL pages ----
def update_all_pages():
    files = [
        'about.html', 'blog-details.html', 'blog.html', 'contact.html', 'error-404.html',
        'faq-2.html', 'faq.html', 'index.html', 'login.html', 'portfolio-details.html',
        'portfolio.html', 'pricing.html', 'reset-password.html', 'services.html',
        'signup.html', 'team-details.html', 'teams.html'
    ]
    
    for fname in files:
        filepath = os.path.join(base_dir, fname)
        if not os.path.exists(filepath):
            print(f"Skipping missing: {fname}")
            continue
        
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Title tag fallback for all pages
        content = content.replace(
            'Azzle - AI Technology &amp; Startup HTML Template',
            'Nextology Innovation | Digital Solutions Partner'
        )
        content = content.replace(
            'AIMass Tailwind based SASS Template',
            'Nextology Innovation delivers enterprise cloud solutions, AI development, mobile apps, and digital transformation services in Chennai.'
        )
        
        # Footer copyright
        content = content.replace(
            '&copy; Copyright 2023, All Rights Reserved by Mthemeus',
            '&copy; Copyright 2025, All Rights Reserved by Nextology Innovation'
        )
        # Also handle footer contact info
        content = content.replace(
            'Website: <a href="https://www.example.com">www.example.com</a>',
            'Email: <a href="mailto:contact@nextologyinnovations.com">contact@nextologyinnovations.com</a><br>Phone: <a href="tel:+918925017127">+91 89250 17127</a>'
        )
        content = content.replace(
            'Our mission is to harness the power of AI to solve complex\n                            business challenges &amp; decision-makers with data-driven insights,\n                            and enhance user experiences across digital platforms.',
            'Nextology Innovation pioneers the future of cloud computing and digital transformation, delivering enterprise-grade solutions that empower businesses to thrive in the digital age.'
        )
        # Footer slider text
        content = content.replace('Start building software', "Let's Build Something Remarkable")
        
        # Header login/signup -> Book a Call/Get Started
        content = content.replace(
            '>Login</a>',
            '>Book a Call</a>'
        ).replace('href="login.html"', 'href="contact.html"')
        content = content.replace(
            '>Sign\n                            up free</a>',
            '>Get Started</a>'
        ).replace('href="signup.html"\n                            class="button hidden rounded-[50px] border-black', 'href="contact.html"\n                            class="button hidden rounded-[50px] border-black')
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated common content: {fname}")

# ---- about.html ----
def update_about():
    filepath = os.path.join(base_dir, 'about.html')
    if not os.path.exists(filepath):
        print("about.html not found")
        return
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    content = content.replace(
        '<h2>Analyze any data perfectly with AI</h2>',
        '<h2>Welcome to the Age of Digital Transformation</h2>'
    )
    content = content.replace(
        'AI data analysis, also known as artificial intelligence\n                                        data analysis or AI-driven data analysis, refers to the\n                                        process of using artificial intelligence and machine\n                                        learning techniques.',
        'At Nextology Innovation, we\'re pioneering the future of cloud computing by delivering enterprise-grade solutions that empower businesses to thrive in the digital age.'
    )
    content = content.replace('Data Preprocessing', 'Cloud Infrastructure')
    content = content.replace(
        'AI data analysis can begin, and raw data must be\n                                             collected, cleaned.',
        'Scalable, secure cloud solutions tailored to your specific business requirements.'
    )
    content = content.replace('Predictive Analytics', 'DevOps Automation')
    content = content.replace(
        'Algorithms use historical data to forecast future\n                                             trends, behaviors.',
        'Automate deployment pipelines for faster, more reliable software delivery.'
    )
    content = content.replace(
        '<h2>Widely used throughout the industry for work</h2>',
        '<h2>Trusted Across Industries Worldwide</h2>'
    )
    content = content.replace('1. Businesses and Corporations:', '1. Startups & Scale-ups:')
    content = content.replace(
        'Businesses use AI data analysis to gain competitive\n                                             advantages, optimize operations, &amp; make data-driven\n                                             decisions. This includes industries such as retail,\n                                             finance, manufacturing.',
        'We help emerging startups build scalable cloud-native architectures that grow with their user base, reducing time-to-market and operational costs.'
    )
    content = content.replace(
        '2. Data Scientists and Analysts:\n                                         </h5>',
        '2. Enterprise Organizations:</h5>'
    )
    content = content.replace(
        'Data scientists and analysts leverage AI tools and\n                                             algorithms to extract actionable insights from large\n                                             datasets. They alsouse AI for predictive modeling,\n                                             anomaly detection, and data visualization.',
        'Fortune 500 companies trust our enterprise-grade solutions for digital transformation, cloud migration, and AI integration that delivers measurable business results.'
    )
    content = content.replace(
        '3. Government and Public Sector:\n                                         </h5>',
        '3. Digital-First Businesses:</h5>'
    )
    content = content.replace(
        'Government agencies use AI data analysis for various\n                                             purposes, including public policy development, law\n                                             enforcement, urban planning, and disaster.',
        'E-commerce, FinTech, and SaaS companies leverage our mobile app development, AI chatbots, and cloud infrastructure to deliver exceptional digital experiences.'
    )
    content = content.replace(
        '<h2 class="text-white">AI-powered that streamline tasks</h2>',
        '<h2 class="text-white">12+ Years of Innovation</h2>'
    )
    content = content.replace(
        'As your business grows or your AI SaaS needs change, you can\n                                    easily adjust your subscription level to match those needs.\n                                    This flexibility ensures that AI remains an asset.',
        'Great brands aren\'t accidental — they\'re carefully crafted with vision and expertise. We combine strategic thinking with hands-on creativity to help you stand out.'
    )
    content = content.replace('<h2>Manage large amounts of data</h2>', '<h2>Cloud-First Solutions That Scale</h2>')
    content = content.replace(
        'AI data analysis also can handle vast amounts of data,\n                                        making it suitable for big data environments. Data\n                                        analysis can automate many aspects of data processing and\n                                        analysis',
        'Your digital foundation is more than just lines of code — it\'s the backbone of your success. We design scalable, secure cloud solutions that deliver and endure for years to come.'
    )
    content = content.replace('Real-Time Analysis', 'Mission-Driven')
    content = content.replace(
        'Some AI data analysis solutions are design to process\n                                             making instant.',
        'Our mission is to make cutting-edge technology accessible, empowering every business to achieve its digital transformation goals.'
    )
    content = content.replace('Automation', 'Customer-First Approach')
    content = content.replace(
        'his leads to increased efficiency and quicker\n                                             decision-making.',
        'We combine deep technical expertise with a commitment to your success, ensuring your journey is smooth, secure, and successful.'
    )
    content = content.replace(
        'We always want to connect our clients',
        'We Always Want to Connect With Our Clients'
    )
    content = content.replace(
        'AI accessible and beneficial for organizations, and we\n                                        look forward to partnering with businesses to achieve\n                                        their AI goals.',
        'Nextology Innovation is accessible and beneficial for organizations of all sizes. We look forward to partnering with businesses to achieve their digital transformation goals.'
    )
    content = content.replace('href="https://www.example.com"\n                                            class="text-white hover:text-colorOrangyRed">www.example.com', 
                               'href="https://nextologyinnovation.com"\n                                            class="text-white hover:text-colorOrangyRed">nextologyinnovation.com')
    content = content.replace('href="mailto:yourmail@mail.com"\n                                            class="text-white hover:text-colorOrangyRed">yourmail@mail.com',
                               'href="mailto:contact@nextologyinnovations.com"\n                                            class="text-white hover:text-colorOrangyRed">contact@nextologyinnovations.com')
    content = content.replace('href="tel:+1234567890" class="text-white hover:text-colorOrangyRed">(123)\n                                            456-7890',
                               'href="tel:+918925017127" class="text-white hover:text-colorOrangyRed">+91 89250 17127')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Updated about.html")

# ---- contact.html ----
def update_contact():
    filepath = os.path.join(base_dir, 'contact.html')
    if not os.path.exists(filepath):
        print("contact.html not found")
        return
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    content = content.replace('yourmail@mail.com', 'contact@nextologyinnovations.com')
    content = content.replace('+1 800 234 3456', '+91 89250 17127')
    content = content.replace('172 Collins Street, Melbourne, Australia', '172A, Bharathipuram, Chrompet, Chennai, India')
    content = content.replace('(123) 456-7890', '+91 89250 17127')
    content = content.replace('www.example.com', 'nextologyinnovation.com')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Updated contact.html")

# ---- services.html ----
def update_services():
    filepath = os.path.join(base_dir, 'services.html')
    if not os.path.exists(filepath):
        print("services.html not found")
        return
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    content = content.replace(
        '<h1 class="breadcrumb-title">Data Analytics</h1>',
        '<h1 class="breadcrumb-title">Our Services</h1>'
    )
    content = content.replace(
        '<h2>Analyze any data perfectly with AI</h2>',
        '<h2>Mobile App Development</h2>'
    )
    content = content.replace(
        'AI data analysis, also known as artificial intelligence\n                                        data analysis or AI-driven data analysis, refers to the\n                                        process of using artificial intelligence and machine\n                                        learning techniques.',
        'Build powerful, scalable mobile applications for iOS and Android platforms with stunning design and peak performance. From concept to deployment, we handle it all.'
    )
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Updated services.html")

# Run all updates
update_all_pages()
update_index()
update_about()
update_contact()
update_services()
print("\nAll pages updated successfully!")
