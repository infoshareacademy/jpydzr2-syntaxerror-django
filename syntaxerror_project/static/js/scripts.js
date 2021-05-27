// Datatables
$(document).ready(function () {
    $('#results_table').DataTable();
});

// Change nav color on scroll
$(function () {
    $(document).scroll(function () {
        var $nav = $("#main-nav");
        $nav.toggleClass('scrolled', $(this).scrollTop() > $nav.height());
    });
});

// Remove hashes from the page when using #anchor links
$(document).ready(function () {
    const menuBtn = $('.hack15-menu-button');
    menuBtn.click(() => {
        setTimeout(() => {
            removeHash();
        }, 5);
    });

    function removeHash() {
        history.replaceState('', document.title, window.location.origin + window.location.pathname + window.location.search);
    }
});
