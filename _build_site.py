#!/usr/bin/env python3
"""Generate Global Route Company website pages from the Logistica template."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent

COMPANY = "Global Route Company"
TAGLINE = "Connecting India to Global Markets"
PHONE = "+91 9225159719"
PHONE_TEL = "+919225159719"
EMAIL = "lokeshghagare@gmail.com"
ADDRESS = "Plot No. 188, CA Road, Garoba Maidan, Nagpur, Maharashtra (Near Dalvi Hospital) - 440008"
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
    <link href="img/favicon.svg" rel="icon" type="image/svg+xml">
    <link href="img/favicon-32.png" rel="icon" type="image/png" sizes="32x32">
    <link href="img/apple-touch-icon.png" rel="apple-touch-icon">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.10.0/css/all.min.css" rel="stylesheet">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.4.1/font/bootstrap-icons.css" rel="stylesheet">
    <link href="lib/animate/animate.min.css" rel="stylesheet">
    <link href="lib/owlcarousel/assets/owl.carousel.min.css" rel="stylesheet">
    <link href="css/bootstrap.min.css" rel="stylesheet">
    <link href="css/style.css" rel="stylesheet">
    <style>body{{font-family:"Plus Jakarta Sans",sans-serif;}} h1,h2,h3,h4,h5,.display-3{{font-weight:700;}}</style>
    <script type="application/ld+json">{ORG_SCHEMA}</script>
</head>

<body>
    <div id="spinner" class="show bg-white position-fixed translate-middle w-100 vh-100 top-50 start-50 d-flex align-items-center justify-content-center">
        <div class="spinner-grow text-primary" style="width: 3rem; height: 3rem;" role="status">
            <span class="sr-only">Loading...</span>
        </div>
    </div>
"""


def nav(active: str) -> str:
    def c(name: str) -> str:
        return "nav-item nav-link active" if active == name else "nav-item nav-link"

    return f"""
    <nav class="navbar navbar-expand-lg bg-white navbar-light shadow border-top border-5 border-primary sticky-top p-0">
        <a href="index.html" class="navbar-brand navbar-brand-logo px-3 px-lg-4">
            <img src="img/logo.svg" alt="{COMPANY}">
        </a>
        <button type="button" class="navbar-toggler me-4" data-bs-toggle="collapse" data-bs-target="#navbarCollapse">
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
                <a href="tel:{PHONE_TEL}" class="navbar-phone me-3"><i class="fa fa-phone-alt text-primary me-2"></i>{PHONE} <span class="navbar-tz">IST</span></a>
                <a href="quote.html" class="btn btn-primary py-2 px-3 me-2">Request a Quote</a>
                <a href="{WHATSAPP}" class="btn btn-whatsapp py-2 px-3" target="_blank" rel="noopener"><i class="fab fa-whatsapp me-1"></i>WhatsApp</a>
            </div>
        </div>
    </nav>
"""


FOOTER = f"""
    <div class="container-fluid bg-dark text-light footer pt-5 wow fadeIn" data-wow-delay="0.1s" style="margin-top: 6rem;">
        <div class="container py-5">
            <div class="row g-5">
                <div class="col-lg-4 col-md-6">
                    <div class="footer-brand">{COMPANY}</div>
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
                    <a href="contact.html" class="btn btn-primary py-2 px-4 mt-2">Contact Us</a>
                    <a href="quote.html" class="btn btn-outline-light py-2 px-4 mt-2">Request a Quote</a>
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
    <a href="#" class="btn btn-lg btn-primary btn-lg-square rounded-0 back-to-top"><i class="bi bi-arrow-up"></i></a>

    <script src="https://code.jquery.com/jquery-3.4.1.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0/dist/js/bootstrap.bundle.min.js"></script>
    <script src="lib/wow/wow.min.js"></script>
    <script src="lib/easing/easing.min.js"></script>
    <script src="lib/waypoints/waypoints.min.js"></script>
    <script src="lib/counterup/counterup.min.js"></script>
    <script src="lib/owlcarousel/owl.carousel.min.js"></script>
    <script src="js/main.js"></script>
</body>
</html>
"""


