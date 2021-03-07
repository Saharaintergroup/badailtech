$(function () {
  "use strict";
    $('.odoo_customer_slider').owlCarousel({
        loop:true,
        margin:5,
        nav:true,
        center:true,
        autoplay:true,
        responsive:{
            0: {
                items: 1,
            },
            481: {
                items: 2,
            },
            768: {
                items: 3,
            },
            1024: {
                items:4
            }
        }
    });

});
//$owl.trigger('refresh.owl.carousel');