$(function(){

  initDateTimePicker = function(){
    $("input.datetimepicker-widget").each(function(i, o){
      var field = $(this);
      var widget_data = field.data("datetimewidget");
      if (!field.val()){
        field.datetimepicker("destroy");  // May be initialized falsy, e.g. by datagridwidget
      }

      field.datetimepicker(widget_data);
    });
  };

  initDateTimePicker();

  $(document).on("change", ".datetimepicker-widget", initDateTimePicker);

});
