django.jQuery(document).on('change', '#id_match_type', function(){
    var match_type =  django.jQuery(this).val()
    if (match_type != 'BO1'){
        django.jQuery('.field-team_score').hide()
        django.jQuery('.field-opposing_score').hide()
        django.jQuery('.field-map').hide()
    } else {
        django.jQuery('.field-team_score').show()
        django.jQuery('.field-opposing_score').show()
        django.jQuery('.field-map').show()
    }
})
