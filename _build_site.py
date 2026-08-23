#!/usr/bin/env python3
"""Generate Global Route Company website pages from the Logistica template."""
import json
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parent

COMPANY = "Global Route Company"
TAGLINE = "Connecting India to Global Markets"
PHONE = "+91 9225159719"
PHONE_TEL = "+919225159719"
EMAIL = "lokeshghagare@gmail.com"
ADDRESS = "Plot No. 188, CA Road, Garoba Maidan, Nagpur, Maharashtra (Near Dalvi Hospital) - 440008"
MAP_LAT = "21.1473515"
MAP_LNG = "79.1214913"
MAP_EMBED = f"https://www.google.com/maps?q={MAP_LAT},{MAP_LNG}&z=17&hl=en&output=embed"
MAP_LINK = f"https://www.google.com/maps?q={MAP_LAT},{MAP_LNG}"
WHATSAPP = "https://wa.me/919225159719?text=Hello%20Global%20Route%20Company%2C%20I%20would%20like%20to%20enquire%20about%20sourcing%20from%20India."
SITE = "https://groute.co.in"

SEO_KEYWORDS = (
    "Import Export Company India, Agricultural Exporter India, Agricultural Products Export, "
    "Indian Agricultural Products, Import Export Trading Company, Global Sourcing, "
    "Agricultural Commodities, Export from India"
)
SEO_DESC = (
    "Global Route Company is an India-based import and export trading company connecting "
    "agricultural products, suppliers and global buyers through reliable sourcing and "
    "international trade solutions."
)


ORG_SCHEMA = json.dumps(
    {
        "@context": "https://schema.org",
        "@type": "Organization",
        "name": COMPANY,
        "url": f"{SITE}/",
        "logo": f"{SITE}/img/logo.svg",
        "email": EMAIL,
        "telephone": PHONE,
        "description": SEO_DESC,
        "address": {
            "@type": "PostalAddress",
            "streetAddress": "Plot No. 188, CA Road, Garoba Maidan",
            "addressLocality": "Nagpur",
            "addressRegion": "Maharashtra",
            "postalCode": "440008",
            "addressCountry": "IN",
        },
        "geo": {
            "@type": "GeoCoordinates",
            "latitude": MAP_LAT,
            "longitude": MAP_LNG,
        },
        "hasMap": MAP_LINK,
    },
    ensure_ascii=False,
)


def head(title: str, description: str, page: str, noindex: bool = False) -> str:
    path = "/" if page == "index.html" else f"/{page}"
    url = SITE + path
    robots = "noindex, follow" if noindex else "index, follow"
    return f"""<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="utf-8">
    <title>{title}</title>
    <meta content="width=device-width, initial-scale=1.0" name="viewport">
    <meta name="robots" content="{robots}">
    <meta content="{SEO_KEYWORDS}" name="keywords">
    <meta content="{description}" name="description">
    <link rel="canonical" href="{url}">
    <meta property="og:type" content="website">
    <meta property="og:site_name" content="{COMPANY}">
    <meta property="og:title" content="{title}">
    <meta property="og:description" content="{description}">
    <meta property="og:url" content="{url}">
    <meta property="og:image" content="{SITE}/img/og.jpg">
    <meta property="og:locale" content="en_IN">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{title}">
    <meta name="twitter:description" content="{description}">
    <meta name="twitter:image" content="{SITE}/img/og.jpg">
    <link href="img/favicon.svg?v=2" rel="icon" type="image/svg+xml">
    <link href="img/favicon-32.png?v=2" rel="icon" type="image/png" sizes="32x32">
    <link href="img/apple-touch-icon.png?v=2" rel="apple-touch-icon">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.10.0/css/all.min.css" rel="stylesheet">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.4.1/font/bootstrap-icons.css" rel="stylesheet">
    <link href="css/bootstrap.min.css" rel="stylesheet">
    <link href="css/style.css" rel="stylesheet">
    <style>body{{font-family:"Plus Jakarta Sans",sans-serif;}} h1,h2,h3,h4,h5{{font-weight:700;}}</style>
    <script type="application/ld+json">{ORG_SCHEMA}</script>
</head>

<body>
    <a class="skip-link" href="#main">Skip to content</a>
"""


def nav(active: str) -> str:
    def c(name: str) -> str:
        return "nav-item nav-link active" if active == name else "nav-item nav-link"

    return f"""
    <div class="topbar d-none d-md-block">
        <div class="container d-flex justify-content-between align-items-center">
            <span>Nagpur, India</span>
            <div class="topbar-links">
                <a href="mailto:{EMAIL}">{EMAIL}</a>
                <a href="tel:{PHONE_TEL}">{PHONE} <span>IST</span></a>
            </div>
        </div>
    </div>
    <nav class="navbar navbar-expand-lg bg-white navbar-light sticky-top p-0">
        <a href="index.html" class="navbar-brand navbar-brand-logo" aria-label="{COMPANY}">
            <img src="img/logo.svg?v=3" alt="{COMPANY}" width="280" height="52">
        </a>
        <button type="button" class="navbar-toggler me-4" data-bs-toggle="collapse" data-bs-target="#navbarCollapse" aria-controls="navbarCollapse" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarCollapse">
            <div class="navbar-nav ms-auto p-4 p-lg-0">
                <a href="index.html" class="{c('home')}">Home</a>
                <a href="about.html" class="{c('about')}">About Us</a>
                <a href="products.html" class="{c('products')}">Products</a>
                <a href="service.html" class="{c('services')}">Services</a>
                <a href="contact.html" class="{c('contact')}">Contact</a>
                <a href="quote.html" class="nav-item nav-link d-lg-none">Request a Quote</a>
                <a href="{WHATSAPP}" class="nav-item nav-link d-lg-none" target="_blank" rel="noopener">WhatsApp</a>
            </div>
            <div class="navbar-actions d-none d-lg-flex align-items-center pe-lg-4">
                <a href="quote.html" class="btn btn-primary py-2 px-3 me-2">Request a Quote</a>
                <a href="{WHATSAPP}" class="btn btn-whatsapp py-2 px-3" target="_blank" rel="noopener"><i class="fab fa-whatsapp me-1"></i>WhatsApp</a>
            </div>
        </div>
    </nav>
"""


