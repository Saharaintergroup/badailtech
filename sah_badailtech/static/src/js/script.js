$(function () {
  "use strict";
    $('.odoo_customer_slider').owlCarousel({
        loop:true,
        margin:5,
        nav:true,
        center:true,
        autosahay:true,
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
    $('.odoo_services_slider').owlCarousel({
        loop:true,
        margin:10,
        nav:false,
        center:true,
        autosahay:true,
        responsive:{
            768: {
                items: 1,
            },
            1024: {
                items:1.5
            }
        }
    });
    $('.odoo_blog_details_slider').owlCarousel({
        loop:true,
        margin:10,
        nav:false,
        center:false,
        autosahay:true,
        responsive:{
            768: {
                items: 1,
            },
            1024: {
                items:1.5
            }
        }
    });

});
function tabEventNews(e,imgName) {
    $('.tab-head-item, .tabs_event_news').removeClass("active");
    $(e).addClass("active");

    $('.sah-tab, .tab-content-item').hide();
    $('#'+imgName).fadeIn();

    $('.sah-tab, .tab-content-item').removeClass("active");
    $('#'+imgName).addClass("active");
    return false;
}
//$owl.trigger('refresh.owl.carousel');