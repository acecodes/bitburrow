$( "#encode" ).submit(function( event ) {
  var value = {{ encode('Boom')|tojson|safe }};
  $( "h3.results" ).text( value );
  event.preventDefault();
});

$( "#results" ).click(function() {
  $( "#encode" ).submit();
});
