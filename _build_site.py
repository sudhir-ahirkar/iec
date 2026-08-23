#!/usr/bin/env python3
"""Generate Global Route Company website pages from the Logistica template."""
import json
from datetime import date
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parent

COMPANY = "Global Route Company"
BRAND_SHORT = "Global Route"
BRAND_ABBR = "GRoute"
TAGLINE = "Connecting India to Global Markets"
PHONE = "+91 9225159719"
PHONE_TEL = "+919225159719"
EMAIL = "lokeshghagare@gmail.com"
ADDRESS = "Plot No. 188, CA Road, Garoba Maidan, Nagpur, Maharashtra, India - 440008"
ADDRESS_LANDMARK = "Near Dalvi Hospital"
ADDRESS_FULL = f"{ADDRESS} ({ADDRESS_LANDMARK})"
MAP_LAT = "21.1473515"
MAP_LNG = "79.1214913"
MAP_EMBED = f"https://www.google.com/maps?q={MAP_LAT},{MAP_LNG}&z=17&hl=en&output=embed"
MAP_LINK = f"https://www.google.com/maps?q={MAP_LAT},{MAP_LNG}"
WHATSAPP = "https://wa.me/919225159719?text=Hello%20Global%20Route%20Company%2C%20I%20would%20like%20to%20enquire%20about%20sourcing%20from%20India."
SITE = "https://groute.co.in"
AVAILABILITY = (
    "Product availability depends on buyer requirements, seasonality, sourcing availability "
    "and applicable regulations."
)

# Pretty public paths. Filenames stay *.html so Netlify and local preview can serve them.
# Use U_* names so they are not overwritten by page-body variables.
HOME = "/"
U_ABOUT, U_EXPORTS, U_IMPORTS = "/about", "/exports", "/imports"
U_PRODUCTS, U_SERVICES, U_MARKETS = "/products", "/services", "/markets"
U_CONTACT, U_QUOTE, U_PRIVACY, U_THANK_YOU = "/contact", "/quote", "/privacy", "/thank-you"

CANONICAL = {
    "index.html": HOME,
    "about.html": U_ABOUT,
    "exports.html": U_EXPORTS,
    "imports.html": U_IMPORTS,
    "products.html": U_PRODUCTS,
    "service.html": U_SERVICES,
    "markets.html": U_MARKETS,
    "contact.html": U_CONTACT,
    "quote.html": U_QUOTE,
    "privacy.html": U_PRIVACY,
    "thank-you.html": U_THANK_YOU,
}

# Future product detail pages and blog posts — add entries only when real content exists.
PRODUCT_DETAIL_PAGES = []
BLOG_POSTS = []

SEO_DESC = (
    "Global Route Company is an India-based import and export trading company connecting "
    "agricultural products, trusted suppliers and global buyers through reliable sourcing and "
    "international trade solutions."
)
OG_HOME_DESC = (
    "Connecting Indian agricultural products with global markets through reliable sourcing "
    "and international trade."
)


def absolute(path: str) -> str:
    return f"{SITE}/" if path == "/" else SITE + path


