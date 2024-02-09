function summonDemon() {
    fetch('/summon')
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                alert('Failed to summon demon: ' + data.error);
            } else {
                const demonInfo = document.getElementById('demonInfo');
                demonInfo.innerHTML = `
                    <h2>You have summoned ${data.Name} (${data.Rank}):</h2>
                    <p>${data.Description}</p>
                    <p><strong>Abilities:</strong> ${data.Abilities}</p>
                `;
            }
        })
        .catch(error => {
            console.error('Error:', error);
            alert('Error summoning demon.');
        });
}
