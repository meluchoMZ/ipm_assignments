// Moves list from IPM Practicum 3
// Authors:
// Miguel Blanco Godón
// Christian David Outeda García

var source = "https://pokeapi.co/api/v2/move";
var offset = 0;

let div = document.getElementById("typesTable");
let table = document.createElement('table');
div.appendChild(table);
let head = table.createTHead();
let row = head.insertRow();
row.insertCell(0).innerHTML = "<b>#</b>";
row.insertCell(1).innerHTML = "<b>Move</b>";
row.insertCell(2).innerHTML = "<b>Type</b>";
var body = table.createTBody();

addGroup();

window.onscroll = function(ev) {
	if ((window.innerHeight + window.scrollY) >= document.body.offsetHeight) {
		addGroup();
	}
};

function addGroup() {
	if (source == null) return;
	fetch(source)
		.then(response => {
			if (response.ok) {
				return response.json();
			} else {
				throw Error("Error");
			}
		})
		.then(response => {
			for(i = 0; i < response['results'].length; i++) {
				let row = body.insertRow();
				row.insertCell(0).innerHTML = offset+i+1;
				let link = document.createElement('a');
				link.appendChild(document.createTextNode(response['results'][i]['name']));
				link.title = response['results'][i]['name'];
				link.href = "move.html?move_id="+response['results'][i]['name'];
				row.insertCell(1).appendChild(link);
				row.insertCell(2);
				insertType(response['results'][i]['url'], offset+i);
			}
			source = response['next'];
			offset = offset + response['results'].length;
		})
		.catch(error => console.log(error.message));
}

function insertType(url, offsetPosition) {
	fetch(url)
		.then(response => {
			if(response.ok) {
				return response.json();
			} else {
				throw Error("Error");
			}
		})
		.then(response => {
			console.log("inserting "+response['id']);
			console.log(response['type']['name']);
			let link = document.createElement('a');
			link.appendChild(document.createTextNode(response['type']['name']));
			link.title = response['type']['name'];
			link.href = "type.html?type_id="+response['type']['name'];
			body.rows[offsetPosition].cells[2].appendChild(link);
		})
		.catch(error => console.log(error.message));
}