FOOTER = f"""
    <div class="container-fluid bg-dark text-light footer pt-5">
        <div class="container py-5">
            <div class="row g-5">
                <div class="col-lg-4 col-md-6">
                    <a href="index.html" class="footer-logo-link" aria-label="{COMPANY}"><img src="img/logo-white.svg?v=3" alt="{COMPANY}" class="footer-logo" width="280" height="52"></a>
                    <p class="footer-tagline">{TAGLINE}</p>
                    <p class="mb-2"><i class="fa fa-map-marker-alt me-3"></i>{ADDRESS}</p>
                    <p class="mb-2"><i class="fa fa-phone-alt me-3"></i><a class="text-light" href="tel:{PHONE_TEL}">{PHONE}</a> <span class="text-white-50">(IST)</span></p>
                    <p class="mb-2"><i class="fab fa-whatsapp me-3"></i><a class="text-light" href="{WHATSAPP}" target="_blank" rel="noopener">WhatsApp</a></p>
                    <p class="mb-2"><i class="fa fa-envelope me-3"></i><a class="text-light" href="mailto:{EMAIL}">{EMAIL}</a></p>
                </div>
                <div class="col-lg-2 col-md-6">
                    <h4 class="text-light mb-4">Quick Links</h4>
                    <a class="btn btn-link" href="index.html">Home</a>
                    <a class="btn btn-link" href="about.html">About Us</a>
                    <a class="btn btn-link" href="exports.html">Exports</a>
                    <a class="btn btn-link" href="imports.html">Imports</a>
                    <a class="btn btn-link" href="products.html">Products</a>
                    <a class="btn btn-link" href="service.html">Services</a>
                    <a class="btn btn-link" href="contact.html">Contact</a>
                    <a class="btn btn-link" href="privacy.html">Privacy Policy</a>
                </div>
                <div class="col-lg-3 col-md-6">
                    <h4 class="text-light mb-4">What We Do</h4>
                    <a class="btn btn-link" href="exports.html">Export from India</a>
                    <a class="btn btn-link" href="imports.html">Import to India</a>
                    <a class="btn btn-link" href="products.html">Agricultural Products</a>
                    <a class="btn btn-link" href="service.html">Global Sourcing</a>
                    <a class="btn btn-link" href="markets.html">Target Markets</a>
                    <a class="btn btn-link" href="quote.html">Request a Quote</a>
                </div>
                <div class="col-lg-3 col-md-6">
                    <h4 class="text-light mb-4">Start a Conversation</h4>
                    <p>Tell us what you are looking for and our team will explore suitable sourcing opportunities.</p>
                    <a href="quote.html" class="btn btn-primary py-2 px-4 mt-2">Request a Quote</a>
                    <a href="{WHATSAPP}" class="btn btn-whatsapp py-2 px-4 mt-2" target="_blank" rel="noopener">WhatsApp</a>
                </div>
            </div>
        </div>
        <div class="container">
            <div class="copyright">
                <div class="row">
                    <div class="col-md-12 text-center mb-3 mb-md-0">
                        &copy; 2026 {COMPANY}. All Rights Reserved. · <a class="border-bottom" href="privacy.html">Privacy Policy</a>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <a href="{WHATSAPP}" class="whatsapp-float" target="_blank" rel="noopener" aria-label="Chat on WhatsApp"><i class="fab fa-whatsapp"></i></a>
    <div class="grc-chat" id="grcChat">
        <div class="grc-chat-panel" id="grcChatPanel" hidden>
            <div class="grc-chat-head">
                <div>
                    <strong>Global Route</strong>
                    <span>Ask about products, trade or contact</span>
                </div>
                <button type="button" class="grc-chat-close" id="grcChatClose" aria-label="Close chat">&times;</button>
            </div>
            <div class="grc-chat-log" id="grcChatLog" role="log" aria-live="polite"></div>
            <div class="grc-chat-chips" id="grcChatChips"></div>
            <form class="grc-chat-form" id="grcChatForm" autocomplete="off">
                <label class="visually-hidden" for="grcChatInput">Your question</label>
                <input id="grcChatInput" type="text" maxlength="240" placeholder="Ask about products, export or contact">
                <button type="submit" aria-label="Send">Send</button>
            </form>
            <p class="grc-chat-note">Not a live agent. For a person, use WhatsApp or Request a Quote.</p>
        </div>
        <button type="button" class="grc-chat-launch" id="grcChatLaunch" aria-expanded="false" aria-controls="grcChatPanel">
            <i class="fa fa-comment-dots" aria-hidden="true"></i>
            <span>Ask us</span>
        </button>
    </div>
    <a href="#" class="btn btn-lg btn-primary btn-lg-square rounded-0 back-to-top"><i class="bi bi-arrow-up"></i></a>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0/dist/js/bootstrap.bundle.min.js"></script>
    <script src="js/main.js"></script>
    <script src="js/chat.js"></script>
</body>
</html>
"""