def page_header(title: str, crumb: str) -> str:
    return f"""
    <div class="container-fluid page-header py-5" style="margin-bottom: 6rem;">
        <div class="container py-5">
            <h1 class="display-3 text-white mb-3 animated slideInDown">{title}</h1>
            <nav aria-label="breadcrumb animated slideInDown">
                <ol class="breadcrumb">
                    <li class="breadcrumb-item"><a class="text-white" href="index.html">Home</a></li>
                    <li class="breadcrumb-item text-white active" aria-current="page">{crumb}</li>
                </ol>
            </nav>
        </div>
    </div>
"""


ENQUIRY_FORM = """
                    <form name="business-enquiry" method="POST" action="thank-you.html" data-netlify="true" netlify-honeypot="bot-field">
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
    html = head(title, description or SEO_DESC, name, noindex) + nav(active) + body + FOOTER
    (ROOT / name).write_text(html, encoding="utf-8")
    print("wrote", name)


# ---- Page bodies ----

INDEX = f"""
    <div class="container-fluid p-0 pb-5">
        <div class="owl-carousel header-carousel position-relative mb-5">
            <div class="owl-carousel-item position-relative">
                <img class="img-fluid" src="img/carousel-1.jpg" alt="Indian agricultural fields for export">
                <div class="position-absolute top-0 start-0 w-100 h-100 d-flex align-items-center" style="background: rgba(11, 29, 54, .58);">
                    <div class="container">
                        <div class="row justify-content-start">
                            <div class="col-10 col-lg-8">
                                <h5 class="text-white text-uppercase mb-3 animated slideInDown">Import &amp; Export | Global Sourcing | Agricultural Trade</h5>
                                <h1 class="display-3 text-white animated slideInDown mb-4">Connecting India to <span class="text-primary">Global Markets</span></h1>
                                <p class="fs-5 fw-medium text-white mb-4 pb-2">{COMPANY} is an international import and export trading company focused on connecting quality products, trusted suppliers and global buyers.</p>
                                <a href="products.html" class="btn btn-primary py-md-3 px-md-5 me-3 animated slideInLeft">Explore Our Products</a>
                                <a href="quote.html" class="btn btn-secondary py-md-3 px-md-5 animated slideInRight">Request a Quote</a>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="owl-carousel-item position-relative">
                <img class="img-fluid" src="img/carousel-2.jpg" alt="International trade and shipping">
                <div class="position-absolute top-0 start-0 w-100 h-100 d-flex align-items-center" style="background: rgba(11, 29, 54, .58);">
                    <div class="container">
                        <div class="row justify-content-start">
                            <div class="col-10 col-lg-8">
                                <h5 class="text-white text-uppercase mb-3 animated slideInDown">India → World | World → India</h5>
                                <h1 class="display-3 text-white animated slideInDown mb-4">Reliable Sourcing for <span class="text-primary">International Trade</span></h1>
                                <p class="fs-5 fw-medium text-white mb-4 pb-2">We source agricultural products from India for international markets and explore reliable products from around the world for the Indian market.</p>
                                <a href="exports.html" class="btn btn-primary py-md-3 px-md-5 me-3 animated slideInLeft">Export from India</a>
                                <a href="imports.html" class="btn btn-secondary py-md-3 px-md-5 animated slideInRight">Import to India</a>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <div class="container-fluid tagline-strip py-3">
        <div class="container">
            <div class="row g-3">
                <div class="col-md-3 tagline-item wow fadeInUp" data-wow-delay="0.1s">India <span>→</span> Global Markets</div>
                <div class="col-md-3 tagline-item wow fadeInUp" data-wow-delay="0.2s">Global Markets <span>→</span> India</div>
                <div class="col-md-3 tagline-item wow fadeInUp" data-wow-delay="0.3s">Agriculture <span>→</span> International Trade</div>
                <div class="col-md-3 tagline-item wow fadeInUp" data-wow-delay="0.4s">Sourcing <span>→</span> Partnerships</div>
            </div>
        </div>
    </div>

    <div class="container-xxl py-5">
        <div class="container py-5">
            <div class="text-center wow fadeInUp" data-wow-delay="0.1s">
                <h6 class="text-secondary text-uppercase">Export From India</h6>
                <h1 class="mb-4">Taking India's Agricultural Products to the World</h1>
                <p class="mb-5 mx-auto" style="max-width: 760px;">India is home to a diverse agricultural ecosystem producing a wide range of fruits, vegetables, spices, grains and other food products. We aim to connect these products with international markets through reliable sourcing and professional trade coordination.</p>
            </div>
            <div class="row g-4">
                <div class="col-md-6 col-lg-3 wow fadeInUp" data-wow-delay="0.1s">
                    <div class="service-item p-4">
                        <div class="overflow-hidden mb-4"><img class="img-fluid" src="img/products/fruits.jpg" alt="Fresh fruits"></div>
                        <h4 class="mb-3">Fresh Fruits</h4>
                        <p>Papaya, mango, banana, grapes, pomegranate and other seasonal fruits sourced according to buyer requirements.</p>
                        <a class="btn-slide mt-2" href="exports.html"><i class="fa fa-arrow-right"></i><span>View Exports</span></a>
                    </div>
                </div>
                <div class="col-md-6 col-lg-3 wow fadeInUp" data-wow-delay="0.2s">
                    <div class="service-item p-4">
                        <div class="overflow-hidden mb-4"><img class="img-fluid" src="img/products/vegetables.jpg" alt="Fresh vegetables"></div>
                        <h4 class="mb-3">Fresh Vegetables</h4>
                        <p>Onion, potato and other vegetables based on market conditions and buyer specifications.</p>
                        <a class="btn-slide mt-2" href="exports.html"><i class="fa fa-arrow-right"></i><span>View Exports</span></a>
                    </div>
                </div>
                <div class="col-md-6 col-lg-3 wow fadeInUp" data-wow-delay="0.3s">
                    <div class="service-item p-4">
                        <div class="overflow-hidden mb-4"><img class="img-fluid" src="img/products/chilli.jpg" alt="Chilli and spices"></div>
                        <h4 class="mb-3">Chilli &amp; Spices</h4>
                        <p>Indian chilli, red chilli and selected spices for international food and commodity buyers.</p>
                        <a class="btn-slide mt-2" href="exports.html"><i class="fa fa-arrow-right"></i><span>View Exports</span></a>
                    </div>
                </div>
                <div class="col-md-6 col-lg-3 wow fadeInUp" data-wow-delay="0.4s">
                    <div class="service-item p-4">
                        <div class="overflow-hidden mb-4"><img class="img-fluid" src="img/products/rice.jpg" alt="Rice and grains"></div>
                        <h4 class="mb-3">Grains &amp; Pulses</h4>
                        <p>Rice, pulses, grains and other agricultural commodities sourced for export markets.</p>
                        <a class="btn-slide mt-2" href="exports.html"><i class="fa fa-arrow-right"></i><span>View Exports</span></a>
                    </div>
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
                <div class="col-lg-6 pe-lg-0 wow fadeInRight" data-wow-delay="0.1s" style="min-height: 400px;">
                    <div class="position-relative h-100">
                        <img class="position-absolute img-fluid w-100 h-100" src="img/import-hero.jpg" style="object-fit: cover;" alt="Import coordination">
                    </div>
                </div>
            </div>
        </div>
    </div>
