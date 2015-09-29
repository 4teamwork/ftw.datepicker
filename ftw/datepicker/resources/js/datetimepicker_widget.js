$(function(){

  initDateTimePicker = function(){
    $("input.datetimepicker-widget").each(function(i, o){
      var field = $(this);
      var lang = $('html').attr('lang')
      var widget_data = field.data("datetimewidget");
      var params = {};
      if (widget_data[lang]){
          params['format'] = widget_data[lang];

      }
      else if (widget_data[lang.split('-')[0]]){
        params['format'] = widget_data[lang.split('-')[0]];

      }
      else {
          params['format'] = "d.m.Y H:i";
      }
      if (lang.indexOf('-') > -1){
        lang = lang.split('-')[0];
      }
      params['lang'] = lang;
      if (field.hasClass('date-field')){
        params['timepicker'] = false;
        params['format'] = params['format'].split(' ')[0];
      }
      if (!field.val()){
        field.datetimepicker("destroy");  // May be initialized falsy, e.g. by datagridwidget
      }
      field.datetimepicker(params);
    });
  };

  initDateTimePicker();

  $(document).on("change", ".datetimepicker-widget", initDateTimePicker);

});