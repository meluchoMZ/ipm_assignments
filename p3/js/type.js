// Type page JS from IPM Practicum 3
// Authors:
// Miguel Blanco Godón
// Christian David Outeda García


let id = new URLSearchParams(window.location.search).get('type_id');

fetch("https://pokeapi.co/api/v2/type/"+id)
	.then(response => {
		if (response.ok) {
			return response.json();
		} else {
			throw Error("Error");
		}
	})
	.then(response => {
		// type name
		let name = document.getElementById('name');
		name.innerHTML = "Type "+response['name'];

		let moveName = document.getElementById('moveName');
		moveName.innerHTML = response['name']+" moves";

		let pokemonName = document.getElementById('pokemonName');
		pokemonName.innerHTML = response['name']+" pokemons";

		//image
		let image = document.getElementById('image');
		image.src = imagen(response['name']);
		image.alt = "type "+response['name']+" main picture"
		
		// damage_relations tables
		let double_from_relations = document.getElementById('double_from_relations');
		let double_from_relationsTable = document.createElement('table');
		double_from_relations.appendChild(double_from_relationsTable);
		let double_from_relationsHead = double_from_relationsTable.createTHead();
		let double_from_row = double_from_relationsHead.insertRow();
		double_from_row.insertCell(0).innerHTML = "<b>Double damage from</b>";
		double_from_row.insertCell(1).innerHTML = "<b>Name</b>";
		let double_from_relationsBody = double_from_relationsTable.createTBody();
		for(j=0; j<response['damage_relations']['double_damage_from'].length; j++) {
			let double_from_newRow = double_from_relationsBody.insertRow();
			let element_img = document.createElement('img');
			element_img.src = imagen(response['damage_relations']['double_damage_from'][j]['name']);
			element_img.alt = "image type" + response['damage_relations']['double_damage_from'][j]['name'];
			double_from_newRow.insertCell(0).appendChild(element_img);
			let damageLink = document.createElement('a');
			damageLink.appendChild(document.createTextNode(response['damage_relations']['double_damage_from'][j]['name']));
			damageLink.title = response['damage_relations']['double_damage_from'][j]['name'];
			damageLink.href = "type.html?type_id="+response['damage_relations']['double_damage_from'][j]['name'];
			double_from_newRow.insertCell(1).appendChild(damageLink);
		}

		let double_to_relations = document.getElementById('double_to_relations');
		let double_to_relationsTable = document.createElement('table');
		double_to_relations.appendChild(double_to_relationsTable);
		let double_to_relationsHead = double_to_relationsTable.createTHead();
		let double_to_row = double_to_relationsHead.insertRow();
		double_to_row.insertCell(0).innerHTML = "<b>Double damage to</b>";
		double_to_row.insertCell(1).innerHTML = "<b>Name</b>"
		let double_to_relationsBody = double_to_relationsTable.createTBody();
		for(j=0; j<response['damage_relations']['double_damage_to'].length; j++) {
			let double_to_newRow = double_to_relationsBody.insertRow();
			let element_img = document.createElement('img');
			element_img.src = imagen(response['damage_relations']['double_damage_to'][j]['name']);
			element_img.alt = "image type" + response['damage_relations']['double_damage_to'][j]['name'];
			double_to_newRow.insertCell(0).appendChild(element_img);
			let damageLink = document.createElement('a');
			damageLink.appendChild(document.createTextNode(response['damage_relations']['double_damage_to'][j]['name']));
			damageLink.title = response['damage_relations']['double_damage_to'][j]['name'];
			damageLink.href = "type.html?type_id="+response['damage_relations']['double_damage_to'][j]['name'];
			double_to_newRow.insertCell(1).appendChild(damageLink);
		}

		let half_from_relations = document.getElementById('half_from_relations');
		let half_from_relationsTable = document.createElement('table');
		half_from_relations.appendChild(half_from_relationsTable);
		let half_from_relationsHead =half_from_relationsTable.createTHead();
		let half_from_row = half_from_relationsHead.insertRow();
		half_from_row.insertCell(0).innerHTML = "<b>Half damage from</b>";
		half_from_row.insertCell(1).innerHTML = "<b>Name</b>";
		let half_from_relationsBody = half_from_relationsTable.createTBody();
		for(j=0; j<response['damage_relations']['half_damage_from'].length; j++) {
			let half_from_newRow = half_from_relationsBody.insertRow();
			let element_img = document.createElement('img');
			element_img.src = imagen(response['damage_relations']['half_damage_from'][j]['name']);
			element_img.alt = "image type" + response['damage_relations']['half_damage_from'][j]['name'];
			half_from_newRow.insertCell(0).appendChild(element_img);
			let damageLink = document.createElement('a');
			damageLink.appendChild(document.createTextNode(response['damage_relations']['half_damage_from'][j]['name']));
			damageLink.title = response['damage_relations']['half_damage_from'][j]['name'];
			damageLink.href = "type.html?type_id="+response['damage_relations']['half_damage_from'][j]['name'];
			half_from_newRow.insertCell(1).appendChild(damageLink);
		}

		let half_to_relations = document.getElementById('half_to_relations');
		let half_to_relationsTable = document.createElement('table');
		half_to_relations.appendChild(half_to_relationsTable);
		let half_to_relationsHead =half_to_relationsTable.createTHead();
		let half_to_row = half_to_relationsHead.insertRow();
		half_to_row.insertCell(0).innerHTML = "<b>Half damage to</b>";
		half_to_row.insertCell(1).innerHTML = "<b>Name</b>";
		let half_to_relationsBody = half_to_relationsTable.createTBody();
		for(j=0; j<response['damage_relations']['half_damage_to'].length; j++) {
			let half_to_newRow = half_to_relationsBody.insertRow();
			let element_img = document.createElement('img');
			element_img.src = imagen(response['damage_relations']['half_damage_to'][j]['name']);
			element_img.alt = "image type" + response['damage_relations']['half_damage_to'][j]['name'];
			half_to_newRow.insertCell(0).appendChild(element_img);
			let damageLink = document.createElement('a');
			damageLink.appendChild(document.createTextNode(response['damage_relations']['half_damage_to'][j]['name']));
			damageLink.title = response['damage_relations']['half_damage_to'][j]['name'];
			damageLink.href = "type.html?type_id="+response['damage_relations']['half_damage_to'][j]['name'];
			half_to_newRow.insertCell(1).appendChild(damageLink);;
		}

		let no_from_relations = document.getElementById('no_from_relations');
		let no_from_relationsTable = document.createElement('table');
		no_from_relations.appendChild(no_from_relationsTable);
		let no_from_relationsHead = no_from_relationsTable.createTHead();
		let no_from_row = no_from_relationsHead.insertRow();
		no_from_row.insertCell(0).innerHTML = "<b>No damage from</b>";
		no_from_row.insertCell(1).innerHTML = "<b>Name</b>";
		let no_from_relationsBody = no_from_relationsTable.createTBody();
		for(j=0; j<response['damage_relations']['no_damage_from'].length; j++) {
			let no_from_newRow = no_from_relationsBody.insertRow();
			let element_img = document.createElement('img');
			element_img.src = imagen(response['damage_relations']['no_damage_from'][j]['name']);
			element_img.alt = "image type" + response['damage_relations']['no_damage_from'][j]['name'];
			no_from_newRow.insertCell(0).appendChild(element_img);
			let damageLink = document.createElement('a');
			damageLink.appendChild(document.createTextNode(response['damage_relations']['no_damage_from'][j]['name']));
			damageLink.title = response['damage_relations']['no_damage_from'][j]['name'];
			damageLink.href = "type.html?type_id="+response['damage_relations']['no_damage_from'][j]['name'];
			no_from_newRow.insertCell(1).appendChild(damageLink);
		}

		let no_to_relations = document.getElementById('no_to_relations');
		let no_to_relationsTable = document.createElement('table');
		no_to_relations.appendChild(no_to_relationsTable);
		let no_to_relationsHead = no_to_relationsTable.createTHead();
		let no_to_row = no_to_relationsHead.insertRow();
		no_to_row.insertCell(0).innerHTML = "<b>No damage to</b>";
		no_to_row.insertCell(1).innerHTML = "<b>Name</b>";
		let no_to_relationsBody = no_to_relationsTable.createTBody();
		for(j=0; j<response['damage_relations']['no_damage_to'].length; j++) {
			let no_to_newRow = no_to_relationsBody.insertRow();
			let element_img = document.createElement('img');
			element_img.src = imagen(response['damage_relations']['no_damage_to'][j]['name']);
			element_img.alt = "image type" + response['damage_relations']['no_damage_to'][j]['name'];
			no_to_newRow.insertCell(0).appendChild(element_img);
			let damageLink = document.createElement('a');
			damageLink.appendChild(document.createTextNode(response['damage_relations']['no_damage_to'][j]['name']));
			damageLink.title = response['damage_relations']['no_damage_to'][j]['name'];
			damageLink.href = "type.html?type_id="+response['damage_relations']['no_damage_to'][j]['name'];
			no_to_newRow.insertCell(1).appendChild(damageLink);
		}
	

		//moves table

		let moves = document.getElementById('moves');
		let movesTable = document.createElement('table');
		moves.appendChild(movesTable);
		let movesHead = movesTable.createTHead();
		let moves_row = movesHead.insertRow();
		moves_row.insertCell(0).innerHTML = "<b>#</b>";
		moves_row.insertCell(1).innerHTML = "<b>name</b>";
		
		let movesBody = movesTable.createTBody();
		for(j=0; j<response['moves'].length;j++) {
			let mv = response['moves'][j]['url'];
			fetch(mv)
				.then(response2 => {
				if (response2.ok) {
				return response2.json();
				} else {
				throw Error("Error");
				}
			})
				.then(response2 => {
			let moves_newRow = movesBody.insertRow();
			moves_newRow.insertCell(0).appendChild(document.createTextNode(response2['id']));
			let moveLink = document.createElement('a');
			moveLink.appendChild(document.createTextNode(response2['name']));
			moveLink.title = response2['name'];
			moveLink.href = "move.html?move_id="+response2['id'];
			moves_newRow.insertCell(1).appendChild(moveLink);
			})
		}	

		//pokemon tables

		let pokemon = document.getElementById('pokemon');
		let pokemonTable = document.createElement('table');
		pokemon.appendChild(pokemonTable);
		let pokemonHead = pokemonTable.createTHead();
		let pokemon_row = pokemonHead.insertRow();
		pokemon_row.insertCell(0).innerHTML = "<b>#</b>";
		pokemon_row.insertCell(1).innerHTML = "<b>pokemon</b>";
		pokemon_row.insertCell(2).innerHTML = "<b>name</b>";
		
		let pokemonBody = pokemonTable.createTBody();
		for(j=0; j<response['pokemon'].length;j++) {
			let pokemon_newRow = pokemonBody.insertRow();
			let poke = response['pokemon'][j]['pokemon']['url'];
			fetch(poke)
				.then(response2 => {
				if (response2.ok) {
				return response2.json();
				} else {
				throw Error("Error");
				}
			})
				.then(response2 => {
				pokemon_newRow.insertCell(0).appendChild(document.createTextNode(response2['id']));
				let image_poke = document.createElement('img');
				if (response2['sprites']['front_default'] == null){
					image_poke.src = 'assets/no available.png';
					image_poke.alt = response2['name'] + " pokemon image not available";
				}	
				else{	
					image_poke.src = response2['sprites']['front_default'];
					image_poke.alt = response2['name'] + " pokemon image" ;
				}	
				pokemon_newRow.insertCell(1).appendChild(image_poke);
				let pokeLink = document.createElement('a');
				pokeLink.appendChild(document.createTextNode(response2['name']));
				pokeLink.title = response2['name'];
				pokeLink.href = "pokemon.html?pokemon_id="+response2['id'];
				pokemon_newRow.insertCell(2).appendChild(pokeLink);
			})
			.catch(error => console.log(error.message));
		}	
	})
	.catch(error => console.log(error.message));

