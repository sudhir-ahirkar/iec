(function () {
    "use strict";

    var back = document.querySelector(".back-to-top");
    window.addEventListener("scroll", function () {
        if (!back) return;
        back.style.display = window.scrollY > 300 ? "flex" : "none";
    });
    if (back) {
        back.addEventListener("click", function (event) {
            event.preventDefault();
            window.scrollTo({ top: 0, behavior: "smooth" });
        });
    }

    var params = new URLSearchParams(window.location.search);
    var product = params.get("product");
    var type = params.get("type");
    var productField = document.getElementById("product");
    var typeField = document.getElementById("enquiryType");

    if (product && productField) {
        productField.value = product;
    }
    if (type && typeField) {
        var match = Array.prototype.find.call(typeField.options, function (option) {
            return option.value === type || option.text === type;
        });
        if (match) {
            typeField.value = match.value || match.text;
        }
    }

    document.querySelectorAll("form[name='business-enquiry']:not(.d-none)").forEach(function (form) {
        form.addEventListener("submit", function (event) {
            if (!form.checkValidity()) {
                return;
            }
            event.preventDefault();
            var local = location.hostname === "127.0.0.1" || location.hostname === "localhost";
            if (local) {
                window.location.assign("/thank-you.html");
                return;
            }
            var body = new URLSearchParams(new FormData(form)).toString();
            fetch("/", {
                method: "POST",
                headers: { "Content-Type": "application/x-www-form-urlencoded" },
                body: body,
            })
                .then(function () {
                    window.location.assign("/thank-you.html");
                })
                .catch(function () {
                    window.location.assign("/thank-you.html");
                });
        });
    });

    if (product) {
        var message =
            "Hello Global Route Company, I would like to enquire about sourcing from India. Product: " +
            product +
            ".";
        var url =
            "https://wa.me/919225159719?text=" + encodeURIComponent(message);
        document.querySelectorAll('a[href*="wa.me/919225159719"]').forEach(function (link) {
            link.setAttribute("href", url);
        });
    }
})();
