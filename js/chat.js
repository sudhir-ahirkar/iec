(function () {
    "use strict";

    var root = document.getElementById("grcChat");
    var panel = document.getElementById("grcChatPanel");
    var launch = document.getElementById("grcChatLaunch");
    var closeBtn = document.getElementById("grcChatClose");
    var log = document.getElementById("grcChatLog");
    var form = document.getElementById("grcChatForm");
    var input = document.getElementById("grcChatInput");
    var chips = document.getElementById("grcChatChips");
    if (!root || !panel || !launch || !log || !form || !input || !chips) {
        return;
    }

    var wa =
        "https://wa.me/919225159719?text=" +
        encodeURIComponent(
            "Hello Global Route Company, I would like to enquire about sourcing from India."
        );
    var quote = "/quote";
    var contact = "/contact";
    var products = "/products";
    var actions =
        '<p><a href="' +
        quote +
        '">Request a Quote</a> · <a href="' +
        wa +
        '" target="_blank" rel="noopener">WhatsApp</a></p>';

    var topics = [
        {
            id: "hello",
            keys: ["hi", "hello", "hey", "good morning", "good afternoon", "namaste"],
            html:
                "<p>Hello. Global Route Company is an India-based import and export trading company in Nagpur. Ask about products, export, import or how to reach us.</p>",
        },
        {
            id: "products",
            keys: [
                "product",
                "fruit",
                "mango",
                "papaya",
                "banana",
                "grape",
                "pomegranate",
                "vegetable",
                "onion",
                "potato",
                "chilli",
                "chili",
                "spice",
                "rice",
                "grain",
                "pulse",
                "commodity",
                "food",
            ],
            html:
                "<p>We source agricultural and food products according to buyer requirements. Categories include fresh fruits (papaya, mango, banana, grapes, pomegranate), vegetables (onion, potato and others), chilli and spices, rice, grains, pulses, selected processed food, and custom sourcing. Specifications are confirmed on enquiry.</p><p><a href=\"" +
                products +
                "\">View products</a></p>" +
                actions,
        },
        {
            id: "export",
            keys: ["export", "from india", "overseas buyer", "ship from"],
            html:
                "<p>We source agricultural products from India for international buyers — fruits, vegetables, spices, grains and related food products. Availability depends on seasonality, quality, quantity and destination.</p><p><a href=\"/exports\">Agricultural export from India</a></p>" +
                actions,
        },
        {
            id: "import",
            keys: ["import", "into india", "to india", "overseas supplier"],
            html:
                "<p>Alongside exports, we review international products that may fit Indian demand — based on quality, supplier reliability and commercial viability.</p><p><a href=\"/imports\">Import and global sourcing India</a></p>" +
                actions,
        },
        {
            id: "price",
            keys: [
                "price",
                "rate",
                "cost",
                "quote",
                "moq",
                "quantity",
                "fob",
                "cif",
                "incoterm",
            ],
            html:
                "<p>We do not publish prices on the website. Commercial terms such as FOB or CIF can be discussed once we understand the product, quantity and destination.</p>" +
                actions,
        },
        {
            id: "services",
            keys: [
                "service",
                "sourcing",
                "freight",
                "shipping",
                "logistics",
                "customs",
                "documentation",
                "warehouse",
                "certification",
            ],
            html:
                "<p>We support trade through sourcing and coordination. Freight, certification and documentation are handled with external partners when required. We coordinate shipment with logistics partners rather than operating freight ourselves.</p><p><a href=\"/services\">Import export and global sourcing services</a></p>" +
                actions,
        },
        {
            id: "markets",
            keys: [
                "market",
                "country",
                "middle east",
                "africa",
                "southeast asia",
                "europe",
                "destination",
            ],
            html:
                "<p>Target markets include the Middle East, Africa, Southeast Asia and Europe. These are regions we are building conversations in — not a claim of current shipment volume. We also review other regions when product fit and commercial terms align.</p><p><a href=\"/markets\">Indian agricultural products for global markets</a></p>" +
                actions,
        },
        {
            id: "contact",
            keys: [
                "contact",
                "phone",
                "call",
                "email",
                "whatsapp",
                "address",
                "office",
                "nagpur",
                "location",
                "map",
                "where",
            ],
            html:
                "<p>Global Route Company, Plot No. 188, CA Road, Garoba Maidan, Nagpur, Maharashtra (Near Dalvi Hospital) - 440008.</p><p>Phone <a href=\"tel:+919225159719\">+91 9225159719</a> (IST) · <a href=\"mailto:lokeshghagare19@gmail.com\">lokeshghagare19@gmail.com</a> · <a href=\"" +
                wa +
                '" target="_blank" rel="noopener">WhatsApp</a></p><p><a href="' +
                contact +
                '">Contact page</a></p>',
        },
        {
            id: "about",
            keys: ["about", "who", "company", "what do you do", "trading"],
            html:
                "<p>Global Route Company is an India-based trading company connecting Indian producers, global buyers and international suppliers. We focus on agricultural and food products, with responsible sourcing and clear communication.</p><p><a href=\"/about\">About Global Route Company</a></p>" +
                actions,
        },
        {
            id: "hours",
            keys: ["hour", "timing", "open", "ist", "time"],
            html:
                "<p>Reach us on <a href=\"tel:+919225159719\">+91 9225159719</a> (IST), WhatsApp or email. For a written requirement, use the quote form.</p>" +
                actions,
        },
    ];

    var fallback =
        "<p>I can only share what is published on this website. I cannot confirm prices, certificates, shipment history or documents here. Share the product, quantity and destination and the team will review it.</p>" +
        actions;

    var chipItems = [
        { label: "Products", id: "products" },
        { label: "Export", id: "export" },
        { label: "Import", id: "import" },
        { label: "Contact", id: "contact" },
        { label: "Get a quote", id: "price" },
    ];

    function topicById(id) {
        return topics.find(function (topic) {
            return topic.id === id;
        });
    }

    function normalize(text) {
        return String(text || "")
            .toLowerCase()
            .replace(/[^a-z0-9\s&]/g, " ")
            .replace(/\s+/g, " ")
            .trim();
    }

    function answer(text) {
        var q = normalize(text);
        if (!q) {
            return fallback;
        }
        var i;
        var topic;
        for (i = 0; i < topics.length; i += 1) {
            topic = topics[i];
            if (
                topic.keys.some(function (key) {
                    return q.indexOf(key) !== -1;
                })
            ) {
                return topic.html;
            }
        }
        return fallback;
    }

    function addMessage(html, who) {
        var item = document.createElement("div");
        item.className = "grc-chat-msg is-" + who;
        item.innerHTML = html;
        log.appendChild(item);
        log.scrollTop = log.scrollHeight;
    }

    function welcome() {
        if (log.childElementCount) {
            return;
        }
        addMessage(
            "<p>Hello. I can help with products, export from India, import to India, or how to contact Global Route Company. I am not a live agent.</p>",
            "bot"
        );
    }

    function openChat() {
        panel.hidden = false;
        root.classList.add("is-open");
        launch.setAttribute("aria-expanded", "true");
        welcome();
        input.focus();
    }

    function closeChat() {
        panel.hidden = true;
        root.classList.remove("is-open");
        launch.setAttribute("aria-expanded", "false");
        launch.focus();
    }

    function send(text) {
        var value = String(text || "").trim();
        if (!value) {
            return;
        }
        addMessage("<p></p>", "user");
        log.lastElementChild.querySelector("p").textContent = value;
        addMessage(answer(value), "bot");
        input.value = "";
    }

    chipItems.forEach(function (chip) {
        var button = document.createElement("button");
        button.type = "button";
        button.textContent = chip.label;
        button.addEventListener("click", function () {
            var topic = topicById(chip.id);
            addMessage("<p></p>", "user");
            log.lastElementChild.querySelector("p").textContent = chip.label;
            addMessage(topic ? topic.html : fallback, "bot");
        });
        chips.appendChild(button);
    });

    launch.addEventListener("click", function () {
        if (panel.hidden) {
            openChat();
        } else {
            closeChat();
        }
    });
    closeBtn.addEventListener("click", closeChat);
    document.addEventListener("keydown", function (event) {
        if (event.key === "Escape" && !panel.hidden) {
            closeChat();
        }
    });
    form.addEventListener("submit", function (event) {
        event.preventDefault();
        send(input.value);
    });
})();
