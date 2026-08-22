(function ($) {
    "use strict";

    setTimeout(function () {
        if ($("#spinner").length > 0) {
            $("#spinner").removeClass("show");
        }
    }, 1);

    if (typeof WOW === "function") {
        new WOW().init();
    }

    $(".sticky-top").css("top", "0px");

    $(window).scroll(function () {
        if ($(this).scrollTop() > 300) {
            $(".back-to-top").fadeIn("slow");
        } else {
            $(".back-to-top").fadeOut("slow");
        }
    });

    $(".back-to-top").click(function () {
        $("html, body").animate({ scrollTop: 0 }, 800, "easeInOutExpo");
        return false;
    });

    var product = new URLSearchParams(window.location.search).get("product");
    if (product && $("#product").length) {
        $("#product").val(product);
    }
})(jQuery);
