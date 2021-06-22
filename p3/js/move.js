// Move page JS from IPM Practicum 3
// Authors:
// Miguel Blanco Godón
// Christian David Outeda García


let id = new URLSearchParams(window.location.search).get('move_id');

fetch("https://pokeapi.co/api/v2/move/"+id)
	.then(response => {
		if (response.ok) {
			return response.json();
		} else {
			throw Error("Error");
		}
	})
	.then(response => {
		// move name
		let name = document.getElementById('name');
        name.innerHTML = response['name'];

        //move description
        let move_description = document.getElementById('parrafo');
        move_description.innerHTML = response['effect_entries'][0]['effect'];

        // move type table
        let move_type = document.getElementById('type');
        let move_typeTable = document.createElement('table');
        move_type.appendChild(move_typeTable);
        let typeHead = move_typeTable.createTHead();
        let type_row = typeHead.insertRow();
        type_row.insertCell(0).innerHTML = "<b>type</b>";
        type_row.insertCell(1).innerHTML = "<b>name</b>";
        let typeBody = move_typeTable.createTBody();
        let type_newRow = typeBody.insertRow();
        let element_img = document.createElement('img');
        element_img.src = imagen(response['type']['name']);
        element_img.alt = "type "+response['type']['name']+ " image";
        type_newRow.insertCell(0).appendChild(element_img);
        let typeLink = document.createElement('a');
        typeLink.appendChild(document.createTextNode(response['type']['name']));
        typeLink.title =  response['type']['name'];
        typeLink.href = "type.html?type_id="+response['type']['name'];
        type_newRow.insertCell(1).appendChild(typeLink);

        //info table
        let move = document.getElementById('move');
        let moveTable = document.createElement('table');
        move.appendChild(moveTable);
        let moveHead = moveTable.createTHead();
        let move_row = moveHead.insertRow();
        move_row.insertCell(0).innerHTML = "<b>#</b>";
        move_row.insertCell(1).innerHTML = "<b>Power</b>";
        move_row.insertCell(2).innerHTML = "<b>pp</b>";
        move_row.insertCell(3).innerHTML = "<b>Accuracy</b>";
        move_row.insertCell(4).innerHTML = "<b>Damage class</b>";
        move_row.insertCell(5).innerHTML = "<b>target</b>";
        let moveBody = moveTable.createTBody();
        let move_newRow = moveBody.insertRow();
        move_newRow.insertCell(0).appendChild(document.createTextNode(response['id']));
        if (response['power'] == null)
            move_newRow.insertCell(1).appendChild(document.createTextNode("0"));
        else    
            move_newRow.insertCell(1).appendChild(document.createTextNode(response['power']));
        move_newRow.insertCell(2).appendChild(document.createTextNode(response['pp']));
        if (response['accuracy'] == null)
            move_newRow.insertCell(3).appendChild(document.createTextNode("100"));
        else    
            move_newRow.insertCell(3).appendChild(document.createTextNode(response['accuracy']));
        move_newRow.insertCell(4).appendChild(document.createTextNode(response['damage_class']['name']));
        move_newRow.insertCell(5).appendChild(document.createTextNode(response['target']['name']));
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