function fetchClientes() {
    fetch('/api/clientes')  
        .then(response => response.json()) 
        .then(data => {
            const tableBody = document.getElementById('clientes-table-body'); 

            data.forEach(cliente => {
                const row = document.createElement('tr');  
                row.innerHTML = `
                    <td>${cliente.id_cliente}</td>
                    <td>${cliente.nome}</td>
                    <td>${cliente.email}</td>
                    <td>${cliente.cpf}</td>
                    <td>${cliente.telefone}</td>
                `; 
                tableBody.appendChild(row);  
            });
        })
        .catch(error => console.error('Erro ao buscar clientes:', error)); 
}


function fetchPets() {
    fetch('/api/pets')  
        .then(response => response.json()) 
        .then(data => {
            const tableBody = document.getElementById('pets-table-body'); 

            data.forEach(pets => {
                const row = document.createElement('tr');  
                row.innerHTML = `
                    <td>${pets.id_pet}</td>
                    <td>${pets.nome_pet}</td>
                    <td>${pets.especie}</td>
                    <td>${pets.idade}</td>
                    <td>${pets.raca}</td>
                    <td>${pets.observacoes}</td>
                    <td>${pets.id_cliente}</td>
                `; 
                tableBody.appendChild(row);  
            });
        })
        .catch(error => console.error('Erro ao buscar pets:', error)); 
}

window.onload = function() {
    fetchClientes();
    fetchPets();
};