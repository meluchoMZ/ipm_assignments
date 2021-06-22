fetch("https://pokeapi.co/api/v2/type")
	.then(response => {
		if (response.ok) {
			return response.json();
		} else {
			throw Error('Error');
		}
	})
	.then(response => {
		let table = document.createElement('table');
		document.body.appendChild(table);
		let header = table.createTHead();
		let hrow = header.insertRow();
		hrow.insertCell(0).innerHTML = "<b>#</b>";
		hrow.insertCell(1).innerHTML = "<b>Type name</b>";
		let body = table.createTBody();
		for (i = 0; i < response['results'].length; i++) {
			let row = body.insertRow();
			row.insertCell(0).innerHTML = i+1;
			let link = document.createElement('a');
			link.appendChild(document.createTextNode(response['results'][i]['name']));
			link.title = response['results'][i]['name'];
			link.href = "type.html?type_id="+response['results'][i]['name'];
			row.insertCell(1).appendChild(link);
		}
	})
	.catch(error => console.log(error.message));