"""

for i, (num, title, desc) in enumerate([
    ("01", "Requirement", "Understand buyer and product requirements."),
    ("02", "Source", "Identify suitable products and suppliers."),
    ("03", "Verify & Coordinate", "Align product details, quality needs and commercial discussions."),
    ("04", "Trade", "Discuss commercial terms such as FOB or CIF and coordinate documentation with logistics partners."),
    ("05", "Deliver", "Support shipment through reliable logistics partners."),
]):
    if i == 0:
        INDEX += """
    <div class="container-xxl py-5">
        <div class="container py-5">
            <div class="text-center wow fadeInUp" data-wow-delay="0.1s">
                <h6 class="text-secondary text-uppercase">How We Work</h6>
                <h1 class="mb-5">A Clear Path from Requirement to Delivery</h1>
            </div>
            <div class="row g-4 justify-content-center">
"""
    INDEX += f"""
                <div class="col-6 col-md-4 col-lg wow fadeInUp" data-wow-delay="0.{i+1}s" style="min-width:160px;">
                    <div class="process-item">
                        <div class="process-number">{num}</div>
                        <h5>{title}</h5>
                        <p class="mb-0">{desc}</p>
                    </div>
                </div>"""

INDEX += """
            </div>
        </div>
    </div>

    <div class="container-fluid cta-band py-5">
        <div class="container py-5">
            <div class="row g-4">
                <div class="col-lg-6 wow fadeInUp" data-wow-delay="0.1s">
                    <div class="cta-card text-white">
                        <h3 class="text-white mb-3">Looking for Reliable Products from India?</h3>
                        <p class="mb-4">Tell us what you are looking for and our team will explore suitable sourcing opportunities.</p>
                        <a href="quote.html" class="btn btn-primary py-3 px-4 me-2">Request a Quote</a>
                        <a href="contact.html" class="btn btn-outline-light py-3 px-4">Contact Us</a>
                    </div>
                </div>
                <div class="col-lg-6 wow fadeInUp" data-wow-delay="0.3s">
                    <div class="cta-card text-white">
                        <h3 class="text-white mb-3">Have a Product to Import into India?</h3>
                        <p class="mb-4">Let's explore the opportunity together.</p>
                        <a href="imports.html" class="btn btn-secondary py-3 px-4">Discuss Your Requirement</a>
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
                <div class="col-lg-6 ps-lg-0 wow fadeInLeft" data-wow-delay="0.1s" style="min-height: 400px;">
                    <div class="position-relative h-100">
                        <img class="position-absolute img-fluid w-100 h-100" src="img/about.jpg" style="object-fit: cover;" alt="About {COMPANY}">
                    </div>
                </div>
                <div class="col-lg-6 about-text wow fadeInUp" data-wow-delay="0.3s">
                    <h6 class="text-secondary text-uppercase mb-3">Who We Are</h6>
                    <h1 class="mb-4">About {COMPANY}</h1>
                    <p class="mb-4">{COMPANY} is an India-based international trading company focused on creating reliable connections between Indian producers, global buyers and international suppliers.</p>
                    <p class="mb-4">Our business is built around responsible sourcing, quality products, transparent communication and long-term business relationships.</p>
                    <p class="mb-4">We aim to support international buyers with carefully sourced agricultural products from India while exploring opportunities to bring selected quality products from global markets to India.</p>
                    <p class="mb-4 fw-medium fs-5">Source responsibly. Trade transparently. Deliver reliably.</p>
                    <p class="mb-4">Learn more about <a href="exports.html">exports from India</a>, <a href="imports.html">imports to India</a>, and our <a href="markets.html">target markets</a>.</p>
                    <a href="contact.html" class="btn btn-primary py-3 px-5">Get in Touch</a>
                </div>
            </div>
        </div>
    </div>
    <div class="container-xxl py-5 bg-light">
        <div class="container py-5">
            <div class="row g-4">
                <div class="col-md-4 wow fadeInUp" data-wow-delay="0.1s"><div class="why-item h-100"><h5 class="mb-3">Our Focus</h5><p class="mb-0">Import &amp; export trading with a primary emphasis on agricultural and food products, supported by professional trade coordination.</p></div></div>
                <div class="col-md-4 wow fadeInUp" data-wow-delay="0.2s"><div class="why-item h-100"><h5 class="mb-3">Our Approach</h5><p class="mb-0">Understand requirements, identify suitable products and suppliers, coordinate quality and commercial discussions, and support delivery through trusted partners.</p></div></div>
                <div class="col-md-4 wow fadeInUp" data-wow-delay="0.3s"><div class="why-item h-100"><h5 class="mb-3">Our Commitment</h5><p class="mb-0">Clear communication, realistic expectations and a partnership mindset — without exaggerated claims or unsupported guarantees.</p></div></div>
            </div>
        </div>
    </div>
