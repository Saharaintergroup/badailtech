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
$(function() {
    'use strict';
    $('.langs_dropdown').on('click', function() {
        $(this).find('ul').toggle();
    });
    $('body').on('click', '.o_header_affix .langs_dropdown, .o_header_affix .langs_dropdown ul', function() {
        $(this).find('ul').toggle();
    });
    $(document).on('click', function() {
        $('.nav_menu_language').hide();
    });
    $(document).on('click', '.o_header_affix .langs_dropdown .nav_menu_language', function() {
        $(this).hide();
    });
    $('.langs_dropdown').on('click', function(e) {
        e.stopPropagation();
    });
    $('body').on('click', '.o_header_affix .langs_dropdown', function(e) {
        e.stopPropagation();
    });
})
//$owl.trigger('refresh.owl.carousel');