def page_header(title: str, crumb: str, image: str | None = None) -> str:
    if not image:
        return f"""
    <div class="container-xxl pt-5">
        <div class="container page-intro">
            <nav aria-label="breadcrumb">
                <ol class="breadcrumb mb-2">
                    <li class="breadcrumb-item"><a href="index.html">Home</a></li>
                    <li class="breadcrumb-item active" aria-current="page">{crumb}</li>
                </ol>
            </nav>
            <h1 class="page-intro-title">{title}</h1>
        </div>
    </div>
"""
    return f"""
    <div class="page-header" style="background-image: linear-gradient(rgba(11, 29, 54, .62), rgba(11, 29, 54, .62)), url({image});">
        <div class="container">
            <h1>{title}</h1>
            <nav aria-label="breadcrumb">
                <ol class="breadcrumb mb-0">
                    <li class="breadcrumb-item"><a class="text-white" href="index.html">Home</a></li>
                    <li class="breadcrumb-item text-white-50 active" aria-current="page">{crumb}</li>
                </ol>
            </nav>
        </div>
    </div>
"""


def product_href(name: str, enquiry: str = "Export from India") -> str:
    href = f"quote.html?product={quote(name)}"
    if enquiry:
        href += f"&type={quote(enquiry)}"
    return href


ENQUIRY_FORM = """
                    <form name="business-enquiry" method="POST" action="/thank-you.html" data-netlify="true" netlify-honeypot="bot-field">
                        <input type="hidden" name="form-name" value="business-enquiry">
                        <p class="d-none"><label>Don’t fill this out: <input name="bot-field"></label></p>
                        <div class="row g-3">
                            <div class="col-md-6">
                                <div class="form-floating">
                                    <input type="text" class="form-control" id="fullName" name="full_name" placeholder="Full Name" required>
                                    <label for="fullName">Full Name *</label>
                                </div>
                            </div>
                            <div class="col-md-6">
                                <div class="form-floating">
                                    <input type="text" class="form-control" id="companyName" name="company_name" placeholder="Company Name" required>
                                    <label for="companyName">Company Name *</label>
                                </div>
                            </div>
                            <div class="col-md-6">
                                <div class="form-floating">
                                    <input type="email" class="form-control" id="email" name="email" placeholder="Email" required>
                                    <label for="email">Email *</label>
                                </div>
                            </div>
                            <div class="col-md-6">
                                <div class="form-floating">
                                    <input type="tel" class="form-control" id="phone" name="phone" placeholder="Phone">
                                    <label for="phone">Phone</label>
                                </div>
                            </div>
                            <div class="col-md-6">
                                <div class="form-floating">
                                    <input type="text" class="form-control" id="country" name="country" placeholder="Country" required>
                                    <label for="country">Country *</label>
                                </div>
                            </div>
                            <div class="col-md-6">
                                <div class="form-floating">
                                    <select class="form-select" id="enquiryType" name="enquiry_type" required>
                                        <option value="" selected disabled>Select enquiry type</option>
                                        <option>Export from India</option>
                                        <option>Import to India</option>
                                        <option>Product Sourcing</option>
                                        <option>Supplier Partnership</option>
                                        <option>General Enquiry</option>
                                    </select>
                                    <label for="enquiryType">Enquiry Type *</label>
                                </div>
                            </div>
                            <div class="col-md-6">
                                <div class="form-floating">
                                    <input type="text" class="form-control" id="product" name="product" placeholder="Product / Commodity">
                                    <label for="product">Product / Commodity</label>
                                </div>
                            </div>
                            <div class="col-md-6">
                                <div class="form-floating">
                                    <input type="text" class="form-control" id="quantity" name="quantity" placeholder="Quantity">
                                    <label for="quantity">Quantity</label>
                                </div>
                            </div>
                            <div class="col-12">
                                <div class="form-floating">
                                    <input type="text" class="form-control" id="destination" name="destination_origin" placeholder="Destination / Origin">
                                    <label for="destination">Destination / Origin</label>
                                </div>
                            </div>
                            <div class="col-12">
                                <div class="form-floating">
                                    <textarea class="form-control" placeholder="Message" id="message" name="message" style="height: 120px"></textarea>
                                    <label for="message">Message</label>
                                </div>
                            </div>
                            <div class="col-12">
                                <button class="btn btn-primary w-100 py-3" type="submit">Submit Enquiry</button>
                            </div>
                        </div>
                    </form>
"""


def write(name: str, title: str, active: str, body: str, description: str = None, noindex: bool = False):
    html = head(title, description or SEO_DESC, name, noindex) + nav(active) + '<main id="main">\n' + body + "</main>\n" + FOOTER
    (ROOT / name).write_text(html, encoding="utf-8")
    print("wrote", name)


# ---- Page bodies ----

