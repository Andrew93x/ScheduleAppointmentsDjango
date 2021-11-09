async function ShowValues() {
    const response = await fetch('http://192.168.0.40:8000/list', {
        method: 'GET', // get, post, put, delete, ect.
    });
    const myJson = await response.json(); //exract JSON from the http responde
    console.log(myJson)
}

$('a').click(ShowValues);