"""

EXPORTS = page_header("Exports", "Exports") + f"""
    <div class="container-xxl py-5">
        <div class="container py-5">
            <div class="row g-5 align-items-center mb-5">
                <div class="col-lg-6 wow fadeInUp" data-wow-delay="0.1s">
                    <h6 class="text-secondary text-uppercase mb-3">Export From India</h6>
                    <h1 class="mb-4">Taking India's Agricultural Products to the World</h1>
                    <p class="mb-4">India is home to a diverse agricultural ecosystem producing a wide range of fruits, vegetables, spices, grains and other food products. {COMPANY} aims to connect these products with international markets through reliable sourcing and professional trade coordination.</p>
                    <p class="mb-0">We source and supply a wide range of agricultural and food products based on buyer requirements and market demand. Availability depends on seasonality, quality standards, quantity and destination requirements.</p>
                </div>
                <div class="col-lg-6 wow fadeInUp" data-wow-delay="0.3s">
                    <img class="img-fluid w-100" src="img/export-hero.jpg" alt="Export from India" style="object-fit:cover; max-height:420px;">
                </div>
            </div>
            <div class="row g-4">
                <div class="col-md-6 col-lg-4 wow fadeInUp" data-wow-delay="0.1s"><div class="service-item p-4"><div class="overflow-hidden mb-4"><img class="img-fluid" src="img/products/fruits.jpg" alt="Fresh Fruits"></div><h4 class="mb-3">Fresh Fruits</h4><p>Papaya, mango, banana, grapes, pomegranate and other seasonal fruits.</p></div></div>
                <div class="col-md-6 col-lg-4 wow fadeInUp" data-wow-delay="0.2s"><div class="service-item p-4"><div class="overflow-hidden mb-4"><img class="img-fluid" src="img/products/vegetables.jpg" alt="Fresh Vegetables"></div><h4 class="mb-3">Fresh Vegetables</h4><p>Onion, potato and other vegetables based on market and buyer requirements.</p></div></div>
                <div class="col-md-6 col-lg-4 wow fadeInUp" data-wow-delay="0.3s"><div class="service-item p-4"><div class="overflow-hidden mb-4"><img class="img-fluid" src="img/products/chilli.jpg" alt="Chilli and Spices"></div><h4 class="mb-3">Chilli &amp; Spices</h4><p>Indian chilli, red chilli and selected spices for global buyers.</p></div></div>
                <div class="col-md-6 col-lg-4 wow fadeInUp" data-wow-delay="0.4s"><div class="service-item p-4"><div class="overflow-hidden mb-4"><img class="img-fluid" src="img/products/rice.jpg" alt="Grains and Pulses"></div><h4 class="mb-3">Grains &amp; Pulses</h4><p>Rice, pulses, grains and other agricultural commodities.</p></div></div>
                <div class="col-md-6 col-lg-4 wow fadeInUp" data-wow-delay="0.5s"><div class="service-item p-4"><div class="overflow-hidden mb-4"><img class="img-fluid" src="img/products/custom.jpg" alt="Custom Sourcing"></div><h4 class="mb-3">Custom Sourcing</h4><p>Products sourced according to specific buyer requirements.</p></div></div>
                <div class="col-md-6 col-lg-4 wow fadeInUp" data-wow-delay="0.6s"><div class="service-item p-4 bg-primary text-white"><h4 class="mb-3 text-white">Share Your Requirement</h4><p class="text-white">Tell us the product, quantity, quality preference and destination — we will explore suitable sourcing options.</p><a href="quote.html" class="btn btn-secondary py-2 px-4">Request a Quote</a></div></div>
            </div>
        </div>
    </div>
