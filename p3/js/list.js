// Main JS from IPM Practicum 3
// Authors:
// Miguel Blanco Godón
// Christian David Outeda García
//


// function creates tables 
function createTable(tableID) {
    var response = JSON.parse(localStorage.getItem(tableID));
    
    // visibility and creation control
    if (localStorage.getItem('table'+response['id']+'status') == "SHOWING") {
        localStorage.removeItem('table'+response['id']+'status');
        localStorage.setItem('table'+response['id']+'status', "NOT_SHOWING");
        document.getElementById('gen'+response['id']+'t').style.display = "none";
        return;
    }
    
    if (localStorage.getItem('table'+response['id']+'status') == "NOT_SHOWING") {
        localStorage.removeItem('table'+response['id']+'status');
        localStorage.setItem('table'+response['id']+'status', "SHOWING");
        document.getElementById('gen'+response['id']+'t').style.display = null;
        return;
    }
    
    // At this point table must be created 
    localStorage.removeItem('table'+response['id']+'status');
    localStorage.setItem('table'+response['id']+'status', "SHOWING");
    
    let table = document.createElement('table');
	table.id = "gen"+response['id']+"t";
	let header = table.createTHead();
	let hrow = header.insertRow();
	hrow.insertCell(0).innerHTML = "<b>#</b>";
	hrow.insertCell(1).innerHTML = "<b>Pokémon</b>";
	hrow.insertCell(2).innerHTML = "<b>Sprite</b>";
	hrow.insertCell(3).innerHTML = "<b>Primary type</b>";
	hrow.insertCell(4).innerHTML = "<b>Secondary type</b>";
	let div = document.getElementById('div'+response['id']);
	div.appendChild(table);
	let tbody = table.createTBody();    
	// creating table skeletton
	for(i=1; i<=response['pokemon_species'].length;i++) {
		let tbrow = tbody.insertRow();
		for(c=0;c<5;c++) tbrow.insertCell(c);
    }

	// Filling table
	var gentable = "gen"+response['id']+"t";
	var first_pokemon = response['pokemon_species'][0]['url'].substring(42, response['pokemon_species'][0]['url'].length-1);
	for(i=0; i <response['pokemon_species'].length; i++) {
		fetch("https://pokeapi.co/api/v2/pokemon/"+response['pokemon_species'][i]['url'].substring(42,response['pokemon_species'][i]['url'].lenght))
			.then(response => {
				if (response.ok) {
					return response.json();
				} else {
					throw Error("Error");
				}
			})
			.then(response => {
				let table = document.getElementById(gentable);
				let row_index = response['id'] - first_pokemon+1;
				// pokedex index
				table.rows[row_index].cells[0].appendChild(document.createTextNode(response['id']));
				// sprite
				let img = document.createElement('img');
				if (response['sprites']['front_default'] == null)
					img.src = '/assets/no available.png';
				else	
					img.src = response['sprites']['front_default'];
				img.alt = "sprite de pokémon "+response['name'];
				table.rows[row_index].cells[1].appendChild(img);
				// name
				let pokemonID = response['id'];
				let link = document.createElement('a');
				link.appendChild(document.createTextNode(response['name']));
				link.title = response['name'];
				link.href = "pokemon.html?pokemon_id="+response['id'];
				table.rows[row_index].cells[2].appendChild(link);
				// types
				let typeLink = document.createElement('a');
				typeLink.appendChild(document.createTextNode(response['types']['0']['type']['name']));
				typeLink.title = response['types']['0']['type']['name'];
				typeLink.href = "type.html?type_id="+response['types']['0']['type']['name'];
		                table.rows[row_index].cells[3].appendChild(typeLink);
				try {
					let typeLink2 = document.createElement('a');
					typeLink2.appendChild(document.createTextNode(response['types']['1']['type']['name']));
					typeLink2.title = response['types']['1']['type']['name'];
					typeLink2.href = "type.html?type_id="+response['types']['1']['type']['name'];
					table.rows[row_index].cells[4].appendChild(typeLink2);
				} catch (error) {
					table.rows[row_index].cells[4].appendChild(document.createTextNode(""));
				}
				return;
			})
			.catch(error =>
				console.log(error.message)
			);
    }
}




// Creating table cells
// obtaining generations and pokemons
fetch("https://pokeapi.co/api/v2/generation/")
	.then(response => {
		if (response.ok) {
			return response.json();
		} else {
			throw Error("Error");
		}
	})
	.then(response => {
		for(i=1; i<=response['count']; i++) {
			let body = document.getElementById("divMaster");
			let div = document.createElement("div");
			div.id = "div"+i;
			div.className="gendiv";
			body.appendChild(div);
			fetch("https://pokeapi.co/api/v2/generation/"+i)
				.then(response => {
					if (response.ok) {
						return response.json();
					} else {
						throw Error("Error");
					}
				})
				.then(response => {
					//let div = document.createElement("div");
					let div = document.getElementById("div"+response['id']);
					div.innerHTML = "<h2>"+response['name'].toUpperCase()+"</h2>"+"<button id='button"+response['id']+"' onclick='createTable(\"table"+response['id']+"\")'>&#9660;</button>";
                    localStorage.setItem('table'+response['id'], JSON.stringify(response));
                    localStorage.setItem('table'+response['id']+'status', "NOT_CREATED");
				})
				.catch(error => console.log(error.message));
		}
	})
	.catch(error => console.log("Failed to fetch data"));




// table filter function
function filterPokemons() {
	var target = 2;
	if(document.getElementById('input0').checked) target = 0;
	if(document.getElementById('input2').checked) target = 3;
	// to upperCase, so do not distinguish case
	let input = document.getElementById("pokeSearch").value.toLowerCase();
	for(i=1; i<=localStorage.length/2;i++) {
		let tableStatus = localStorage.getItem('table'+i+'status');
		if (tableStatus == "SHOWING") {
			var table = document.getElementById('gen'+i+'t');
			for(j=1; j<table.rows.length; j++) {
				if(target == 3) {
					if(table.rows[j].cells[target].textContent.includes(input) || (table.rows[j].cells[target+1].textContent && table.rows[j].cells[target+1].textContent.includes(input))) {
						table.rows[j].style.display = null;
					} else {
						table.rows[j].style.display = "none";
					}
				} else {
					if (table.rows[j].cells[target].textContent.includes(input)) {
						table.rows[j].style.display = null;
					} else {
						table.rows[j].style.display = "none";
					}
				}
			}
		}
	}
}

function changeInputType(type) {
	let searchBar = document.getElementById('pokeSearch');
	if(type==0) {
		searchBar.placeholder = "Search by pokédex number...";
		searchBar.type = "number";
		document.getElementById('input1').checked = false;
		document.getElementById('input2').checked = false;
	}
	if(type==1) {
		searchBar.placeholder = "Search by name...";
		searchBar.type = "text";
		document.getElementById('input0').checked = false;
		document.getElementById('input2').checked = false;
	}
	if (type==2) {
		searchBar.placeholder = "Search by Pokémon type...";
		searchBar.type = "text";
		document.getElementById('input0').checked = false;
		document.getElementById('input1').checked = false;
	}
}
