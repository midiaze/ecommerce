
var updateBtns = document.getElementsByClassName('update-cart')

for (i = 0; i < updateBtns.length; i++) {
	updateBtns[i].addEventListener('click', function(){
		var productId = this.dataset.product
		var action = this.dataset.action
		alert(productId)

		if ('{{request.session.id}}'){
			updateUserOrder(productId, action)
		}
	})
}

// //Logeado
function updateUserOrder(productId, action){
	if (action == 'add'){
		if (cart[productId] == undefined){
		cart[productId] = {'quantity':1}

		}else{
			cart[productId]['quantity'] += 1
		}
	}
	if (action == 'remove'){
		cart[productId]['quantity'] -= 1

		if (cart[productId]['quantity'] <= 0){
			console.log('Remove item')
			delete cart[productId];
		}
	}
	document.cookie ='cart=' + JSON.stringify(cart) + ";domain=;path=/"
	location.reload()
	// window.location.href = `/pedidos/add/${productId}/${cart[productId]['quantity']}`

	// console.log('User is authenticated, sending data...')
	// 	var url = '/pedidosupdate_item/'
	// 	alert(productId)
	// 	fetch(url, {
	// 		method:'POST',
	// 		headers:{
	// 			'Content-Type':'application/json',
	// 			'X-CSRFToken':csrftoken,
	// 		}, 
	// 		body:JSON.stringify({'productId':productId, 'action':action})
	// 	})
	// 	.then((response) => {
	// 		return response.json();
	// 	})
	// 	.then((data) => {
	// 		location.reload()
	// 	});
}

// No loggeado
// function addCookieItem(productId, action){
// 	// console.log('User is not authenticated')
// 	alert(productId)
// 	if (action == 'add'){
// 		if (cart[productId] == undefined){
// 		cart[productId] = {'quantity':1}

// 		}else{
// 			cart[productId]['quantity'] += 1
// 		}
// 	}
// 	if (action == 'remove'){
// 		cart[productId]['quantity'] -= 1

// 		if (cart[productId]['quantity'] <= 0){
// 			console.log('Remove item')
// 			delete cart[productId];
// 		}

	// console.log('CART:', cart)
	// document.cookie ='cart=' + JSON.stringify(cart) + ";domain=;path=/"
	// location.reload()
	// updateUserOrder()
	