"""

IMPORTS = page_header("Imports", "Imports") + f"""
    <div class="container-xxl py-5">
        <div class="container py-5">
            <div class="row g-5 align-items-center mb-5">
                <div class="col-lg-6 wow fadeInUp" data-wow-delay="0.1s">
                    <h6 class="text-secondary text-uppercase mb-3">Import to India</h6>
                    <h1 class="mb-4">Bringing Global Opportunities to India</h1>
                    <p class="mb-4">Alongside exports, {COMPANY} explores international sourcing opportunities for products that have potential in the Indian market.</p>
                    <p class="mb-4">We are continuously exploring international sourcing opportunities to bring quality products to the Indian market.</p>
                    <a href="contact.html" class="btn btn-primary py-3 px-5">Discuss an Import Opportunity</a>
                </div>
                <div class="col-lg-6 wow fadeInUp" data-wow-delay="0.3s">
                    <img class="img-fluid w-100" src="img/import-hero.jpg" alt="Import to India" style="object-fit:cover; max-height:420px;">
                </div>
            </div>
            <div class="row g-4">
"""
for i, (icon, title, desc) in enumerate([
    ("fa-globe", "International Supplier Sourcing", "Identifying and engaging with potential overseas suppliers."),
    ("fa-lightbulb", "Product Identification", "Evaluating products with relevance to Indian market demand."),
    ("fa-comments", "Supplier Communication", "Clear discussions on specifications, commercial terms and feasibility."),
    ("fa-calculator", "Commercial Evaluation", "Assessing viability before progressing trade discussions."),
    ("fa-clipboard-list", "Import Coordination", "Supporting coordination across documentation and related trade steps."),
    ("fa-store", "Market-Oriented Sourcing", "Focusing on products with practical potential in India."),
]):
    IMPORTS += f"""
                <div class="col-md-6 col-lg-4 wow fadeInUp" data-wow-delay="0.{i+1}s">
                    <div class="why-item"><i class="fa {icon} fa-2x text-primary mb-3"></i><h5 class="mb-3">{title}</h5><p class="mb-0">{desc}</p></div>
                </div>"""
IMPORTS += """
            </div>
            <div class="text-center mt-5">
                <h4 class="mb-3">Have a Product to Import into India?</h4>
                <p class="mb-4">Let's explore the opportunity together.</p>
                <a href="quote.html" class="btn btn-primary py-3 px-5">Discuss Your Requirement</a>
            </div>
        </div>
    </div>