ORG_SCHEMA = json.dumps(
    {
        "@context": "https://schema.org",
        "@type": "Organization",
        "@id": f"{SITE}/#organization",
        "name": COMPANY,
        "alternateName": [BRAND_SHORT, BRAND_ABBR, "groute.co.in"],
        "url": f"{SITE}/",
        "logo": f"{SITE}/img/logo.svg",
        "image": f"{SITE}/img/og.jpg",
        "email": EMAIL,
        "telephone": PHONE,
        "description": SEO_DESC,
        "address": {
            "@type": "PostalAddress",
            "streetAddress": "Plot No. 188, CA Road, Garoba Maidan (Near Dalvi Hospital)",
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
        "areaServed": {"@type": "Country", "name": "India"},
    },
    ensure_ascii=False,
)

WEBSITE_SCHEMA = json.dumps(
    {
        "@context": "https://schema.org",
        "@type": "WebSite",
        "name": COMPANY,
        "alternateName": [BRAND_SHORT, BRAND_ABBR, "groute.co.in"],
        "url": f"{SITE}/",
        "inLanguage": "en-IN",
        "publisher": {"@id": f"{SITE}/#organization"},
    },
    ensure_ascii=False,
)


def breadcrumb_schema(crumbs: list[tuple[str, str | None]]) -> str:
    items = []
    for index, (name, path) in enumerate(crumbs, start=1):
        entry = {"@type": "ListItem", "position": index, "name": name}
        if path:
            entry["item"] = absolute(path)
        items.append(entry)
    return json.dumps(
        {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": items},
        ensure_ascii=False,
    )


def head(
    title: str,
    description: str,
    page: str,
    noindex: bool = False,
    crumbs: list[tuple[str, str | None]] | None = None,
    og_description: str | None = None,
) -> str:
    path = CANONICAL.get(page, "/" if page == "index.html" else "/" + page.replace(".html", ""))
    url = absolute(path)
    robots = "noindex, follow" if noindex else "index, follow"
    og_desc = og_description or description
    trail = crumbs or [("Home", HOME), (title.split(" | ")[0], None)]
    crumbs_json = breadcrumb_schema(trail)
    return f"""<!DOCTYPE html>
<html lang="en-IN">

<head>
    <meta charset="utf-8">
    <title>{title}</title>
    <meta content="width=device-width, initial-scale=1.0" name="viewport">
    <meta name="robots" content="{robots}">
    <meta name="description" content="{description}">
    <meta name="author" content="{COMPANY}">
    <meta name="theme-color" content="#1A5F4A">
    <link rel="canonical" href="{url}">
    <meta property="og:type" content="website">
    <meta property="og:site_name" content="{COMPANY}">
    <meta property="og:title" content="{title}">
    <meta property="og:description" content="{og_desc}">
    <meta property="og:url" content="{url}">
    <meta property="og:image" content="{SITE}/img/og.jpg">
    <meta property="og:image:alt" content="{COMPANY} — import and export trading from India">
    <meta property="og:locale" content="en_IN">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{title}">
    <meta name="twitter:description" content="{og_desc}">
    <meta name="twitter:image" content="{SITE}/img/og.jpg">
    <link href="/img/favicon.svg?v=2" rel="icon" type="image/svg+xml">
    <link href="/img/favicon-32.png?v=2" rel="icon" type="image/png" sizes="32x32">
    <link href="/img/apple-touch-icon.png?v=2" rel="apple-touch-icon">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.10.0/css/all.min.css" rel="stylesheet">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.4.1/font/bootstrap-icons.css" rel="stylesheet">
    <link href="/css/bootstrap.min.css" rel="stylesheet">
    <link href="/css/style.css" rel="stylesheet">
    <style>body{{font-family:"Plus Jakarta Sans",sans-serif;}} h1,h2,h3,h4,h5{{font-weight:700;}}</style>
    <script type="application/ld+json">{ORG_SCHEMA}</script>
    <script type="application/ld+json">{WEBSITE_SCHEMA}</script>
    <script type="application/ld+json">{crumbs_json}</script>
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
        <a href="{HOME}" class="navbar-brand navbar-brand-logo" aria-label="{COMPANY}">
            <img src="/img/logo.svg?v=3" alt="{COMPANY}" width="280" height="52">
        </a>
        <button type="button" class="navbar-toggler me-4" data-bs-toggle="collapse" data-bs-target="#navbarCollapse" aria-controls="navbarCollapse" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarCollapse">
            <div class="navbar-nav ms-auto p-4 p-lg-0">
                <a href="{HOME}" class="{c('home')}">Home</a>
                <a href="{U_ABOUT}" class="{c('about')}">About Us</a>
                <a href="{U_PRODUCTS}" class="{c('products')}">Products</a>
                <a href="{U_SERVICES}" class="{c('services')}">Services</a>
                <a href="{U_CONTACT}" class="{c('contact')}">Contact</a>
                <a href="{U_QUOTE}" class="nav-item nav-link d-lg-none">Request a Quote</a>
                <a href="{WHATSAPP}" class="nav-item nav-link d-lg-none" target="_blank" rel="noopener">WhatsApp</a>
            </div>
            <div class="navbar-actions d-none d-lg-flex align-items-center pe-lg-4">
                <a href="{U_QUOTE}" class="btn btn-primary py-2 px-3 me-2">Request a Quote</a>
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
                    <a href="{HOME}" class="footer-logo-link" aria-label="{COMPANY}"><img src="/img/logo-white.svg?v=3" alt="{COMPANY}" class="footer-logo" width="280" height="52"></a>
                    <p class="footer-tagline">{TAGLINE}</p>
                    <p class="mb-2"><i class="fa fa-map-marker-alt me-3"></i>{ADDRESS_FULL}</p>
                    <p class="mb-2"><i class="fa fa-phone-alt me-3"></i><a class="text-light" href="tel:{PHONE_TEL}">{PHONE}</a> <span class="text-white-50">(IST)</span></p>
                    <p class="mb-2"><i class="fab fa-whatsapp me-3"></i><a class="text-light" href="{WHATSAPP}" target="_blank" rel="noopener">WhatsApp</a></p>
                    <p class="mb-2"><i class="fa fa-envelope me-3"></i><a class="text-light" href="mailto:{EMAIL}">{EMAIL}</a></p>
                </div>
                <div class="col-lg-2 col-md-6">
                    <h4 class="text-light mb-4">Quick Links</h4>
                    <a class="btn btn-link" href="{HOME}">Home</a>
                    <a class="btn btn-link" href="{U_ABOUT}">About {COMPANY}</a>
                    <a class="btn btn-link" href="{U_EXPORTS}">Agricultural export from India</a>
                    <a class="btn btn-link" href="{U_IMPORTS}">Import to India</a>
                    <a class="btn btn-link" href="{U_PRODUCTS}">Agricultural products</a>
                    <a class="btn btn-link" href="{U_SERVICES}">Global sourcing services</a>
                    <a class="btn btn-link" href="{U_CONTACT}">Contact {COMPANY}</a>
                    <a class="btn btn-link" href="{U_PRIVACY}">Privacy Policy</a>
                </div>
                <div class="col-lg-3 col-md-6">
                    <h4 class="text-light mb-4">What We Do</h4>
                    <a class="btn btn-link" href="{U_EXPORTS}">Export from India</a>
                    <a class="btn btn-link" href="{U_IMPORTS}">Import to India</a>
                    <a class="btn btn-link" href="{U_PRODUCTS}">Agricultural products</a>
                    <a class="btn btn-link" href="{U_SERVICES}">Global sourcing</a>
                    <a class="btn btn-link" href="{U_MARKETS}">Target markets</a>
                    <a class="btn btn-link" href="{U_QUOTE}">Request an export quotation</a>
                </div>
                <div class="col-lg-3 col-md-6">
                    <h4 class="text-light mb-4">Start a Conversation</h4>
                    <p>Tell us what you are looking for and our team will explore suitable sourcing opportunities.</p>
                    <a href="{U_QUOTE}" class="btn btn-primary py-2 px-4 mt-2">Request a Quote</a>
                    <a href="{WHATSAPP}" class="btn btn-whatsapp py-2 px-4 mt-2" target="_blank" rel="noopener">WhatsApp</a>
                </div>
            </div>
        </div>
        <div class="container">
            <div class="copyright">
                <div class="row">
                    <div class="col-md-12 text-center mb-3 mb-md-0">
                        &copy; 2026 {COMPANY}. All Rights Reserved. · <a class="border-bottom" href="{U_PRIVACY}">Privacy Policy</a>
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
    <script src="/js/main.js"></script>
    <script src="/js/chat.js"></script>
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
                    <li class="breadcrumb-item"><a href="{HOME}">Home</a></li>
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
                    <li class="breadcrumb-item"><a class="text-white" href="{HOME}">Home</a></li>
                    <li class="breadcrumb-item text-white-50 active" aria-current="page">{crumb}</li>
                </ol>
            </nav>
        </div>
    </div>
"""


def product_href(name: str, enquiry: str = "Export from India") -> str:
    href = f"{U_QUOTE}?product={quote(name)}"
    if enquiry:
        href += f"&type={quote(enquiry)}"
    return href


ENQUIRY_FORM = """
                    <form name="business-enquiry" method="POST" action="/thank-you" data-netlify="true" netlify-honeypot="bot-field">
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


def write(
    name: str,
    title: str,
    active: str,
    body: str,
    description: str = None,
    noindex: bool = False,
    crumbs: list[tuple[str, str | None]] | None = None,
    og_description: str | None = None,
):
    html = (
        head(title, description or SEO_DESC, name, noindex, crumbs, og_description)
        + nav(active)
        + '<main id="main">\n'
        + body
        + "</main>\n"
        + FOOTER
    )
    (ROOT / name).write_text(html, encoding="utf-8")
    print("wrote", name)


# ---- Page bodies ----

INDEX = f"""
    <form name="business-enquiry" method="POST" action="/thank-you" data-netlify="true" netlify-honeypot="bot-field" class="d-none" aria-hidden="true" tabindex="-1">
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
        <img src="/img/carousel-1.jpg" alt="Agricultural fields in India used for export sourcing" width="1920" height="1080" loading="eager" fetchpriority="high">
        <div class="hero-overlay">
            <div class="container">
                <div class="row justify-content-start">
                    <div class="col-11 col-lg-7">
                        <p class="hero-kicker">Import &amp; export · Agricultural trade · India</p>
                        <h1 class="hero-title">Connecting India to <span>Global Markets</span></h1>
                        <p class="hero-lead">{COMPANY} is an India-based import and export trading company. We source agricultural products from India for international buyers and review selected import and global sourcing opportunities into India.</p>
                        <a href="{U_QUOTE}" class="btn btn-primary py-3 px-4 me-3">Request a Quote</a>
                        <a href="{U_PRODUCTS}" class="btn btn-outline-light py-3 px-4">Explore agricultural products</a>
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
                <p class="mb-0">Buyers can source fruits, vegetables, chilli, spices, rice, grains and related food products through {COMPANY}. {AVAILABILITY} See our <a href="{U_EXPORTS}">agricultural export from India</a> page or <a href="{U_PRODUCTS}">agricultural products</a>.</p>
            </div>
            <div class="row g-4">
                <div class="col-md-6 col-lg-3">
                    <a class="product-card" href="{product_href('Fresh Fruits')}">
                        <div class="product-img"><img src="/img/products/fruits.jpg" alt="Fresh Indian fruits for export, including papaya and mango" width="640" height="400" loading="lazy"></div>
                        <div class="p-4"><h4>Fresh Fruits</h4><p>Papaya, mango, banana, grapes, pomegranate and other seasonal fruits.</p><span class="enquire-link">Enquire</span></div>
                    </a>
                </div>
                <div class="col-md-6 col-lg-3">
                    <a class="product-card" href="{product_href('Fresh Vegetables')}">
                        <div class="product-img"><img src="/img/products/vegetables.jpg" alt="Fresh Indian vegetables including onion and potato" width="640" height="400" loading="lazy"></div>
                        <div class="p-4"><h4>Fresh Vegetables</h4><p>Onion, potato and other vegetables based on buyer specifications.</p><span class="enquire-link">Enquire</span></div>
                    </a>
                </div>
                <div class="col-md-6 col-lg-3">
                    <a class="product-card" href="{product_href('Chilli & Spices')}">
                        <div class="product-img"><img src="/img/products/chilli.jpg" alt="Fresh Indian red chilli for export" width="640" height="400" loading="lazy"></div>
                        <div class="p-4"><h4>Chilli &amp; Spices</h4><p>Indian chilli, red chilli and selected spices for food and commodity buyers.</p><span class="enquire-link">Enquire</span></div>
                    </a>
                </div>
                <div class="col-md-6 col-lg-3">
                    <a class="product-card" href="{product_href('Grains & Pulses')}">
                        <div class="product-img"><img src="/img/products/rice.jpg" alt="Indian rice and grains for commodity trade" width="640" height="400" loading="lazy"></div>
                        <div class="p-4"><h4>Grains &amp; Pulses</h4><p>Rice, pulses, grains and other agricultural commodities for export markets.</p><span class="enquire-link">Enquire</span></div>
                    </a>
                </div>
            </div>
            <div class="text-center mt-5">
                <a href="{U_PRODUCTS}" class="btn btn-primary py-3 px-5">Explore our agricultural export products</a>
            </div>
        </div>
    </div>

    <div class="container-fluid overflow-hidden py-5 px-lg-0 bg-light">
        <div class="container feature py-5 px-lg-0">
            <div class="row g-5 mx-lg-0">
                <div class="col-lg-6 feature-text wow fadeInUp" data-wow-delay="0.1s">
                    <h6 class="text-secondary text-uppercase mb-3">Import to India</h6>
                    <h2 class="mb-4">Import and global sourcing into India</h2>
                    <p class="mb-4">Alongside agricultural product export from India, {COMPANY} reviews international sourcing opportunities for the Indian market — based on demand, quality, supplier reliability and commercial viability.</p>
                    <a href="{U_IMPORTS}" class="btn btn-primary py-3 px-5">Discuss an import opportunity</a>
                </div>
                <div class="col-lg-6 pe-lg-0" style="min-height: 360px;">
                    <div class="position-relative h-100">
                        <img class="position-absolute img-fluid w-100 h-100" src="/img/import-hero.jpg" style="object-fit: cover;" alt="Global sourcing discussion for import into India" width="900" height="600" loading="lazy">
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
                        <a href="{U_QUOTE}" class="btn btn-primary py-3 px-4 me-2">Request an export quotation</a>
                        <a href="{U_CONTACT}" class="btn btn-outline-light py-3 px-4">Contact {COMPANY}</a>
                    </div>
                </div>
                <div class="col-lg-6">
                    <div class="cta-card text-white">
                        <h3 class="text-white mb-3">Have a product to import into India?</h3>
                        <p class="mb-4">Share the opportunity and we will review commercial fit together.</p>
                        <a href="{U_QUOTE}?type=Import%20to%20India" class="btn btn-secondary py-3 px-4">Discuss an import opportunity</a>
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

ABOUT = page_header("About Global Route Company", "About Us") + f"""
    <div class="container-fluid overflow-hidden py-5 px-lg-0">
        <div class="container about py-5 px-lg-0">
            <div class="row g-5 mx-lg-0">
                <div class="col-lg-6 ps-lg-0" style="min-height: 400px;">
                    <div class="position-relative h-100">
                        <img class="position-absolute img-fluid w-100 h-100" src="/img/about.jpg" style="object-fit: cover;" alt="Global Route Company agricultural trade discussion" width="900" height="600" loading="lazy">
                    </div>
                </div>
                <div class="col-lg-6 about-text">
                    <h6 class="text-secondary text-uppercase mb-3">Who we are</h6>
                    <h2 class="mb-4">An international trading company based in India</h2>
                    <p class="mb-4">{COMPANY} — also referred to as {BRAND_SHORT} or {BRAND_ABBR} — is an India-based import and export trading company. From our office in Nagpur, Maharashtra, we connect Indian producers, global buyers and international suppliers.</p>
                    <p class="mb-4">The work focuses on agricultural and food products: sourcing from India for overseas buyers, and reviewing selected import opportunities into India. We do not operate freight or customs ourselves; those steps are coordinated with logistics partners when a trade moves forward.</p>
                    <p class="mb-4 fw-medium">Source responsibly. Trade transparently. Deliver reliably.</p>
                    <p class="mb-4">Explore <a href="{U_EXPORTS}">agricultural product export from India</a>, <a href="{U_IMPORTS}">import and global sourcing into India</a>, and <a href="{U_MARKETS}">Indian agricultural products for global markets</a>.</p>
                    <a href="{U_CONTACT}" class="btn btn-primary py-3 px-5">Contact {COMPANY}</a>
                </div>
            </div>
        </div>
    </div>
    <div class="container-xxl py-5 bg-light">
        <div class="container">
            <div class="row g-4">
                <div class="col-md-4"><div class="why-item h-100"><h2 class="h5 mb-3">Focus</h2><p class="mb-0">Import and export trading in agricultural and food products, with professional trade coordination from Nagpur.</p></div></div>
                <div class="col-md-4"><div class="why-item h-100"><h2 class="h5 mb-3">Approach</h2><p class="mb-0">Understand the requirement, identify suitable products and suppliers, then support delivery through trusted partners.</p></div></div>
                <div class="col-md-4"><div class="why-item h-100"><h2 class="h5 mb-3">Commitment</h2><p class="mb-0">Clear communication and realistic expectations — without exaggerated claims.</p></div></div>
            </div>
        </div>
    </div>
    <div class="container-xxl py-5">
        <div class="container text-center">
            <h2 class="h3 mb-3">Ready to discuss a requirement?</h2>
            <p class="mb-4">Share the product, quantity and destination and the {COMPANY} team will respond.</p>
            <a href="{U_QUOTE}" class="btn btn-primary py-3 px-5">Request an export quotation</a>
        </div>
    </div>
"""

EXPORTS = page_header("Agricultural Product Export from India", "Exports", "/img/export-hero.jpg") + f"""
    <div class="container-xxl py-5">
        <div class="container py-5">
            <div class="mx-auto mb-5" style="max-width: 760px;">
                <p class="mb-3">{COMPANY} sources Indian agricultural products for international buyers — fruits, vegetables, chilli, spices, rice, grains, pulses and related food commodities. {AVAILABILITY} Specifications are confirmed on enquiry, not as a standing catalogue.</p>
                <p class="mb-0">Browse categories below, see the full <a href="{U_PRODUCTS}">agricultural products</a> list, or <a href="{U_QUOTE}?type=Export%20from%20India">request an export quotation</a>.</p>
            </div>
            <div class="row g-4">
                <div class="col-md-6 col-lg-4"><a class="product-card" href="{product_href('Fresh Fruits')}"><div class="product-img"><img src="/img/products/fruits.jpg" alt="Fresh papaya, mango and other Indian fruits for export" width="640" height="400" loading="lazy"></div><div class="p-4"><h2>Fresh Fruits</h2><p>Papaya, mango, banana, grapes, pomegranate and other seasonal fruits.</p><span class="enquire-link">Enquire</span></div></a></div>
                <div class="col-md-6 col-lg-4"><a class="product-card" href="{product_href('Fresh Vegetables')}"><div class="product-img"><img src="/img/products/vegetables.jpg" alt="Fresh Indian vegetables for export, including onion and potato" width="640" height="400" loading="lazy"></div><div class="p-4"><h2>Fresh Vegetables</h2><p>Onion, potato and other vegetables based on buyer requirements.</p><span class="enquire-link">Enquire</span></div></a></div>
                <div class="col-md-6 col-lg-4"><a class="product-card" href="{product_href('Chilli & Spices')}"><div class="product-img"><img src="/img/products/chilli.jpg" alt="Fresh Indian red chilli for export" width="640" height="400" loading="lazy"></div><div class="p-4"><h2>Chilli &amp; Spices</h2><p>Indian chilli, red chilli and selected spices for global buyers.</p><span class="enquire-link">Enquire</span></div></a></div>
                <div class="col-md-6 col-lg-4"><a class="product-card" href="{product_href('Rice, Grains & Pulses')}"><div class="product-img"><img src="/img/products/rice.jpg" alt="Indian rice, grains and pulses for export" width="640" height="400" loading="lazy"></div><div class="p-4"><h2>Rice, Grains &amp; Pulses</h2><p>Rice, pulses, grains and other agricultural commodities.</p><span class="enquire-link">Enquire</span></div></a></div>
                <div class="col-md-6 col-lg-4"><a class="product-card" href="{product_href('Custom Agricultural Sourcing')}"><div class="product-img"><img src="/img/products/custom.jpg" alt="Custom agricultural sourcing discussion" width="640" height="400" loading="lazy"></div><div class="p-4"><h2>Custom Agricultural Sourcing</h2><p>Products sourced according to specific buyer requirements.</p><span class="enquire-link">Enquire</span></div></a></div>
                <div class="col-md-6 col-lg-4"><div class="cta-tile"><h2 class="h4 text-white mb-3">Share your requirement</h2><p class="text-white">Tell us the product, quantity, quality preference and destination.</p><a href="{U_QUOTE}?type=Export%20from%20India" class="btn btn-secondary py-2 px-4">Request an export quotation</a></div></div>
            </div>
        </div>
    </div>
"""

IMPORTS = page_header("Import and Global Sourcing India", "Imports", "/img/import-hero.jpg") + f"""
    <div class="container-xxl py-5">
        <div class="container py-5">
            <div class="mx-auto mb-5" style="max-width: 760px;">
                <p class="mb-3">Alongside agricultural export from India, {COMPANY} reviews international products that may fit Indian demand. We look at quality, supplier reliability and commercial viability before progressing a discussion — we do not list a standing import catalogue.</p>
                <p class="mb-0">If you are an overseas supplier or an Indian buyer exploring an inbound shipment, <a href="{U_QUOTE}?type=Import%20to%20India">share the opportunity</a> or <a href="{U_CONTACT}">contact {COMPANY} in Nagpur</a>.</p>
            </div>
            <div class="row g-4">
                <div class="col-md-4"><div class="why-item h-100"><i class="fa fa-globe fa-lg text-primary mb-3"></i><h2 class="h5 mb-3">Supplier sourcing</h2><p class="mb-0">Identifying and engaging with potential overseas suppliers.</p></div></div>
                <div class="col-md-4"><div class="why-item h-100"><i class="fa fa-calculator fa-lg text-primary mb-3"></i><h2 class="h5 mb-3">Commercial evaluation</h2><p class="mb-0">Assessing viability before progressing trade discussions.</p></div></div>
                <div class="col-md-4"><div class="why-item h-100"><i class="fa fa-clipboard-list fa-lg text-primary mb-3"></i><h2 class="h5 mb-3">Import coordination</h2><p class="mb-0">Supporting documentation and related trade steps with partners.</p></div></div>
            </div>
            <div class="text-center mt-5">
                <h2 class="h4 mb-3">Have a product to import into India?</h2>
                <p class="mb-4">Share the details and we will review the opportunity together.</p>
                <a href="{U_QUOTE}?type=Import%20to%20India" class="btn btn-primary py-3 px-5">Discuss an import opportunity</a>
            </div>
        </div>
    </div>
"""

PRODUCT_ALTS = {
    "fruits.jpg": "Fresh Indian fruits for export, including papaya and mango",
    "vegetables.jpg": "Fresh Indian vegetables including onion and potato",
    "chilli.jpg": "Fresh Indian red chilli for export",
    "rice.jpg": "Indian rice and grains for commodity trade",
    "pulses.jpg": "Indian pulses for agricultural commodity trade",
    "commodities.jpg": "Indian agricultural commodities prepared for trade discussion",
    "processed.jpg": "Selected processed food products for sourcing discussion",
    "custom.jpg": "Custom agricultural sourcing for a specific buyer requirement",
}

PRODUCTS = page_header("Agricultural Products &amp; Commodities", "Products", "/img/products/fruits.jpg") + f"""
    <div class="container-xxl py-5">
        <div class="container py-5">
            <div class="mx-auto mb-5" style="max-width:720px;">
                <p class="mb-3">{COMPANY} sources agricultural and food products according to buyer requirements. Categories include fresh fruits such as papaya and mango, vegetables, chilli and spices, rice, pulses, grains and selected processed food. {AVAILABILITY}</p>
                <p class="mb-0">These are sourcing categories, not a claim that every item is always in shipment. <a href="{U_EXPORTS}">Read about export from India</a> or <a href="{U_QUOTE}">request an export quotation</a>.</p>
            </div>
            <div class="row g-4">
"""
for img, title, desc in PRODUCT_CARDS:
    PRODUCTS += f"""
                <div class="col-md-6 col-lg-3">
                    <a class="product-card" href="{product_href(title)}">
                        <div class="product-img"><img src="/img/products/{img}" alt="{PRODUCT_ALTS[img]}" width="640" height="400" loading="lazy"></div>
                        <div class="p-4"><h2>{title}</h2><p>{desc}</p><span class="enquire-link">Enquire</span></div>
                    </a>
                </div>"""
PRODUCTS += f"""
            </div>
            <div class="enquiry-band mt-5 text-center">
                <h2 class="h3 mb-3">Need a specific commodity?</h2>
                <p class="mb-4">Share the product, quantity and destination and we will explore sourcing options.</p>
                <a href="{U_QUOTE}" class="btn btn-primary py-3 px-5">Request an export quotation</a>
            </div>
        </div>
    </div>
"""

SERVICES = page_header("Import Export and Global Sourcing Services", "Services", "/img/carousel-2.jpg") + f"""
    <div class="container-xxl py-5">
        <div class="container py-5">
            <div class="mx-auto mb-5" style="max-width:760px;">
                <p class="mb-3">{COMPANY} supports international trade through sourcing and coordination. Freight, certification and customs are handled with external partners when required — we do not operate those services ourselves.</p>
                <p class="mb-0">Commercial terms such as FOB or CIF can be discussed on enquiry. <a href="{U_CONTACT}">Contact {COMPANY}</a> or <a href="{U_QUOTE}">request a quotation</a> once you know the product, quantity and destination.</p>
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
                        <h2 class="h5 mb-3">{title}</h2>
                        <p class="mb-3">{desc}</p>
                        <a class="enquire-link" href="{U_CONTACT}">Contact {COMPANY}</a>
                    </div>
                </div>"""
SERVICES += """
            </div>
        </div>
    </div>
"""

MARKETS = page_header("Indian Agricultural Products for Global Markets", "Markets", "/img/markets.jpg") + f"""
    <div class="container-xxl py-5">
        <div class="container py-5">
            <div class="row g-5">
                <div class="col-lg-7">
                    <h2 class="h4 mb-4">Regions we are building conversations in</h2>
                    <p class="mb-4">{COMPANY} connects Indian agricultural products with overseas buyers and explores selected import opportunities into India. The regions below are target markets — not a claim of current shipment volume.</p>
                    <div class="market-list">
                        <div class="market-row"><h3 class="h5">Middle East</h3><p>A priority region for agricultural and food trade discussions.</p></div>
                        <div class="market-row"><h3 class="h5">Africa</h3><p>Opportunities aligned with demand for Indian agricultural products.</p></div>
                        <div class="market-row"><h3 class="h5">Southeast Asia</h3><p>Markets with food and commodity trade potential.</p></div>
                        <div class="market-row"><h3 class="h5">Europe</h3><p>Conversations around quality-focused agricultural sourcing.</p></div>
                    </div>
                    <p class="mt-4 mb-0">We also review other regions when product fit, buyer interest and commercial terms align. See <a href="{U_EXPORTS}">agricultural product export from India</a> for product categories.</p>
                </div>
                <div class="col-lg-5">
                    <div class="enquiry-panel h-100">
                        <h2 class="h4 mb-3">Discuss a destination</h2>
                        <p class="mb-4">Share the product and market you have in mind. We will review suitability together.</p>
                        <a href="{U_QUOTE}" class="btn btn-primary py-3 px-4">Request an export quotation</a>
                    </div>
                </div>
            </div>
        </div>
    </div>
"""

CONTACT = page_header("Contact Global Route Company", "Contact", "/img/cta-bg.jpg") + f"""
    <div class="container-xxl py-5">
        <div class="container py-5">
            <div class="row g-5">
                <div class="col-lg-6">
                    <h2 class="h4 mb-4">Tell us what you need</h2>
                    <p class="mb-4">Contact {COMPANY} in Nagpur to discuss agricultural export from India, import into India, or a supplier partnership. Share your details below or continue on WhatsApp.</p>
                    <div class="enquiry-panel">
{ENQUIRY_FORM}
                    </div>
                </div>
                <div class="col-lg-6">
                    <div class="contact-aside text-white h-100">
                        <h4 class="text-white mb-4">Contact Information</h4>
                        <p class="mb-3"><i class="fa fa-building me-3"></i><strong>{COMPANY}</strong></p>
                        <p class="mb-4"><i class="fa fa-map-marker-alt me-3"></i>{ADDRESS_FULL}</p>
                        <p class="mb-3"><i class="fa fa-phone-alt me-3"></i><a class="text-white" href="tel:{PHONE_TEL}">{PHONE}</a></p>
                        <p class="mb-3"><i class="fab fa-whatsapp me-3"></i><a class="text-white" href="{WHATSAPP}" target="_blank" rel="noopener">Chat on WhatsApp</a></p>
                        <p class="mb-4"><i class="fa fa-envelope me-3"></i><a class="text-white" href="mailto:{EMAIL}">{EMAIL}</a></p>
                        <hr class="border-light">
                        <h5 class="text-white mb-3">Office Location</h5>
                        <p class="mb-3">{ADDRESS_FULL}</p>
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

QUOTE = page_header("Request a Quote", "Request a Quote", "/img/carousel-2.jpg") + f"""
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
            <p class="mb-0">For a privacy question or a request about your enquiry data, email <a href="mailto:{EMAIL}">{EMAIL}</a> or write to {COMPANY}, {ADDRESS_FULL}.</p>
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
                    <a class="btn btn-primary py-3 px-5 me-2 mb-2" href="{HOME}">Back to Home</a>
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
                    <a class="btn btn-primary py-3 px-5" href="{HOME}">Go Back To Home</a>
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

def write_sitemap() -> None:
    today = date.today().isoformat()
    entries = [
        (HOME, "1.0"),
        (U_ABOUT, "0.8"),
        (U_EXPORTS, "0.8"),
        (U_IMPORTS, "0.7"),
        (U_PRODUCTS, "0.8"),
        (U_SERVICES, "0.7"),
        (U_MARKETS, "0.6"),
        (U_CONTACT, "0.8"),
        (U_QUOTE, "0.7"),
        (U_PRIVACY, "0.3"),
    ]
    for post in BLOG_POSTS:
        entries.append((f"/blog/{post['slug']}", "0.5"))
    for product in PRODUCT_DETAIL_PAGES:
        entries.append((f"/products/{product['slug']}", "0.6"))
    urls = "\n".join(
        (
            "  <url>"
            f"<loc>{absolute(path)}</loc>"
            f"<lastmod>{today}</lastmod>"
            f"<changefreq>monthly</changefreq>"
            f"<priority>{priority}</priority>"
            "</url>"
        )
        for path, priority in entries
    )
    (ROOT / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        f"{urls}\n"
        "</urlset>\n",
        encoding="utf-8",
    )
    print("wrote sitemap.xml")


def write_robots() -> None:
    (ROOT / "robots.txt").write_text(
        "User-agent: *\n"
        "Allow: /\n"
        "\n"
        f"Sitemap: {SITE}/sitemap.xml\n",
        encoding="utf-8",
    )
    print("wrote robots.txt")


def write_redirects() -> None:
    (ROOT / "_redirects").write_text(
        """# Pretty URLs and retired template paths for Global Route Company
/about              /about.html          200
/exports            /exports.html        200
/imports            /imports.html        200
/products           /products.html       200
/services           /service.html        200
/markets            /markets.html        200
/contact            /contact.html        200
/quote              /quote.html          200
/privacy            /privacy.html        200
/thank-you          /thank-you.html      200

/about.html         /about               301
/exports.html       /exports             301
/imports.html       /imports             301
/products.html      /products            301
/service.html       /services            301
/service            /services            301
/markets.html       /markets             301
/contact.html       /contact             301
/quote.html         /quote               301
/privacy.html       /privacy             301

/feature.html       /about               301
/feature            /about               301
/price.html         /products            301
/price              /products            301
/team.html          /about               301
/team               /about               301
/testimonial.html   /about               301
/testimonial        /about               301

/404.html           /404.html            404
""",
        encoding="utf-8",
    )
    print("wrote _redirects")


if __name__ == "__main__":
    write(
        "index.html",
        f"{COMPANY} | Import & Export Trading Company India",
        "home",
        INDEX,
        SEO_DESC,
        crumbs=[("Home", None)],
        og_description=OG_HOME_DESC,
    )
    write(
        "about.html",
        f"About {COMPANY} | International Trading Company India",
        "about",
        ABOUT,
        f"{COMPANY} is an India-based international trading company in Nagpur, focused on agricultural import, export and global sourcing.",
        crumbs=[("Home", HOME), ("About Us", None)],
    )
    write(
        "exports.html",
        f"Agricultural Product Export from India | {COMPANY}",
        "exports",
        EXPORTS,
        f"{COMPANY} sources agricultural products from India for international buyers. Availability depends on seasonality, quality, quantity and destination.",
        crumbs=[("Home", HOME), ("Exports", None)],
    )
    write(
        "imports.html",
        f"Import & Global Sourcing India | {COMPANY}",
        "imports",
        IMPORTS,
        f"{COMPANY} reviews selected international products for the Indian market based on demand, quality and commercial fit.",
        crumbs=[("Home", HOME), ("Imports", None)],
    )
    write(
        "products.html",
        f"Agricultural Products & Commodities | {COMPANY}",
        "products",
        PRODUCTS,
        f"Agricultural and food categories sourced by {COMPANY}: fruits, vegetables, chilli, rice, pulses and custom sourcing. Specifications are confirmed on enquiry.",
        crumbs=[("Home", HOME), ("Products", None)],
    )
    write(
        "service.html",
        f"Import Export & Global Sourcing Services | {COMPANY}",
        "services",
        SERVICES,
        f"{COMPANY} supports global sourcing, supplier coordination and documentation. Freight is coordinated with logistics partners.",
        crumbs=[("Home", HOME), ("Services", None)],
    )
    write(
        "markets.html",
        f"Indian Agricultural Products for Global Markets | {COMPANY}",
        "markets",
        MARKETS,
        f"Target markets for {COMPANY} include the Middle East, Africa, Southeast Asia and Europe, subject to product fit and buyer interest.",
        crumbs=[("Home", HOME), ("Markets", None)],
    )
    write(
        "contact.html",
        f"Contact {COMPANY} | Import Export Company Nagpur",
        "contact",
        CONTACT,
        f"Contact {COMPANY} in Nagpur, Maharashtra to discuss agricultural export, import or supplier requirements. Phone {PHONE}.",
        crumbs=[("Home", HOME), ("Contact", None)],
    )
    write(
        "quote.html",
        f"Request a Quote | {COMPANY}",
        "contact",
        QUOTE,
        f"Request a quote from {COMPANY} for agricultural sourcing from India or selected imports into India.",
        crumbs=[("Home", HOME), ("Request a Quote", None)],
    )
    write(
        "privacy.html",
        f"Privacy Policy | {COMPANY}",
        "home",
        PRIVACY,
        f"How {COMPANY} uses enquiry information submitted through this website.",
        crumbs=[("Home", HOME), ("Privacy Policy", None)],
    )
    write(
        "thank-you.html",
        f"Thank You | {COMPANY}",
        "contact",
        THANK_YOU,
        noindex=True,
        crumbs=[("Home", HOME), ("Thank You", None)],
    )
    write(
        "404.html",
        f"Page Not Found | {COMPANY}",
        "home",
        NOT_FOUND,
        noindex=True,
        crumbs=[("Home", HOME), ("404", None)],
    )

    for old, target in [
        ("feature.html", U_ABOUT),
        ("price.html", U_PRODUCTS),
        ("team.html", U_ABOUT),
        ("testimonial.html", U_ABOUT),
    ]:
        (ROOT / old).write_text(REDIRECT.format(target=target), encoding="utf-8")
        print("redirect", old, "->", target)

    write_sitemap()
    write_robots()
    write_redirects()

    products_dir = ROOT / "products"
    products_dir.mkdir(exist_ok=True)
    (products_dir / ".gitkeep").write_text(
        "Add a product detail page only when genuine specifications exist.\n",
        encoding="utf-8",
    )
    blog_dir = ROOT / "blog"
    blog_dir.mkdir(exist_ok=True)
    (blog_dir / ".gitkeep").write_text(
        "Add a blog article only when there is useful original content.\n",
        encoding="utf-8",
    )

    (ROOT / "READ-ME.txt").write_text(
        f"{COMPANY} Website\n"
        f"Preferred domain: {SITE}/\n"
        "Static site — deploy via GitHub → Netlify.\n"
        "Pretty URLs: /about /exports /imports /products /services /markets /contact\n"
        f"Search Console: verify {SITE}, then submit {SITE}/sitemap.xml and inspect key URLs.\n"
        "Forms use Netlify Forms. Set email notifications in the Netlify dashboard.\n"
        "Future product pages: add entries to PRODUCT_DETAIL_PAGES in _build_site.py.\n"
        "Future blog posts: add entries to BLOG_POSTS in _build_site.py. Do not publish empty articles.\n",
        encoding="utf-8",
    )
    print("done")