INDEX = f"""
    <form name="business-enquiry" method="POST" action="/thank-you.html" data-netlify="true" netlify-honeypot="bot-field" class="d-none" aria-hidden="true" tabindex="-1">
        <input type="hidden" name="form-name" value="business-enquiry">
        <input name="bot-field">
        <input name="full_name">
        <input name="company_name">
        <input name="email">
        <input name="phone">
        <input name="country">
        <input name="enquiry_type">
        <input name="product">
        <input name="quantity">
        <input name="destination_origin">
        <input name="message">
    </form>
    <div class="hero-single">
        <img src="img/carousel-1.jpg" alt="Indian agricultural fields for export" width="1920" height="1080" loading="eager" fetchpriority="high">
        <div class="hero-overlay">
            <div class="container">
                <div class="row justify-content-start">
                    <div class="col-11 col-lg-7">
                        <p class="hero-kicker">Import &amp; export · Agricultural trade · India</p>
                        <h1 class="hero-title">Connecting India to <span>global markets</span></h1>
                        <p class="hero-lead">{COMPANY} sources agricultural products from India for international buyers and explores selected import opportunities into India.</p>
                        <a href="quote.html" class="btn btn-primary py-3 px-4 me-3">Request a Quote</a>
                        <a href="products.html" class="btn btn-outline-light py-3 px-4">View Products</a>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <div class="container-xxl py-5">
        <div class="container py-5">
            <div class="text-center mx-auto mb-5" style="max-width: 720px;">
                <h6 class="text-secondary text-uppercase">Export from India</h6>
                <h2 class="mb-3">Agricultural products for international buyers</h2>
                <p class="mb-0">We source fruits, vegetables, spices, grains and related food products according to buyer requirements, seasonality and destination needs.</p>
            </div>
            <div class="row g-4">
                <div class="col-md-6 col-lg-3">
                    <a class="product-card" href="{product_href('Fresh Fruits')}">
                        <div class="product-img"><img src="img/products/fruits.jpg" alt="Fresh fruits" loading="lazy"></div>
                        <div class="p-4"><h4>Fresh Fruits</h4><p>Papaya, mango, banana, grapes, pomegranate and other seasonal fruits.</p><span class="enquire-link">Enquire</span></div>
                    </a>
                </div>
                <div class="col-md-6 col-lg-3">
                    <a class="product-card" href="{product_href('Fresh Vegetables')}">
                        <div class="product-img"><img src="img/products/vegetables.jpg" alt="Fresh vegetables" loading="lazy"></div>
                        <div class="p-4"><h4>Fresh Vegetables</h4><p>Onion, potato and other vegetables based on buyer specifications.</p><span class="enquire-link">Enquire</span></div>
                    </a>
                </div>
                <div class="col-md-6 col-lg-3">
                    <a class="product-card" href="{product_href('Chilli & Spices')}">
                        <div class="product-img"><img src="img/products/chilli.jpg" alt="Chilli and spices" loading="lazy"></div>
                        <div class="p-4"><h4>Chilli &amp; Spices</h4><p>Indian chilli, red chilli and selected spices for food and commodity buyers.</p><span class="enquire-link">Enquire</span></div>
                    </a>
                </div>
                <div class="col-md-6 col-lg-3">
                    <a class="product-card" href="{product_href('Grains & Pulses')}">
                        <div class="product-img"><img src="img/products/rice.jpg" alt="Rice and grains" loading="lazy"></div>
                        <div class="p-4"><h4>Grains &amp; Pulses</h4><p>Rice, pulses, grains and other agricultural commodities for export markets.</p><span class="enquire-link">Enquire</span></div>
                    </a>
                </div>
            </div>
            <div class="text-center mt-5">
                <a href="products.html" class="btn btn-primary py-3 px-5">View All Products</a>
            </div>
        </div>
    </div>

    <div class="container-fluid overflow-hidden py-5 px-lg-0 bg-light">
        <div class="container feature py-5 px-lg-0">
            <div class="row g-5 mx-lg-0">
                <div class="col-lg-6 feature-text wow fadeInUp" data-wow-delay="0.1s">
                    <h6 class="text-secondary text-uppercase mb-3">Import to India</h6>
                    <h1 class="mb-4">Bringing Global Opportunities to India</h1>
                    <p class="mb-4">Alongside exports, {COMPANY} explores international sourcing opportunities for products that have potential in the Indian market — based on demand, quality, supplier reliability and commercial viability.</p>
                    <a href="imports.html" class="btn btn-primary py-3 px-5">Discuss an Import Opportunity</a>
                </div>
                <div class="col-lg-6 pe-lg-0" style="min-height: 360px;">
                    <div class="position-relative h-100">
                        <img class="position-absolute img-fluid w-100 h-100" src="img/import-hero.jpg" style="object-fit: cover;" alt="Import coordination" loading="lazy">
                    </div>
                </div>
            </div>
        </div>
    </div>

    <div class="container-xxl py-5">
        <div class="container py-5">
            <div class="text-center mx-auto mb-5" style="max-width: 720px;">
                <h6 class="text-secondary text-uppercase">How we work</h6>
                <h2 class="mb-3">From requirement to delivery</h2>
            </div>
            <div class="process-line">
                <div class="process-step">
                    <div class="process-number">01</div>
                    <h5>Requirement</h5>
                    <p>Understand buyer and product requirements.</p>
                </div>
                <div class="process-step">
                    <div class="process-number">02</div>
                    <h5>Source</h5>
                    <p>Identify suitable products and suppliers.</p>
                </div>
                <div class="process-step">
                    <div class="process-number">03</div>
                    <h5>Verify</h5>
                    <p>Align quality needs and commercial discussions.</p>
                </div>
                <div class="process-step">
                    <div class="process-number">04</div>
                    <h5>Trade</h5>
                    <p>Discuss FOB or CIF and coordinate documentation with partners.</p>
                </div>
                <div class="process-step">
                    <div class="process-number">05</div>
                    <h5>Deliver</h5>
                    <p>Support shipment through logistics partners.</p>
                </div>
            </div>
        </div>
    </div>

    <div class="container-fluid cta-band py-5">
        <div class="container py-5">
            <div class="row g-4">
                <div class="col-lg-6">
                    <div class="cta-card text-white">
                        <h3 class="text-white mb-3">Looking for products from India?</h3>
                        <p class="mb-4">Tell us the commodity, quantity and destination. We will explore suitable sourcing options.</p>
                        <a href="quote.html" class="btn btn-primary py-3 px-4 me-2">Request a Quote</a>
                        <a href="contact.html" class="btn btn-outline-light py-3 px-4">Contact Us</a>
                    </div>
                </div>
                <div class="col-lg-6">
                    <div class="cta-card text-white">
                        <h3 class="text-white mb-3">Have a product to import into India?</h3>
                        <p class="mb-4">Share the opportunity and we will review commercial fit together.</p>
                        <a href="quote.html?type=Import%20to%20India" class="btn btn-secondary py-3 px-4">Discuss Your Requirement</a>
                    </div>
                </div>
            </div>
        </div>
    </div>
"""