"""

PRODUCTS = page_header("Products", "Products") + """
    <div class="container-xxl py-5">
        <div class="container py-5">
            <div class="text-center mx-auto mb-5 wow fadeInUp" data-wow-delay="0.1s" style="max-width:720px;">
                <h6 class="text-secondary text-uppercase">Our Product Categories</h6>
                <h1 class="mb-3">Agricultural &amp; Food Product Categories</h1>
                <p>We source and supply a wide range of agricultural and food products based on buyer requirements and market demand.</p>
            </div>
            <div class="row g-4">
"""
for i, (img, title, desc) in enumerate(PRODUCT_CARDS):
    PRODUCTS += f"""
                <div class="col-md-6 col-lg-3 wow fadeInUp" data-wow-delay="0.{i+1}s">
                    <div class="product-item">
                        <div class="product-img"><img src="img/products/{img}" alt="{title}"></div>
                        <div class="p-4"><h5 class="mb-2">{title}</h5><p class="mb-0">{desc}</p></div>
                    </div>
                </div>"""
PRODUCTS += """
            </div>
            <div class="bg-light p-5 mt-5 text-center wow fadeInUp" data-wow-delay="0.2s">
                <h3 class="mb-3">Need a Specific Commodity?</h3>
                <p class="mb-4">Share your product requirement and we will explore suitable sourcing options.</p>
                <a href="quote.html" class="btn btn-primary py-3 px-5">Request a Quote</a>
            </div>
        </div>
    </div>
"""

SERVICES = page_header("Services", "Services") + f"""
    <div class="container-xxl py-5">
        <div class="container py-5">
            <div class="text-center mx-auto mb-5 wow fadeInUp" data-wow-delay="0.1s" style="max-width:760px;">
                <h6 class="text-secondary text-uppercase">Our Services</h6>
                <h1 class="mb-3">International Trading Services</h1>
                <p>{COMPANY} supports international trade through sourcing, coordination and partnership-focused engagement. Where specialised activities such as freight or certification are required, we coordinate with appropriate external partners.</p>
                <p>Commercial terms such as FOB or CIF can be discussed on enquiry. We coordinate documentation with logistics partners rather than operating freight ourselves.</p>
            </div>
            <div class="row g-4">
"""
for i, (img, title, desc) in enumerate([
    ("service-1.jpg", "Global Sourcing", "Identifying suitable products and reliable suppliers according to buyer requirements."),
    ("service-2.jpg", "Import & Export", "Supporting international trade opportunities between India and global markets."),
    ("service-3.jpg", "Agricultural Product Sourcing", "Connecting buyers with suitable agricultural products from Indian markets."),
    ("service-4.jpg", "Supplier Coordination", "Working with suppliers and producers to support product availability and commercial requirements."),
    ("service-5.jpg", "Quality & Documentation Coordination", "Supporting product information, documentation and trade-related coordination."),
    ("service-6.jpg", "Logistics Coordination", "Coordinating with appropriate logistics partners for transportation and shipment requirements."),
]):
    SERVICES += f"""
                <div class="col-md-6 col-lg-4 wow fadeInUp" data-wow-delay="0.{i+1}s">
                    <div class="service-item p-4">
                        <div class="overflow-hidden mb-4"><img class="img-fluid" src="img/{img}" alt="{title}"></div>
                        <h4 class="mb-3">{title}</h4>
                        <p>{desc}</p>
                        <a class="btn-slide mt-2" href="contact.html"><i class="fa fa-arrow-right"></i><span>Enquire</span></a>
                    </div>
                </div>"""
SERVICES += """
            </div>
        </div>
    </div>