function imagen(tipo){
	if(tipo == "normal")
		return "assets/types/normal.png"
	if(tipo == "fighting")
		return "assets/types/fighting.png"
	if(tipo == "flying")
		return "assets/types/flying.png"
	if(tipo == "poison")
		return "assets/types/poison.png"
	if(tipo == "ground")
		return "assets/types/ground.png"
	if(tipo == "rock")
		return "assets/types/rock.png"
	if(tipo == "bug")
		return "assets/types/bug.png"
	if(tipo == "ghost")
		return "assets/types/ghost.png"
	if(tipo == "steel")
		return "assets/types/steel.png"
	if(tipo == "fire")
		return "assets/types/fire.png"
	if(tipo == "water")
		return "assets/types/water.png"
	if(tipo == "grass")
		return "assets/types/grass.png"
	if(tipo == "electric")
		return "assets/types/electric.png"
	if(tipo == "psychic")
		return "assets/types/psychic.png"
	if(tipo == "ice")
		return "assets/types/ice.png"
	if(tipo == "dragon")
		return "assets/types/dragon.png"
	if(tipo == "dark")
		return "assets/types/dark.png"
	if(tipo == "fairy")
		return "assets/types/fairy.png"
	if(tipo == "unknown")
		return "assets/types/unknown.png"
	if(tipo == "shadow")
		return "assets/types/shadow.png"
}