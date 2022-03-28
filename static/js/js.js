window.addEventListener('load',function(){
	var add_btn = document.querySelector('#add_fields');
	var count_btn = 0;
	var field = document.querySelector('input[type="text"]');
	var div_input = document.querySelector('#add_input');
	
	add_btn.addEventListener('click',function(e){
		++count_btn;
		cloneField = field.cloneNode();
		cloneField.setAttribute('name',field.getAttribute('name') + count_btn);
		cloneField.setAttribute('placeholder',field.getAttribute('placeholder') +count_btn);
		div_input.appendChild(cloneField);
	e.preventDefault();
})
})