"""

MARKETS = page_header("Markets", "Markets") + f"""
    <div class="container-xxl py-5">
        <div class="container py-5">
            <div class="row g-5 align-items-center mb-5">
                <div class="col-lg-6 wow fadeInUp" data-wow-delay="0.1s">
                    <h6 class="text-secondary text-uppercase mb-3">Global Markets</h6>
                    <h1 class="mb-4">From India to Global Markets</h1>
                    <p class="mb-4">{COMPANY} works with an international outlook — connecting Indian agricultural products with overseas buyers and exploring selected import opportunities into India.</p>
                    <p class="mb-0">Our target markets include the Middle East, Africa, Southeast Asia, Europe and other international markets where product fit, demand and commercial viability align.</p>
                </div>
                <div class="col-lg-6 wow fadeInUp" data-wow-delay="0.3s">
                    <img class="img-fluid w-100" src="img/markets.jpg" alt="Global markets" style="object-fit:cover; max-height:420px;">
                </div>
            </div>
            <div class="row g-4">
"""
for i, (region, desc) in enumerate([
    ("Middle East", "A priority target region for agricultural and food trade discussions."),
    ("Africa", "Exploring opportunities aligned with demand for Indian agricultural products."),
    ("Southeast Asia", "Engaging markets with strong food and commodity trade potential."),
    ("Europe", "Developing conversations around quality-focused agricultural sourcing."),
]):
    MARKETS += f"""
                <div class="col-md-6 col-lg-3 wow fadeInUp" data-wow-delay="0.{i+1}s">
                    <div class="market-item h-100">
                        <i class="fa fa-map-marker-alt fa-2x text-primary mb-3"></i>
                        <h5>{region}</h5>
                        <p class="mb-0">{desc}</p>
                    </div>
                </div>"""
MARKETS += """
            </div>
            <div class="bg-light p-5 mt-5 wow fadeInUp" data-wow-delay="0.2s">
                <h4 class="mb-3">Other International Markets</h4>
                <p class="mb-0">We remain open to opportunities in additional regions based on product suitability, buyer interest and commercial alignment.</p>
            </div>
        </div>
    </div>
"""

CONTACT = page_header("Contact", "Contact") + f"""
    <div class="container-fluid overflow-hidden py-5 px-lg-0">
        <div class="container contact-page py-5 px-lg-0">
            <div class="row g-5 mx-lg-0">
                <div class="col-lg-6 contact-form wow fadeIn" data-wow-delay="0.1s">
                    <h6 class="text-secondary text-uppercase">Business Enquiry</h6>
                    <h1 class="mb-4">Tell Us What You Need</h1>
                    <p class="mb-4">Whether you are looking to source products from India, discuss an import opportunity, or explore a supplier partnership — share your details and we will respond. You can also reach us on WhatsApp.</p>
                    <div class="bg-light p-4">
{ENQUIRY_FORM}
                    </div>
                </div>
                <div class="col-lg-6 pe-lg-0 wow fadeInRight" data-wow-delay="0.1s">
                    <div class="bg-primary h-100 p-5 text-white">
                        <h4 class="text-white mb-4">Contact Information</h4>
                        <p class="mb-3"><i class="fa fa-building me-3"></i><strong>{COMPANY}</strong></p>
                        <p class="mb-4"><i class="fa fa-map-marker-alt me-3"></i>{ADDRESS}</p>
                        <p class="mb-3"><i class="fa fa-phone-alt me-3"></i><a class="text-white" href="tel:{PHONE_TEL}">{PHONE}</a></p>
                        <p class="mb-3"><i class="fab fa-whatsapp me-3"></i><a class="text-white" href="{WHATSAPP}" target="_blank" rel="noopener">Chat on WhatsApp</a></p>
                        <p class="mb-4"><i class="fa fa-envelope me-3"></i><a class="text-white" href="mailto:{EMAIL}">{EMAIL}</a></p>
                        <hr class="border-light">
                        <h5 class="text-white mb-3">Office Location</h5>
                        <div class="ratio ratio-4x3 bg-white">
                            <iframe src="https://www.google.com/maps?q=Garoba+Maidan+Nagpur+440008&output=embed" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade" title="{COMPANY} office location"></iframe>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