PRODUCT_CARDS = [
    ("fruits.jpg", "Fruits", "Seasonal fresh fruits including papaya, mango, banana, grapes and pomegranate."),
    ("vegetables.jpg", "Vegetables", "Onion, potato and other vegetables based on market and buyer needs."),
    ("chilli.jpg", "Chilli & Spices", "Indian chilli, red chilli and selected spice varieties."),
    ("rice.jpg", "Rice & Grains", "Rice, grains and related agricultural commodities."),
    ("pulses.jpg", "Pulses", "Pulses and related food commodities for trade opportunities."),
    ("commodities.jpg", "Agricultural Commodities", "Broader commodity sourcing aligned to buyer requirements."),
    ("processed.jpg", "Processed Food Products", "Selected processed food opportunities subject to demand and feasibility."),
    ("custom.jpg", "Custom Sourcing", "Tailored sourcing for specific product, quantity and destination needs."),
]

ABOUT = page_header("About Us", "About Us") + f"""
    <div class="container-fluid overflow-hidden py-5 px-lg-0">
        <div class="container about py-5 px-lg-0">
            <div class="row g-5 mx-lg-0">
                <div class="col-lg-6 ps-lg-0" style="min-height: 400px;">
                    <div class="position-relative h-100">
                        <img class="position-absolute img-fluid w-100 h-100" src="img/about.jpg" style="object-fit: cover;" alt="About {COMPANY}" loading="lazy">
                    </div>
                </div>
                <div class="col-lg-6 about-text">
                    <h6 class="text-secondary text-uppercase mb-3">Who we are</h6>
                    <h2 class="mb-4">{COMPANY}</h2>
                    <p class="mb-4">{COMPANY} is an India-based trading company connecting Indian producers, global buyers and international suppliers. We focus on agricultural and food products, with responsible sourcing and clear communication.</p>
                    <p class="mb-4 fw-medium">Source responsibly. Trade transparently. Deliver reliably.</p>
                    <p class="mb-4">See <a href="exports.html">exports from India</a>, <a href="imports.html">imports to India</a>, and <a href="markets.html">target markets</a>.</p>
                    <a href="contact.html" class="btn btn-primary py-3 px-5">Get in Touch</a>
                </div>
            </div>
        </div>
    </div>
    <div class="container-xxl py-5 bg-light">
        <div class="container">
            <div class="row g-4">
                <div class="col-md-4"><div class="why-item h-100"><h5 class="mb-3">Focus</h5><p class="mb-0">Import and export trading in agricultural and food products, with professional trade coordination.</p></div></div>
                <div class="col-md-4"><div class="why-item h-100"><h5 class="mb-3">Approach</h5><p class="mb-0">Understand the requirement, identify suitable products and suppliers, then support delivery through trusted partners.</p></div></div>
                <div class="col-md-4"><div class="why-item h-100"><h5 class="mb-3">Commitment</h5><p class="mb-0">Clear communication and realistic expectations — without exaggerated claims.</p></div></div>
            </div>
        </div>
    </div>
    <div class="container-xxl py-5">
        <div class="container text-center">
            <h3 class="mb-3">Ready to discuss a requirement?</h3>
            <p class="mb-4">Share the product, quantity and destination and our team will respond.</p>
            <a href="quote.html" class="btn btn-primary py-3 px-5">Request a Quote</a>
        </div>
    </div>
"""

EXPORTS = page_header("Exports", "Exports", "img/export-hero.jpg") + f"""
    <div class="container-xxl py-5">
        <div class="container py-5">
            <div class="mx-auto mb-5" style="max-width: 760px;">
                <h6 class="text-secondary text-uppercase mb-3">Export from India</h6>
                <h2 class="mb-3">Agricultural products for overseas buyers</h2>
                <p class="mb-0">{COMPANY} connects Indian fruits, vegetables, spices, grains and related food products with international markets. Availability depends on seasonality, quality, quantity and destination.</p>
            </div>
            <div class="row g-4">
                <div class="col-md-6 col-lg-4"><a class="product-card" href="{product_href('Fresh Fruits')}"><div class="product-img"><img src="img/products/fruits.jpg" alt="Fresh Fruits" loading="lazy"></div><div class="p-4"><h4>Fresh Fruits</h4><p>Papaya, mango, banana, grapes, pomegranate and other seasonal fruits.</p><span class="enquire-link">Enquire</span></div></a></div>
                <div class="col-md-6 col-lg-4"><a class="product-card" href="{product_href('Fresh Vegetables')}"><div class="product-img"><img src="img/products/vegetables.jpg" alt="Fresh Vegetables" loading="lazy"></div><div class="p-4"><h4>Fresh Vegetables</h4><p>Onion, potato and other vegetables based on buyer requirements.</p><span class="enquire-link">Enquire</span></div></a></div>
                <div class="col-md-6 col-lg-4"><a class="product-card" href="{product_href('Chilli & Spices')}"><div class="product-img"><img src="img/products/chilli.jpg" alt="Chilli and Spices" loading="lazy"></div><div class="p-4"><h4>Chilli &amp; Spices</h4><p>Indian chilli, red chilli and selected spices for global buyers.</p><span class="enquire-link">Enquire</span></div></a></div>
                <div class="col-md-6 col-lg-4"><a class="product-card" href="{product_href('Grains & Pulses')}"><div class="product-img"><img src="img/products/rice.jpg" alt="Grains and Pulses" loading="lazy"></div><div class="p-4"><h4>Grains &amp; Pulses</h4><p>Rice, pulses, grains and other agricultural commodities.</p><span class="enquire-link">Enquire</span></div></a></div>
                <div class="col-md-6 col-lg-4"><a class="product-card" href="{product_href('Custom Sourcing')}"><div class="product-img"><img src="img/products/custom.jpg" alt="Custom Sourcing" loading="lazy"></div><div class="p-4"><h4>Custom Sourcing</h4><p>Products sourced according to specific buyer requirements.</p><span class="enquire-link">Enquire</span></div></a></div>
                <div class="col-md-6 col-lg-4"><div class="cta-tile"><h4 class="text-white mb-3">Share your requirement</h4><p class="text-white">Tell us the product, quantity, quality preference and destination.</p><a href="quote.html?type=Export%20from%20India" class="btn btn-secondary py-2 px-4">Request a Quote</a></div></div>
            </div>
        </div>
    </div>
"""

