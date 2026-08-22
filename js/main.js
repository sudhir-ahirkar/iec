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
