// Pokemon page JS from IPM Practicum 3
// Authors:
// Miguel Blanco Godón
// Christian David Outeda García
//

// getting url parameter
var id = new URLSearchParams(window.location.search).get('pokemon_id');

fetch("https://pokeapi.co/api/v2/pokemon/"+id)
	.then(response => {
		if (response.ok) {
			return response.json();
		} else {
			throw Error("Error");
		}
	})
	.then(response => {
		// pokemon name
		let name = document.getElementById('name');
		name.innerHTML = "#"+response['id']+" "+response['name'].toUpperCase();
		// image
		let image = document.getElementById('image');
		if (response['sprites']['other']['official-artwork']['front_default'] == null && response['sprites']['other']['dream_world']['front_default']  == null)
			image.src = '/assets/no available.png';
		else	
			image.src = response['sprites']['other']['official-artwork']['front_default'] != null ? response['sprites']['other']['official-artwork']['front_default'] : response['sprites']['other']['dream_world']['front_default'];
		image.alt = response['sprites']['front_default'];
		let tlink = document.createElement('a');
		let typeDiv = document.getElementById('types');
		typeDiv.appendChild(tlink);
		tlink.title = response['types']['0']['type']['name'];
		tlink.href = "type.html?type_id="+response['types']['0']['type']['name'];
		tlink.appendChild(document.createTextNode(response['types']['0']['type']['name']));
		if (response['types'].length > 1) {
			typeDiv.appendChild(document.createTextNode("     "));
			let tlink2 = document.createElement('a');
			typeDiv.appendChild(tlink2);
			tlink2.title = response['types']['1']['type']['name'];
			tlink2.href = "type.html?type_id="+response['types']['1']['type']['name'];
			tlink2.appendChild(document.createTextNode(response['types']['1']['type']['name']));
		}

		// attibutes
		let attrib = document.getElementById('attributes');
		let attText = document.createElement('P');
		attrib.appendChild(attText);
		attText.innerHTML = "This pokémon has a base experience of "+response['base_experience']+".</br>"+
			"It's height is "+response['height']/10+" m ("+response['height']/10*3.2808+" ft) "+
			"and it's weight is "+response['weight']/10+" kg ("+response['weight']/10*2.2046226218487757+" lb)";
		// abilities table
		let abies = document.getElementById('abilities');
		let abTab = document.createElement('table');
		abies.appendChild(abTab);
		let abtheader = abTab.createTHead();
		let ar = abtheader.insertRow()
		ar.insertCell(0).innerHTML = "<b>Ability</b>";
		ar.insertCell(1).innerHTML = "<b>Hidden</b>";
		ar.insertCell(2).innerHTML = "<b>Slots</b>";
		let abtbody = abTab.createTBody();
		for(i=0; i<response['abilities'].length; i++) {
			let nr = abtbody.insertRow();
			nr.insertCell(0).appendChild(document.createTextNode(response['abilities'][i]['ability']['name'].toUpperCase()));
			nr.insertCell(1).appendChild(document.createTextNode(response['abilities'][i]['is_hidden'] == false ? 'No' : 'Yes'));
			nr.insertCell(2).appendChild(document.createTextNode(response['abilities'][i]['slot']));
		}
		// stat table
		//
		let stats = document.getElementById('stats');
		let statsTable = document.createElement('table');
		stats.appendChild(statsTable);
		let statsHead = statsTable.createTHead();
		let row = statsHead.insertRow();
		row.insertCell(0).innerHTML = "<b>Stat</b>";
		row.insertCell(1).innerHTML = "<b>Base stat</b>";
		row.insertCell(2).innerHTML = "<b>Effort</b>";
		let statsBody = statsTable.createTBody();
		for(i=0; i<response['stats'].length; i++) {
			let newRow = statsBody.insertRow();
			newRow.insertCell(0).appendChild(document.createTextNode(response['stats'][i]['stat']['name'].toUpperCase()));
			newRow.insertCell(1).appendChild(document.createTextNode(response['stats'][i]['base_stat']));
			newRow.insertCell(2).appendChild(document.createTextNode(response['stats'][i]['effort']));
		}
		
		// sprite table
		let spr = document.getElementById('sprites');
		let order = ['front_default','back_default','front_female','back_female','front_shiny','back_shiny','front_shiny_female','back_shiny_female'];
		let orderText = ['Front default','Back default','Front female','Back female','Front shiny','Back shiny','Front shiny female','Back shiny female'];
		for(i=0; i<6; i++) {
			if (response['sprites'][order[i]] != null) {
				let card = document.createElement('div');
				spr.appendChild(card);
				card.className = "card";
				let cim = document.createElement('img');
				cim.src = response['sprites'][order[i]];
				cim.alt = "sprite de pokémon "+response['name'];
				card.appendChild(cim);
				let td = document.createElement('div');
				card.appendChild(td);
				td.innerHTML = "<h4>"+orderText[i]+"</h4>";
				td.className = "container";
			}
		}
		
		// moves
		let mov = document.getElementById('moves');
		let movTable = document.createElement('table');
		mov.appendChild(movTable);
		let movHeader = movTable.createTHead();
		let movTT = movHeader.insertRow();
		movTT.insertCell(0).innerHTML = "<b>Movement</b>";
		movTT.insertCell(1).innerHTML = "<b>Learning Method</b>";
		movTT.insertCell(2).innerHTML = "<b>Minimum level</b>";
		let movBody = movTable.createTBody();
		for(i=0; i<response['moves'].length;i++) {
			let snrow = movBody.insertRow();
			let movelink = document.createElement('a');
			snrow.insertCell(0).appendChild(movelink);
			movelink.title = response['moves'][i]['move']['name'].toUpperCase();
			movelink.href = "move.html?move_id="+response['moves'][i]['move']['name'];
			movelink.appendChild(document.createTextNode(response['moves'][i]['move']['name'].toUpperCase()));
			snrow.insertCell(1).innerHTML = response['moves'][i]['version_group_details'][0]['move_learn_method']['name'];
			snrow.insertCell(2).innerHTML = response['moves'][i]['version_group_details'][0]['level_learned_at'];
		}

		// pokedex descriptions
		//
		fetch("https://pokeapi.co/api/v2/pokemon-species/"+response['id'])
			.then(response => {
				if (response.ok) {
					return response.json();
				} else {
					throw Error("Cannot fetch pokemon species");
				}
			})
			.then(response => {
				let pokedex = document.getElementById('pokedex_descriptions');
				if (response['flavor_text_entries'].length == 0) {
					let disclaimer = document.createElement('p');
					p.innerHTML = "Sorry, we do not have any pokedex description for this pokémon";
					pokedex.appendChild(disclaimer);
				} else {
					let table = document.createElement('table');
					let head = table.createTHead();
					let title = head.insertRow();
					title.insertCell(0).innerHTML = '<b>Version</b>';
					title.insertCell(1).innerHTML = '<b>Pokédex description</b>';
					let body = table.createTBody();
					for(i=0;i<response['flavor_text_entries'].length;i++) {
						if(response['flavor_text_entries'][i]['language']['name'] == 'en') {
							let line = body.insertRow();
							line.insertCell(0).appendChild(document.createTextNode(response['flavor_text_entries'][i]['version']['name']));
							line.insertCell(1).appendChild(document.createTextNode(response['flavor_text_entries'][i]['flavor_text']));
						}
					}
					pokedex.appendChild(table);
				}
			})
			.catch(error => console.log(error.message));

	})
	.catch(error => console.log(error.message));