"""

QUOTE = page_header("Request a Quote", "Request a Quote") + f"""
    <div class="container-xxl py-5">
        <div class="container py-5">
            <div class="row g-5 align-items-start">
                <div class="col-lg-5 wow fadeInUp" data-wow-delay="0.1s">
                    <h6 class="text-secondary text-uppercase mb-3">Get a Quote</h6>
                    <h1 class="mb-4">Share Your Trade Requirement</h1>
                    <p class="mb-4">Provide product, quantity and destination or origin details. Our team will review your enquiry and explore suitable sourcing opportunities.</p>
                    <p class="mb-4">Commercial terms such as FOB or CIF can be discussed once we understand the product, quantity and destination. Freight and documentation are coordinated with logistics partners.</p>
                    <div class="d-flex align-items-center mb-4">
                        <i class="fa fa-phone-alt fa-2x flex-shrink-0 bg-primary p-3 text-white"></i>
                        <div class="ps-4"><h6>Call us</h6><h3 class="text-primary m-0"><a href="tel:{PHONE_TEL}">{PHONE}</a></h3></div>
                    </div>
                    <div class="d-flex align-items-center mb-4">
                        <i class="fab fa-whatsapp fa-2x flex-shrink-0 bg-primary p-3 text-white"></i>
                        <div class="ps-4"><h6>WhatsApp</h6><h5 class="text-primary m-0"><a href="{WHATSAPP}" target="_blank" rel="noopener">Message us</a></h5></div>
                    </div>
                    <div class="d-flex align-items-center">
                        <i class="fa fa-envelope fa-2x flex-shrink-0 bg-primary p-3 text-white"></i>
                        <div class="ps-4"><h6>Email us</h6><h5 class="text-primary m-0"><a href="mailto:{EMAIL}">{EMAIL}</a></h5></div>
                    </div>
                </div>
                <div class="col-lg-7">
                    <div class="bg-light p-5 wow fadeIn" data-wow-delay="0.3s">
{ENQUIRY_FORM}
                    </div>
                </div>
            </div>
        </div>
    </div>
"""

PRIVACY = page_header("Privacy Policy", "Privacy Policy") + f"""
    <div class="container-xxl py-5">
        <div class="container py-5" style="max-width: 820px;">
            <h6 class="text-secondary text-uppercase mb-3">Privacy Policy</h6>
            <h1 class="mb-4">How we handle enquiries</h1>
            <p class="mb-4">This page explains how {COMPANY} uses information you send through this website. We do not sell personal information.</p>
            <h4 class="mb-3">What we collect</h4>
            <p class="mb-4">When you submit the business enquiry form, we receive the details you enter — typically name, company, email, phone, country, enquiry type, product, quantity, destination or origin, and your message. If you contact us by phone, WhatsApp or email, we also receive the information you choose to share in that conversation.</p>
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
    <div class="container-xxl py-5 wow fadeInUp" data-wow-delay="0.1s">
        <div class="container text-center">
            <div class="row justify-content-center">
                <div class="col-lg-7">
                    <i class="fa fa-check-circle display-1 text-primary mb-4"></i>
                    <h1 class="mb-4">Thank you for your enquiry</h1>
                    <p class="mb-4">We have received your message. Our team will review your requirement and get back to you.</p>
                    <a class="btn btn-primary py-3 px-5 me-2 mb-2" href="index.html">Back to Home</a>
                    <a class="btn btn-whatsapp py-3 px-5 mb-2" href="{WHATSAPP}" target="_blank" rel="noopener"><i class="fab fa-whatsapp me-2"></i>WhatsApp</a>
                </div>
            </div>
        </div>
    </div>
"""

NOT_FOUND = page_header("Page Not Found", "404") + f"""
    <div class="container-xxl py-5 wow fadeInUp" data-wow-delay="0.1s">
        <div class="container text-center">
            <div class="row justify-content-center">
                <div class="col-lg-6">
                    <i class="bi bi-exclamation-triangle display-1 text-primary"></i>
                    <h1 class="display-1">404</h1>
                    <h1 class="mb-4">Page Not Found</h1>
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
    write("about.html", f"About Us | {COMPANY}", "about", ABOUT)
    write("exports.html", f"Exports from India | {COMPANY}", "exports", EXPORTS)
    write("imports.html", f"Imports to India | {COMPANY}", "imports", IMPORTS)
    write("products.html", f"Products | {COMPANY}", "products", PRODUCTS)
    write("service.html", f"Services | {COMPANY}", "services", SERVICES)
    write("markets.html", f"Markets | {COMPANY}", "markets", MARKETS)
    write("contact.html", f"Contact | {COMPANY}", "contact", CONTACT)
    write("quote.html", f"Request a Quote | {COMPANY}", "contact", QUOTE)
    write("privacy.html", f"Privacy Policy | {COMPANY}", "home", PRIVACY)
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