IMPORTS = page_header("Imports", "Imports", "img/import-hero.jpg") + f"""
    <div class="container-xxl py-5">
        <div class="container py-5">
            <div class="mx-auto mb-5" style="max-width: 760px;">
                <h6 class="text-secondary text-uppercase mb-3">Import to India</h6>
                <h2 class="mb-3">Selected opportunities for the Indian market</h2>
                <p class="mb-0">Alongside exports, {COMPANY} reviews international products that may fit Indian demand — based on quality, supplier reliability and commercial viability.</p>
            </div>
            <div class="row g-4">
                <div class="col-md-4"><div class="why-item h-100"><i class="fa fa-globe fa-lg text-primary mb-3"></i><h5 class="mb-3">Supplier sourcing</h5><p class="mb-0">Identifying and engaging with potential overseas suppliers.</p></div></div>
                <div class="col-md-4"><div class="why-item h-100"><i class="fa fa-calculator fa-lg text-primary mb-3"></i><h5 class="mb-3">Commercial evaluation</h5><p class="mb-0">Assessing viability before progressing trade discussions.</p></div></div>
                <div class="col-md-4"><div class="why-item h-100"><i class="fa fa-clipboard-list fa-lg text-primary mb-3"></i><h5 class="mb-3">Import coordination</h5><p class="mb-0">Supporting documentation and related trade steps with partners.</p></div></div>
            </div>
            <div class="text-center mt-5">
                <h4 class="mb-3">Have a product to import into India?</h4>
                <p class="mb-4">Share the details and we will review the opportunity together.</p>
                <a href="quote.html?type=Import%20to%20India" class="btn btn-primary py-3 px-5">Discuss Your Requirement</a>
            </div>
        </div>
    </div>
"""

PRODUCTS = page_header("Products", "Products", "img/products/fruits.jpg") + """
    <div class="container-xxl py-5">
        <div class="container py-5">
            <div class="mx-auto mb-5" style="max-width:720px;">
                <h6 class="text-secondary text-uppercase">Product categories</h6>
                <h2 class="mb-3">Agricultural and food products</h2>
                <p class="mb-0">We source according to buyer requirements and market demand. Specifications are confirmed on enquiry.</p>
            </div>
            <div class="row g-4">
"""
for img, title, desc in PRODUCT_CARDS:
    PRODUCTS += f"""
                <div class="col-md-6 col-lg-3">
                    <a class="product-card" href="{product_href(title)}">
                        <div class="product-img"><img src="img/products/{img}" alt="{title}" loading="lazy"></div>
                        <div class="p-4"><h5 class="mb-2">{title}</h5><p>{desc}</p><span class="enquire-link">Enquire</span></div>
                    </a>
                </div>"""
PRODUCTS += """
            </div>
            <div class="enquiry-band mt-5 text-center">
                <h3 class="mb-3">Need a specific commodity?</h3>
                <p class="mb-4">Share the product, quantity and destination and we will explore sourcing options.</p>
                <a href="quote.html" class="btn btn-primary py-3 px-5">Request a Quote</a>
            </div>
        </div>
    </div>
"""

SERVICES = page_header("Services", "Services", "img/carousel-2.jpg") + f"""
    <div class="container-xxl py-5">
        <div class="container py-5">
            <div class="mx-auto mb-5" style="max-width:760px;">
                <h6 class="text-secondary text-uppercase">Services</h6>
                <h2 class="mb-3">International trading support</h2>
                <p>{COMPANY} supports trade through sourcing and coordination. Freight and certification are handled with external partners when required.</p>
                <p class="mb-0">Commercial terms such as FOB or CIF can be discussed on enquiry. We coordinate documentation with logistics partners rather than operating freight ourselves.</p>
            </div>
            <div class="row g-4">
"""
for icon, title, desc in [
    ("fa-search-location", "Global sourcing", "Identifying suitable products and reliable suppliers according to buyer requirements."),
    ("fa-exchange-alt", "Import and export", "Supporting trade discussions between India and overseas markets."),
    ("fa-seedling", "Agricultural sourcing", "Connecting buyers with suitable agricultural products from Indian markets."),
    ("fa-people-carry", "Supplier coordination", "Working with suppliers and producers on availability and commercial requirements."),
    ("fa-file-alt", "Documentation coordination", "Supporting product information and trade-related paperwork."),
    ("fa-shipping-fast", "Logistics coordination", "Coordinating transportation and shipment with logistics partners."),
]:
    SERVICES += f"""
                <div class="col-md-6 col-lg-4">
                    <div class="why-item h-100">
                        <i class="fa {icon} fa-lg text-primary mb-3"></i>
                        <h5 class="mb-3">{title}</h5>
                        <p class="mb-3">{desc}</p>
                        <a class="enquire-link" href="contact.html">Enquire</a>
                    </div>
                </div>"""
SERVICES += """
            </div>
        </div>
    </div>
"""

