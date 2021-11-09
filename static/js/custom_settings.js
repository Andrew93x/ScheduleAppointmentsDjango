async function showValues() {
    url = 'http://192.168.0.40/list_cs'
    const response = await fetch(url, {
        method: 'GET',
    });
    const myJson = await response.json();
    console.log(myJson)
}

$('#').click(showValues);