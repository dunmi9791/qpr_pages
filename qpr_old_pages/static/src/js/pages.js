odoo.define('qpr_pages.pages', function(require) {
    'use strict';

    require('web.dom_ready');
    var $page = $('#wrap.pricing');
    $('#singup_modal #plan_id').hide();
    if (!$page.length) {
        return;
    }

    $page.find('.o_plan_launch_btn').on('click', function(ev) {
        var plan = $(ev.currentTarget).data('plan');
        $('#singup_modal #plan_id').show();
        $('#singup_modal #plan_id').val(plan);
        $('#singup_modal #exp_period').val('monthly');
        $('.modal-header-text').text('Create your live store ...');
    });

})