MARKETS = page_header("Markets", "Markets", "img/markets.jpg") + f"""
    <div class="container-xxl py-5">
        <div class="container py-5">
            <div class="row g-5">
                <div class="col-lg-7">
                    <h6 class="text-secondary text-uppercase mb-3">Target markets</h6>
                    <h2 class="mb-4">Regions we are building conversations in</h2>
                    <p class="mb-4">{COMPANY} connects Indian agricultural products with overseas buyers and explores selected import opportunities into India. These are target markets — not a claim of current shipment volume.</p>
                    <div class="market-list">
                        <div class="market-row"><h5>Middle East</h5><p>A priority region for agricultural and food trade discussions.</p></div>
                        <div class="market-row"><h5>Africa</h5><p>Opportunities aligned with demand for Indian agricultural products.</p></div>
                        <div class="market-row"><h5>Southeast Asia</h5><p>Markets with food and commodity trade potential.</p></div>
                        <div class="market-row"><h5>Europe</h5><p>Conversations around quality-focused agricultural sourcing.</p></div>
                    </div>
                    <p class="mt-4 mb-0">We also review other regions when product fit, buyer interest and commercial terms align.</p>
                </div>
                <div class="col-lg-5">
                    <div class="enquiry-panel h-100">
                        <h4 class="mb-3">Discuss a destination</h4>
                        <p class="mb-4">Share the product and market you have in mind. We will review suitability together.</p>
                        <a href="quote.html" class="btn btn-primary py-3 px-4">Request a Quote</a>
                    </div>
                </div>
            </div>
        </div>
    </div>
"""

CONTACT = page_header("Contact", "Contact", "img/cta-bg.jpg") + f"""
    <div class="container-xxl py-5">
        <div class="container py-5">
            <div class="row g-5">
                <div class="col-lg-6">
                    <h6 class="text-secondary text-uppercase">Business enquiry</h6>
                    <h2 class="mb-4">Tell us what you need</h2>
                    <p class="mb-4">Share your details for an export, import or supplier discussion. You can also reach us on WhatsApp.</p>
                    <div class="enquiry-panel">
{ENQUIRY_FORM}
                    </div>
                </div>
                <div class="col-lg-6">
                    <div class="contact-aside text-white h-100">
                        <h4 class="text-white mb-4">Contact Information</h4>
                        <p class="mb-3"><i class="fa fa-building me-3"></i><strong>{COMPANY}</strong></p>
                        <p class="mb-4"><i class="fa fa-map-marker-alt me-3"></i>{ADDRESS}</p>
                        <p class="mb-3"><i class="fa fa-phone-alt me-3"></i><a class="text-white" href="tel:{PHONE_TEL}">{PHONE}</a></p>
                        <p class="mb-3"><i class="fab fa-whatsapp me-3"></i><a class="text-white" href="{WHATSAPP}" target="_blank" rel="noopener">Chat on WhatsApp</a></p>
                        <p class="mb-4"><i class="fa fa-envelope me-3"></i><a class="text-white" href="mailto:{EMAIL}">{EMAIL}</a></p>
                        <hr class="border-light">
                        <h5 class="text-white mb-3">Office Location</h5>
                        <p class="mb-3">{ADDRESS}</p>
                        <div class="ratio ratio-4x3 bg-white mb-3">
                            <iframe src="{MAP_EMBED}" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade" title="{COMPANY} office, Plot No. 188, CA Road, Garoba Maidan, Nagpur"></iframe>
                        </div>
                        <a class="btn btn-secondary py-2 px-4" href="{MAP_LINK}" target="_blank" rel="noopener">Open in Google Maps</a>
                    </div>
                </div>
            </div>
        </div>
    </div>
"""

QUOTE = page_header("Request a Quote", "Request a Quote", "img/carousel-2.jpg") + f"""
    <div class="container-xxl py-5">
        <div class="container py-5">
            <div class="row g-5 align-items-start">
                <div class="col-lg-5">
                    <h6 class="text-secondary text-uppercase mb-3">Get a quote</h6>
                    <h2 class="mb-4">Share your trade requirement</h2>
                    <p class="mb-4">Provide product, quantity and destination or origin details. We will review the enquiry and explore suitable sourcing options.</p>
                    <p class="mb-4">Commercial terms such as FOB or CIF can be discussed once we understand the product, quantity and destination. Freight and documentation are coordinated with logistics partners.</p>
                    <div class="contact-mini">
                        <i class="fa fa-phone-alt"></i>
                        <div><span>Call</span><a href="tel:{PHONE_TEL}">{PHONE}</a></div>
                    </div>
                    <div class="contact-mini">
                        <i class="fab fa-whatsapp"></i>
                        <div><span>WhatsApp</span><a href="{WHATSAPP}" target="_blank" rel="noopener">Message us</a></div>
                    </div>
                    <div class="contact-mini">
                        <i class="fa fa-envelope"></i>
                        <div><span>Email</span><a href="mailto:{EMAIL}">{EMAIL}</a></div>
                    </div>
                </div>
                <div class="col-lg-7">
                    <div class="enquiry-panel">
{ENQUIRY_FORM}
                    </div>
                </div>
            </div>
        </div>
    </div>
"""

