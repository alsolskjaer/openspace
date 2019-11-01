var pxScrolled = 200;
var duration = 500;

$(window).scroll(function() {
	if ($(this).scrollTop() > pxScrolled) {
		$('.to-top-container').css({ bottom: '0px', transition: '.3s' });
	} else {
		$('.to-top-container').css({ bottom: '-100px' });
	}
});

$('.top').click(function() {
	$('html, body').animate(
		{
			scrollTop: $('#page-top').offset().top
		},
		1500
	);
});

$('#scroll').click(function() {
	$('html, body').animate(
		{
			scrollTop: $('#about').offset().top
		},
		700
	);
});

$('#btn-features').click(function() {
	$('html, body').animate(
		{
			scrollTop: $('#features').offset().top
		},
		1000
	);
});

$('#btn-contact').click(function() {
	$('html, body').animate(
		{
			scrollTop: $('#contact').offset().top
		},
		1000
	);
});

$('#btn-value').click(function() {
	var sectionTo = $(this).attr('href');
	$('html, body').animate(
		{
			scrollTop: $(sectionTo).offset().top
		},
		1000
	);
});

$('#btn-people').click(function() {
	var sectionTo = $(this).attr('href');
	$('html, body').animate(
		{
			scrollTop: $(sectionTo).offset().top
		},
		1500
	);
});

$('.slider').owlCarousel({
	items: 1,
	singleItem: true,
	nav: true,
	dots: false,
	loop: true,
	autoPlay: 2000
});