PRIVACY = page_header("Privacy Policy", "Privacy Policy") + f"""
    <div class="container-xxl pb-5">
        <div class="container pb-5" style="max-width: 820px;">
            <h2 class="mb-4">How we handle enquiries</h2>
            <p class="mb-4">This page explains how {COMPANY} uses information you send through this website. We do not sell personal information.</p>
            <h4 class="mb-3">What we collect</h4>
            <p class="mb-4">When you submit the business enquiry form, we receive the details you enter — typically name, company, email, phone, country, enquiry type, product, quantity, destination or origin, and your message. If you contact us by phone, WhatsApp or email, we also receive the information you choose to share in that conversation.</p>
            <h4 class="mb-3">Website assistant</h4>
            <p class="mb-4">The “Ask us” assistant on this website answers from published company information in your browser. It does not send your typed questions to us unless you continue on WhatsApp, email, phone or the enquiry form.</p>
            <h4 class="mb-3">How we use it</h4>
            <p class="mb-4">We use enquiry details only to understand your requirement and respond. Form submissions are processed by our website host (Netlify Forms) and then reviewed by our team.</p>
            <h4 class="mb-3">How long we keep it</h4>
            <p class="mb-4">We keep enquiry records for as long as they are useful for ongoing trade discussions, then delete them when they are no longer needed.</p>
            <h4 class="mb-3">Contact</h4>
            <p class="mb-0">For a privacy question or a request about your enquiry data, email <a href="mailto:{EMAIL}">{EMAIL}</a> or write to {COMPANY}, {ADDRESS}.</p>
        </div>
    </div>
"""

THANK_YOU = page_header("Thank You", "Thank You") + f"""
    <div class="container-xxl pb-5">
        <div class="container text-center py-4">
            <div class="row justify-content-center">
                <div class="col-lg-7">
                    <i class="fa fa-check-circle text-primary mb-4" style="font-size: 3.5rem;"></i>
                    <h2 class="mb-4">Thank you for your enquiry</h2>
                    <p class="mb-4">We have received your message. Our team will review your requirement and get back to you.</p>
                    <a class="btn btn-primary py-3 px-5 me-2 mb-2" href="index.html">Back to Home</a>
                    <a class="btn btn-whatsapp py-3 px-5 mb-2" href="{WHATSAPP}" target="_blank" rel="noopener"><i class="fab fa-whatsapp me-2"></i>WhatsApp</a>
                </div>
            </div>
        </div>
    </div>
"""

NOT_FOUND = page_header("Page Not Found", "404") + f"""
    <div class="container-xxl pb-5">
        <div class="container text-center py-4">
            <div class="row justify-content-center">
                <div class="col-lg-6">
                    <p class="text-primary fw-bold mb-2">404</p>
                    <h2 class="mb-4">Page not found</h2>
                    <p class="mb-4">The page you are looking for may have been moved. Return to the homepage to continue exploring {COMPANY}.</p>
                    <a class="btn btn-primary py-3 px-5" href="index.html">Go Back To Home</a>
                </div>
            </div>
        </div>
    </div>
"""

REDIRECT = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Redirecting — Global Route Company</title>
  <meta http-equiv="refresh" content="0; url={target}">
  <link rel="canonical" href="{target}">
</head>
<body>
  <p>This page has moved. <a href="{target}">Continue here</a>.</p>
</body>
</html>
"""

if __name__ == "__main__":
    write("index.html", f"{COMPANY} | Import & Export Trading Company", "home", INDEX)
    write(
        "about.html",
        f"About Us | {COMPANY}",
        "about",
        ABOUT,
        f"{COMPANY} is an India-based import and export trading company in Nagpur, focused on agricultural and food products.",
    )
    write(
        "exports.html",
        f"Exports from India | {COMPANY}",
        "exports",
        EXPORTS,
        f"Agricultural products {COMPANY} sources from India for international buyers. Availability and specifications are confirmed on enquiry.",
    )
    write(
        "imports.html",
        f"Imports to India | {COMPANY}",
        "imports",
        IMPORTS,
        f"{COMPANY} reviews selected international products for the Indian market based on demand, quality and commercial fit.",
    )
    write(
        "products.html",
        f"Products | {COMPANY}",
        "products",
        PRODUCTS,
        f"Agricultural and food categories sourced by {COMPANY}: fruits, vegetables, chilli, rice, pulses and custom sourcing.",
    )
    write(
        "service.html",
        f"Services | {COMPANY}",
        "services",
        SERVICES,
        f"{COMPANY} supports global sourcing, supplier coordination and documentation. Freight is coordinated with logistics partners.",
    )
    write(
        "markets.html",
        f"Markets | {COMPANY}",
        "markets",
        MARKETS,
        f"Target markets for {COMPANY} include the Middle East, Africa, Southeast Asia and Europe, subject to product fit and buyer interest.",
    )
    write(
        "contact.html",
        f"Contact | {COMPANY}",
        "contact",
        CONTACT,
        f"Contact {COMPANY} in Nagpur to discuss export, import or supplier requirements. Phone {PHONE}.",
    )
    write(
        "quote.html",
        f"Request a Quote | {COMPANY}",
        "contact",
        QUOTE,
        f"Request a quote from {COMPANY} for agricultural sourcing from India or selected imports into India.",
    )
    write(
        "privacy.html",
        f"Privacy Policy | {COMPANY}",
        "home",
        PRIVACY,
        f"How {COMPANY} uses enquiry information submitted through this website.",
    )
    write("thank-you.html", f"Thank You | {COMPANY}", "contact", THANK_YOU, noindex=True)
    write("404.html", f"Page Not Found | {COMPANY}", "home", NOT_FOUND, noindex=True)

    for old, target in [
        ("feature.html", "about.html"),
        ("price.html", "products.html"),
        ("team.html", "about.html"),
        ("testimonial.html", "about.html"),
    ]:
        (ROOT / old).write_text(REDIRECT.format(target=target), encoding="utf-8")
        print("redirect", old, "->", target)

    (ROOT / "READ-ME.txt").write_text(
        f"{COMPANY} Website\n"
        "Built on the Logistica HTML template structure.\n"
        "Static site — deploy via GitHub → Netlify.\n"
        "Forms use Netlify Forms (data-netlify). Set email notifications in the Netlify dashboard (not shown on the public site).\n",
        encoding="utf-8",
    )
    print("done")
